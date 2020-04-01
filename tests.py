from animeflv import AnimeFLV

def test_init():
    api = AnimeFLV()
    assert api != None

def test_downloadLinksByEpisodeID():
    api = AnimeFLV()    
    out = api.downloadLinksByEpisodeID('36557/nanatsu-no-taizai-1')

    assert out != None
    assert isinstance(out, list)
    assert len(out) != 0
    assert isinstance(out[0], dict)
    
def test_search():
    api = AnimeFLV()    
    out = api.search('Nanatsu no Taizai')

    assert out != None
    assert isinstance(out, list)
    assert len(out) != 0
    assert isinstance(out[0], dict)