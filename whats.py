# coding: utf-8

import os
import io
import re
import argparse

import wawa.tuples


def open(filepath):


def getMessages(filepath):
    """Read messages from a WhatsApp file and returns them as a list.

    The messages are not parsed in any way (a single string, containing the
    date, time, name, as well as the message contents)."""
    f = io.open(filepath,
                mode="r",
                encoding="utf-8")

    lines = f.readlines()

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
    """Split a message into date, time, name and content, returned as strings."""
    comma = line.find(",")
    date = line[0 : comma]
    time = line[comma + 2 : comma + 7]

    # from the first occurrence of "-" to the second occurrence of ":",
    # plus appropriate indices.
    name = line[line.find("-") + 2 : line.find(":", line.find(":") + 1)]

    msg = line[line.find(":", line.find(":") + 1) + 2 : -1]

    return date, time, name, msg

def getMessagesAsTuples(file):
    """Reads messages from a WhatsApp file and stores them in a list as tuples"""
    out = getMessages(file)
    out = [splitMessage(i) for i in out]

    return out


# maybe at some point
def getFormat():
    return Format.whatsapp


#tuples = getMessagesAsTuples(f)


#tuples[11][3]


#d_sorted


d = dict()


def thingy():
    for i in tuples:
        d[i[2]] = 0

    for i in tuples:
        d[i[2]] += 1

    import operator
    d_sorted = sorted(d.items(), key = operator.itemgetter(1))

    d_sorted = sorted(d.items(), key = operator.itemgetter(1))


def drawFrequenciesPieChart():
    """Needs some work"""
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





def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-c", "--cache",
                        help="Saves a cache file for faster loading",
                        action="store_true")

if __name__ == "__main__":
    main()

    # cache
    # split
    # word cloud
    # cache
    # pie chart
    # tuples
