import requests
from bs4 import BeautifulSoup
from newspaper import Article
import json
import os
import time
from datetime import datetime

def scrape_antara_news(category="politik", limit=5):
    """
    Scrapes news from Antara News Indonesia.
    """
    base_url = f"https://www.antaranews.com/{category}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"Fetching news from: {base_url}")
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching base URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Antara News structure usually has articles in <article> tags or thematic blocks
    # We look for links to articles
    links = []
    for article_tag in soup.find_all('article'):
        a_tag = article_tag.find('a', href=True)
        if a_tag and '/berita/' in a_tag['href']:
            link = a_tag['href']
            if link not in links:
                links.append(link)
        
        if len(links) >= limit:
            break

    # If no <article> tags found, try h3/h2 (fallback)
    if not links:
        for h3 in soup.find_all(['h3', 'h2']):
            a_tag = h3.find('a', href=True)
            if a_tag and '/berita/' in a_tag['href']:
                link = a_tag['href']
                if link not in links:
                    links.append(link)
            if len(links) >= limit:
                break

    print(f"Found {len(links)} article links. Extracting content...")

    extracted_data = []
    for link in links:
        try:
            print(f"Processing: {link}")
            article = Article(link)
            article.download()
            article.parse()
            
            data = {
                "title": article.title,
                "text": article.text,
                "url": link,
                "date": str(article.publish_date) if article.publish_date else str(datetime.now()),
                "source": "Antara News"
            }
            extracted_data.append(data)
            time.sleep(1) # Be polite
        except Exception as e:
            print(f"Error processing {link}: {e}")

    return extracted_data

def save_to_json(data, folder="data/raw"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(folder, f"scraped_news_{timestamp}.json")
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"Saved {len(data)} articles to {filename}")

if __name__ == "__main__":
    news_data = scrape_antara_news(category="politik", limit=5)
    if news_data:
        save_to_json(news_data)
    else:
        print("No news data found.")
