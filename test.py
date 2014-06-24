import requests

base='http://127.0.0.1:1234'

r=requests.get(base+'/shop')
print r.text

r=requests.get(base+'/shop?test=1')
print r.text

r=requests.get(base+'/shop/1/food')
print r.text

r=requests.get(base+'/food/23')
print r.text

r=requests.get(base+'/shop/123')
print r.text

r=requests.delete(base+'/shop/123')
print r.text

r=requests.get(base+'/order')
print r.text

r=requests.get(base+'/order/56598')
print r.text
