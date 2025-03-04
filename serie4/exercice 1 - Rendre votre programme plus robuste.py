class CustomError(Exception):
    def __init__(self, message="Une erreur s'est produite"):
        self.message = message
        super().__init__(self.message)


def int_input(func):
    def wrapper(*args, **kwargs):
        try:
            return int(func(*args, **kwargs))
        except ValueError:
            raise CustomError
    return wrapper

    input = int_input(input)
while True:
    try:
        user_number = input("Entrez un nombre : ")
    except CustomError as e:
        print(e)
    else:
        print(f"Vous+ avez entré : {user_number}")
        break