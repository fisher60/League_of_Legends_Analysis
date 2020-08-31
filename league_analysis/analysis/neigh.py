import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from league_analysis.parsing.get_data import get_columns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

def dragons_to_kills(team="blue"):
    data = get_columns([f"{team}Dragons", f"{team}Kills", f"{team}Wins"])

    drags_killed = data[0]
    team_kills = data[1]
    team_wins = data[2]
    objectives = [[drag, kill] for drag, kill in zip(drags_killed, team_kills)]

    outcome = [i for i in team_wins]


    X = np.array(objectives)
    y = np.array(outcome)
    # print(X.shape)
    # print(y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)


    error = []
    for i in range(1, 40):

        neigh = KNeighborsClassifier(n_neighbors=i)
        neigh.fit(X_train, y_train)
        y_pred = neigh.predict(X_test)
        error.append((np.mean(y_pred != y_test)))


    print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    plt.figure(figsize=(12, 6))
    plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
             markerfacecolor='blue', markersize=10)
    plt.title('Error Rate K Value')
    plt.xlabel('K Value')
    plt.ylabel('Mean Error')
    plt.show()



    # print(neigh.predict([[1,7]]))
    # print(neigh.predict([[0, 10]]))
    # print(neigh.predict([[0, 5]]))
