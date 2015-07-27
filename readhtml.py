import urllib.request
import json

file = open('/git/bitcoinrichlist/richlist.txt', 'w')
file.write("at_btc,sum_100,sum_500\n")

for at_block in range(500,352700+1,500):

    req = urllib.request.urlopen('http://bitcoinrichlist.com/api/v1/top100?atblock=%d' %(at_block))
    charset = req.info().get_param('charset', 'utf8')
    data = req.read()
    decoded = json.loads(data.decode(charset))

    req_500 = urllib.request.urlopen('http://bitcoinrichlist.com/api/v1/top500?atblock=%d' %(at_block))
    charset_500 = req_500.info().get_param('charset', 'utf8')
    data_500 = req_500.read()
    decoded_500 = json.loads(data_500.decode(charset_500))

    file.write("%d,%d,%d\n" %(decoded['at_btc'], decoded['sumtop'], decoded_500['sumtop']))

file.close()
