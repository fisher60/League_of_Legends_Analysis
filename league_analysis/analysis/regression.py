import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from league_analysis.parsing.get_data import get_columns


def vision_to_deaths(team="blue"):
    data = get_columns([f"{team}WardsPlaced", f"{team}Deaths"])
    print(data)
    vision_data = data[0]
    deaths_data = data[1]

    staged_data = [[wards, deaths] for wards, deaths in zip(vision_data, deaths_data)]

    if len(staged_data) % 2:
        staged_data.pop()

    x_train = [[x[0]] for x in staged_data[:len(staged_data) // 2]]
    y_train = [[x[1]] for x in staged_data[:len(staged_data) // 2]]

    x_test = [[x[0]] for x in staged_data[len(staged_data) // 2:]]
    y_test = [[x[1]] for x in staged_data[len(staged_data) // 2:]]

    X = np.array(x_train)
    y = np.array(y_train)

    reg = LinearRegression().fit(X, y)
    y_pred = reg.predict(np.array(x_test))

    print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print('Coefficient of determination: %.2f' % r2_score(y_test, y_pred))

    # Plot outputs
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.scatter(x_test, y_test, color='b')
    ax.scatter(x_test, y_pred, color='r')
    ax.set_xlabel('Vision')
    ax.set_ylabel('Deaths')
    ax.set_title('Vision/Deaths')
    plt.show()
