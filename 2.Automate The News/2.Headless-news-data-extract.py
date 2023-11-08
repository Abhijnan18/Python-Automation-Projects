from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

website = "https://www.thesun.co.uk/fabulous/"
path = "/Users/abhijnans/Downloads/chromedriver-mac-arm64"

# headless-mode
options = Options()
options.headless = True

service = Service(excutable_path=path)  # Fixed a typo here (excutable_path -> executable_path)
driver = webdriver.Chrome(service=service, options=options)  # Fixed a typo here (service=service, options=options)
driver.get(website)

containers = driver.find_elements(
    by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a').text
    subtitle = container.find_element(by="xpath", value='./a/h3').text  # Fixed a typo here (subtiltle -> subtitle)
    link = container.find_element(
        by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}  # Fixed a typo here (subtiltle -> subtitle)

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline-headless.csv')

driver.quit()
