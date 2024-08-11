import numpy as np

# Hyperparameter
learning_rate = 0.1
n_iterations = 10

# Eingabedaten (X) und Zielwerte (y) für die AND-Operation
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 0, 0, 1])  # Zielwerte für die AND-Operation

# Initialisierung der Gewichte und des Bias
n_samples, n_features = X.shape
weights = np.zeros(n_features)
bias = 0

# Training des Perzeptrons
for _ in range(n_iterations):
    for idx, x_i in enumerate(X):
        # Berechnung der gewichteten Summe
        linear_output = np.dot(x_i, weights) + bias
        # Anwendung der Schritt-Aktivierungsfunktion
        y_predicted = 1 if linear_output >= 0 else 0

        # Aktualisierung der Gewichte und des Bias
        update = learning_rate * (y[idx] - y_predicted)
        weights += update * x_i
        bias += update

# Vorhersagen treffen
predictions = []
for x_i in X:
    linear_output = np.dot(x_i, weights) + bias
    y_predicted = 1 if linear_output >= 0 else 0
    predictions.append(y_predicted)

# Ausgabe der Vorhersagen
print("Vorhersagen:", predictions)
