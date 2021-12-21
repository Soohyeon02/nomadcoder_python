import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
# indeed_result 변수에 requests.get 을 이용해서 url 정보를 저장

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# url 정보가 저장 되어있는 indeed_result 변수에서, text 파일만 불러와 indeed_soup 에 저장(text 파일 = html 코드)

pagination = indeed_soup.find("ul", class_="pagination-list")
# url 의 html 코드가 저장되어있는 indeed_soup 변수에서 html 구성요소가 "ul" 이며 class 이름이 "pagination-list"인 코드를 pagination 변수에 저장

pages = pagination.find_all('a')
# pages 변수를 만들어 pagination-list(html 코드)안의 a(링크)부분을 저장함


spans = []
# pages 를 하나하나 넣을 리스트 spans 선언

for page in pages:
    spans.append(page.find("span"))
# pages 변수 안에 있는 요소 하나하나를 spans 리스트에 넣어줌
print(spans[0:-1])
# 마지막 하나 빼고 처음부터 출력
