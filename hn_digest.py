from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(mega_links, mega_subtext):
    hn = []
    for idx, item in enumerate(mega_links):
        title = item.getText()
        href = item.get('href', None)
        vote = mega_subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


digest = create_custom_hn(mega_links, mega_subtext)

news1 = {
    digest[0]['title'],
    digest[0]['votes'],
    digest[0]['link']
}

news2 = {
    digest[1]['title'],
    digest[1]['votes'],
    digest[1]['link']
}

news3 = {
    digest[2]['title'],
    digest[2]['votes'],
    digest[2]['link']
}

news4 = {
    digest[3]['title'],
    digest[3]['votes'],
    digest[3]['link']
}

news5 = {
    digest[4]['title'],
    digest[4]['votes'],
    digest[4]['link']
}
