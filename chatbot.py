from preprocessing import preprocess_text
from model import prepare_sequences
from dialog_manager import DialogManager
import tensorflow as tf

# Assume these are loaded from trained models
model = tf.keras.models.load_model('intent_model.h5')
tokenizer = None  # Load your trained tokenizer
le = None  # Load your trained LabelEncoder

dialog_manager = DialogManager()

def chatbot():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        # Preprocess and predict intent
        processed_input = preprocess_text(user_input)
        input_seq = prepare_sequences([processed_input], tokenizer, max_length=100)[0]
        intent_prediction = model.predict(input_seq)
        predicted_intent = le.inverse_transform(intent_prediction.argmax(axis=1))[0]
        
        # Generate and print response
        response = dialog_manager.get_response(predicted_intent, {})
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
