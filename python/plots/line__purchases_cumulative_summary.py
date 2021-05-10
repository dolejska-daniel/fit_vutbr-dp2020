import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from mpl_axes_aligner import align
from sklearn.linear_model import LinearRegression
from matplotlib.ticker import FuncFormatter


def run():
    sales = pd.read_csv("../data/sales_per_day.csv")
    sales.set_index("time", inplace=True)

    cumulative_sum = sales.sort_index().cumsum()

    fig, ax = plt.subplots()
    ax1 = cumulative_sum.plot(ax=ax)
    ax2 = sales.plot(ax=ax, secondary_y=True)

    # taken from: https://stackoverflow.com/a/65824524/3078351
    ax1_ylims = ax1.axes.get_ylim()
    ax1_yratio = ax1_ylims[0] / ax1_ylims[1]

    ax2_ylims = ax2.axes.get_ylim()
    ax2_yratio = ax2_ylims[0] / ax2_ylims[1]

    if ax1_yratio < ax2_yratio:
        ax2.set_ylim(bottom=ax2_ylims[1] * ax1_yratio, top=ax2_ylims[1] * (.998 + ax1_yratio))

    else:
        ax1.set_ylim(bottom=ax1_ylims[1] * ax2_yratio)

    ax.legend(["Cumulative Sales"], loc="upper left", bbox_to_anchor=(0, 1.11))  # .remove()
    ax2.legend(["Sales per Day"], loc="upper right", bbox_to_anchor=(1, 1.11))
    ax.xaxis.set_label_text("Date")
    ax.yaxis.set_label_text("Total Detected Sales")
    ax2.yaxis.set_label_text("Detected Sales per Day")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ",")))

    ax.set_xticklabels(ax.get_xmajorticklabels(), rotation=20)
    ax1.grid(color="black", alpha=.3, linestyle="-")

    # decomposition = sm.tsa.seasonal_decompose(sales, period=7, model="additive")

    # plt.plot(decomposition.trend.index, decomposition.trend, c="red")
    plt.savefig("../../build/sales_per_day.pdf", bbox_inches="tight")

    # decomposition.plot()


if __name__ == '__main__':
    run()
    plt.tight_layout(pad=1)
    plt.show()
