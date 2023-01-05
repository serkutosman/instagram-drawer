from instagrapi import Client
from time import sleep


def get_credentials():
    usr = str()
    pwd = str()

    with open("credentials.txt", "r", encoding="utf-8") as file:
        usr = file.readline()
        pwd = file.readline()

    return [usr, pwd]


# returns whether a comment is valid or not
# a comment is only valid if the user who commented
# tagged 3 other users
def is_comment_valid(comment):
    content = comment[1]

    if content.count("@") != 3:
        return False

    taggedUsers = [taggedUser.split(" ")[0] for taggedUser in content.split("@")[1:]]

    if list(set(taggedUsers)) != taggedUsers:
        return False

    return True


# determines whether a comment is valid or not
def get_valid_users(comments, followers):
    valid_users = list()

    for comment in comments:
        comment_owner = comment[0]

        if comment_owner in followers and is_comment_valid(comment):
            valid_users.append(comment.user)

    return valid_users


def get_media_id(cl, link):
    # extracting media pk, this is only useful in getting media id
    media_pk = cl.media_pk_from_url(link)

    # extracting media_id
    media_id = cl.media_id(media_pk)

    return media_id


# returns the comments of the post with the given media_id.
# returns in the form of a list of tuples, where the first
# element of the tuple is the username and the second element
# is the content of the comment
def get_comments(client: Client, media_id):
    [usr, pwd] = get_credentials()

    client.login(usr, pwd, relogin=True)

    comments = client.media_comments(media_id)

    return [(comment.user.username, comment.text) for comment in comments]


# might take a little time
# returns the usernames of the followers
def get_followers(client: Client, user_id):
    followers_data = list()
    sleep(2)

    followers = client.user_followers(user_id)

    sleep(1)

    return [user.username for user in followers.values()]


if __name__ == "__main__":
    print()



