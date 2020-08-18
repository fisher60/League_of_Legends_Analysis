from pandas import read_csv
from league_analysis.settings import DATA_DIR
from pathlib import Path



def get_columns(names: list) -> list:
    """input list of column names, get dataframe with column names."""

    csv = read_csv(Path(DATA_DIR, "high_diamond_ranked_10min.csv"))
    return [csv[i] for i in names]
