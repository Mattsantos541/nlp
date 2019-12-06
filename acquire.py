#make new request
# imports
from requests import get
from bs4 import BeautifulSoup
import os
import pandas as pd


def get_article_text():
    # if we already have the data, read it locally
    if os.path.exists('article.txt'):
        with open('article.txt') as f:
            return f.read()

    # otherwise go fetch the data
    
    headers = {'User-Agent': 'Codeup Ada Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article = soup.find('div', class_='mk-single-content')

    # save it for next time
    with open('article.txt', 'w') as f:
        f.write(article.text)

    return article.text


def get_articles_from_topic(url):
     headers = {'user-agent': 'Codeup Bayes Instructor Example'}
     response = get(url, headers=headers)
     soup = BeautifulSoup(response.content, 'html.parser')

     output = []

     articles = soup.select(".news-card")

     for article in articles: 
         title = article.select("[itemprop='headline']")[0].get_text()
         content = article.select("[itemprop='articleBody']")[0].get_text()
         author = article.select(".author")[0].get_text()
         published_date = article.select(".time")[0]["content"]
         category = response.url.split("/")[-1]

         article_data = {
             'title': title,
             'content': content,
             'category': category,
             'author': author,
             'published_date': published_date,
         }
         output.append(article_data)


     return output


def make_new_request():
    urls = [
         "https://inshorts.com/en/read/business",
         "https://inshorts.com/en/read/sports",
         "https://inshorts.com/en/read/technology",
         "https://inshorts.com/en/read/entertainment"
     ]

    output = []

    for url in urls:
     # We use .extend in order to make a flat output list.
        output.extend(get_articles_from_topic(url))

        print("stuff")
        print(output)
        df = pd.DataFrame(output)
        df.to_csv('inshorts_news_articles.csv') 
        
        return df





def get_news_articles():
    filename = 'inshorts_news_articles.csv'
    return make_new_request()

     # filename = 'inshorts_news_articles.csv'

     # # check for presence of the file or make a new request
     # if os.path.exists(filename):
     #     return pd.read_csv(filename)
     # else:
     #     return make_new_request()
     # check for presence of the file or make a new request
    if os.path.exists(filename):
         return pd.read_csv(filename)
    else:
         return make_new_request()

def get_articles_from_topic(url):
    headers = {'user-agent': 'Codeup Bayes Instructor Example'}