import random

def imprimeVetor(vetor):
    for i in range(len(vetor)):
        print(vetor[i])

def aleatorio():
    vet = []
    for i in range(6):
        a = random.randint(1, 60)
        if a not in vet: vet.append(a)
    imprimeVetor(vet)

def main():
    aleatorio()

if __name__ == "__main__":
    main()
