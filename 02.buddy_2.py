from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pyautogui

import time

import pyperclip

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

#불필요한 에러메세지 제거
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬드라이버를 자동으로 설치해서 서비스를 만들어냄
service = Service(executable_path=ChromeDriverManager().install())


# 크롬 드라이버 연결


browser = webdriver.Chrome("C:/chromedriver.exe", service = service,options=chrome_options)



browser.implicitly_wait(10) # 페이지가 로딩될때까지 최대 10초 기다려줌


# 1.로그인

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

browser.get(url) # 페이지 열기

browser.maximize_window() # 화면 최대화



# 아이디 입력창
time.sleep(2)
naver_id = browser.find_element(By.CSS_SELECTOR,"#id")
naver_id.click()
pyperclip.copy("shoon199")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)


# 비밀번호 입력창

naver_pw = browser.find_element(By.CSS_SELECTOR,"#pw")
naver_pw.click()
pyperclip.copy("1234")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 로그인 버튼

login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
login_btn.click()




# 2. view탭, 최신순의 키워드로 이동

keyword = "제태크"
url = f"https://m.search.naver.com/search.naver?where=m_blog&query={keyword}&sm=mtb_viw.blog&nso=so%3Add%2Cp%3Aall"
browser.get(url) 


# 3. 초기 15개 작성자 아이디 
user_ids = browser.find_elements(By.CSS_SELECTOR,".sub_txt.sub_name")

for user in user_ids:
    user.send_keys(Keys.CONTROL +"\n")   #새창으로 열기
    browser.switch_to.window(browser.window_handles[1])  #탭으로 이동

    ######################################

    time.sleep(2)
    try:
        # 4. 이웃추가 버튼 클릭  (오류 발생할 수 있는 구간)
        buddy_add = browser.find_element(By.CSS_SELECTOR,".link__RsHMX.add_buddy_btn__oGR_B")
        buddy_add.click()

        #5. 서로이웃추가 체크 (오류 발생할 수 있는 구간)
        both_buddy_check = browser.find_element(By.CSS_SELECTOR,"#bothBuddyRadio")
        both_buddy_check.click()

        input_message = "제태크에 관심 많은 청년인데, 서로이웃해요!"
        text = browser.find_element(By.CSS_SELECTOR,".textarea_t1.ng-pristine.ng-untouched.ng-valid.ng-not-empty")
        text.click()
        text.send_keys(Keys.CONTROL, "a")
        time.sleep(1)
        text.send_keys(Keys.DELETE)
        time.sleep(1)
        text.send_keys(input_message)

        #7. 확인
        btn_ok = browser.find_element(By.CSS_SELECTOR,".btn_ok")
        btn_ok.click()
    except:
        pass

    #######################################
    # 현재 사용중인 탭 종료
    browser.close()

    # 메인 탭으로 이동
    browser.switch_to.window(browser.window_handles[0])



