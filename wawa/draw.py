import matplotlib.pyplot as plt


<<<<<<< HEAD
def drawFrequenciesPieChart(data, countType='message'):
    """Draw a pie chart.
    
    what a surprise.
    countType accepts parameters 'message', 'word' and 'character'."""
    import matplotlib.pyplot as plt

    labels = list(data['users'])
    sizes = []
    for user in labels:
        sizes.append(data[countType + 'Counts'][user])
=======
def drawFrequenciesPieChart(data):
    """Draw a pie chart.
    
    what a surprise."""
    import matplotlib.pyplot as plt

    labels = [i[0] for i in l]
    sizes  = [i[1] for i in l]
>>>>>>> d6f4161a80715b17fde3aa82f327deb8ca9a6e93

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
