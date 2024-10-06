from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(X_train, X_test):
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_features = vectorizer.fit_transform(X_train)
    X_test_features = vectorizer.transform(X_test)
    return X_train_features, X_test_features, vectorizer

if __name__ == "__main__":
    # This is just for demonstration, you would typically import your data here
    X_train = ["This is a sample", "Another example"]
    X_test = ["Test sample"]
    X_train_features, X_test_features, vectorizer = extract_features(X_train, X_test)
    print("Feature extraction completed.")
    print(f"Training features shape: {X_train_features.shape}")
    print(f"Test features shape: {X_test_features.shape}")
