import cloudscraper
import json, re

from typing import Dict, List, Optional, Tuple, Type, Union
from types import TracebackType
from bs4 import BeautifulSoup, Tag, ResultSet
from urllib.parse import unquote, quote, urlencode
from enum import Flag, auto
from .exception import AnimeFLVParseError


def parse_table(table: Tag):
    columns = list([x.string for x in table.thead.tr.find_all("th")])
    rows = []

    for row in table.tbody.find_all("tr"):
        values = row.find_all("td")

        if len(values) != len(columns):
            raise AnimeFLVParseError("Don't match values size with columns size")

        rows.append({h: x for h, x in zip(columns, values)})

    return rows


BASE_URL = "https://animeflv.net"
BROWSE_URL = "https://animeflv.net/browse"
ANIME_VIDEO_URL = "https://animeflv.net/ver/"
ANIME_URL = "https://animeflv.net/anime/"
BASE_EPISODE_IMG_URL = "https://cdn.animeflv.net/screenshots/"


class EpisodeFormat(Flag):
    Subtitled = auto()
    Dubbed = auto()


class AnimeFLV(object):
    def __init__(self, *args, **kwargs):
        session = kwargs.get("session", None)
        self._scraper = cloudscraper.create_scraper(session)

    def close(self) -> None:
        self._scraper.close()

    def __enter__(self) -> "AnimeFLV":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        self.close()

    def get_links(
        self,
        id: str,
        episode: Union[str, int],
        format: EpisodeFormat = EpisodeFormat.Subtitled,
        **kwargs,
    ) -> List[Dict[str, str]]:
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

        :param id: Anime id, like as 'nanatsu-no-taizai'.
        :param episode: Episode id, like as '1'.
        :param **kwargs: Optional arguments for filter output (see doc).
        :rtype: list
        """
        response = self._scraper.get(f"{ANIME_VIDEO_URL}{id}-{episode}")
        soup = BeautifulSoup(response.text, "lxml")
        table = soup.find("table", attrs={"class": "RTbl"})

        try:
            rows = parse_table(table)
            ret = []

            for row in rows:
                if (
                    row["FORMATO"].string == "SUB"
                    and EpisodeFormat.Subtitled in format
                    or row["FORMATO"].string == "LAT"
                    and EpisodeFormat.Dubbed in format
                ):
                    ret.append(
                        {
                            "server": row["SERVIDOR"].string,
                            "url": re.sub(
                                r"^http[s]?://ouo.io/[A-Za-z0-9]+/[A-Za-z0-9]+\?[A-Za-z0-9]+=",
                                "",
                                unquote(row["DESCARGAR"].a["href"]),
                            ),
                        }
                    )

            return ret
        except Exception as e:
            raise AnimeFLVParseError(e)

    def list(self, page: int = None) -> List[Dict[str, str]]:
        """
        Shortcut for search(query=None)
        """

        return self.search(page=page)

    def search(self, query: str = None, page: int = None) -> List[Dict[str, str]]:
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
        :param page: Page of the information return.
        :rtype: list
        """

        if page is not None and not isinstance(page, int):
            raise TypeError

        params = dict()
        if query is not None:
            params["q"] = query
        if page is not None:
            params["page"] = page
        params = urlencode(params)

        url = f"{BROWSE_URL}"
        if params != "":
            url += f"?{params}"

        response = self._scraper.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        elements = soup.select("div.Container ul.ListAnimes li article")

        if elements is None:
            raise AnimeFLVParseError("Unable to get list of animes")

        return self._process_anime_list_info(elements)

    def get_video_servers(
        self,
        id: str,
        episode: int,
        format: EpisodeFormat = EpisodeFormat.Subtitled,
        **kwargs,
    ) -> List[Dict[str, str]]:
        """
        Get in video servers, this work only using the iframe element.
        Return a list of dictionaries.

        :param id: Anime id, like as 'nanatsu-no-taizai'.
        :param episode: Episode id, like as '1'.
        :rtype: list
        """

        response = self._scraper.get(f"{ANIME_VIDEO_URL}{id}-{episode}")
        soup = BeautifulSoup(response.text, "lxml")
        scripts = soup.find_all("script")

        servers = []

        for script in scripts:
            content = str(script)
            if "var videos = {" in content:
                videos = content.split("var videos = ")[1].split(";")[0]
                data = json.loads(videos)

                if "SUB" in data and EpisodeFormat.Subtitled in format:
                    servers.append(data["SUB"])
                if "LAT" in data and EpisodeFormat.Dubbed in format:
                    servers.append(data["LAT"])

        return servers

    def get_latest_episodes(self) -> List[Dict[str, str]]:
        """
        Get a list of new episodes released (possibly this last week).
        Return a list

        :rtype: list
        """

        response = self._scraper.get(BASE_URL)
        soup = BeautifulSoup(response.text, "lxml")

        elements = soup.select("ul.ListEpisodios li a")
        ret = []

        for element in elements:
            try:
                anime, _, id = element["href"].rpartition("-")

                ret.append(
                    {
                        "id": id,
                        "anime": anime.removeprefix("/ver/"),
                        "image_preview": f"{BASE_URL}{element.select_one('span.Image img')['src']}",
                    }
                )
            except Exception as e:
                raise AnimeFLVParseError(e)

        return ret

    def get_latest_animes(self) -> List[Dict[str, str]]:
        """
        Get a list of new animes released.
        Return a list

        :rtype: list
        """

        response = self._scraper.get(BASE_URL)
        soup = BeautifulSoup(response.text, "lxml")

        elements = soup.select("ul.ListAnimes li article")

        if elements is None:
            raise AnimeFLVParseError("Unable to get list of animes")

        return self._process_anime_list_info(elements)

    def get_anime_info(
        self, id: str
    ) -> Dict[str, Union[Dict[str, str], List[str], str]]:
        """
        Get information about specific anime.
        Return a dictionary.

        :param id: Anime id, like as 'nanatsu-no-taizai'.
        :rtype: dict
        """
        episodes, genres, extraInfo = self._get_anime_episodes_info(id)

        return {
            "id": id,
            "title": extraInfo["title"] or None,
            "poster": extraInfo["poster"] or None,
            "banner": extraInfo["banner"] or None,
            "synopsis": extraInfo["synopsis"] or None,
            "rating": extraInfo["rating"] or None,
            "debut": extraInfo["debut"] or None,
            "type": extraInfo["type"] or None,
            "genres": genres or None,
            "episodes": episodes or None,
        }

    def _process_anime_list_info(
        self, elements: ResultSet
    ) -> List[Dict[str, str]]:
        ret = []

        for element in elements:
            try:
                ret.append(
                    {
                        "id": element.select_one("div.Description a.Button")["href"][
                            1:
                        ].removeprefix("anime/"),
                        "title": element.select_one("a h3").string,
                        "poster": (
                            element.select_one("a div.Image figure img").get(
                                "src", None
                            )
                            or element.select("a div.Image figure img")["data-cfsrc"]
                        ),
                        "banner": (
                            element.select_one("a div.Image figure img").get(
                                "src", None
                            )
                            or element.select("a div.Image figure img")["data-cfsrc"]
                        )
                        .replace("covers", "banners")
                        .strip(),
                        "type": element.select_one(
                            "div.Description p span.Type"
                        ).string,
                        "synopsis": (
                            element.select("div.Description p")[1].string.strip()
                            if element.select("div.Description p")[1].string
                            else None
                        ),
                        "rating": element.select_one(
                            "div.Description p span.Vts"
                        ).string,
                        "debut": (
                            element.select_one("a span.Estreno").string.lower()
                            if element.select_one("a span.Estreno")
                            else None
                        ),
                    }
                )
            except Exception as e:
                raise AnimeFLVParseError(e)

        return ret

    def _get_anime_episodes_info(
        self, id: str
    ) -> Tuple[List[Dict[str, str]], List[str], Dict[str, str]]:
        response = self._scraper.get(f"{ANIME_URL}/{id}")
        soup = BeautifulSoup(response.text, "lxml")

        information = {
            "title": soup.select_one(
                "body div.Wrapper div.Body div div.Ficha.fchlt div.Container h1.Title"
            ).string,
            "poster": BASE_URL
            + "/"
            + soup.select_one(
                "body div div div div div aside div.AnimeCover div.Image figure img"
            )["src"],
            "synopsis": soup.select_one(
                "body div div div div div main section div.Description p"
            ).string.strip(),
            "rating": soup.select_one(
                "body div div div.Ficha.fchlt div.Container div.vtshr div.Votes span#votes_prmd"
            ).string,
            "debut": soup.select_one(
                "body div.Wrapper div.Body div div.Container div.BX.Row.BFluid.Sp20 aside.SidebarA.BFixed p.AnmStts"
            ).string,
            "type": soup.select_one(
                "body div.Wrapper div.Body div div.Ficha.fchlt div.Container span.Type"
            ).string,
        }
        information["banner"] = (
            information["poster"].replace("covers", "banners").strip()
        )
        genres = []

        for element in soup.select("main.Main section.WdgtCn nav.Nvgnrs a"):
            if "=" in element["href"]:
                genres.append(element["href"].split("=")[1])

        info_ids = []
        episodes_data = []
        episodes = []

        try:
            for script in soup.find_all("script"):
                contents = str(script)

                if "var anime_info = [" in contents:
                    anime_info = contents.split("var anime_info = ")[1].split(";")[0]
                    info_ids.append(json.loads(anime_info))

                if "var episodes = [" in contents:
                    data = contents.split("var episodes = ")[1].split(";")[0]
                    episodes_data.extend(json.loads(data))

            AnimeThumbnailsId = info_ids[0][0]
            animeId = info_ids[0][2]
            # nextEpisodeDate = info_ids[0][3] if len(info_ids[0]) > 4 else None

            for episode, id in episodes_data:
                episodes.append(
                    {
                        "id": episode,
                        "image_preview": f"{BASE_EPISODE_IMG_URL}{AnimeThumbnailsId}/{episode}/th_3.jpg",
                    }
                )

        except Exception as e:
            raise AnimeFLVParseError(e)

        return (episodes, genres, information)
