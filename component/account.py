from config import *
from component.sliderlogin import SliderHelper

class TTAcount:
    def __init__(self):
        self.helper = SliderHelper()

    def login(self, username=USERNAME, password=PASSWORD):
        self.login_headers = self.helper.login(username=username, password=password)


if __name__ == '__main__':
    t = TTAcount()
    t.login()
