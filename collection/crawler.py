import sys
from datetime import datetime
from urllib.request import Request, urlopen


# def error(e):
#    print(f'{e}: {datetime.now()}', file=sys.stderr)
#
# lambda e: print(f'{e}: {datetime.now()}', file=sys.stderr)
# lambda는 함수 정의를 간단하게 해주기 위해 사용한다.



def crawling(url='',
             encoding='utf-8',
             err=lambda e: print(f'{e}: {datetime.now()}', file=sys.stderr)):
    try:

        request = Request(url)
        response = urlopen(request)
        print(f'{datetime.now()}: success for request[{url}]')


        receive = response.read()
        return receive.decode(encoding, errors='replace')  # errors='replace' 엔코딩 에러난 경우 알아서 찾아서 동작

    except Exception as e:
        if err is not None:
            err(e)