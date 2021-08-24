# import telebot
# from mytoken import token
from typing import KeysView
import requests
from bs4 import BeautifulSoup
import csv

# def start_message(message):
#         chat_id = message.chat.id
#         user_info = f'{message.from_user.first_name} {message.from_user.username}'
#         bot.send_message(chat_id, "Выберите какую новость: ")


data_ = {}


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    key = 0
    soup = BeautifulSoup(html, 'lxml')
    news = soup.find('div', class_="Tag--articles")
    all_news = news.find_all('div', class_='ArticleItem')
    for i in all_news:
        try:
            title = i.find('a', class_="ArticleItem--name").text.strip()
            # print(title)
        except:
            title = ''
        try:
            info = i.find('a', class_="ArticleItem--name").get('href')
            # print(info)
        except:
            info = ''
        try:
            img = i.find('img', class_="ArticleItem--image-img").get('data-src')
        except:
            img = ''
        data = {'title': title,
                'info': info,
                'img': img}
        data_[key] = data
        key += 1
    print(data_)


def main():
    url = 'https://kaktus.media/?date=2021-06-25&lable=8&order=time'

    get_html(url)
    get_data(get_html(url))


main()