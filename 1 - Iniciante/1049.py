p1 = input()
p2 = input()
p3 = input()

try:
    if p1 == 'vertebrado' and p2 == 'ave' and p3 == 'carnivoro':
        animal = 'aguia'
    elif p1 == 'vertebrado' and p2 == 'ave' and p3 == 'onivoro':
        animal = 'pomba'
    elif p1 == 'vertebrado' and p2 == 'mamifero' and p3 == 'onivoro':
        animal = 'homem'
    elif p1 == 'vertebrado' and p2 == 'mamifero' and p3 == 'herbivoro':
        animal = 'vaca'
    elif p1 == 'invertebrado' and p2 == 'inseto' and p3 == 'hematofago':
        animal = 'pulga'
    elif p1 == 'invertebrado' and p2 == 'inseto' and p3 == 'herbivoro':
        animal = 'lagarta'
    elif p1 == 'invertebrado' and p2 == 'anelideo' and p3 == 'hematofago':
        animal = 'sanguessuga'
    elif p1 == 'invertebrado' and p2 == 'anelideo' and p3 == 'onivoro':
        animal = 'minhoca'

    print(animal)
except NameError:
    print('Digite um tipo válido')