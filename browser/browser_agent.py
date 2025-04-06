from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_ai_news():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://news.google.com/search?q=artificial+intelligence")
    headlines = driver.find_elements(By.CSS_SELECTOR, 'article h3')
    top_news = [headline.text for headline in headlines[:5]]
    driver.quit()
    return top_news