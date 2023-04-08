# AnimeFLV API

[![Build Status](https://github.com/jorgeajimenezl/animeflv-api/actions/workflows/python-package.yml/badge.svg)](https://github.com/jorgeajimenezl/animeflv-api/actions/workflows/python-package.yml)
[![Upload Python Package](https://github.com/jorgeajimenezl/animeflv-api/actions/workflows/python-publish.yml/badge.svg)](https://github.com/jorgeajimenezl/animeflv-api/actions/workflows/python-publish.yml)

> AnimeFLV is a python custom API for [animeflv.net](https://animeflv.net) a Spanish anime content website.

## Installation

For install with pip:

```bash
pip install animeflv
```

Install from source:

```bash
git clone https://github.com/jorgeajimenezl/animeflv-api.git
cd animeflv
git install -r requirements.txt
pip install .
```

## API Documentation

#### [Read this](https://github.com/jorgeajimenezl/animeflv-api/wiki) | [Watch videos](https://youtube.com)

#### Create animeflv api instance

```python
>>> from animeflv import AnimeFLV
>>> with AnimeFLV() as api:
>>>     # Do anything with api object
>>>    ...
```

#### Features

- [X] Get download links by episodes
- [X] Search
- [X] Get Video Servers
- [X] Get Anime Info
- [X] Get new releases (animes and episodes)

## License

[MIT](./LICENSE)

## Authors

- [Jorge Alejandro Jiménez Luna](https://github.com/jorgeajimenezl)
- [Jimmy Angel Pérez Díaz](https://github.com/JimScope)
