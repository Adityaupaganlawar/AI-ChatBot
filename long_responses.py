import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_AGE = "I am just as that of your age!!"
R_NAME = "My name is your ChatBot_Buddy!"
R_SHOP = "I would like to buy something","What are your products?","what do you recommend","What are you selling?"
R_HOURS = "24/7"
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
