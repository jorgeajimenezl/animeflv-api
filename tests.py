from animeflv import AnimeFLV
import time

def test_init():
    api = AnimeFLV()
    assert api != None
    time.sleep(1.0)

def test_downloadLinksByEpisodeID():
    api = AnimeFLV()    
    out = api.downloadLinksByEpisodeID('36557/nanatsu-no-taizai-1')

    assert out != None
    assert isinstance(out, list)
    time.sleep(1.0)
    
def test_search():
    api = AnimeFLV()    
    out = api.search('Nanatsu no Taizai')

    assert out != None
    assert isinstance(out, list)
    time.sleep(1.0)

def test_getVideoServers():
    api = AnimeFLV()    
    out = api.getVideoServers('36557/nanatsu-no-taizai-1')

    assert out != None
    assert isinstance(out, list)
    time.sleep(1.0)

def test_getAnimeInfo():
    api = AnimeFLV()    
    out = api.getAnimeInfo('anime/1590/nanatsu-no-taizai')

    assert out != None
    assert isinstance(out, dict)
    time.sleep(1.0)