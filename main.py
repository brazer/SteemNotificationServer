import threading

from steem.blockchain import Blockchain

from model import Vote, Comment, Follow


def parse_next_block(block):
    transactions = block['transactions']
    for transaction in transactions:
        operations = transaction['operations']
        for operation in operations:
            name = operation[0]
            if name == "vote":
                process_vote(operation)
            elif name == "custom_json":
                process_custom_json(operation)
            elif name == "comment":
                process_comment(operation)
            #else:
             #   print(operation)


# ['vote', {'voter': 'onelovecuration', 'author': 'enjoyinglife', 'permlink': 'ixtf4g8l', 'weight': 2000}]
def process_vote(operation):
    vote = Vote()
    vote.author = operation[1]["author"]


# ['custom_json', {'required_auths': [], 'required_posting_auths': ['frebie'], 'id': 'follow',
# 'json': '["follow",{"follower":"frebie","following":"jabbir","what":["blog"]}]'}]
def process_custom_json(operation):
    id = operation[1]["id"]
    if id == "follow":
        follow = Follow()  # todo
    else:
        print(operation)


# ['comment', {'parent_author': 'changelly', 'parent_permlink': 'getting-listed-on-changelly-why-and-how',
#  'author': 'coinratecap', 'permlink': 're-changelly-getting-listed-on-changelly-why-and-how-20180913t203330725z',
#  'title': '', 'body': 'Nice one Changelly', 'json_metadata': '{"tags":["cryptocurrency"],"app":"steemit/0.1"}'}]
def process_comment(operation):
    comment = Comment()
    comment.author = operation[1]['author']


current_id = ""  # todo: save in file


def run():
    blockchain = Blockchain()
    id = blockchain.get_current_block_num()
    global current_id
    if id != current_id :
        block = blockchain.get_current_block()
        thread = threading.Thread(target=parse_next_block, args=(block,))
        print("Start new thread", thread.name)
        thread.start()
        current_id = id
    threading.Timer(1, run).start()


if __name__ == '__main__':
    run()
