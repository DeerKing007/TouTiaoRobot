import requests
from datetime import datetime
from component.weather import city_dict

class Weather():
    def get_init_data(self):
        '''
        初始化基础数据
        :return: None
        '''
        city_name = input('请输入城市\n')
        city_code = city_dict.city_dict.get(city_name)
        return city_code


    def isJson(self, resp):
        '''
        判断数据是否能被 Json 化。 True 能，False 否。
        :param resp: request
        :return: bool, True 数据可 Json 化；False 不能 JOSN 化。
        '''
        try:
            resp.json()
            return True
        except:
            return False
    def get_weather_info(self, dictum_msg='', city_code='101030100'):
        '''
        获取天气信息。网址：https://www.sojson.com/blog/305.html
        :param dictum_msg: str,发送给朋友的信息
        :param city_code: str,城市对应编码
        :return: str,需要发送的话。
        '''
        print('获取天气信息...')
        weather_url = f'http://t.weather.sojson.com/api/weather/city/{city_code}'
        resp = requests.get(url=weather_url)
        if resp.status_code == 200 and self.isJson(resp) and resp.json().get('status') == 200:
            weatherJson = resp.json()
            # 今日天气
            today_weather = weatherJson.get('data').get('forecast')[1]
            # 今日日期
            today_time = datetime.now().strftime('%Y{y}%m{m}%d{d} %H:%M:%S').format(y='年', m='月', d='日')
            # 今日天气注意事项
            notice = today_weather.get('notice')
            # 温度
            high = today_weather.get('high')
            high_c = high[high.find(' ') + 1:]
            low = today_weather.get('low')
            low_c = low[low.find(' ') + 1:]
            temperature = f"温度 : {low_c}/{high_c}"

            # 风
            fx = today_weather.get('fx')
            fl = today_weather.get('fl')
            wind = f"{fx} : {fl}"

            # 空气指数
            aqi = today_weather.get('aqi')
            aqi = f"空气 : {aqi}"

            # 要发送的消息内容
            today_msg = f'{today_time}\n{notice}。\n{temperature}\n{wind}\n{aqi}\n{dictum_msg}\n'
            return today_msg


if __name__ == '__main__':
    w = Weather()
    c = w.get_init_data()
    b = w.get_weather_info(city_code=c)
    print(b)
