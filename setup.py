import re
from setuptools import setup, find_packages

with open('animeflv/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

with open('requirements.txt', 'r') as file:                        
    INSTALL_REQUIRES = file.readlines()

with open('README.md', 'r') as readme:
    setup(
        name='animeflv',
        version=version,
        description="AnimeFLV is a python custom API for https://animeflv.net website",
        long_description=readme.read(),
        long_description_content_type='text/markdown',
        license="MIT License",
        author="Jorge Alejandro Jimenez Luna",
        author_email="jorgeajimenezl17@gmail.com",
        url="https://github.com/jorgeajimenezl/animeflv-api",
        classifiers=[
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        keywords="animeflv, anime, videos, manga",
        install_requires=INSTALL_REQUIRES,
        test_suite="tests",
        packages=find_packages(),
    )