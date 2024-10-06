from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

def prepare_intent_recognition(y_train, y_test):
    le = LabelEncoder()
    y_train_encoded = le.fit_transform(y_train)
    y_test_encoded = le.transform(y_test)
    
    y_train_categorical = to_categorical(y_train_encoded)
    y_test_categorical = to_categorical(y_test_encoded)
    
    return y_train_categorical, y_test_categorical, le

if __name__ == "__main__":
    # This is just for demonstration
    y_train = ['greeting', 'farewell', 'greeting', 'query']
    y_test = ['greeting', 'query']
    y_train_cat, y_test_cat, le = prepare_intent_recognition(y_train, y_test)
    print("Intent recognition preparation completed.")
    print(f"Number of intents: {len(le.classes_)}")
