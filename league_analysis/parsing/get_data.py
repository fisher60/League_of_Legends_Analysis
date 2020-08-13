from pandas import read_csv
import numpy

def get_column(name = []):
    csv = read_csv("league_analysis/datasets/high_diamond_ranked_10min.csv")
    return csv[[i for i in name]]

