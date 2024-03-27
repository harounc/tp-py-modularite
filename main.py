# main.py

import operations

# Demander l'opération jusqu'à ce que l'utilisateur en donne une qui est valide
while True:
  op = input("Entrez le l'opération à effectuer (+, -, *, /) : ")
  if op in "+-*/": # il faut que ça appartient à ces caractères

    # Mais n'oublie pas que si l'utilisateur tape "+*", la condition précédente serait vérifiée.
    # Ce n'est donc pas suffisant
    if len(op) == 1: # Il faut que ce soit un seul caractère
      break
  # Sinon, la boucle s'exécute encore

a = int(input("Entrez l'opérande a : "))
b = int(input("Entrez l'opérande b: "))

resultat = None

if op == "+":
  resultat = operations.addition(a, b)

elif op == "-":
  resultat = operations.soustraction(a, b)

elif op == "*":
  resultat = operations.multiplication(a, b)

elif op == "/":
  resultat = operations.division(a, b)

elif op == "%":
  resultat = operations.modulo(a, b)

print(f"Le résultat de {a} {op} {b} est: {resultat} ")