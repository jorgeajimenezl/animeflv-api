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
Example: Get download links of **episode 1 of Nanatsu no Taizai Season 1**:
```python
>>> api.downloadLinksByEpisodeID('36557/nanatsu-no-taizai-1')
```
Output:
```json
[
    {
        "server": "Zippyshare",
        "url": "http://www9.zippyshare.com/v/tnAF0l2S/file.html"
    },
    {
        "server": "MEGA",
        "url": "https://mega.nz/#!yagHlRKB!AKBvkABb-kiMnb02tMfQDgARiTcAOCIOjPB-MLTxO5s"
    },
    {
        "server": "Openload",
        "url": "https://openload.co/f/MIiuhaEG680/"
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

#### Get Video Servers:
Example: Obtaining video servers of **episode 1 of Nanatsu no Taizai Season 1**:
```python
>>> api.getVideoServers('36557/nanatsu-no-taizai-1')
```
Output:
```json
[
    [
        {
            "server": "amus",
            "title": "Izanagi",
            "allow_mobile": true,
            "code": "https://s1.animeflv.net/embed.php?s=izanagi&v=dE9WckYxM0QzMnZkK1pmTUxvOEIzNkE1OE96YktRSzRCRFpQWmFkQ3MrMlN3d0xBVHliZmlVUU9SUVJQMmtXSGR6V0tyNmxjaGYzRTlyVGxkelM3MU9ySmFXanZ5VHM5NWEwazFSbFVTMmlERG1VbUE0a2JPZTFoWTdQeHZGOEY3TDRSVWMvMEMycnc0Wk1RSDdsejhnPT0="
        },
        {
            "server": "fembed",
            "title": "Fembed",
            "allow_mobile": true,
            "code": "https://s1.animeflv.net/redirector.php?top=/ver/36557/nanatsu-no-taizai-1&server=fembed&value="
        },
        {
            "server": "mega",
            "title": "MEGA",
            "url": "https://mega.nz/#!yagHlRKB!AKBvkABb-kiMnb02tMfQDgARiTcAOCIOjPB-MLTxO5s",
            "allow_mobile": true,
            "code": "https://s1.animeflv.net/redirector.php?top=/ver/36557/nanatsu-no-taizai-1&server=mega&value=!yagHlRKB!AKBvkABb-kiMnb02tMfQDgARiTcAOCIOjPB-MLTxO5s"
        },
        {
            "server": "okru",
            "title": "Okru",
            "allow_mobile": true,
            "code": "https://ok.ru/videoembed/1225695693322"
        },
        {
            "server": "yu",
            "title": "YourUpload",
            "allow_mobile": true,
            "code": "https://www.yourupload.com/embed/md8EfHmrylKX"
        },
        {
            "server": "maru",
            "title": "Maru",
            "allow_mobile": true,
            "code": "https://my.mail.ru/video/embed/8995617145282890301#budyak.rus#2621"
        },
        {
            "server": "netu",
            "title": "Netu",
            "allow_mobile": true,
            "code": "https://hqq.tv/player/embed_player.php?vid=276224236260234223262278263266254209194271217261258"
        }
    ]
]
```

#### Get Anime Info:
Example: Obtaining information about **Nanatsu no Taizai Season 1**:
```python
>>> api.getAnimeInfo('anime/1590/nanatsu-no-taizai')
```
Output:
```json
{
    "id": "anime/1590/nanatsu-no-taizai",
    "title": "Nanatsu no Taizai",
    "poster": "https://animeflv.net//uploads/animes/covers/1620.jpg",
    "banner": "https://animeflv.net//uploads/animes/banners/1620.jpg",
    "synopsis": "Los \u201cSiete Pecados Capitales\u201d, un grupo de caballeros malignos que conspiraron para derrocar al Reino de Britania, se dice que fueron erradicados por los Caballeros Sagrados, aunque algunos dicen que a\u00fan viven. Diez a\u00f1os despu\u00e9s, los Caballeros Sagrados dieron un golpe de estado y asesinaron al rey, convirti\u00e9ndose en los nuevos y tir\u00e1nicos regidores del reino. Elizabeth, la \u00fanica hija del rey, emprende un viaje para encontrar a los \u201cSiete Pecados Capitales\u201d y conseguir su ayuda para recuperar el reino.",
    "rating": "4.6",
    "debut": "Finalizado",
    "type": "Anime",
    "genres": [
        "accion",
        "aventura",
        "ecchi",
        "fantasia",
        "shounen",
        "sobrenatural"
    ],
    "episodes": [
        {
            "episode": 26,
            "id": "36645/nanatsu-no-taizai-26",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/26/th_3.jpg"
        },
        {
            "episode": 25,
            "id": "35491/nanatsu-no-taizai-25",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/25/th_3.jpg"
        },
        {
            "episode": 24,
            "id": "36580/nanatsu-no-taizai-24",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/24/th_3.jpg"
        },
        {
            "episode": 23,
            "id": "36579/nanatsu-no-taizai-23",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/23/th_3.jpg"
        },
        {
            "episode": 22,
            "id": "36578/nanatsu-no-taizai-22",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/22/th_3.jpg"
        },
        {
            "episode": 21,
            "id": "36577/nanatsu-no-taizai-21",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/21/th_3.jpg"
        },
        {
            "episode": 20,
            "id": "36576/nanatsu-no-taizai-20",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/20/th_3.jpg"
        },
        {
            "episode": 19,
            "id": "36575/nanatsu-no-taizai-19",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/19/th_3.jpg"
        },
        {
            "episode": 18,
            "id": "36574/nanatsu-no-taizai-18",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/18/th_3.jpg"
        },
        {
            "episode": 17,
            "id": "36573/nanatsu-no-taizai-17",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/17/th_3.jpg"
        },
        {
            "episode": 16,
            "id": "36572/nanatsu-no-taizai-16",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/16/th_3.jpg"
        },
        {
            "episode": 15,
            "id": "36571/nanatsu-no-taizai-15",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/15/th_3.jpg"
        },
        {
            "episode": 14,
            "id": "36570/nanatsu-no-taizai-14",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/14/th_3.jpg"
        },
        {
            "episode": 13,
            "id": "36569/nanatsu-no-taizai-13",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/13/th_3.jpg"
        },
        {
            "episode": 12,
            "id": "36568/nanatsu-no-taizai-12",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/12/th_3.jpg"
        },
        {
            "episode": 11,
            "id": "36567/nanatsu-no-taizai-11",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/11/th_3.jpg"
        },
        {
            "episode": 10,
            "id": "36566/nanatsu-no-taizai-10",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/10/th_3.jpg"
        },
        {
            "episode": 9,
            "id": "36565/nanatsu-no-taizai-9",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/9/th_3.jpg"
        },
        {
            "episode": 8,
            "id": "36564/nanatsu-no-taizai-8",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/8/th_3.jpg"
        },
        {
            "episode": 7,
            "id": "36563/nanatsu-no-taizai-7",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/7/th_3.jpg"
        },
        {
            "episode": 6,
            "id": "36562/nanatsu-no-taizai-6",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/6/th_3.jpg"
        },
        {
            "episode": 5,
            "id": "36561/nanatsu-no-taizai-5",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/5/th_3.jpg"
        },
        {
            "episode": 4,
            "id": "36560/nanatsu-no-taizai-4",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/4/th_3.jpg"
        },
        {
            "episode": 3,
            "id": "36559/nanatsu-no-taizai-3",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/3/th_3.jpg"
        },
        {
            "episode": 2,
            "id": "36558/nanatsu-no-taizai-2",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/2/th_3.jpg"
        },
        {
            "episode": 1,
            "id": "36557/nanatsu-no-taizai-1",
            "imagePreview": "https://cdn.animeflv.net/screenshots/1620/1/th_3.jpg"
        }
    ]
}
```

## License
[MIT](./LICENSE)

## Authors
+ [Jorge Alejandro Jimenez Luna](https://github.com/jorgeajimenezl)
+ [Jimmy Angel Pérez Díaz](https://github.com/JimScope)

Copyright © 2021 [RevDev](https://revdev.cc).
