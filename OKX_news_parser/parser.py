import os
import re
import requests
from bs4 import BeautifulSoup


class OKXNewsDownloader:
    """Class for downloading news from OKX to folder

     Args: 
        start_date (str) : Start date of the time range. 
        end_date (str) : End date of the time range.   
        folder (str) : Folder's name to download news to.
        """
    def __init__(self, start_date, end_date, folder):
        self.start_date = start_date
        self.end_date = end_date
        self.folder = folder

    def download_news(self):
        """ Method of the class which parse news dats from OKX in
            specified time range, write content of each new to txt file named by the title
            and store it in the folder.
            """
            
        url = "https://www.okx.com/ru/help/section/announcements-latest-announcements"
        response = requests.get(url)
        all_news = list()
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            news_items = soup.find('script', attrs={"data-id": "__app_data_for_ssr__"} ).get_text()
            pages = int(re.findall(r'\d+', news_items)[0])
            
            for page in range(1, (pages//15+2)):
                url = f"https://www.okx.com/ru/help/section/announcements-latest-announcements/page/{page}"
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    news_items = soup.find('script', attrs={"data-id": "__app_data_for_ssr__"} ).get_text()
                    news_page = eval('{'+news_items.split('[{')[1].split(']}')[0])
                    all_news.append(list(news_page))
        
                for news_item in all_news[page-2]:
                    news_date = news_item['publishTime']
                    if self.start_date <= news_date <= self.end_date:
                        
                        title = news_item['title']
                        url = f"https://www.okx.com/ru/help/{news_item['slug']}"
                        response = requests.get(url)
                        content = BeautifulSoup(response.content, 'html.parser')
                        news_text = content.find('div', class_="index_content__03zP1").get_text()
                        
                        file_name = f"{title}.txt"
                        if not os.path.exists(self.folder):
                            os.makedirs(self.folder)
                        file_path = os.path.join(self.folder, file_name)
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(news_text.split('>>>')[0])

        else:
            print("Failed to fetch data from the website.")
