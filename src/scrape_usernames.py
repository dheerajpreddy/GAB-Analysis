from api import Gab
import json

gab = Gab('dheerajpreddy', 'Test@123')
user_count = 1
visited = set()
queue = ['farmer-general']

fp = open('data.json', 'w')

while user_count < 50000 and queue:
	user_name = queue.pop(0)
	if user_name not in visited:
		user = gab.getuser(user_name)
		json.dump(user, fp)
		user_count += 1
		print (user_count)
		visited.add(user_name)
		followers = gab.getfollowers(user_name, 10000)
		for user in followers:
			follower_username = user['username']
			if follower_username not in visited:
				queue.append(follower_username)
fp.close()
