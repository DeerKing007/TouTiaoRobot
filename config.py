# ------ 用户账户设置 ------
#今日头条账户密码
USERNAME = '16604348816'
PASSWORD = 'Zp920316'

HEADERS = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}


# ------ URL -------
URL_LOGIN_HOME = 'https://mp.toutiao.com/login/'

# ------ selenium、滑块相关设置 ------
CHROME_PATH = '/usr/local/bin/chromedriver'
IMG_BIG_PATH = 'img/big.png'
IMG_BLOCK_PATH = 'img/block.png'
IMG_S_BIG_PATH = 'img/big_s.png'
IMG_S_BLOCK_PATH = 'img/block_s.png'
LOGIN_VERIFY = 'captcha_verify_img--wrapper'
SLIDER_BTN_CLASS = 'secsdk-captcha-drag-icon'
VALIDATE_CLASS = 'validate-main'
## 滑块微调距离
SLIDER_DEBUG = 25


# ------ 日志设置 ------
#启用日志
LOG_ENABLE = True
#日志显示级别
LOG_LEVEL = 'INFO'
#日志文件编码
LOG_FILE_ENCODING = 'UTF-8'
#日志文件路径
LOG_FILE_SAVE_PATH = r'log/log.txt'
#日志时间格式
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#日志级别对应格式
LOG_FORMAT = {
    'DEBUG'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'INFO'      : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'WARNING'   : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'ERROR'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'CRITICAL'  : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
}