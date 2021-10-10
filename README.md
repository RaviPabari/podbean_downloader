# podbean_downloader
Downloads podcast from creator's podbean url.

## Clone the repo
```
$ git clone https://github.com/RaviPabari/podbean_downloader
$ cd podbean_downloader/
```
## Activate the python virtual env
```
$ source podbean/bin/activate
```
## Usage
```
usage: downloader.py [-h] [-p PAGES] -u URL [-l LOCATION]

This will download podcasts from podbean to the current working directory

optional arguments:
  -h, --help            show this help message and exit
  -p PAGES, --pages PAGES
  -u URL, --url URL
  -l LOCATION, --location LOCATION
```

## Example
```
$ python downloader.py -u https://neilbhatt.podbean.com/ -p 2 -l folder_name
```
![image](https://user-images.githubusercontent.com/46424422/136688220-9420327e-d7a1-4dfa-aeda-fbb09540a77d.png)
