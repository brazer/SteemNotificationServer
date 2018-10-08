# ['vote', {'voter': 'onelovecuration', 'author': 'enjoyinglife', 'permlink': 'ixtf4g8l', 'weight': 2000}]
class Vote:
    name = "vote"
    voter = ""
    author = ""
    permlink = ""
    weight = 0


# ['custom_json', {'required_auths': [], 'required_posting_auths': ['frebie'], 'id': 'follow',
# 'json': '["follow",{"follower":"frebie","following":"jabbir","what":["blog"]}]'}]
class Follow:
    name = "custom_json"
    id = "follow"
    follower = ""
    following = ""


# ['comment', {'parent_author': 'changelly', 'parent_permlink': 'getting-listed-on-changelly-why-and-how',
#  'author': 'coinratecap', 'permlink': 're-changelly-getting-listed-on-changelly-why-and-how-20180913t203330725z',
#  'title': '', 'body': 'Nice one Changelly', 'json_metadata': '{"tags":["cryptocurrency"],"app":"steemit/0.1"}'}]
class Comment:
    name = "comment"
    parent_author = ""
    parent_permlink = ""
    author = ""
    permlink = ""
    title = ""
    body = ""





# ['transfer', {'from': 'byresteem', 'to': 'arunava', 'amount': '0.001 SBD',
# 'memo': 'Campaign !!! Byresteem is much stronger now. !!! Hello users , My account with the most followers .
# I can promote your post.28.000 Followers + Byresteem Upvote 7600Sp  + Upvote min +250 Different accounts +
# New followers + Loyality bonus FREE and more. Send 2 SBD or 2 STEEM To ByResteem URL as Memo Service ACTIVE'}]
class Transfer:
    name = "transfer"
    from_ = ""
    to = ""


# ['claim_reward_balance', {'account': 'occpresents', 'reward_steem': '0.000 STEEM', 'reward_sbd': '0.000 SBD',
# 'reward_vests': '12.127383 VESTS'}]
class ClaimRewardBalance:
    name = "claim_reward_balance"


