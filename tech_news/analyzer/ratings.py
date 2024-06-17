from tech_news.database import db
from collections import Counter


# Requisito 10
def top_5_categories():
    news = db["news"]
    results = news.find()
    categories = [result["category"] for result in results]
    sorted_categories = Counter(sorted(categories)).most_common(5)
    return [category[0] for category in sorted_categories]
