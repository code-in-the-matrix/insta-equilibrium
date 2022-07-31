followers = set();
following = set();

p1 = []
p2 = []

# extracting followers list
with open("followersRaw.txt","rt") as f:
    i = 0;
    for str in f:
        if i%2 == 0:
           str = str[:-1]
           followers.add(str);
        i = i+1;
# print("Follower List:")
# print(followers);

# extracting following list
with open("followingRaw.txt","rt") as f:
    i = 0;
    for str in f:
        if i%2 == 0:
           str = str[:-1]
           following.add(str);
        i = i+1;
# print("Following List: ")
# print(following);

for f in following:
	if f not in followers:
		p1.append(f);

for f in followers:
	if f not in following:
		p2.append(f);

print ("People who don't follow you back:");
print(p1);

print ("People who you don't follow back:");
print(p2);

