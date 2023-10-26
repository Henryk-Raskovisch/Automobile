from locadora import Automovel, Carro, Moto, mostrar_fatura
from time import sleep
import random

fiesta = Carro("Ford", "Fiesta", False)
fiesta.alugar("Joao")
print(Automovel.numero_total_locacoes)

sleep(random.randint(7, 10))
fiesta.devolver_automovel()

fiesta.gerar_valor_fatura(5, 750)


print(Carro.numero_total_locacoes_carro)
Carro.calcular_media_locacoes()
