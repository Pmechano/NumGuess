import requests as req

class Weather:
    def __init__(self):
        self.api_key = "45f881ba1daeaf75a680e5aa9ca9745c"
        self.city_code = "440115" #南沙区的编号
        self.URL = f"https://restapi.amap.com/v3/weather/weatherInfo?city={self.city_code}&key={self.api_key}"

    def getWea(self):
        r = req.get(self.URL)

        # 检查请求是否成功
        if r.status_code == 200:
            data = r.json()  # 解析 JSON 数据
            lives = data["lives"][0]
            weather = lives["weather"]
            tem = lives["temperature"]
            return f"| 天气：{weather} | 温度：{tem}°C |"
        else:
            return f"请求失败，状态码: {r.status_code}"
