from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,sys,requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# def requests_function(url):  #Soup 사용할때 쓰는거, 이번엔 안썼음
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
#     }
#     response = requests.get(url, headers=header)
#
#     soup = BeautifulSoup(response.text, 'lxml')
#
#     return soup

cd=r"C:\Users\진만킴\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(cd)
driver.implicitly_wait(15)
driver.get('https://shopping.naver.com/home')

search = driver.find_element(By.CLASS_NAME,'_searchInput_search_text_3CUDs') #검색창 컴포넌트가 #query임
search.send_keys('구스 이불')  # keys:건담 담아서 보내고
search.send_keys(Keys.ENTER)  # Keys: 엔터 입력 == 검색
time.sleep(2)
# goose_url="https://search.shopping.naver.com/search/all?query=%EA%B5%AC%EC%8A%A4%20%EC%9D%B4%EB%B6%88&cat_id=&frm=NVSHATC"
# goose_soup = requests_function(goose_url)
# summary = goose_soup.find_all('a',attrs={'class':'basicList_link__JLQJf'})
while True:
    driver = webdriver.Chrome(cd)
    driver.implicitly_wait(15)
    driver.get('https://shopping.naver.com/home')

    search = driver.find_element(By.CLASS_NAME,'_searchInput_search_text_3CUDs') #검색창 컴포넌트가 #query임
    search.send_keys('구스 이불')  # keys:구스 담아서 보내고
    search.send_keys(Keys.ENTER)  # Keys: 엔터 입력 == 검색
    time.sleep(2)
    goose = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[3]/li/div/div[2]/div[1]/a'))).click()  #상품 XPATH 복사
    driver.close()
    time.sleep(3)




