import numpy as np
from sklearn.linear_model import LinearRegression
from league_analysis.parsing.get_data import get_column


def vision_to_deaths(team="blue"):
    vision_data = get_column(f"{team}WardsPlaced")
    deaths_data = get_column(f"{team}Deaths")

    X = np.array([[wards, deaths] for wards, deaths in zip(vision_data, deaths_data)])
    y = np.dot(X, np.array([1, 2])) + 3

    reg = LinearRegression().fit(X, y)
    print(f"Score is: {reg.score(X, y)}")

    print(reg.predict(np.array([[25, 6]])))


vision_to_deaths()
