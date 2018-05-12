# coding: utf-8

import os
import re

def readMessages(file):
    """Read messages from a WhatsApp file and returns them as a list.

    The messages are not parsed (return value consists of strings containing the
    date, time, name, as well as the message contents)."""

    lines = file.readlines()
    messages = []

    for i in range(len(lines)):
        # this regex checks if the given string starts with
        # a date, a time, and a name
        # (plus the appropriate punctuation)
        if re.search(r"^\d\d?\/\d\d?\/[\d]*, \d\d:\d\d - .+ ", lines[i]):
            messages.append(lines[i])
        else:
            # debug
            #print(messages)
            messages[-1] += lines[i]

    return messages


def splitMessage(line):
    """Split a message into date, time, name and content, returned as strings in a tuple."""
    comma = line.find(",")
    date = line[0 : comma]
    time = line[comma + 2 : comma + 7]

    # from the first occurrence of "-" to the second occurrence of ":",
    # plus appropriate indices.
    name = line[line.find("-") + 2 : line.find(":", line.find(":") + 1)]

    msg = line[line.find(":", line.find(":") + 1) + 2 : -1]

    return date, time, name, msg


def getMessagesAsTuples(file):
    """Read messages from a WhatsApp file and store them in a list of tuples."""
    messages = readMessages(file)
    messages = [splitMessage(i) for i in messages]

    return messages
