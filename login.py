from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # 인터넷 창 최대화

# Chrome 웹 드라이버 생성
driver = webdriver.Chrome('C:/Users/student.M703/site_login/chromedriver.exe', chrome_options=options)

# url 로딩
driver.get('<URL>')  # site URL

assert '<title>' in driver.title  # site 타이틀을 보고 확인 (없어도 상관 없음)


user_id = driver.find_element_by_id('userId')
user_id.send_keys('<Id>')  # Id를 인자로 받음

user_pwd = driver.find_element_by_id('userPwd')
user_pwd.send_keys('<Pwd>')  # Password를 인자로 받음

login_btn = driver.find_element_by_css_selector('.btn.btn-lg.btn-wide.btn-primary')  # site html의 클래스 등을 통해 특정 가능
login_btn.click()

pop_up = driver.find_elements_by_css_selector('.pop-wrap')  # popup 클래스를 통해 확인

if pop_up:  # popup이 있을 시 팝업 지우기
    not_today = driver.find_element_by_css_selector('.btn.btn-wide.btn-md.btn-default')
    not_today.click()
