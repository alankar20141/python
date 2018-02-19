import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]

while True:
        #Input = raw_input(">>> ")
        if Input in greetings:
                random_greeting = random.choice(greetings)
                print(random_greeting)
        elif Input in question:
                random_response = random.choice(responses)
                print(random_response)
        else:
                print("I did not understand what you said")
