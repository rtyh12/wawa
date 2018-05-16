import matplotlib.pyplot as plt


def drawFrequenciesPieChart(data, countType='message'):
    """Draw a pie chart.
    
    what a surprise.
    countType accepts parameters 'message', 'word' and 'character'."""
    import matplotlib.pyplot as plt

    labels = list(data['users'])
    sizes = []
    for user in labels:
        sizes.append(data[countType + 'Counts'][user])

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

    plt.figure(num=0, figsize=(16, 16))
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig1.set_size_inches(16, 16)
    fig1.set_facecolor('white')

    plt.show()
