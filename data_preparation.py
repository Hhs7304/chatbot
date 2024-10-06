import pandas as pd
import re
from sklearn.model_selection import train_test_split

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().strip()

def prepare_data(file_path):
    df = pd.read_csv(file_path)
    df['clean_text'] = df['text'].apply(clean_text)
    
    X_train, X_test, y_train, y_test = train_test_split(df['clean_text'], df['label'], test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = prepare_data('conversations.csv')
    print("Data preparation completed.")
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
