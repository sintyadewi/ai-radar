from src.sources.rss import fetch_feed


def test_fetch_feed_returns_list():
    articles = fetch_feed("https://openai.com/news/rss.xml")

    assert isinstance(articles, dict)