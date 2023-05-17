def somar(*args: float) -> float:
   soma = 0
   for num in args:
      soma += num
   return soma


valor = somar(5, 7, 9, 3)
valor2 = somar(7, 6, 3, 2)
print(valor, valor2)
