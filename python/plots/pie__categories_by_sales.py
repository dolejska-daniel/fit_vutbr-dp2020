import pandas as pd
import matplotlib.pyplot as plt


def run():
    categories = pd.read_csv("../data/categories_by_sales.csv")
    categories.set_index("category", inplace=True)

    percent = 100 * categories["sales"] / categories["sales"].sum()
    labels = ["{0}$\,-\,{1:1.1f}$%".format(i, p) for i, p in zip(categories.index, percent)]

    ax = categories.plot.pie(
        y="sales", ylabel="", labels=["" for _ in categories.index],
        fontsize=16, labeldistance=1.1
    )

    ax.legend(labels, bbox_to_anchor=(.95, .8))  # .remove()
    plt.savefig("../../build/categories_by_sales.pdf", bbox_inches="tight")


if __name__ == '__main__':
    run()
    plt.tight_layout(pad=0)
    plt.show()
