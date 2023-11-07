from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/abhijnans/Downloads/chromedriver-mac-arm64"

service = Service(excutable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(
    by="xpath", value='//div[@class = "teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a').text
    subtiltle = container.find_element(by="xpath", value='./a/h3').text
    link = container.find_element(
        by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtiltle)
    links.append(link)

my_dict = {'title': titles, 'subtiltle': subtitles, 'link': links}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')

driver.quit()
