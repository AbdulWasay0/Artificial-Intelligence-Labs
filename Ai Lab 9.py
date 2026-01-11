import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATASET
# ==========================================
# UNCOMMENT THE LINE BELOW TO USE YOUR ACTUAL FILE:
# df = pd.read_csv('diabetes_prediction_dataset.csv')

# --- SYNTHETIC DATA FOR DEMONSTRATION (REMOVE IF USING REAL DATA) ---
data = {
    'gender': ['Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female'],
    'age': [80, 54, 28, 36, 76, 20, 44, 12, 30, 50],
    'hypertension': [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    'heart_disease': [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    'smoking_history': ['never', 'No Info', 'never', 'current', 'current', 'never', 'former', 'No Info', 'current', 'former'],
    'bmi': [25.19, 27.32, 27.32, 23.45, 20.14, 27.32, 18.5, 22.0, 30.1, 25.5],
    'HbA1c_level': [6.6, 6.6, 5.7, 5.0, 4.8, 6.6, 6.5, 6.0, 7.0, 6.2],
    'blood_glucose_level': [140, 80, 158, 155, 155, 85, 200, 100, 180, 140],
    'diabetes': [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
}
df = pd.DataFrame(data)
# --------------------------------------------------------------------

print("--- Raw Data Head ---")
print(df.head())

# ==========================================
# 2. PREPROCESS DATA
# ==========================================

# Convert Categorical Features
def preprocess_inputs(df):
    df_processed = df.copy()
    
    # Map Gender
    gender_map = {'Female': 0, 'Male': 1, 'Other': 2}
    df_processed['gender'] = df_processed['gender'].map(gender_map).fillna(0)
    
    # Map Smoking History
    smoking_map = {
        'never': 0, 'former': 1, 'current': 2, 
        'No Info': 3, 'not current': 4, 'ever': 5
    }
    df_processed['smoking_history'] = df_processed['smoking_history'].map(smoking_map).fillna(0)
    
    # Normalize Numerical Features
    # Simple Min-Max scaling manually or just dividing by max to keep it in [0,1] range
    for col in ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']:
        df_processed[col] = (df_processed[col] - df_processed[col].min()) / (df_processed[col].max() - df_processed[col].min())
        
    return df_processed

processed_df = preprocess_inputs(df)
print("\n--- Processed Data Head ---")
print(processed_df.head())

# Split X (features) and y (target)
# Dropping target 'diabetes'. Assuming all other columns are features.
X = processed_df.drop('diabetes', axis=1).values
y_true = processed_df['diabetes'].values

# ==========================================
# 3. CORE TASKS & PREDICT FUNCTION
# ==========================================

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(X, weights, bias):
    # z = dot product + bias
    z = np.dot(X, weights) + bias
    # Return probabilities
    return sigmoid(z)

def get_accuracy(y_true, y_prob):
    # Round predictions to 0 or 1
    y_pred = [1 if p >= 0.5 else 0 for p in y_prob]
    # Calculate Mean Accuracy
    return np.mean(y_pred == y_true)

# ==========================================
# 4. WEIGHT TUNING EXPERIMENTS
# ==========================================

# Initialize weights randomly or with specific values
# We have 8 features in the standard dataset. We need 8 weights.
# Adjust this array size if your specific dataset has different feature counts.
num_features = X.shape[1]
initial_weights = np.random.rand(num_features) 
initial_bias = 0.05

print(f"\n--- Initial Random Experiment (Bias: {initial_bias}) ---")
probs = predict(X, initial_weights, initial_bias)
acc = get_accuracy(y_true, probs)
print(f"Accuracy with random weights: {acc * 100:.2f}%")

# ==========================================
# 5. ANSWERING QUESTIONS
# ==========================================

# --- Q: How does the bias term shift predictions? ---
print("\n--- Bias Shift Experiment ---")

# Test Bias = -1
bias_neg = -1.0
probs_neg = predict(X, initial_weights, bias_neg)
acc_neg = get_accuracy(y_true, probs_neg)
print(f"Bias = -1.0 -> Mean Prob: {np.mean(probs_neg):.4f}, Accuracy: {acc_neg:.2f}")

# Test Bias = +1
bias_pos = 1.0
probs_pos = predict(X, initial_weights, bias_pos)
acc_pos = get_accuracy(y_true, probs_pos)
print(f"Bias = +1.0 -> Mean Prob: {np.mean(probs_pos):.4f}, Accuracy: {acc_pos:.2f}")


# --- Q: Accuracy vs. Single Weight (Bar Plot) ---
print("\n--- Generating Weight Sensitivity Plot... ---")

# We will modify the weight of the 7th feature (HbA1c_level) specifically 
# as requested in source 28 example, or loop through variations.
# Let's try changing the weight of 'HbA1c_level' (index 6 typically)
feature_index = 6 # Assuming HbA1c is at index 6
weight_variations = [-2, -1, 0, 1, 2, 5]
accuracies = []

for w in weight_variations:
    temp_weights = initial_weights.copy()
    if feature_index < len(temp_weights):
        temp_weights[feature_index] = w
        
    p = predict(X, temp_weights, initial_bias)
    accuracies.append(get_accuracy(y_true, p))

# Plotting
plt.figure(figsize=(8, 5))
plt.bar([str(w) for w in weight_variations], accuracies, color='skyblue')
plt.xlabel(f'Weight Value for Feature Index {feature_index}')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Single Weight Variation')
plt.ylim(0, 1.1)
plt.show()

print("Done. Take screenshots of the output above for your report.")