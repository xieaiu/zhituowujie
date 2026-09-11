import requests

# 提醒：发送最后一页时，请将 userAgent 修改为：yuanrenxue，否则将不会返回最后一页的数据
# 提醒2：发送请求时请携带 sessionid 参数，每个已登录用户 数字答案都不同~
def get_data():
    result = 0
    for page in range(1,6):
        cookies = {
            'Hm_lvt_f80b2b389f44bbfb3bfe1704817d44e0': '1789096040',
            'HMACCOUNT': 'EAF572EC3FEC1CFB',
            'sessionid': 'y9zg9cu61ar58xbfc1jgrh9xeex7oib2',
            'Hm_lpvt_f80b2b389f44bbfb3bfe1704817d44e0': '1789096837',
        }

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://match.yuanrenxue.cn/match/19',
            'sec-ch-ua': '"Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            # 'cookie': 'Hm_lvt_f80b2b389f44bbfb3bfe1704817d44e0=1789096040; HMACCOUNT=EAF572EC3FEC1CFB; sessionid=y9zg9cu61ar58xbfc1jgrh9xeex7oib2; Hm_lpvt_f80b2b389f44bbfb3bfe1704817d44e0=1789096837',
        }

        params = {
            'page': str(page),
            'pageSize': '10',
            'kw': '',
        }

        if page < 5:
            response = requests.get('https://match.yuanrenxue.cn/api/question/19', params=params, cookies=cookies, headers=headers).json()
        else:
            headers['user-agent'] = 'yuanrenxue'
            response = requests.get('https://match.yuanrenxue.cn/api/question/19', params=params, cookies=cookies,headers=headers).json()

        for item in response['data']:
            result += item

    print(result)

if __name__ == '__main__':
    get_data()
