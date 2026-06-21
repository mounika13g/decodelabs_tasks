response = {
    "hello": "hello! how can i help you?",
    "hi": "hey there!",
    "hey" : "hey there!",
    "how are you": "im good thanks for asking! What about you?",
    "what is the full form of ai":"Artifical Intelligence",
    "what is ai": "ai is basically making computers think like humans",
    "difference between ai and human": "humans understand any language naturally and learn on their own, but ai like me only responds to what i was programmed with. humans think, ai just matches.",
    "bye": "bye see you!",
    "thanks": "no problem!",
    "help": "I can answer for questions such as 'hello', 'how are you', 'what is the full form of ai', 'what is ai' and 'difference between ai and human'",
    "about": "im a simple userfriendly chatbot "
}
print("Heyy How are you doing? Need some help?")
print()
while True:
    msg = input("you: ")
    msg = msg.lower().strip()
    if msg == "exit":
        print("bot: goodbye!")
        break
    reply = response.get(msg, "sorry i dont understand that")
    print("bot:", reply)
    print()