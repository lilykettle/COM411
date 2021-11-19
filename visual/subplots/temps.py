import matplotlib.pyplot as plt


def read_data(file_path):
    temps = []

    with open(file_path) as file:
        data = file.read()
        line = data.split ('\n')
        return line


def run():
    data = read_data("temps.txt")
    fig, axs = plt.subplots(1, 2)
    days = range (1, 8)

    axs[0].plot(days, data)
    axs[1].bar(days, data)



    plt.tight_layout()
    plt.show()


run()


