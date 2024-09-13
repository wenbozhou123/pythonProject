from urllib.parse import quote
import requests, time

# encodeStr =  'http://127.0.0.1:9090/proxies/%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD-%E5%B9%BF%E4%B8%9C%E4%B8%93%E7%BA%BF%20BGP%202/delay?timeout=5000&url=http:%2F%2Fwww.gstatic.com%2Fgenerate_204'
#str2 = unquote(encodeStr)


all_proxies_request = 'http://127.0.0.1:9090/providers/proxies'
proxies_response = requests.get(all_proxies_request)
res = proxies_response.json()

all_proxies = res['providers']['Bitz Net']['proxies'][0]['all']
print(all_proxies)
urls=[]
for proxy in all_proxies:
    template = '/delay?timeout=5000&url=http://www.gstatic.com/generate_204'
    suffix = '/delay?timeout=5000&url=http:%2F%2Fwww.gstatic.com%2Fgenerate_204'
    urls.append('http://127.0.0.1:9090/proxies/' + quote(proxy) + suffix)

while(True):
    with requests.Session() as session:
        for url in urls:
            res = session.get(url)
            print(res.json())
    print("---"*30)
    time.sleep(3)



