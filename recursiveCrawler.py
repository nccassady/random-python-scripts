import urllib2
from bs4 import BeautifulSoup

def FindLinks(url):
    links = []
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    soup = BeautifulSoup(html)
    for link in soup.find_all(href=True):
        try:
            if link.get('href') in links:
                break
            else:
                if link.get('href').find('accounts.google') > -1 \
                        or link.get('href').find('google.com') > -1:
                    pass
                else:
                    print link.get('href')
                    links.append(link.get('href'))
                    FindLinks(link.get('href'))
        except:
            pass
    return links