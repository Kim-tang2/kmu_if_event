import time
import random
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

print(time.asctime(time.localtime(time.time())) + ' 학생회 인스타그램 계정 (' + username + ') 로그인 성공')

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()  # 계정 정보 저장 X
time.sleep(2)

numFollowers = int(
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text)
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

soup = BeautifulSoup(driver.page_source, 'html.parser')
followers = soup.find_all('a', ['FPmhX', 'notranslate', '_0imsa'])
followersName = soup.find_all('div', ['wFPL8'])

followersIdText = []
followersNameText = []
[followersIdText.append(follower.get_text()) for follower in followers]
[followersNameText.append(followerName.get_text()) for followerName in followersName]
followersDict = {instaID: name for instaID, name in zip(followersIdText, followersNameText)}

print(followersDict)


def prize(productName, count):
    print(f'\n{productName}({count}명)을(를) 추첨하겠습니다. >__<!')
    print("두구 두구 두구 두구 두구 두구!!!!!!!")

    for i in range(3, -1, -1):
        time.sleep(1)
        if (i == 0): continue
        print(i)

    prizeStudents = random.sample(followersIdText, count)
    [print(followersDict[prizeStudent], prizeStudent) for prizeStudent in prizeStudents]


prize('손목 받침대', 3)
prize('전기방석', 3)
prize('노트북 받침대', 3)
prize('기프티콘', 40)
