import unittest
import time
from animeflv import AnimeFLV


def wrap_request(func, *args, count: int = 5):
    notes = []

    while True:
        try:
            r = func(*args)
            return r
        except Exception as e:
            if count > 0:
                count -= 1
                notes.append(e)

                time.sleep(5)
            else:
                raise Exception([e] + notes)


class AnimeFLVTest(unittest.TestCase):
    def test_search(self):
        with AnimeFLV() as api:
            res = wrap_request(api.search, "Nanatsu no Taizai")

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, list))

            item = res[0]
            self.assertTrue(isinstance(item, dict))

    def test_list(self):
        with AnimeFLV() as api:
            res = wrap_request(api.list, 1)

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, list))

            item = res[0]
            self.assertTrue(isinstance(item, dict))

    def test_get_video_servers(self):
        with AnimeFLV() as api:
            res = wrap_request(api.get_video_servers, "nanatsu-no-taizai", 1)

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, list))

    def test_get_anime_info(self):
        with AnimeFLV() as api:
            res = wrap_request(api.get_anime_info, "nanatsu-no-taizai")

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, dict))

    def test_get_latest_episodes(self):
        with AnimeFLV() as api:
            res = wrap_request(api.get_latest_episodes)

            self.assertGreater(len(res), 0)
            self.assertTrue(isinstance(res, list))

            item = res[0]
            self.assertTrue(isinstance(item, dict))
