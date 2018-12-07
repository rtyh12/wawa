#!/usr/bin/env python
# coding: utf-8

import io
import os
import sys
import re
import argparse


# hardly perfect
# (probably) doesn't handle languages other than English,
# and it can have false positives
def isNonUser(string):
    false = [
        " left",
        " added ",
        " changed this group's icon",
        " changed to ",
        "Messages to this group are now secured with end-to-end encryption. Tap for more info.",
        "'s security code changed. Tap for more info.",
        "changed their phone number to a new number. Tap to message or add the new number.",
        " changed the subject from ",
        " created group "]
    if any(s in string for s in false):
        return 1
    else:
        return 0


def stripNonUsers(input):
    output = set()
    for i in input:
        if not isNonUser(i):
            output.add(i)

    return output


def countWords(string):
    return 1


def get_data(tuples, users_set):
    output = dict()

    #print(users_set)

    output['messageCounts'] = dict(total=0)
    output['characterCounts'] = dict(total=0)
    output['wordCounts'] = dict(total=0)

    for u in users_set:
        output['messageCounts'][u] = 0
        output['characterCounts'][u] = 0
        output['wordCounts'][u] = 0
    for t in tuples:
        if t[2] in users_set:      # to ignore system generated messages
            output['messageCounts'][t[2]]    += 1
            output['messageCounts']['total'] += 1

            output['characterCounts'][t[2]]    += len(t[3])
            output['characterCounts']['total'] += len(t[3])

            output['wordCounts'][t[2]]    += countWords(t[3])
            output['wordCounts']['total'] += countWords(t[3])

    output['users'] = users_set

    return output


def main():
    import wawa.tuples
    import wawa.cache

    #  --  Arguments  --  #
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("filepath",
                        help="the input file, in either WhatsApp (.txt) or JSON format")
    parser.add_argument("-j", "--jsonsave",
                        help="save conversation as a JSON file",
                        action="store_true")
    parser.add_argument("-p", "--pie",
                        help="draw a pie chart of senders",
                        action="store_true")
    parser.add_argument("-c", "--cloud",
                        help="draw a word cloud",
                        action="store_true")
    parser.add_argument("-x", "--characters",
                        help="use characters instead of messages for all counts",
                        action="store_true")
    parser.add_argument("-w", "--words",
                        help="use tokens (words) instead of messages for all counts",
                        action="store_true")
    parser.add_argument("-m", "--messages",
                        help="use messages for all counts. This is the default behavior",
                        action="store_true")
    parser.add_argument("-u", "--users",
                        help="print all users in conversation",
                        action="count")
    parser.add_argument("--user",
                        help="restrict counts to a specific sender or senders",
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
            tuples = wawa.tuples.getMessagesAsTuples(file)
    elif type == "json":
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            tuples = wawa.cache.load_json(file)
    print(" done.")

    #  --  users idk  --  #

    users_and_system_messages_set = set()

    # i[2] is either a user's name, or a system generated message
    # on certain events.
    for i in tuples:
        users_and_system_messages_set.add(i[2])

    if args.users is None:
        args.users = 0

    if args.users > 0:
        print()
        print("Users in conversation:")
        print("----------------------")
        for i in stripNonUsers(users_and_system_messages_set):
            print(i)

    if args.users > 1:
        print("----------------------")
        for i in (set(users_and_system_messages_set) - set(stripNonUsers(users_and_system_messages_set))):
            print(i)
        print()
        
    users_set = stripNonUsers(users_and_system_messages_set)
    #print(users_set)

    if args.user is not None:
        tuples = [i for i in tuples if i[2] in args.user]

    #  --  JSON saving  --  #

    if args.jsonsave:
        wawa.cache.save_json(tuples, os.path.basename(filepath))

    #  --  Analysis  --  #

    data = get_data(tuples, users_set)
    print(data)

    #  --  Drawing stuff  --  #

    if args.pie:
        print("Loading pyplot...")
        import wawa.draw
        if args.characters:
            wawa.draw.drawFrequenciesPieChart(data, 'character')
        elif args.words:
            wawa.draw.drawFrequenciesPieChart(data, 'word')
        else:    
            wawa.draw.drawFrequenciesPieChart(data, 'message')

    #print(tuples[151][3])

    return 0


if __name__ == "__main__":
    main()
