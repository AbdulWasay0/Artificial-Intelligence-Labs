import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv(r"C:\.Me\.Semester 5\Coding\Python\VS Code\titanic.csv")

# -----------------------------
# 2. Keep ONLY required columns
# -----------------------------
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]

# -----------------------------
# 3. Handle Missing Values
# -----------------------------
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna('S')

# -----------------------------
# 4. Encode Categorical Columns
# -----------------------------
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# -----------------------------
# 5. Features & Target
# -----------------------------
X = df.drop('Survived', axis=1)
y = df['Survived']

print("X shape:", X.shape)
print("y shape:", y.shape)

# -----------------------------
# 6. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 7. Train Model
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# -----------------------------
# 8. Prediction & Evaluation
# -----------------------------
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
