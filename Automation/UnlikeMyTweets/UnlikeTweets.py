"""
Unlike my Twitter likes.

"""

from json import dumps, loads
from sys import argv

import twitter

###
# Do not forget to put Authentication information
# To use, first save your likes to file (res.json and ids.json) "python UnlikeMyTweets.py g"
# Second unlike tweets (it reads ids.json) "python UnlikeMyTweets.py r"
###
api = twitter.Api(
    consumer_key="", consumer_secret="", access_token_key="", access_token_secret=""
)


def getAllLikes():
    doNotStop = True
    out = []
    max_id = -1
    all_ids = []
    while doNotStop:
        if max_id > 0:
            result = api.GetFavorites(
                count=200, max_id=max_id, return_json=True)
        else:
            result = api.GetFavorites(count=200, return_json=True)
        if len(result) == 0:
            break
        for item in result:
            out.append(item)
            max_id = item["id"]
            all_ids.append(item["id"])
        open("res.json", "w").write(dumps(out))
        open("ids.json", "w").write(dumps(all_ids))


def removeAllLikes():
    ids = list(set(loads(open("ids.json").read())))
    print(f"We will delete {len(ids)} likes")
    for id in ids:
        try:
            res = api.DestroyFavorite(status_id=id)
        except:
            pass


if __name__ == "__main__":
    if len(argv) != 2:
        print("What do you want? g == get all, r == remove all")
        exit(1)

    if argv[1] == "r":
        removeAllLikes()
    if argv[1] == "g":
        getAllLikes()
