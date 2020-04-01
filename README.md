# AnimeFLV API

[![Build Status](https://travis-ci.com/jorgeajimenezl/animeflv-api.svg?branch=master)](https://travis-ci.com/jorgeajimenezl/animeflv-api)

> AnimeFLV is a python custom API for [animeflv.net](https://animeflv.net) a Spanish anime content website.

## Installation
For install with pip:
```bash
$ pip install animeflv
```

Install from source:
```bash
$ git clone https://github.com/
$ jorgeajimenezl/animeflv.git
$ cd animeflv
$ git submodule --recursive update
$ pip install .
```

## API Documentation
#### [Read this](https://github.com/jorgeajimenezl/animeflv/wiki) | [Watch videos](https://youtube.com)

#### Create animeflv api instance:
```python
>>> from animeflv import AnimeFLV
>>> api = AnimeFLV()
```

#### Get download links by episodes:
Example: Get download links of episode 1 of Nanatsu no Taizai Season 1:
```python
>>> api.downloadLinksByEpisodeID('36557/nanatsu-no-taizai-1')
```
Output:
```json
[
    {
        "server": "Zippyshare",
        "url": "http://ouo.io/s/y0d65LCP?s=http://www9.zippyshare.com/v/tnAF0l2S/file.html"
    },
    {
        "server": "MEGA",
        "url": "http://ouo.io/s/y0d65LCP?s=https://mega.nz/#!yagHlRKB!AKBvkABb-kiMnb02tMfQDgARiTcAOCIOjPB-MLTxO5s"
    },
    {
        "server": "Openload",
        "url": "http://ouo.io/s/y0d65LCP?s=https://openload.co/f/MIiuhaEG680/"
    },
    {
        "server": "MEGA",
        "url": "http://ouo.io/s/y0d65LCP?s=https://mega.nz/#!XnRzFSIQ!NSNLmlXjp_liEe8_zoxTXGaJoszC3IcmwNN25FgcZr0"
    },
    {
        "server": "Zippyshare",
        "url": "http://ouo.io/s/y0d65LCP?s=https://www113.zippyshare.com/v/xfkBpxAX/file.html"
    }
]
```

## License
[MIT](./LICENSE)

## Authors
+ [Jorge Alejandro Jimenez Luna](https://github.com/jorgeajimenezl)
+ [Jimmy Angel](https://github.com/JimScope)
+ [Victor Javier Lopez Roque](https://github.com/VictorJaja)

Copyright © 2020 [RevolutionDev](https://revdev.xyz).