from src.data.load_data import scrape_antara_news, save_to_json

def main():
    print("=== GovPulse Data Acquisition Tool ===")
    print("Target: Antara News (Politik)")
    
    # Scrape data
    data = scrape_antara_news(category="politik", limit=10)
    
    if data:
        save_to_json(data)
        print("Scraping completed successfully.")
    else:
        print("Scraping failed or no news found.")

if __name__ == "__main__":
    main()
