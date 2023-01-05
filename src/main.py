from utils import *
from igramscraper.instagram import Instagram


def main():
    i = 1
    username = input("username: ")                      # a username of any instagram account, unimportant but needed
    password = input("password: ")                      # the password of given account
    media_id = input("media id: ")                      # media id of the post
    account = input("account: ")                        # owner account of the post with the given media_id
    follower_count = int(input("follower_count: "))       # follower count of the given account

    instagram = Instagram()
    instagram.with_credentials(username, password)
    instagram.login(force=False, two_step_verificator=True)

    get_followers(instagram, account, follower_count)

    followers_file = open(".followers", "r", encoding="utf-8")
    followers = eval(followers_file.read())
    followers_file.close()

    comment_count = get_comments(instagram, media_id, followers, follower_count)

    comments_file = open(".comments", "r", encoding="utf-8")
    comments = eval(comments_file.read())
    comments_file.close()

    comments_list = list(comments.keys())

    winners = random_comments(comments_list, comment_count)

    print("\nwinners:")

    for winner in winners:
        print(f"  {i}: {winner}")
        i += 1

    print("\n")


if __name__ == "__main__":
    main()
    exit()
