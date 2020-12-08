# 每日贴吧名人堂的自动投票 http://tieba.baidu.com/celebrity/rankHome
# 使用 selenium 的首次尝试
# 2020年12月8日

from selenium import webdriver
import time
import random

# 找到浏览器并设置默认等待上限
wd = webdriver.Chrome('E:\\chromedriver.exe')  # 将路径手动设置为本地的chromedriver.exe的路径
wd.implicitly_wait(10)
wd.get('http://tieba.baidu.com/celebrity/rankHome')

### 请在这里填写昵称和密码 ###
default_nickname = ''
default_keys = ''
### 请在这里填写昵称和密码 ###

def perform_login(account):
    # 登录

    # 找到“登录”按钮
    login = wd.find_element_by_css_selector('.u_login  [rel="noreferrer"]')
    login.click()

    # 选择“账号登录”
    login = wd.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn')
    login.click()

    # 输入昵称和密码
    login_username = wd.find_element_by_id('TANGRAM__PSP_11__userName')
    login_password = wd.find_element_by_id('TANGRAM__PSP_11__password')
    login_username.send_keys(account[0])
    time.sleep(random.uniform(0.2,0.5))
    login_password.send_keys(account[1]+'\n')

    '''
    login_skip_captcha = wd.find_element_by_id('pass-slide-auxiliary')
    login_skip_captcha.click()
    '''

    # 关闭验证码界面，设置等待时间避免被判定为机器人
    time.sleep(random.uniform(2.3,3.0))
    login_skip_captcha = wd.find_element_by_class_name('vcode-close')
    login_skip_captcha.click()

    # 再次点击登录，设置等待时间避免被判定为机器人
    time.sleep(random.uniform(0.5,0.7))
    login_submit = wd.find_element_by_id('TANGRAM__PSP_11__submit')
    login_submit.click()


def perform_vote(number):
    # 投票
    time.sleep(random.uniform(0.2,0.3))
    vote = wd.find_element_by_css_selector('[data-forumid="'+number+'"]')

    # 界面滚动到元素所在位置，并点击
    wd.execute_script("arguments[0].scrollIntoView();",vote)    
    vote = wd.find_element_by_css_selector('[data-forumid="'+number+'"]')
    vote.click()

    # 点击助攻以及关闭对话框
    time.sleep(random.uniform(0.2,0.3))
    vote = wd.find_element_by_css_selector('.sign_btn.j_sign_btn')
    vote.click()
    time.sleep(random.uniform(0.2,0.3))
    vote = wd.find_element_by_css_selector('.dialogJclose')
    vote.click()


perform_login((default_nickname,default_keys))
time.sleep(4) # 等待登录过程

# 分别给编号为 30227（灰原哀） 与 154782（江户川哀） 投票
perform_vote('30227')
perform_vote('154782')

print("Done")