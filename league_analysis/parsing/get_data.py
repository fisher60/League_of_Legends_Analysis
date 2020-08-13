from pandas import read_csv


def get_column(name: str):
    csv = read_csv("../datasets/high_diamond_ranked_10min.csv")
    return csv[name]
