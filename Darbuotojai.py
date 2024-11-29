darbuotojai = []

darb_skaicius = int(input("Iveskite darbuotoju skaiciu > "))

for i in range(1, darb_skaicius + 1):
    vardas = input(f"Iveskite {i} darbuotojo varda")
    pareigos = input(f"Iveskite {i} darbuotojo pareigas")
    atlyginimas = int(input(f"Iveskite {i} darbuotojo atlyginima"))
    darbuotojas = [vardas, pareigos, atlyginimas]
    darbuotojai.append(darbuotojas)

print(darbuotojai)