import random
from time import sleep


def binary_search(arr, low, high, x):
    if high == -1:
        return -1

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        try:
        # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return binary_search(arr, mid + 1, high, x)

        except IndexError:
            print(mid, high, x)

    else:
        # Element is not present in the array
        return -1


def is_valid(comment, followers, followers_count, owner):

    """
    determines whether a comment is valid or not
    """

    return comment.count("@") >= 3 and binary_search(followers, 0, followers_count - 1, owner) != -1


def get_comments(instagram, media_id, followers, followers_count):

    """
    scrapes the comments of the post with the given media_id. username and password are not important but necessary.
    writes the comments to the file .comments
    """

    comment_data = dict()
    accounts = list()

    comment_count = instagram.get_number_of_media_comments_by_id(media_id)
    comments = instagram.get_media_comments_by_id(media_id, comment_count)

    for comment in comments['comments']:
        if comment.owner.username not in accounts and is_valid(comment.text, followers, followers_count, comment.owner.username):
            comment_data[comment.owner.username] = comment.text
            accounts.append(comment.owner.username)

    file = open(".comments", "w", encoding="utf-8")
    file.write(str(comment_data))
    file.close()

    return len(comment_data)


def get_followers(instagram, account, follower_count):

    """
    gets the followers of the given account with the given username 'account'. username and password are not important but necessary.
    might take a little time.
    writes the followers to the file .followers
    """

    followers_data = list()
    sleep(2)
    acc = instagram.get_account(account)
    sleep(1)

    followers = instagram.get_followers(acc.identifier, follower_count, 100,
                                        delayed=True)

    for follower in followers['accounts']:
        followers_data.append(follower.username)

    followers_data.sort()
    file = open(".followers", "w", encoding="utf-8")
    file.write(str(followers_data))
    file.close()


def random_comments(comments, count):
    winners = list()

    for i in range(10):
        winners.append(comments.pop(random.randint(0, count)))
        count -= 1

    return winners


if __name__ == "__main__":
    print()



