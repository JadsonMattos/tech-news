from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import patch
import pytest


def test_reading_plan_group_news():
    with patch('tech_news.database.find_news') as mock_find_news:
        mock_find_news.return_value = [
            {"title": "Notícia 1", "reading_time": 5},
            {"title": "Notícia 2", "reading_time": 3},
            {"title": "Notícia 3", "reading_time": 10},
            {"title": "Notícia 4", "reading_time": 15},
        ]

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    with patch(
        'tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy',
        mock_find_news
    ):
        result = ReadingPlanService.group_news_for_available_time(10)

        assert result == {
            "readable": [
                {"unfilled_time": 2, "chosen_news": [
                    ("Notícia 1", 5), ("Notícia 2", 3)
                ]},
                {"unfilled_time": 0, "chosen_news": [("Notícia 3", 10)]},
            ],
            "unreadable": [("Notícia 4", 15)],
        }
