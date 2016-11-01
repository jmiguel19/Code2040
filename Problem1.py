import requests
start = {'token' : '59402b28f1730f82897d3e78666c0eba', 'github': 'https://github.com/jmiguel19/Code2040.git'}
req = requests.post('http://challenge.code2040.org/api/register', start)

reverse = requests.post('http://challenge.code2040.org/api/reverse', start)
output = ''
for letter in reverse.content[::-1]:
	output += letter
newjson = {'token':'59402b28f1730f82897d3e78666c0eba', 'string':output}
req2 = requests.post('http://challenge.code2040.org/api/reverse/validate', newjson)

