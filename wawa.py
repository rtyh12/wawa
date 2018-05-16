# coding: utf-8

import argparse
import io
import os
import sys
import re

def drawFrequenciesPieChart():
    """Needs some work

    Cause it doesn't fucking work"""
    import matplotlib.pyplot as plt

    l = d_sorted[-8:]

    labels = [i[0] for i in l]
    sizes  = [i[1] for i in l]

    def absolute_value(val):
        sum = 0
        for i in sizes:
            sum += i

        a = int(val / 100 * sum)
        return a

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,
            labels = labels,
            autopct = absolute_value,
            startangle = 90)

    #plt.figure(num=0, figsize=(16, 16))
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig1.set_size_inches(16, 16)
    fig1.set_facecolor('white')

    plt.show()


# hardly perfect
# probably doesn't handle languages other than English,
# and it can have false positives
def isNonUser(string):
    false = [
        " left",
        " added ",
        " changed this group's icon",
        " changed to ",
        "Messages to this group are now secured with end-to-end encryption. Tap for more info.",
        "'s security code changed. Tap for more info.",
        "changed their phone number to a new number. Tap to message or add the new number."]
    if any(s in string for s in false):
        #print("AAAAAAA", string)
        return 1
    else:
        return 0


def stripNonUsers(input):
    output = set()
    for i in input:
        if not isNonUser(i):
            output.add(i)

    return output


def main():
    #  --  Arguments  --  #
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("filepath",
                        help="the input file, in either WhatsApp (.txt) or JSON format")
    parser.add_argument("-j", "--jsonsave",
                        help="save conversation as a JSON file for faster loading and better machine readability",
                        action="store_true")
    parser.add_argument("-p", "--pie",
                        help="draw a pie chart of senders",
                        action="store_true")
    parser.add_argument("-c", "--cloud",
                        help="draw a word cloud",
                        action="store_true")
    parser.add_argument("-x", "--characters",
                        help="use characters instead of tokens (words) for all calculations",
                        action="store_true")
    parser.add_argument("-u", "--users",
                        help="print all users in conversation",
                        action="count")
    parser.add_argument("--user",
                        help="restrict calculations to a specific sender or senders",
                        nargs='+')

    args = parser.parse_args()

    #  --  File loading  --  #

    # this is dumb, do it by looking at the file contents
    # rather than the extension
    filepath = args.filepath
    type = ""
    if filepath[-4:] == "json":
        type = "json"
    elif filepath[-3:] == "txt":
        type = "txt"
    else:
        sys.stderr.write("Error: unrecognized file type.")
        return 1

    print("Loading file... ", end='')
    tuples = 0
    if type == "txt":
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            import wawa.tuples
            tuples = wawa.tuples.getMessagesAsTuples(file)
    elif type == "json":
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            import wawa.tuples
            import wawa.cache
            tuples = wawa.cache.open(file)
    print(" done.")

    #  --  users idk  --  #
    if args.users is not None:
        output = set()
        for i in tuples:
            output.add(i[2])

        print()
        print("Users in conversation:")
        print("----------------------")
        for i in stripNonUsers(output):
            print(i)

        if args.users > 1:
            print("----------------------")
            for i in (set(output) - set(stripNonUsers(output))):
                print(i)

        print()

    if args.user is not None:
        tuples = [i for i in tuples if i[2] in args.user]

    #  --  JSON saving  --  #

    if args.jsonsave:
        wawa.cache.save(tuples, os.path.basename(filepath))

    #  --  Drawing stuff  --  #

    if args.pie:
        import wawa.draw

    #print(tuples[151][3])

    return 0


if __name__ == "__main__":
    main()
