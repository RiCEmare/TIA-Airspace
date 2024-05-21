''' This module contains functions to download images from the internet. '''
import urllib3

def urltweaker(url):
    ''' This function modifies the url to download the full image instead of the thumbnail.'''
    parts = url.split("/")
    for i, part in enumerate(parts):
        if part.endswith(".com"):
            parts[i+1] = "full"
            break
    parts[-1] = parts[-1].replace("_tb", "")
    modified_url = "/".join(parts)
    return modified_url

def download_image(url, aircraft=True):
    ''' This function downloads the image from the given url and saves it to the given location. '''
    http = urllib3.PoolManager()
    if aircraft:
        modified_url = urltweaker(url)
    else:
        modified_url = url
    response = http.request('GET', modified_url)
    with open("/tmp/image.jpg", 'wb') as file:
        file.write(response.data)
    return r"/tmp/image.jpg"
