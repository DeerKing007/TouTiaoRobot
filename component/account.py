from config import *
from component.sliderlogin import SliderHelper

class TTAcount:
    def __init__(self):
        self.helper = SliderHelper()

    def login(self):
        self.login_headers = self.helper.login()


if __name__ == '__main__':
    t = TTAcount()
    t.login()
