## WARNING: This project wont receive any further fixes. 
It is deprecated in favor of docker container with controller. 
See [unifi-docker](https://github.com/jacobalberty/unifi-docker).

# Ubnt downloader

Simple python script that downloads specific or last (by release date) released
version of unifi controller for unix. Ubnt do not provide link to 
this package on [download site](https://www.ubnt.com/download/unifi).

## Requiremets

 * Python 3
 * [Selenium Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/)
 * Google Chrome (it is possible to implement other browser support 
 but only Chrome and [PhantomJS](http://phantomjs.org/) support headless directly so currently 
 only Chrome is supported)
 * Python deps from [requirements.txt](requirements.txt)
 
## Instalation

 1. Install system dependencies from above
 1. Install Python dependencies via pip:
     ```bash
    pip3 install -r requiremets.txt
    ```

## Usage

script reads commandline arguments and provide help

### Download last version

```bash
python3 downloader.py 
```

### Download specific version

```bash
python3 downloader.py --version 5.6.36
```

### Save to specific file

```bash
python3 downloader.py -o output_file.zip
```

