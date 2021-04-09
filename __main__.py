from itertools import count

from bs4 import BeautifulSoup

from collection import crawler


def crawling_pelicana():
    results = []

    for index in count(start=110, step=1):
        url = f'https://pelicana.co.kr/store/stroe_search.html?page={index}&branch_name=&gu=&si='
        html = crawler.crawling(url)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class':['table', 'mt20']})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll(('tr'))

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)
            name = datas[1]
            address = datas[3]
            sidogu = address.split()[:2]

            t = (name, address) + tuple(sidogu)
            results.append(t)

            # print(name, address, sidogu)
    # store


if __name__ == '__main__':
    crawling_pelicana()
