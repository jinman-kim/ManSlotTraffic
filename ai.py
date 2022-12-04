import wordcloud
from selenium import webdriver
from selenium.webdriver.common.by import By
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
# from selenium.webdriver.chrome.options import Options

os.environ['JAVA_HOME']=r'C:\Program Files\Java\jdk-19\bin\server'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--start-maximized") # add
options.add_argument("--window-size=1920,1080") # ad
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")

path = r"C:\Users\진만킴\Downloads\chromedriver_win32\chromedriver.exe"  # 웹드라이버 실행
driver = webdriver.Chrome(path,options=options)  # 드라이버 경로 설정, head 안띄움
url='https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8'
driver.get(url)
inkyu=driver.find_element(By.XPATH,'//*[@id="OvrFq8BcO"]/div[2]/div/div[1]/div[7]/div[2]/div/div/div/div/div/div[8]/div/div/div/div[1]/div/div[9]/div')
inkyu_img=inkyu.text
# print(type(inkyu_img))
# print(inkyu_img)
s_words= wordcloud.STOPWORDS.union({'있다','없다'})

wc1 = WordCloud(max_font_size=200, stopwords=s_words, font_path='C:\Windows\Fonts\MALGUNSL.TTF',
                background_color='white', width=800, height=800)
wc1.generate(inkyu_img)

plt.figure(figsize=(10, 8))
plt.imshow(wc1)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
