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
$ git clone https://github.com/jorgeajimenezl/animeflv-api.git
$ cd animeflv
$ git install -r requirements.txt
$ pip install .
```

## API Documentation
#### [Read this](https://github.com/jorgeajimenezl/animeflv-api/wiki) | [Watch videos](https://youtube.com)

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
    }
]
```

#### Search:
Example: Search **Nanatsu no Taizai**:
```python
>>> api.search('Nanatsu no Taizai')
```
Output:
```json
[
    {
        "id": "anime/1590/nanatsu-no-taizai",
        "title": "Nanatsu no Taizai",
        "poster": "https://animeflv.net/uploads/animes/covers/1620.jpg",
        "banner": "https://animeflv.net/uploads/animes/banners/1620.jpg",
        "type": "Anime",
        "synopsis": "Los \u201cSiete Pecados Capitales\u201d, un grupo de caballeros malignos que conspiraron para derrocar al Reino de Britania, se dice que fueron erradicados por los Caballeros Sagrados, aunque algunos dicen que a\u00fan viven. Diez a\u00f1os despu\u00e9s, los Caballeros Sagrados dieron un golpe de estado y asesinaron al rey, convirti\u00e9...",
        "rating": "4.6",
        "debut": ""
    },
    {
        "id": "anime/2997/sin-nanatsu-no-taizai",
        "title": "Sin: Nanatsu no Taizai",
        "poster": "https://animeflv.net/uploads/animes/covers/2731.jpg",
        "banner": "https://animeflv.net/uploads/animes/banners/2731.jpg",
        "type": "Anime",
        "synopsis": "El contexto de la franquicia gira en torno a siete f\u00e9minas que encarnan los siete pecados capitales: lujuria, pereza, gula, ira, envidia, avaricia y soberbia.",
        "rating": "4.3",
        "debut": ""
    },
    {
        "id": "anime/5650/nanatsu-no-taizai-kamigami-no-gekirin",
        "title": "Nanatsu no Taizai: Kamigami no Gekirin",
        "poster": "https://animeflv.net/uploads/animes/covers/3211.jpg",
        "banner": "https://animeflv.net/uploads/animes/banners/3211.jpg",
        "type": "Anime",
        "synopsis": "Nueva temporada de Nanatsu no Taizai",
        "rating": "4.1",
        "debut": ""
    },
    {
        "id": "anime/5041/nanatsu-no-taizai-imashime-no-fukkatsu",
        "title": "Nanatsu no Taizai: Imashime no Fukkatsu",
        "poster": "https://animeflv.net/uploads/animes/covers/2895.jpg",
        "banner": "https://animeflv.net/uploads/animes/banners/2895.jpg",
        "type": "Anime",
        "synopsis": "Nueva temporada de la serie Nanatsu no Taizai.",
        "rating": "4.6",
        "debut": ""
    },
    {
        "id": "anime/5503/nanatsu-no-taizai-movie-tenkuu-no-torawarebito",
        "title": "Nanatsu no Taizai Movie: Tenkuu no Torawarebito",
        "poster": "https://animeflv.net/uploads/animes/covers/3065.jpg",
        "banner": "https://animeflv.net/uploads/animes/banners/3065.jpg",
        "type": "Pel\u00edcula",
        "synopsis": "Los Siete Pecados Capitales viajan a una remota isla en busca del ingrediente conocido como \"pez cielo\". Meliodas y Hawk acaban en el \"Palacio del Cielo\", el cual existe m\u00e1s all\u00e1 de las nubes y est\u00e1 habitado por seres alados. A su llegada, Meliodas es confundido con un chico que cometi\u00f3 un crimen y acaba en prisi\u00f3n. Mientras, sus habitantes pr...",
        "rating": "4.5",
        "debut": ""
    }
]
```

## License
[MIT](./LICENSE)

## Authors
+ [Jorge Alejandro Jimenez Luna](https://github.com/jorgeajimenezl)
+ [Jimmy Angel Pérez Díaz](https://github.com/JimScope)
+ [Victor Javier Lopez Roque](https://github.com/VictorJaja)

Copyright © 2020 [RevolutionDev](https://revdev.xyz).
