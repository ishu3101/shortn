#! /usr/bin/python

import urllib
import urllib2
import json
import argparse

parser = argparse.ArgumentParser(description="Shorten URL using the following services: bit.ly, j.mp, t.cn, is.gd, v.gd, tiny.cc.")
parser.add_argument("url",
    help="Enter the URL to shorten here")
parser.add_argument("-j", "--jmp",
    help="use j.mp to shorten url", action="store_true")
parser.add_argument("-t", "--tcn",
    help="use t.cn to shorten url", action="store_true")
parser.add_argument("-i", "--isgd",
    help="use is.gd to shorten url", action="store_true")
parser.add_argument("-v", "--vgd",
    help="use v.gd to shorten url", action="store_true")
parser.add_argument("-c", "--tinycc",
    help="use tiny.cc to shorten url", action="store_true")

parser.add_argument("-V", "--version", action='version', version='%(prog)s 1.0')
args = parser.parse_args()

url = args.url

if args.jmp:
    type = 'j.mp'
elif args.tcn:
    type = 't.cn'
elif args.isgd:
    type = 'is.gd'
elif args.vgd:
    type = 'v.gd'
elif args.tinycc:
    type = 'tiny.cc'
else :
    type = "bit.ly"

api = {
	'bitly' : 'https://api-ssl.bitly.com/v3/shorten?format=json&login=hzlzh&apiKey=R_e8bcc43adaa5f818cc5d8a544a17d27d&longUrl=',
	'jmp' : 'http://api.j.mp/v3//shorten?format=json&login=hzlzh&apiKey=R_e8bcc43adaa5f818cc5d8a544a17d27d&longUrl=',
	'tcn' : 'https://api.weibo.com/2/short_url/shorten.json?access_token=2.00WSLtpB0GRHJ9745670860ceNWWiC&source=5786724301&url_long=',
	'isgd' : 'http://is.gd/create.php?format=json&url=',
	'vgd' : 'http://v.gd/create.php?format=json&url=',
	'tinycc' : 'http://tiny.cc/?c=rest_api&m=shorten&version=2.0.3&format=json&shortUrl=&login=hzlzh&apiKey=9f175aa2-ff30-4df5-b958-1346c59b4884&longUrl='
}

def getLink(service,url):
    terms = urllib.quote_plus(url.strip())
    url = service + terms
    data = urllib2.urlopen(url).read()
    return data

if (('http' in url) == False):
    url = 'http://'+url

if type == 'bit.ly':
    service = api['bitly']
    output = json.loads(getLink(service,url))["data"]["url"]
elif type == 'j.mp':
    service = api['jmp']
    output = json.loads(getLink(service,url))["data"]["url"]
elif type == 't.cn':
    service = api['tcn']
    output = json.loads(getLink(service,url))["urls"][0]["url_short"]
elif type == 'is.gd':
    service = api['isgd']
    output = json.loads(getLink(service,url))["shorturl"]
elif type == 'v.gd':
    service = api['vgd']
    output = json.loads(getLink(service,url))["shorturl"]
elif type == 'tiny.cc':
    service = api['tinycc']
    output = json.loads(getLink(service,url))["results"]["short_url"]

if (output != ''):
    print output
else:
    print 'Try again!'