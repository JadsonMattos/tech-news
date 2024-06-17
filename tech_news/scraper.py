import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None

    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_urls = selector.css('.entry-title a::attr(href)').getall()
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css('a.next.page-numbers::attr(href)').get()
    return next_page_url if next_page_url else None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css('h1.entry-title::text').get().strip()
    timestamp = selector.css('.meta-date::text').get().strip()
    writer = selector.css('.author a::text').get().strip()
    reading_time = int(selector.css(
        '.meta-reading-time::text').get().strip().split()[0])
    paragraph = selector.xpath("(//p)[1]//text()").getall()
    summary = ''.join(paragraph).strip()
    category = selector.css('.meta-category .label::text').get().strip()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    news = []

    while len(news) < amount:
        html = fetch(url)
        news_urls = scrape_updates(html)

        for news_url in news_urls:
            news_html = fetch(news_url)
            news_data = scrape_news(news_html)
            news.append(news_data)

            if len(news) >= amount:
                break

        url = scrape_next_page_link(html)

        if url is None:
            break

    create_news(news)
    return news
