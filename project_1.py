import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=cc10e115d1ed386e")

print(indeed_result.text)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all('a')

spans = []

for page in pages:
    spans.append(page.find("span"))
print(spans[:-1])
# 위의 문장은 리스트의 마지막 요소를 제외시켜준다는 뜻이다.
# spans[0:-1] 과 똑같다
# spans[0:5] 를 하면 0번째부터 5번째까지
