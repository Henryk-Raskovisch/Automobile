VALOR_PEDAGIO_CARRO = 3
VALOR_KM_RODADO_CARRO = 2
VALOR_PEDAGIO_MOTO = 1.75
VALOR_KM_RODADO_MOTO = 1.5


class Automovel:
    numero_total_locacoes = 0

    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ""
        print(f"Automovel {self.montadora} {self.modelo} adquirido pela locadora!")

    def alugar(self, nome_cliente):
        Automovel.numero_total_locacoes += 1
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f"O automovel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}")

    def devolver_automovel(self):
        self.alugado = False
        print(f"O automovel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}")

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        raise NotImplementedError

    @classmethod
    def mostrar_numero_total_locacoes(cls):
        print(f"O numero total de locacoes de automoveis e de {cls.numero_total_locacoes} locacoes")


class Carro(Automovel):
    valor_total_locacoes = 0.0
    numero_total_locacoes_carro = 0

    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)
        print("O automovel adquirido foi um carro!")

    def alugar(self, nome_cliente):
        super(Carro, self).alugar(nome_cliente)
        Carro.numero_total_locacoes_carro += 1

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_CARRO + km_rodados * VALOR_KM_RODADO_CARRO
        print(f"Fatura do carro {self.montadora} {self.modelo} gerada com sucesso no valor de € {self.valor_fatura}")
        Carro.valor_total_locacoes += self.valor_fatura

    @classmethod
    def calcular_media_locacoes(cls):
        if cls.numero_total_locacoes_carro != 0:
            media_locacoes = cls.valor_total_locacoes / cls.numero_total_locacoes_carro
            print(f"O valor medio de locacao de carros esta em €{media_locacoes}/locacao")
        else:
            print("Numero total de locacoes de carros igual a zero")


class Moto(Automovel):
    valor_total_locacoes = 0.0
    numero_total_locacoes_moto = 0

    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O automovel adquirido foi uma moto!")

    def alugar(self, nome_cliente):
        super(Moto, self).alugar(nome_cliente)
        Moto.numero_total_locacoes_moto += 1

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_MOTO + km_rodados * VALOR_KM_RODADO_MOTO
        print(f"Fatura da moto {self.montadora} {self.modelo} gerada com sucesso no valor de € {self.valor_fatura}")
        Moto.valor_total_locacoes += self.valor_fatura

    @classmethod
    def calcular_media_locacoes(cls):
        if cls.numero_total_locacoes_moto != 0:
            media_locacoes = cls.valor_total_locacoes / cls.numero_total_locacoes_moto
            print(f"O valor medio de locacao de motos esta em €{media_locacoes}/locacao")
        else:
            print("Numero total de locacoes de motos igual a zero")

def mostrar_fatura(automovel):
    print(f"O valor do automovel {automovel.montadora} {automovel.modelo} alugado por {automovel.nome_cliente}"
          f" ficou no valor de €{automovel.valor_fatura:.2f}")


