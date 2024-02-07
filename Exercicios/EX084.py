class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, ler_celsius):
        if float(ler_celsius) < -273.15:
            print("A temperatura em Celsius não pode ser inferior a -273.15")
        else:
            self._celsius = ler_celsius

    def fahrenheit(self):
        return f"A Temperatura em kelvin --> {(self._celsius * 9/5) + 32}"

    def kelvin(self):
        return f"A Temperatura em kelvin --> {self._celsius + 237.15}"


temperatura_atual = float(input("Insira a temperatura em Celsius: "))
temperatura_obj = Temperatura(temperatura_atual)


print(f'{temperatura_obj.celsius} °C')
print(f'{temperatura_obj.fahrenheit()} °F\n')
print(f'{temperatura_obj.kelvin()} K\n')


nova_temperatura = float(input("Digite a nova temperatura em Celsius --> "))
temperatura_obj.celsius = nova_temperatura


print(f'{temperatura_obj.celsius} °C')
print(f'{temperatura_obj.fahrenheit()} °F\n')
print(f'{temperatura_obj.kelvin()} K\n')
