from textwrap import dedent
import re


def welcome():
    print(dedent("""
    Welcome to my Madlib!
    In order to play this game, please follow the prompts"""))
    # It was a {Adjective} and {Adjective} {Noun}.

    noun = input("Please give me a noun ")
    adjective1 = input("Please give me an Adjective ")
    adjective2 = input("Please give me an Adjective ")

    text = ("It was a " + adjective1 + " and " + adjective2 + " " + noun)

    print(text)


def read_template(file):
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError as fnf_error:
        raise fnf_error


def parse_template(string):
    words = tuple(re.findall(r"{([^{}]*)}", string))
    for x in words:
        string = string.replace(x, "")
        return string, words


def merge(stripped, inputs):
    return stripped.format(*inputs)
# with open("madlib_cli/madlib_cli.py", "r") as f:
    contents = f.read()


def save_file(word):
    with open("madlib_text.txt", "w+") as f2:
        f2.write(word)


if __name__ == "__main__":
    welcome()
    print(save_file("madlib_text.txt"))
