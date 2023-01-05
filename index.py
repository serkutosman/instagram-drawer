from src.constants import VERBOSE_FLAG, VERBOSE_FLAG_LONG
from src.drawer import drawer

import sys
from instagrapi import Client
from src.tools import get_credentials

try:
    args = sys.argv[1:]
    verbose = False

    if VERBOSE_FLAG in args or VERBOSE_FLAG_LONG in args:
        verbose = True

    [usr, pwd] = get_credentials()
    cl = Client()
    cl.login(usr, pwd)
    drawer(cl, verbose)
except Exception as e:
    print(e)

