class Calculadora:

    @staticmethod
    def sumar(num1, num2):
        return num1 + num2
    
    @staticmethod
    def restar(num1, num2):
        return num1 - num2
    
    @staticmethod
    def multiplicar(num1, num2):
        return num1 * num2
    
    @staticmethod
    def dividir(num1, num2):
        if num2 == 0:
            print("No se admiten divisiones por 0.")
        else:
            return num1 / num2
    

resultado_suma = Calculadora.sumar(7, 8)
print(resultado_suma)

resultado_resta = Calculadora.restar(9, 1)
print(resultado_resta)

resultado_multiplicacion = Calculadora.multiplicar(3, 9)
resultado_division = Calculadora.dividir(7, 0)
resultado_division = Calculadora.dividir(9, 3)

print(resultado_multiplicacion)
print(resultado_division)