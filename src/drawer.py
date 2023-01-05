from src.getWinners import get_winners
from src.tools import *

from instagrapi import Client


def print_divider():
    print()
    print("#" * 50)
    print()


def drawer(cl: Client, verbose: bool):
    # getting the shortcode of the post
    media_link = input("Link of the post: ")

    media_id = get_media_id(cl, media_link)

    # getting user id
    user_id = media_id.split("_")[1]

    followers = get_followers(cl, user_id)

    if verbose:
        print_divider()
        print("FOLLOWERS:")

        for follower in followers:
            print(follower)

        print_divider()

    comments = get_comments(cl, media_id)

    if verbose:
        print("COMMENTS:")

        for comment in comments:
            print(comment)

        print_divider()

    valid_users = get_valid_users(comments, followers)

    if verbose:
        print("VALID USERS:")

        for valid_user in valid_users:
            print(valid_user)

        print_divider()

    winners = get_winners(valid_users)

    print_divider()

    print("\nWinners:")

    i = 1
    for winner in winners:
        print(f"  {i}: {winner}")
        i += 1

    print("\n")
