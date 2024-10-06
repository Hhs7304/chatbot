from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def create_model(vocab_size, max_length):
    model = Sequential([
        Embedding(vocab_size, 32, input_length=max_length),
        LSTM(64),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def prepare_sequences(X_train, X_test, vocab_size, max_length):
    tokenizer = Tokenizer(num_words=vocab_size)
    tokenizer.fit_on_texts(X_train)
    
    X_train_seq = tokenizer.texts_to_sequences(X_train)
    X_test_seq = tokenizer.texts_to_sequences(X_test)
    
    X_train_pad = pad_sequences(X_train_seq, maxlen=max_length)
    X_test_pad = pad_sequences(X_test_seq, maxlen=max_length)
    
    return X_train_pad, X_test_pad, tokenizer

if __name__ == "__main__":
    # This is just for demonstration
    vocab_size = 5000
    max_length = 100
    model = create_model(vocab_size, max_length)
    model.summary()
