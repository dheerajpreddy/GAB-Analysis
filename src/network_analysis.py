import csv, json
from api import Gab

gab = Gab('dheerajpreddy', 'Test@123')

# myfile =  open("nodes.csv", 'w')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# heading = ['id', 'username', 'name', 'follower_count', 'following_count', 'score', 'is_premium', 'is_pro', 'is_hater', 'is_offender']
# wr.writerow(heading)
#
# fd = open("username.json", "r")
# usernames = json.load(fd)
# fd.close()
#
# for i in range(len(usernames)):
#     row = [usernames[i]['id'], usernames[i]['username'], usernames[i]['name'], usernames[i]['follower_count'], usernames[i]['following_count'], usernames[i]['score'], usernames[i]['is_premium'], usernames[i]['is_pro'] ritvik_add. ritvik_add]
#     wr.writerow(row)

myfile2 =  open("edges.csv", 'w')
wr2 = csv.writer(myfile2, quoting=csv.QUOTE_ALL)
heading = ['source', 'target']
wr2.writerow(heading)

fd = open("username.json", "r")
usernames = json.load(fd)
fd.close()

for i in range(len(usernames)):
    followers = gab.old_getfollowers(usernames[i]['username'])
    try:
        for follower in followers['data']:
            row = [follower['id'], usernames[i]['id']]
            wr2.writerow(row)
    except:
        continue
