h1 = 100
bounce = 0.6

def calcular_rebote(h1,bounce):
    return round(h1*bounce,4)

for i in range(10):
    h1 = calcular_rebote(h1,bounce)
    print(h1)
   