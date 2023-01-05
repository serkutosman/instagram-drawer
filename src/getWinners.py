import random


def get_winners(valid_comments):
    winners = list()
    comment_count = len(valid_comments)

    for i in range(10):
        winners.append(valid_comments.pop(random.randint(0, comment_count - 1)))
        comment_count -= 1

    return winners
