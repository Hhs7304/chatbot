import random

responses = {
    'greeting': ['Hello!', 'Hi there!', 'Greetings!'],
    'farewell': ['Goodbye!', 'See you later!', 'Take care!'],
    # Add more intents and responses
}

def generate_response(intent):
    return random.choice(responses.get(intent, ["I'm not sure how to respond to that."]))

if __name__ == "__main__":
    print(generate_response('greeting'))
    print(generate_response('farewell'))
    print(generate_response('unknown'))
