import random

responses = {
    "hi": [
        "Hello! How are you feeling today?",
        "Hi there! What’s on your mind?",
        "Hey! How are you doing today?"
    ],
    "sad": [
        "I'm sorry you're feeling sad. Want to talk about what's bothering you?",
        "It’s okay to feel sad sometimes. What do you think caused it?",
        "That sounds tough. What usually helps you feel better?"
    ],
    "happy": [
        "That’s great! What made you feel happy today?",
        "Nice! Happiness looks good on you.",
        "Awesome! Keep that positive energy going!"
    ],
    "angry": [
        "Anger can be hard to handle. Want to tell me what happened?",
        "It’s okay to be angry sometimes. What triggered it?",
        "Let’s take a deep breath first. What made you upset?"
    ],
    "default": [
        "I see. Tell me more about that.",
        "Interesting. How does that make you feel?",
        "Hmm, can you explain that a bit more?"
    ]
}

def get_response(user_input):
    user_input = user_input.lower()
    if "hi" in user_input or "hello" in user_input or "hey" in user_input:
        return random.choice(responses["hi"])
    elif "sad" in user_input:
        return random.choice(responses["sad"])
    elif "happy" in user_input:
        return random.choice(responses["happy"])
    elif "angry" in user_input or "mad" in user_input:
        return random.choice(responses["angry"])
    else:
        return random.choice(responses["default"])

print("AI Psychologist: Hi! I'm your AI psychologist. How are you feeling today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("AI Psychologist: Take care of yourself. Goodbye!")
        break
    response = get_response(user_input)
    print("AI Psychologist:", response)


