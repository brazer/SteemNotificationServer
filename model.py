# ['vote', {'voter': 'onelovecuration', 'author': 'enjoyinglife', 'permlink': 'ixtf4g8l', 'weight': 2000}]
class Vote:
    voter = ""
    author = ""
    permlink = ""
    weight = 0


# ['custom_json', {'required_auths': [], 'required_posting_auths': ['frebie'], 'id': 'follow',
# 'json': '["follow",{"follower":"frebie","following":"jabbir","what":["blog"]}]'}]
class Follow:
    ID = "follow"
    follower = ""
    following = ""


# ['comment', {'parent_author': 'changelly', 'parent_permlink': 'getting-listed-on-changelly-why-and-how',
#  'author': 'coinratecap', 'permlink': 're-changelly-getting-listed-on-changelly-why-and-how-20180913t203330725z',
#  'title': '', 'body': 'Nice one Changelly', 'json_metadata': '{"tags":["cryptocurrency"],"app":"steemit/0.1"}'}]
class Comment:
    parent_author = ""
    parent_permlink = ""
    author = ""
    permlink = ""
    title = ""
    body = ""


