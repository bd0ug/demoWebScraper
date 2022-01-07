import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/bdoug/Desktop/chromedriver')
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.find_all(attrs='blog-card__content-wrapper'): # all title cards
    name = a.find('a')
    if name not in results:
        results.append(name.text)

for b in soup.find_all(attrs='blog-card__date-wrapper'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
