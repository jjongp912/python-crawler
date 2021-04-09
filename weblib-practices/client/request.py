from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET


http_response = urlopen('https://www.example.com')
body = http_response.read() # read 해주면 body 출력
body = body.decode('utf-8')
print(body)


print("=====================================================")

# POST
data = {
    'id': 'jjongp',
    'name': '박종진',
    'pw': '1234'
}

data = urlencode(data).encode('utf-8')

request = Request('https://www.example.com', data)
request.add_header('Content-Type', 'text/html')

http_reponse = urlopen(request)
print(http_reponse.status, http_reponse.reason)

body = http_response.read()
html = body.decode('utf-8')
print(html)