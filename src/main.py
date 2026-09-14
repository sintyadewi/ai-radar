from sources.rss import fetch_feed


OPENAI_RSS_URL = "https://openai.com/news/rss.xml"


def main():
    articles = fetch_feed(OPENAI_RSS_URL)

    for article in articles[:5]:
        print(article["title"])
        print(article["url"])
        print("---")


if __name__ == "__main__":
    main()