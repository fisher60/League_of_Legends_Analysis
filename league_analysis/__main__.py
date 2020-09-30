"""Main entry point, accepts arguments for which commands to run."""

from sys import argv
from league_analysis.analysis.regression import vision_to_deaths
from league_analysis.analysis.neigh import dragons_to_kills

if __name__ == "__main__":
    command_1 = argv[1]

    if command_1 == "regression":
        vision_to_deaths()
    elif command_1 == "neigh":
        dragons_to_kills()