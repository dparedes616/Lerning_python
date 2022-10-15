def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors



def run():
    try:
        num = int(input("Ingrese un numero: "))
        print(divisors(num))
        print("Programa Terminado")
    except ValueError:
        print("Debes ingresar un numero")

    





if __name__ == "__main__":
    run()