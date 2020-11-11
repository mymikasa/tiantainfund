import requests


url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183014173252415948667_1605102613633&fundCode=008625&pageIndex=1&pageSize=20&startDate=2020-09-11&endDate=2020-11-11&_=1605103435989'

headers = {
    'Connection': 'keep-alive',
    'Cookie': 'st_si=46173653281025; st_asi=delete; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND0=null; EMFUND8=11-11%2021%3A42%3A50@%23%24%u5E7F%u53D1%u4E2D%u8BC1%u5168%u6307%u6C7D%u8F66%u6307%u6570A@%23%24004854; EMFUND9=11-11 22:51:35@#$%u56FD%u5BCC%u5E73%u8861%u517B%u8001%u4E09%u5E74%u6DF7%u5408%28FOF%29@%23%24008625; st_pvi=26555634600636; st_sp=2020-11-11%2021%3A40%3A50; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=13; st_psi=20201111230152197-112200304021-6787806553',
    'Host': 'api.fund.eastmoney.com',
    'Referer': 'http://fundf10.eastmoney.com/jjjz_008625.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

data = requests.get(url=url, headers=headers)

print(data.text)