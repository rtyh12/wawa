# coding: utf-8

import argparse
import io
import os

import wawa.tuples
import wawa.cache
import wawa.draw


d = dict()


# i don't even know what this is
def thingy():
    for i in tuples:
        d[i[2]] = 0

    for i in tuples:
        d[i[2]] += 1

    import operator
    d_sorted = sorted(d.items(), key = operator.itemgetter(1))

    d_sorted = sorted(d.items(), key = operator.itemgetter(1))


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


def main():
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
    parser.add_argument("-u", "--user",
                        help="restrict calculations to a specific sender",
                        action="store_true")

    args = parser.parse_args()

    # this is dumb, do it by looking at the file contents
    # rather than the extension
    filepath = args.filepath
    type = ""
    if filepath[-4:] == "json":
        type = "json"
    if filepath[-3:] == "txt":
        type = "txt"

    tuples = 0

    if type == "txt":
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            tuples = wawa.tuples.getMessagesAsTuples(file)
    elif type == "json":
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            tuples = wawa.cache.open(file)

    if args.jsonsave:
        wawa.cache.save(tuples, os.path.basename(filepath))

    print(tuples[151][3])


if __name__ == "__main__":
    main()

    # cache
    # split
    # word cloud
    # cache
    # pie chart
    # tuples
