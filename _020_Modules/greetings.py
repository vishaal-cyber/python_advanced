__all__ = ['greet', 'greetName', 'greetInteractive']

def greet():
    print("Hi there")

def greetName(name):
    salutation = "Hello"
    final_greeting = prepGreeting(salutation, name)
    print(final_greeting)

def prepGreeting(salutation, name):
    return f"{salutation}, {name}!"

def greetInteractive():
    name = input("Enter your name: ")
    salutation = "Hey"
    final_greeting = prepGreeting(salutation, name)
    print(final_greeting)

# if __name__ == " __main__":
def TestGreetings():
    print("#"*25)
    greet()
    print("-"*20)
    greetName("Vinayak")
    print("-"*20)
    greetInteractive()
    print("#"*25)


def TestGreetings_NonInteractive():
    print("#"*25)
    greet()
    print("-"*20)
    greetName("Vinayak")
    print("#"*25)


# print(f"{__name__ = }")
if __name__ == "__main__":
    # TestGreetings()
    TestGreetings_NonInteractive
