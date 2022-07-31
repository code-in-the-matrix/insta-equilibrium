import json

followers = set()
following = set()

p1 = []
p2 = []

# playground
with open("./followers.json", "r") as f:
    data = json.load(f)
    # print(data["relationships_followers"])
    # print(type(data["relationships_followers"]))
    for p in data["relationships_followers"]:
        # print(type(p))
        # p = json.loads(p)
        uname = p["string_list_data"][0]["value"]
        # uname = p["string_list_data"]
        followers.add(uname)

with open("./following.json", "r") as f:
    data = json.load(f)
    for p in data["relationships_following"]:
        # print(type(p))
        # p = json.loads(p)
        uname = p["string_list_data"][0]["value"]
        # uname = p["string_list_data"]
        following.add(uname)


for f in following:
    if f not in followers:
        p1.append(f)

for f in followers:
    if f not in following:
        p2.append(f)

print("People who don't follow you back:")
print(p1)

print("People who you don't follow back:")
print(p2)
