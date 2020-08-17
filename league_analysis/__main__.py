from sys import argv
from league_analysis.analysis.regression import vision_to_deaths

if __name__ == "__main__":
    command_1 = argv[1]

    if command_1 == "regression":
        vision_to_deaths()
