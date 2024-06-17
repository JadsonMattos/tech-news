from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = db["news"]
    results = news.find({"title": {"$regex": title, "$options": "i"}})
    return [(result["title"], result["url"]) for result in results]


# Requisito 8
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")

    news = db["news"]
    results = news.find({"timestamp": {"$regex": date, "$options": "i"}})
    return [(result["title"], result["url"]) for result in results]


# Requisito 9
def search_by_category(category):
    news = db["news"]
    results = news.find({"category": {"$regex": category, "$options": "i"}})
    return [(result["title"], result["url"]) for result in results]
