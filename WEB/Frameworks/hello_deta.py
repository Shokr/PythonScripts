from deta import Deta

# initialize with a project key
deta = Deta("a0pnlhsz_TgZroLiYxSrABtU73i1rv5ppbt9ouTav")

# create and use as many DBs as you want!
users = deta.Base("users")

users.insert({"name": "Shokr", "title": "R&D Engineer"})

shokr = next(users.fetch({"name": "Shokr"}))[0]

users.delete(shokr["key"])
