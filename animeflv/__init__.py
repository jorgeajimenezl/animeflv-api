import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import unquote, quote
import requests, json, re

def parseTable(table):
    columns = list([x.string for x in table.thead.tr.find_all('th')])
    rows = []
    
    for row in table.tbody.find_all('tr'):
        values = row.find_all('td')

        if len(values) != len(columns):
            raise Exception("don't match values size with columns size")

        rows.append({h: x for h, x in zip(columns, values)})

    return rows

BASE_URL = 'https://animeflv.net'
BROWSE_URL = 'https://animeflv.net/browse?'
SEARCH_URL = 'https://animeflv.net/browse?q='
ANIME_VIDEO_URL = 'https://animeflv.net/ver/'
BASE_EPISODE_IMG_URL = 'https://cdn.animeflv.net/screenshots/'
ORDER_TITLE = 'https://www3.animeflv.net/browse?order=title&page='
# BASE_JIKA_URL = ' https://api.jikan.moe/v3/search/anime?q='
# BASE_JIKA_ANIME_URL = 'https://api.jikan.moe/v3/anime/'
# BASE_MYANIME_LIST_URL = 'https://myanimelist.net/character/'

class AnimeFLV(object):   
    def __init__(self, *args, **kwargs):
        session = kwargs.get('session', None)
        self.__scraper = cloudscraper.create_scraper(sess=session)

    def downloadLinksByEpisodeID(self, id, **kwargs):
        """
        Get download links of specific episode.
        Return a list of dictionaries like:
        [
            {
                "server": "...",
                "url": "..."
            },
            ...
        ]

        :param id: Episode id, like as '36557/nanatsu-no-taizai-1'.
        :param **kwargs: Optional arguments for filter output (see doc).
        :rtype: list
        """
        res = self.__scraper.get(f"{ANIME_VIDEO_URL}{id}")
        body = res.text        
        soup = BeautifulSoup(body, 'lxml')
        table = soup.find('table', attrs={'class': 'RTbl'})

        latin = kwargs.get('lat', False)
        subtitled = kwargs.get('sub', True)

        try:
            rows = parseTable(table)
            ret = []

            for row in rows:
                if row['FORMATO'].string == 'SUB' and subtitled\
                    or row['FORMATO'].string == 'LAT' and latin:
                    ret.append({
                        'server': row['SERVIDOR'].string,
                        'url': re.sub(r'^http[s]?://ouo.io/[A-Za-z0-9]+/[A-Za-z0-9]+\?[A-Za-z0-9]+=', '', 
                            unquote(row['DESCARGAR'].a['href']))
                    })
                
            return ret
        except Exception:
            return []

    def search(self, query):
        """
        Search in animeflv.net by query.
        Return a list of dictionaries like:
        [
            {
                "id": "...",
                "title": "...",
                "poster": " ... ",
                "banner": "...",
                "type": "...",
                "synopsis": "...",
                "rating": "..."
                "debut": "...",
            },
            ...
        ]

        :param query: Query information like: 'Nanatsu no Taizai'.
        :rtype: list
        """

        res = self.__scraper.get(f"{SEARCH_URL}{quote(query)}")
        body = res.text
        soup = BeautifulSoup(body, 'lxml')
        elements = soup.select('div.Container ul.ListAnimes li article')

        ret = []
        for element in elements:
            try:
                ret.append({
                    'id': element.select_one('div.Description a.Button')['href'][1:],
                    'title': element.select_one('a h3').string,
                    'poster': element.select_one('a div.Image figure img')['src'] or element.select('a div.Image figure img')['data-cfsrc'],
                    'banner': (element.select_one('a div.Image figure img')['src'] or element.select('a div.Image figure img')['data-cfsrc']).replace('covers' , 'banners').strip(),
                    'type': element.select_one('div.Description p span.Type').string,
                    'synopsis': element.select('div.Description p')[1].string,
                    'rating': element.select_one('div.Description p span.Vts').string,
                    'debut': element.select_one('a span.Estreno').string.lower() if element.select_one('a span.Estreno') else None
                })
            except Exception:
                pass

        return ret
    def getLatestEpisodes(self):
        """
        List of the latest episodes uploaded by the platform
        """
        res = self.__scraper.get(f"{BASE_URL}")
        body = res.text
        soup = BeautifulSoup(body, 'lxml')
        elements = soup.select('main.Main ul.ListEpisodios li')
        response = []
        for element in elements:
            try:
                response.append({
                    'id': element.select_one('a.fa-play')['href'][1:],
                    'title': element.select_one('a.fa-play strong.Title').string,
                    'chapter': element.select_one('a.fa-play span.Capi').string,
                    'image':  element.select("a.fa-play span.Image img"),
                })
            except Exception:
                pass
        return response

    def ultimateAnime(self):
        """
        List of the ultimate added anime
        """
        res = self.__scraper.get(f"{BASE_URL}")
        body = res.text
        soup = BeautifulSoup(body, 'lxml')
        elements = soup.select('main.Main ul.ListAnimes li article.alt')
        response = []
        for element in elements:
            try:
                response.append({
                    'id': element.select_one('a')['href'][1:],
                    'title': element.select_one('a h3.Title').string,
                    'image': BASE_URL + element.select_one('a div.Image figure img')['src'],
                    'type': element.select_one('a span.Type').string,
                })
            except Exception:
                pass
        return response

    def emissionAnime(self):
        """
        List of the ultimate added anime
        """
        res = self.__scraper.get(f"{BASE_URL}")
        body = res.text
        soup = BeautifulSoup(body, 'lxml')
        elements = soup.select('div.BFluid aside.BFixed div.Emision div.Bod ul.ListSdbr li')
        response = []
        for element in elements:
            try:
                response.append({
                    'id': element.select_one('a')['href'][1:],
                    'title': element.select_one('a.fa-play-circle').contents[0],
                    'type': element.select_one('a span.Type').string,
                })
            except Exception:
                pass
        return response

    def allAnime(self,id=1):
        """
            get all animes
        """
        res = self.__scraper.get(f"{ORDER_TITLE}{id}")
        body = res.text
        soup = BeautifulSoup(body, 'lxml')
        elements = soup.select('main.Main ul.ListAnimes li article.Anime')
        response = []
        for element in elements:
            try:
                response.append({
                    'id': element.select_one('a')['href'][1:],
                    'title': element.select_one('a h3.Title').string,
                    'image': element.select_one('a div.Image figure img')['src'],
                    'type': element.select_one('a div.Image span.Type').string,
                    'synopsis': element.select('div.Description p')[1].string,
                    'total': soup.select_one('main.Main div.NvCnAnm ul.pagination li:nth-last-of-type(2)').string
                })
            except Exception:
                pass
        return response

    def getVideoServers(self, id, **kwargs):
        """
        Get in video servers, this work only using the iframe element.
        Return a list of dictionaries.    

        :param id: Episode id, like as '36557/nanatsu-no-taizai-1'.
        :rtype: list
        """

        res = self.__scraper.get(f"{ANIME_VIDEO_URL}{id}")
        body = res.text
        soup = BeautifulSoup(body, 'lxml')
        scripts = soup.find_all('script')

        latin = kwargs.get('lat', False)
        subtitled = kwargs.get('sub', True)
        servers = []

        for script in scripts:
            content = str(script)
            if 'var videos = {' in content:
                videos = content.split('var videos = ')[1].split(';')[0]
                data = json.loads(videos)
                if 'SUB' in data and subtitled:
                    servers.append(data['SUB'])
                if 'LAT' in data and latin:
                    servers.append(data['LAT'])
        return servers

    def getAnimeInfo(self, id):
        """
        Get information about specific anime.
        Return a dictionary.

        :param id: Anime id, like as 'anime/1590/nanatsu-no-taizai'.
        :rtype: dict
        """
        episodes, genres, extraInfo = self.__getAnimeEpisodesInfo__(id)
        data = []
        for info in extraInfo:
            try:
                data.append({
                    'title': info['title'],
                    'poster': info['poster'],
                    'synopsis': info['synopsis'],
                    'debut': info['debut'],
                    'type': info['type'],
                })
            except Exception:
                pass
        data.append({
            'id': id,
            'genres': genres or None,
            'episodes': episodes or None
            })
        
        return data

    def __getAnimeEpisodesInfo__(self, id):
        res = self.__scraper.get(f"{BASE_URL}/{id}")
        body = res.text    
        soup = BeautifulSoup(body, 'lxml')
        elements = soup.select('body div.Wrapper div.Body div')
        extraInfo = []
        for element in elements:
            try:
                extraInfo.append({
                    'title': element.select_one('div.Ficha.fchlt div.Container h1.Title').string,
                    'poster': BASE_URL + element.select_one('div.Container div.BFluid aside.SidebarA div.AnimeCover div.Image figure img')['src'],
                    'synopsis': element.select_one('div.Container div.Sp20 main.Main section.WdgtCn div.Description p').string,
                    'debut': element.select_one("div.Container div.Sp20 aside.SidebarA p.AnmStts span.fa-tv").string,
                    'type': element.select_one("div.Ficha.fchlt div.Container span.Type").string,
                })
            except Exception:
                pass
        
        genres = []

        for element in soup.select('main.Main section.WdgtCn nav.Nvgnrs a'):
            if '=' in element['href']:
                genres.append(element['href'].split('=')[1])

        info_ids = []
        episodes_data = []
        episodes = []

        try:
            for script in soup.find_all('script'):
                contents = str(script)

                if 'var anime_info = [' in contents:
                    anime_info = contents.split('var anime_info = ')[1].split(';')[0]
                    info_ids.append(json.loads(anime_info))
                
                if 'var episodes = [' in contents:
                    data = contents.split('var episodes = ')[1].split(';')[0]
                    episodes_data.extend(json.loads(data))

            AnimeThumbnailsId = info_ids[0][0]
            animeId = info_ids[0][2]
            # nextEpisodeDate = info_ids[0][3] if len(info_ids[0]) > 4 else None
            
            for episode, id in episodes_data:                
                episodes.append({
                    'episode': episode,
                    'id': f'{id}/{animeId}-{episode}',
                    'imagePreview': f'{BASE_EPISODE_IMG_URL}{AnimeThumbnailsId}/{episode}/th_3.jpg'
                })

        except Exception:
            pass

        return (episodes, genres, extraInfo)

__version__ = '2.0.0'
__title__ = 'animeflv'
__author__ = 'Jorge Alejandro Jimenez Luna'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 RevDev'