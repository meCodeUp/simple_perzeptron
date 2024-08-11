# Dinfaches Perzeptron
Dieser Python-Code implementiert ein einfaches Perzeptron, ein grundlegendes Modell eines künstlichen Neurons, das für binäre Klassifikationsaufgaben verwendet wird. Das Perzeptron wird mit einer Schritt-Aktivierungsfunktion trainiert und kann verwendet werden, um logische Operationen wie die AND-Operation zu lernen.
Klassen und Methoden

## 1. Perzeptron-Klasse

Die Perzeptron-Klasse enthält die Hauptlogik für das Perzeptron-Modell. Sie umfasst folgende Attribute und Methoden:

### Attribute:

- learning_rate: Die Lernrate, die bestimmt, wie stark die Gewichte bei jeder Aktualisierung angepasst werden.
- n_iterations: Die Anzahl der Trainingsdurchläufe über die gesamte Datenmenge.
- weights: Die Gewichte des Perzeptrons, die während des Trainings angepasst werden.
- bias: Der Bias-Term, der ebenfalls während des Trainings angepasst wird.

### Methoden:

- __init__(self, learning_rate=0.1, n_iterations=100): Konstruktor, der die Lernrate und die Anzahl der Iterationen initialisiert.
- fit(self, X, y): Diese Methode trainiert das Perzeptron. Sie initialisiert die Gewichte und den Bias auf Null und führt dann für die angegebene Anzahl von Iterationen das Training durch. In jeder Iteration wird die gewichtete Summe der Eingaben berechnet, die Aktivierungsfunktion angewendet und die Gewichte sowie der Bias entsprechend der Vorhersagefehler aktualisiert.
- activation_function(self, x): Diese Methode implementiert die Schritt-Aktivierungsfunktion. Sie gibt 1 zurück, wenn der Eingabewert x größer oder gleich 0 ist, und 0, wenn er kleiner ist.

predict(self, X): Diese Methode verwendet die trainierten Gewichte und den Bias, um Vorhersagen für neue Eingabewerte zu treffen. Sie berechnet die gewichtete Summe für jede Eingabe und wendet die Aktivierungsfunktion an.

## 2. Beispielverwendung

Im Hauptteil des Codes wird ein Beispiel für die Verwendung des Perzeptrons gegeben:

- Eingabedaten (X): Ein Array von Eingabewerten, das die möglichen Kombinationen von zwei binären Eingaben (0 und 1) darstellt. In diesem Fall wird die AND-Operation verwendet.
- Zielwerte (y): Ein Array von Zielwerten, das die erwarteten Ausgaben für die AND-Operation darstellt.
- Perzeptron-Instanz: Eine Instanz der Perzeptron-Klasse wird erstellt, und das Modell wird mit den Eingabedaten und Zielwerten trainiert.
- Vorhersagen: Nach dem Training werden Vorhersagen für die Eingabewerte getroffen, und die Ergebnisse werden ausgegeben.

Dieser Code bietet eine einfache Implementierung eines Perzeptrons, das für grundlegende binäre Klassifikationsaufgaben geeignet ist. Er kann leicht erweitert oder modifiziert werden, um komplexere Probleme zu lösen oder andere Aktivierungsfunktionen zu verwenden.
