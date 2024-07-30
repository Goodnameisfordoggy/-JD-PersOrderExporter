import  os
import time
import json
import logging
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__) # ��־��¼��

def logInWithCookies(target_url: str = "https://www.jd.com/"):
    """ 
    ʹ�ñ����cookiesģ���¼ 
    
    Return: webdriver
    """
    cookie_file = 'cookies.json'
    driver = webdriver.Chrome()
    if os.path.exists(cookie_file): # ����Ƿ����cookie�ļ�
        driver.maximize_window()
        driver.get(target_url)
        # time.sleep(2)
        with open(cookie_file, 'r') as f:
            # ��ȡ�ļ��е� cookie
            cookies = json.load(f)
            # ����cookie��Ϣ
            for cookie in cookies:
                driver.add_cookie(cookie)
        logging.info('ʹ���ѱ����cookie��¼')
        # time.sleep(1)
        driver.refresh()
        # time.sleep(2)
        return driver
        


if __name__ == '__main__':
    logInWithCookies()