from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import serpapi

class crawler:
    def __init__(self) -> None:
        return

    def acl2023_crawler(self):
        url = 'https://2023.aclweb.org/program/accepted_main_conference/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find('section', {'class': 'page__content'})

        title_list = []

        for i in tqdm(titles.find_all('p')):
            title_list.append(i.find('strong').text)

        return title_list

    def cvpr2023_crawler(self):
        url = 'https://cvpr.thecvf.com/Conferences/2023/AcceptedPapers'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find('table').find_all('tr')

        title_list = []

        for i in tqdm(titles):
            if i.find('a') != None:
                title_list.append(i.find('a').text)
            elif i.find('strong') != None:
                title_list.append(i.find('strong').text)
        return title_list
    
    def google_scholar_crawler(self) :
        title = []
        def search(StartNum) :
            params = {
                "engine": "google_scholar",
                "q": "ai",
                "api_key": "f345b6c514fc5125cd1665a81099e2176009dc524c6415fc599c3f5cb85ba892",
                "as_ylo" : 2022,
                "num" : 20,
                "start" : StartNum*20
            }
            search = serpapi.search(params)
            results = search.get_dict()
            organic_results = results["organic_results"]
            titles = [result['title'] for result in organic_results]
            return titles
        for i in range(2):
            title.extend(search(i))
        return title

        
    
    def do_all(self):
        methods = dir(self)
        for i in methods:
            if 'crawler' in i:
                print(i)
        # getattr(self, i)(parameter)


