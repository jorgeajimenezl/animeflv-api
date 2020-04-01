import re
from setuptools import setup, find_packages

version = ''
with open('animeflv/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

with open('requirements.txt', 'r') as fd:
    INSTALL_REQUIRES = (fd.read().split())

with open('README.md', 'r') as readme:
    setup(
        name='animeflv',
        version=version,
        description="AnimeFLV is a python custom API for https://animeflv.net website",
        long_description=ascii(readme.read()),
        license="MIT License",
        author="Jorge Alejandro Jimenez Luna",
        author_email="jorgeajimenezl@nauta.cu",
        url="https://github.com/jorgeajimenezl/animeflv",
        classifiers=[
            "Intended Audience :: Developers",
            "License :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
        ],
        keywords="animeflv anime videos manga",
        install_requires=INSTALL_REQUIRES,
        test_suite="tests",
        packages=[
            "animeflv"
        ],
        package_dir={'animeflv': 'animeflv'},
        zip_safe=False,
    )