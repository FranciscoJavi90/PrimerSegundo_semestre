age = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuáles son tus ingresos mensuales? "))
if age > 18 and income >= 3000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")