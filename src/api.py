import requests
import json

class Gab:
	headers = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
	session = {}

	def __init__(self, username, password):
		f = requests.get('https://gab.ai/auth/login', headers=self.headers)
		self.session = f.cookies
		token = f.text.split('"_token" value="')[1].split('"')[0]
		self.session = requests.post('https://gab.ai/auth/login', headers=self.headers, cookies=self.session, data={'_token':token, 'password':password, 'username':username}).cookies

	def getnotifications(self, type='null'):
		return json.loads(requests.get('https://gab.ai/api/notifications?type=' + type, headers=self.headers, cookies=self.session).text)

	def search(self, query, user=False, sort='date'):
		if user:
			return json.loads(requests.get('https://gab.ai/api/search/users?q=' + query, headers=self.headers, cookies=self.session).text)
		else:
			return json.loads(requests.get('https://gab.ai/api/search?sort=' + sort + '&q=' + query, headers=self.headers, cookies=self.session).text)

	def getme(self):
		return json.loads(requests.get('https://gab.ai/home/', headers=self.headers, cookies=self.session).text.split('window.authUser = ')[1].split(';')[0])

	def getuser(self, username):
		return json.loads(requests.get('https://gab.ai/users/' + username, headers=self.headers, cookies=self.session).text)

	def gettopics(self):
		return json.loads(requests.get('https://gab.ai/api/topics', headers=self.headers, cookies=self.session).text)

	def gettimeline(self):
		return json.loads(requests.get('https://gab.ai/feed', headers=self.headers, cookies=self.session).text)

	def getpost(self, postid):
		return json.loads(requests.get('https://gab.ai/posts/' + str(postid), headers=self.headers, cookies=self.session).text)

	def getfollowers(self, user, limit):
		count = 0
		followers = []
		try:
			total = json.loads(requests.get('https://gab.ai/users/' + user + '/followers', headers=self.headers, cookies=self.session).text)['count']
			while count < total and count < limit:
				temp = json.loads(requests.get('https://gab.ai/users/' + user + '/followers?before='+str(count), headers=self.headers, cookies=self.session).text)
				if 'data' in temp:
					followers += temp['data']
					count += 30
		except:
			pass
		return followers

	def old_getfollowers(self, user):
 		return json.loads(requests.get('https://gab.ai/users/' + user + '/followers', headers=self.headers, cookies=self.session).text)

	def getfollowing(self, user):
		return json.loads(requests.get('https://gab.ai/users/' + user + '/following', headers=self.headers, cookies=self.session).text)

	def old_getusertimeline(self, user):
		obj = json.loads(requests.get('https://gab.ai/feed/' + user , headers=self.headers, cookies=self.session).text)['data']
		return obj

	def getusertimeline(self, user, limit):
		gabs = []
		try:
			obj = json.loads(requests.get('https://gab.ai/feed/' + user , headers=self.headers, cookies=self.session).text)['data']
			gabs += obj
			count = len(obj)
			if count == 0:
				return gabs
			while count < limit:
				try:
					date = obj[-1]['published_at']
					obj = json.loads(requests.get('https://gab.ai/feed/' + user + '?before=' + date, headers=self.headers, cookies=self.session).text)['data']
					if len(obj) == 0:
						break
					gabs += obj
					count += len(obj)
				except:
					continue
		except:
			return gabs
		return gabs

gab = Gab('dheerajpreddy', 'Test@123')
ans = gab.getusertimeline('a', 100)
print (len(ans))
