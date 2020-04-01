import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import unquote, quote
import requests, json

def parseTable(table):
    columns = list([x.string for x in table.thead.tr.find_all('th')])
    rows = []
    
    for row in table.tbody.find_all('tr'):
        values = row.find_all('td')

        if len(values) != len(columns):
            raise Exception("don't match values size with columns size")

        rows.append({h: x for h, x in zip(columns, values)})

    return rows

class AnimeFLV(object):
    BASE_URL = 'https://animeflv.net/'
    BROWSE_URL = 'https://animeflv.net/browse?'
    SEARCH_URL = 'https://animeflv.net/browse?q='
    ANIME_VIDEO_URL = 'https://animeflv.net/ver/'
    # BASE_EPISODE_IMG_URL = 'https://cdn.animeflv.net/screenshots/'
    # BASE_JIKA_URL = ' https://api.jikan.moe/v3/search/anime?q='
    # BASE_JIKA_ANIME_URL = 'https://api.jikan.moe/v3/anime/'
    # BASE_MYANIME_LIST_URL = 'https://myanimelist.net/character/'
    
    def __init__(self, *args, **kwargs):
        self.scraper = cloudscraper.create_scraper()

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
        res = self.scraper.get(f"{self.ANIME_VIDEO_URL}{id}")
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
                        'url': unquote(row['DESCARGAR'].a['href'])
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

        res = self.scraper.get(f"{self.SEARCH_URL}{quote(query)}")
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
                    'synopsis': element.select('div.Description p')[1].string.strip(),
                    'rating': element.select_one('div.Description p span.Vts').string,
                    'debut': element.select_one('a span.Estreno').string.lower() if element.select_one('a span.Estreno') else ''
                })
            except Exception:
                pass

        return ret

    # def getVideoServers(self, id):
    #     """
    #     Get in video servers, this work only using the iframe element.
    #     Return a list of dictionaries.    

    #     :param id: Episode id, like as '36557/nanatsu-no-taizai-1'.
    #     :rtype: list
    #     """

    #     res = self.scraper.get(f"{self.ANIME_VIDEO_URL}{id}")
    #     body = res.text
    #     soup = BeautifulSoup(body, 'lxml')
    #     scripts = soup.find_all('script')

    #     for script in scripts:
    #         content = str(script)
    #         if 'var videos = {' in content:
    #             videos = content.split('var videos = ')[1].split(';')[0]
    #             data = json.loads(videos)
    #             serverlist = data['SUB']

    #             return serverlist

    #     return []

__version__ = '0.0.1'
__title__ = 'animeflv'
__author__ = 'Jorge Aleandro Jimenez Luna'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 RevolutionDev'