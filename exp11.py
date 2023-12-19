import requests
def simple_scraper(url):
    response=requests.get(url)
    if response.status_code==200:
        print("Content",response.text)
    else:
        print("failed",response.status_code)
url_to_scrap ="http://ajce.in"
simple_scraper(url_to_scrap)