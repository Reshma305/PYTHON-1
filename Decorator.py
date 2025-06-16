def add_fruits(func):
    def wrapper():
        print("You add fruits🍇")
        func()
    return wrapper

@add_fruits
def get_ice_cream():
    print("Here is your ice cream 🍧")

get_ice_cream()
