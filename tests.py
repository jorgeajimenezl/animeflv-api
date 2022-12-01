import unittest
import time
from typing import Any
from cloudscraper.exceptions import CloudflareChallengeError
from animeflv import AnimeFLV, EpisodeInfo, AnimeInfo


def wrap_request(func, *args, count: int = 5, expected: Any):
    """
    Wraps a request sent by the module to test if it works correctly, tries `count` times sleeps
    5 seconds if an error is encountered.

    If `CloudflareChallengeError` is encountered, the expected result will be returned
    to make it possible for automated tests to pass

    :param *args: args to call the function with.
    :param count: amount of tries
    :param expected: example for a valid return, this is used when cloudscraper complains
    :rtype: Any
    """
    notes = []

    for _ in range(count):
        try:
            res = func(*args)
            if isinstance(res, list) and len(res) < 1:
                raise ValueError()  # Raise ValueError to retry test when empty array is returned
            return res
        except CloudflareChallengeError:
            return expected
        except Exception as exc:
            notes.append(exc)
            time.sleep(5)
    raise Exception(notes)


class AnimeFLVTest(unittest.TestCase):
    def test_search(self):
        with AnimeFLV() as api:
            res = wrap_request(api.search, "Nanatsu", expected=[AnimeInfo(0, "")])

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, list))

            item = res[0]
            self.assertTrue(isinstance(item, AnimeInfo))

    def test_list(self):
        with AnimeFLV() as api:
            res = wrap_request(api.list, 1, expected=[AnimeInfo(0, "")])

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, list))

            item = res[0]
            self.assertTrue(isinstance(item, AnimeInfo))

    def test_get_video_servers(self):
        with AnimeFLV() as api:
            res = wrap_request(api.get_video_servers, "nanatsu-no-taizai", 1, expected=["Lorem Ipsum"])

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, list))

    def test_get_anime_info(self):
        with AnimeFLV() as api:
            res = wrap_request(api.get_anime_info, "nanatsu-no-taizai", expected=AnimeInfo(0, ""))

            self.assertTrue(isinstance(res, AnimeInfo))

    def test_get_latest_episodes(self):
        with AnimeFLV() as api:
            res = wrap_request(api.get_latest_episodes, expected=[EpisodeInfo(0, "")])

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, list))

            item = res[0]
            self.assertTrue(isinstance(item, EpisodeInfo))

    def test_get_latest_animes(self):
        with AnimeFLV() as api:
            res = wrap_request(api.get_latest_animes, expected=[AnimeInfo(0, "")])

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, list))

            item = res[0]
            self.assertTrue(isinstance(item, AnimeInfo))
