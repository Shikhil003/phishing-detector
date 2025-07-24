# preprocess.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.io import arff

def load_and_preprocess_data(arff_path='Training_dataset.arff'):
    # Load .arff file correctly
    data, meta = arff.loadarff(arff_path)
    df = pd.DataFrame(data)

    # Decode byte strings to regular strings
    for col in df.select_dtypes(include=[object]).columns:
        df[col] = df[col].apply(lambda x: x.decode('utf-8'))

    # Drop missing values
    df = df.dropna()

    # Separate features and label
    X = df.drop('Result', axis=1)
    y = df['Result'].astype(int)  # Ensure labels are numeric

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler
