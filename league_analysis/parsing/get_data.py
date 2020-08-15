from pandas import read_csv
from league_analysis.settings import DATA_DIR


def get_column(name: str):
    csv = read_csv(f"{DATA_DIR}\high_diamond_ranked_10min.csv")
    return csv[name]
