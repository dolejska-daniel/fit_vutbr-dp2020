import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


def run():
    sales = pd.read_csv("../data/sales_by_time_of_day.csv")
    sales.set_index("hours", inplace=True)

    sales.pivot_table("")

    # ax.legend(labels, bbox_to_anchor=(.95, .8))  # .remove()
    plt.savefig("../../build/sales_by_daytime.pdf", bbox_inches="tight")


if __name__ == '__main__':
    run()
    plt.tight_layout(pad=1)
    plt.show()
