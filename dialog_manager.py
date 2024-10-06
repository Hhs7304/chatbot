from response_generation import generate_response

class DialogManager:
    def __init__(self):
        self.context = {}

    def update_context(self, intent, entities):
        self.context['last_intent'] = intent
        self.context.update(entities)

    def get_response(self, intent, entities):
        self.update_context(intent, entities)
        # Logic to determine the appropriate response based on intent and context
        response = generate_response(intent)
        return response

if __name__ == "__main__":
    dialog_manager = DialogManager()
    print(dialog_manager.get_response('greeting', {}))
    print(dialog_manager.get_response('farewell', {}))
