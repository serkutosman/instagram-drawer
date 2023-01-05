# instagram-drawer
An app to draw 3 winners from the comments of an Instagram post.

You can install this app to your computer either by downloading the zip file from the [program's GitHub page](https://github.com/aykutkenceevrimkonferansi/instagram-drawer)
or if you have `git` installed in your system, by simply cloning this repo via `git`.

```bash
git clone https://github.com/aykutkenceevrimkonferansi/instagram-drawer 
```

If you don't have `git`, you can install it from [here](https://git-scm.com/downloads).

## Usage

### Setup

First of all, you have to have Python installed in your system in order to run this program.
You can install it from [here](https://www.python.org/downloads/).

You can control whether it is installed in your system by running the following command in your terminal:

```bash
python --version
```
**NOTE:** If you are using Mac or Linux, you may need to type `python3` insted of `python` for all the commands written here.


If you get an output like this:

```bash
Python 3.8.5
```

Then you are good to go. The version number may vary.

After making sure Python is installed, go to the location you downloaded and unzipped (or cloned) this
program. You can find it on your system by simply searching for "instagram-drawer".

Get inside the folder and run `setup.py` to leave the rest to python:

```bash
# again, if you are using mac or linux, you may need to type python3 instead of python.
python setup.py
```

If you consider an error message, specifically something that starts by this:

```bash
Error installing requirements. Please check whether you have pip
```

That means you need to install `pip` to your system as well :(

After that, you will be asked for a username and password. You may enter **ANY** username
and password given that they match, i.e., as long as they belong to a valid Instagram user,
you may type any username and password. You do not need to type in the credentials of your
own account, or akekodtu.

### Running the program

Once `setup.py` is run without any errors, that means you can use the program right away.
You can use it by typing the command:
```bash
# again, python3 if you're not windows
python index.py
```

The program will print out the winners. You can see that it is working by running it several times.

**HOWEVER**, note that the program is really bulky and slow, that is because the requests
sent to servers are sent with some delay. Also, there are many followers and commands, so...

## Notes

Anytime you encounter an error, do not hesitate to connect the [maintainers](https://github.com/aykutkenceevrimkonferansi/instagram-drawer#maintainers).

You can also add an issue from the [issues](https://github.com/aykutkenceevrimkonferansi/instagram-drawer/issues) tab.

## Maintainers

- [AKEK](https://github.com/aykutkenceevrimkonferansi)
- [Baran Yancı](https://github.com/y4nci)
