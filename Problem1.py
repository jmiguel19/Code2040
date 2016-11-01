#step 1
import requests
token = '59402b28f1730f82897d3e78666c0eba'
tokendict = {'token': token}

start = {'token' : '59402b28f1730f82897d3e78666c0eba', 'github': 'https://github.com/jmiguel19/Code2040.git'}
req = requests.post('http://challenge.code2040.org/api/register', start)

#step2
reverse = requests.post('http://challenge.code2040.org/api/reverse', start)
output = ''
for letter in reverse.content[::-1]:
	output += letter
newjson = {'token':'59402b28f1730f82897d3e78666c0eba', 'string':output}
req2 = requests.post('http://challenge.code2040.org/api/reverse/validate', newjson)

#step3
startreq = requests.post('http://challenge.code2040.org/api/haystack', start)
for num in range(len(startreq.json()['haystack'])):
	if startreq.json()['haystack'][num] == startreq.json()['needle']:
		output = num
		break
req3json = {'token': '59402b28f1730f82897d3e78666c0eba', 'needle': output}
req3 = requests.post('http://challenge.code2040.org/api/haystack/validate', req3json)

#step4
prefixdict = requests.post('http://challenge.code2040.org/api/prefix', tokendict)
prefix = prefixdict.json()['prefix']
stringarray = prefixdict.json()['array']
output4 = []
for s in stringarray:
	s = str(s)
	letter_index = 0
	found = True
	for letter in str(prefix):
		if s[letter_index] != letter:
			found = False
			break
		letter_index += 1
	if not found:
		output4.append(s)
print prefix
print stringarray
print output4
req4json = {'token': token, 'array': output4}
req4 = requests.post('http://challenge.code2040.org/api/prefix/validate', json=req4json)


#step5
token = '59402b28f1730f82897d3e78666c0eba'
tokendict = {'token': token}
step5 = requests.post('http://challenge.code2040.org/api/dating', tokendict)
step5dict = step5.json()
stampsecs = int(step5dict['datestamp'][17:19])
stampminutes = int(step5dict['datestamp'][14:16])
stamphours = int(step5dict['datestamp'][11:13])
stampdays = int(step5dict['datestamp'][8:10])
newsecs = stampsecs + step5dict['interval']
if newsecs >= 60:
	minutes = stampminutes + (newsecs / 60)
	seconds = newsecs % 60
else:
	minutes = stampminutes
	seconds = newsecs
if minutes >= 60:
	hours = (stamphours) + (minutes)/60
	minutes = (minutes) % 60
else:
	hours = stamphours
if hours >= 24:
	days = (stampdays) + (hours)/60
	hours = (hours) % 60
else:
	days = stampdays

if len(str(seconds)) < 2:
	seconds = str(0) + str(seconds)
else:
	seconds = str(seconds)

if len(str(minutes)) < 2:
	minutes = str(0) + str(minutes)
else:
	minutes = str(minutes)

if len(str(hours)) < 2:
	hours = str(0) + str(hours)
else:
	hours = str(hours)

if len(str(days)) < 2:
	days = str(0) + str(days)
else:
	days = str(days)

newdatestamp = step5dict['datestamp'][:8]
newdatestamp += days
newdatestamp += 'T'
newdatestamp += hours
newdatestamp += ':'
newdatestamp += minutes
newdatestamp += ':'
newdatestamp += seconds
newdatestamp += 'Z'
newjson5 = {'token':token, 'datestamp':newdatestamp}
req5 = requests.post('http://challenge.code2040.org/api/dating/validate', newjson5)
'''



