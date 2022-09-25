import random

def aleatorio():
    vet = []
    a = []
    for i in range(0, 6):
        a = random.randint(1, 60)
        print(a)

def main():
    aleatorio()

if __name__ == "__main__":
    main()
