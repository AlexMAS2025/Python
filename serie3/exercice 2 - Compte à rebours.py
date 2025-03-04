import time

def countdown(n=10):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
    print("Fin du compte à rebours !")


countdown()
