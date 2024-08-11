import numpy as np

class Perzeptron:
    def __init__(self, learning_rate=0.1, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # Initialisierung der Gewichte und des Bias
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Training des Perzeptrons
        for _ in range(self.n_iterations):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_function(linear_output)

                # Aktualisierung der Gewichte und des Bias
                update = self.learning_rate * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def activation_function(self, x):
        # Schritt-Aktivierungsfunktion
        return 1 if x >= 0 else 0

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = [self.activation_function(x) for x in linear_output]
        return np.array(y_predicted)

# Beispiel für die Verwendung des Perzeptrons
if __name__ == "__main__":
    # Eingabedaten (X) und Zielwerte (y)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([0, 0, 0, 1])  # AND-Operation

    # Perzeptron erstellen und trainieren
    p = Perzeptron(learning_rate=0.1, n_iterations=10)
    p.fit(X, y)

    # Vorhersagen treffen
    predictions = p.predict(X)
    print("Vorhersagen:", predictions)
