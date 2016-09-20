import hashlib

from urllib.parse import urlencode
from urllib.request import Request, urlopen

r = Request("http://salt.training.hackerdom.ru", headers={'Cookie': "login=admin; secret_salted_hash=3042d7230c565a47d72a21d39759cb3d"})
resp = urlopen(r)
print(resp.geturl())
