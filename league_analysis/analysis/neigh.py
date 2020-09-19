import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from league_analysis.parsing.get_data import get_columns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from matplotlib.colors import ListedColormap

import pandas as pd

def dragons_to_kills(team="blue"):
    data = get_columns([f"{team}Dragons", f"{team}Kills", f"{team}Wins"])

    drags_killed = data[0]
    team_kills = data[1]
    team_wins = data[2]
    objectives = [[drag, kill] for drag, kill in zip(drags_killed, team_kills)]

    outcome = [i for i in team_wins]


    X = np.array(objectives)
    y = np.array(outcome)
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


def win_conditions(team="blue"):
    df = get_columns([f"{team}FirstBlood", f"{team}Dragons", f"{team}Kills", f"{team}Heralds", f"{team}Wins"])

    first_blood = df[0]
    dragons = df[1]
    kills = df[2]
    heralds = df[3]
    wins = df[4]
    objectives = [[fb, drags, herald, kill] for fb, drags, herald, kill in zip(first_blood, dragons, heralds, kills)]

    outcome = [i for i in wins]
    X = np.array(objectives)
    y = np.array(outcome)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

    classifier = KNeighborsClassifier(n_neighbors=13)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    X_set, y_set = X_train, y_train
    X1, X2 = np.meshgrid(np.arange(start=X_test[:, 0].min() - 1, stop=X_test[:, 0].max() + 1, step=0.01),
                         np.arange(start=X_test[:, 1].min() - 1, stop=X_test[:, 1].max() + 1, step=0.01))
    plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha=0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_test[y_test == j, 0], X_test[y_set == j, 1],
                    c=ListedColormap(('red', 'green'))(i), label=j)
    plt.title('Classifier (Training set)')
    plt.xlabel('Objectives')
    plt.ylabel('Outcome')
    plt.legend()
    plt.show()



    # error = []
    # for i in range(1, 100):
    #
    #     neigh = KNeighborsClassifier(n_neighbors=i)
    #     neigh.fit(X_train, y_train)
    #     y_pred = neigh.predict(X_test)
    #     error.append((np.mean(y_pred != y_test)))
    #
    #
    #print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))
    #
    # plt.figure(figsize=(12, 6))
    # plt.plot(range(1, 100), error, color='red', linestyle='dashed', marker='o',
    #          markerfacecolor='blue', markersize=10)
    # plt.title('Error Rate K Value')
    # plt.xlabel('K Value')
    # plt.ylabel('Mean Error')
    # plt.show()