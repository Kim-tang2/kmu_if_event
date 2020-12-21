import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from login_info import username, password

options = Options()
options.add_argument("--disable-gpu")  # 그래픽 가속을 사용할 때 크롬에서 버그를 일으키는 현상이 있음
options.add_argument("--no-sandbox")  # 앗 이런 오류! 방지
options.add_argument("enable-automation")  # 알림 표시줄 제거
options.add_argument("--disable-infobars")  # 인포 박스 제거
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome('./chromedriver', options=options)
driver.implicitly_wait(2)

driver.get('https://www.instagram.com/' + username)
driver.execute_script("document.querySelectorAll('.-nal3')[1].click();")  # 팔로워 버튼 클릭

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)

driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button').submit()  # 로그인
time.sleep(3)

print(time.asctime(time.localtime(time.time())) + ' 학생회 인스타그램 계정 ('+username+') 로그인 성공')

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()  # 계정 정보 저장 X
time.sleep(2)

numFollowers = int(driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text)
print(f'({username}) 팔로워 수: {numFollowers}')

driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()

time.sleep(2)

beforeLength = -1
afterLength = -2

while beforeLength != afterLength:
    beforeLength = afterLength
    afterLength = driver.execute_script("return document.querySelectorAll('.jSC57')[0].scrollHeight")
    driver.execute_script(
        "document.querySelectorAll('.isgrP')[0].scrollTo(0,document.querySelectorAll('.jSC57')[0].scrollHeight)")
    time.sleep(0.5)




