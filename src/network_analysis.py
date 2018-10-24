import csv, json
# from api import Gab
#
# gab = Gab('dheerajpreddy', 'Test@123')

# myfile =  open("nodes.csv", 'w')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# heading = ['id', 'username', 'name', 'follower_count', 'following_count', 'score', 'is_premium', 'is_pro']
# wr.writerow(heading)
#
# fd = open("username.json", "r")
# usernames = json.load(fd)
# fd.close()
#
# for i in range(len(usernames)):
#     row = [usernames[i]['id'], usernames[i]['username'], usernames[i]['name'], usernames[i]['follower_count'], usernames[i]['following_count'], usernames[i]['score'], usernames[i]['is_premium'], usernames[i]['is_pro'] ritvik_add. ritvik_add]
#     wr.writerow(row)

# myfile2 =  open("edges.csv", 'w')
# wr2 = csv.writer(myfile2, quoting=csv.QUOTE_ALL)
# heading = ['source', 'target']
# wr2.writerow(heading)
#
# fd = open("username.json", "r")
# usernames = json.load(fd)
# fd.close()
#
# for i in range(len(usernames)):
#     followers = gab.old_getfollowers(usernames[i]['username'])
#     try:
#         for follower in followers['data']:
#             row = [follower['id'], usernames[i]['id']]
#             wr2.writerow(row)
#     except:
#         continue


fd = open("users_with_labels.json", "r")
usernames = json.load(fd)
fd.close()

myfile_all = open("all_nodes.csv", "w")
myfile_hate = open("hate_nodes.csv", "w")
myfile_offense = open("offensive_nodes.csv", "w")
myfile_neither = open("neither_nodes.csv", "w")
wr_nodes_all = csv.writer(myfile_all, quoting=csv.QUOTE_ALL)
wr_nodes_hate = csv.writer(myfile_hate, quoting=csv.QUOTE_ALL)
wr_nodes_offense = csv.writer(myfile_offense, quoting=csv.QUOTE_ALL)
wr_nodes_neither = csv.writer(myfile_neither, quoting=csv.QUOTE_ALL)

# myfile2_hate =  open("hate_edges.csv", 'w')
# myfile2_offense =  open("offensive_edges.csv", 'w')
# myfile2_neither =  open("neither_edges.csv", 'w')
# wr_edges_hate = csv.writer(myfile2_hate, quoting=csv.QUOTE_ALL)
# wr_edges_offense = csv.writer(myfile2_offense, quoting=csv.QUOTE_ALL)
# wr_edges_neither = csv.writer(myfile2_neither, quoting=csv.QUOTE_ALL)

heading = ['id', 'username', 'name', 'follower_count', 'following_count', 'score', 'is_premium', 'is_pro', 'is_hater', 'is_offender', 'is_neither']
wr_nodes_all.writerow(heading)
wr_nodes_hate.writerow(heading)
wr_nodes_offense.writerow(heading)
wr_nodes_neither.writerow(heading)

# heading = ['source', 'target']
# wr_edges_hate.writerow(heading)
# wr_edges_offense.writerow(heading)
# wr_edges_neither.writerow(heading)


for i in range(len(usernames)):
    n = False
    h = False
    o = False
    if 'is_hate_speech' in usernames[i]:
        h = True
    if 'is_offensive_language' in usernames[i]:
        o = True
    if not h and not o:
        n = True
    row = [usernames[i]['id'], usernames[i]['username'], usernames[i]['name'], usernames[i]['follower_count'], usernames[i]['following_count'], usernames[i]['score'], usernames[i]['is_premium'], usernames[i]['is_pro'], h, o, n]
    if n:
        wr_nodes_neither.writerow(row)
    if h:
        wr_nodes_hate.writerow(row)
    if o:
        wr_nodes_offense.writerow(row)
    wr_nodes_all.writerow(row)
    # followers = gab.old_getfollowers(usernames[i]['username'])
    # try:
    #     for follower in followers['data']:
    #         row = [follower['id'], usernames[i]['id']]
    #         wr2.writerow(row)
    # except:
    #     continue
