import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Dynamic Paths (So it works on any computer)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'Crop_recommendation.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.bin')

print("------------------------------------------------")
print(f"STEP 1: Loading Data from {DATA_PATH}...")
df = pd.read_csv(DATA_PATH)
df.columns = df.columns.str.lower()

# Map labels
unique_labels = df['label'].unique()
label_to_id = {label: idx for idx, label in enumerate(unique_labels)}
id_to_label = {idx: label for label, idx in label_to_id.items()}
df['label_idx'] = df['label'].map(label_to_id)

X = df.drop(['label', 'label_idx'], axis=1)
y = df['label_idx']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("STEP 2: Training Model...")
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train, y_train)

acc = accuracy_score(y_test, rf.predict(X_test))
print(f"✅ Model Accuracy: {acc*100:.2f}%")

print(f"STEP 3: Saving model to {MODEL_PATH}...")
with open(MODEL_PATH, 'wb') as f_out:
    pickle.dump((rf, id_to_label), f_out)

print("DONE!")