from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Load dataset
data = load_iris()

X = data.data      # features
y = data.target    # labels

# 2. Split data (80% training - 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Create model
model = DecisionTreeClassifier()

# 4. Train model
model.fit(X_train, y_train)

# 5. Predict
y_pred = model.predict(X_test)

# 6. Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)