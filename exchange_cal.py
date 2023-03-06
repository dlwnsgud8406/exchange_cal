import requests as req
import re

url = 'https://finance.naver.com/marketindex/'

res = req.get(url)

body = res.text


r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

print("------")
print("환율 계산기")
print("------")
print("")

for c in captures:
    print(c[0] + " : " + c[1])

print('')
usd = float(captures[0][1].replace(",",""))
won = int(input("달러로 바꾸길 원하는 금액(원)을 입력해주세요 : "))
dollar = int(won / usd)
print(f"{dollar} 달러로 환전되었습니다")
# pos = html.find('미국 USD')
# print(pos)
