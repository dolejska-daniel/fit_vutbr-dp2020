import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


def run():
    sales = pd.read_csv("../data/sales_by_time_of_day.csv")
    sales.set_index("hours", inplace=True)
    # sales["sales"] /= 7.75

    # percent = 100 * categories["sales"] / categories["sales"].sum()
    # labels = ["{0}$\,-\,{1:1.1f}$%".format(i, p) for i, p in zip(categories.index, percent)]

    # ax = sales.plot.hist(
    #     weights=sales["sales"],
    #     bins=len(sales.index),
    #     fontsize=16
    # )

    fig, ax = plt.subplots()
    values, bins, patches = plt.hist(
        sales.index,
        bins=np.arange(len(sales.index) + 1),
        weights=sales["sales"],
    )

    from matplotlib import colors

    # We'll color code by height, but you could use any scalar
    fracs = values / values.max()

    # we need to normalize the data to 0..1 for the full range of the colormap
    norm = colors.Normalize(fracs.min() - .25, fracs.max())

    # Now, we'll loop through our objects and set the color of each accordingly
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.hot(1-norm(thisfrac))
        thispatch.set_facecolor(color)

    plt.xlabel("Time of Day (UTC)")
    plt.ylabel("Number of Sales")
    ax.set_xlim((0, 24))
    ax.xaxis.set_major_locator(MultipleLocator(4))
    ax.xaxis.set_major_formatter("{x:2.0f}:00")
    plt.grid(color="black", alpha=.3)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.xaxis.set_major_locator(MultipleLocator(4))
    # plt.grid(color="black", alpha=.15, which="minor", linestyle="--")

    # import numpy as np
    # plt.xticks(np.arange(0, 1, step=0.2), labels=[f"{h}:00" for h in sales.index])

    # ax.legend(labels, bbox_to_anchor=(.95, .8))  # .remove()
    plt.savefig("../../build/sales_by_daytime.pdf", bbox_inches="tight")


if __name__ == '__main__':
    run()
    plt.tight_layout(pad=1)
    plt.show()
