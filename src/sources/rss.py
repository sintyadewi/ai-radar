import feedparser


def fetch_feed(feed_url: str) -> list[dict]:
    feed = feedparser.parse(feed_url)

    articles = []

    for entry in feed.entries:
        articles.append({
            "title": entry.get("title", ""),
            "url": entry.get("link", ""),
            "published_at": entry.get("published", ""),
            "summary": entry.get("summary", ""),
        })

    return articles