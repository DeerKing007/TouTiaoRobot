#coding:utf-8
from config import *
import time, random
import cv2
from selenium import webdriver
from component.log import getLogger
from selenium.webdriver.chrome.options import Options
from deco.login import inited
from bs4 import BeautifulSoup as bs
from util.slider import download_img,drag_and_drop


logger = getLogger(__name__)

class SliderHelper:
    def __init__(self):
        self.username = None
        self.password = None
        self.driver = None

    def init_chrome(self):
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-gpu')
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH, options=chrome_options)

    @inited
    def login(self, username=USERNAME, password=PASSWORD):
        self.username = username
        self.password = password
        self.driver.get(URL_LOGIN_HOME)
        self.__account_input()
        self._slider_img_download()
        self._validate_and_drag(DOWN=LOGIN_VERIFY)
        logger.info(f'成功滑动登陆!')
        self.stop()

    # 账号登录
    def __account_input(self):
        self.driver.find_element_by_xpath('//*[@id="sso_pwd_login"]/span').click()  # 账密登录
        # 此时输入账密
        self.driver.find_element_by_xpath('//*[@id="sso_container"]/div/div[1]/form/div[1]/div[2]/input').send_keys(USERNAME)
        time.sleep(random.randint(1, 3))
        self.driver.find_element_by_xpath('//*[@id="sso_container"]/div/div[1]/form/div[2]/input').send_keys(PASSWORD)
        time.sleep(random.randint(1, 3))
        self.driver.find_element_by_xpath('//*[@id="sso_submit"]').click()  # 点击登录
        # 等待进入登陆后的页面 ---> 滑动验证码
        

    # 滑块图片下载
    def _slider_img_download(self, big_path=IMG_BIG_PATH, block_path=IMG_BLOCK_PATH, CLASSNAME=LOGIN_VERIFY):
        page = bs(self.driver.page_source, 'lxml')
        ImgWrapper = page('div', class_=CLASSNAME)
        if ImgWrapper :
            div = ImgWrapper[0]
            imgs = div('img')
            big_src_raw = imgs[0]['src']
            block_src_raw = imgs[-1]['src']
        else:
            return
        download_img(big_src_raw, big_path)
        download_img(block_src_raw, block_path)

    # 滑块间距离
    def _get_img_distance(self, big_path=IMG_BIG_PATH, block_path=IMG_BLOCK_PATH, TYPE=1):
        block_img = cv2.imread(block_path, 0)
        big_img = cv2.imread(big_path, 0)
        res = cv2.matchTemplate(block_img, big_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left_x = max_loc[0]+ SLIDER_DEBUG if TYPE==1 else max_loc[0]
        return top_left_x

    # 拖动验证
    def _validate_and_drag(self, big_path=IMG_BIG_PATH, block_path=IMG_BLOCK_PATH,
                           DRAG=SLIDER_BTN_CLASS, DOWN=VALIDATE_CLASS, TYPE=1):
        img = 1
        while img:
            top_left_x = self._get_img_distance(big_path=big_path, block_path=block_path, TYPE=TYPE)
            drag_and_drop(self.driver, top_left_x, DRAG)
            if TYPE != 1:return
            time.sleep(random.randint(1, 3))
            soup = bs(self.driver.page_source,'lxml')
            wrapper = soup('div',class_=DRAG) if TYPE==1 else soup('img',class_=DRAG)
            if  wrapper:
                print(soup)
                logger.info(f'识别错误，滑动失败.重新滑动')
                time.sleep(random.randint(1, 3))
                self._slider_img_download(big_path,block_path,DOWN)
            else:
                img = 0

    def stop(self):
        self.driver.close()
        self.driver.quit()

