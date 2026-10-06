from datetime import date


class Cliente:
    def __init__(self, nome, documento, telefone):
        self.nome = nome
        self.documento = documento
        self.telefone = telefone


class Veiculo:
    def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.disponivel = True


class Condutor:
    def __init__(self, nome, numero_cnh):
        self.nome = nome
        self.numero_cnh = numero_cnh

    def validar_cnh(self):
        return len(self.numero_cnh) == 11 and self.numero_cnh.isdigit()

    def __str__(self):
        return f"{self.nome} (CNH: {self.numero_cnh})"


class Contrato:
    def __init__(self, cliente, veiculo, data_inicio, data_termino,
                 nome_condutor, cnh_condutor):
        if not veiculo.disponivel:
            raise ValueError("Veículo já possui contrato ativo.")

        # Associação: cliente e veículo são recebidos e existem por conta própria
        self.cliente = cliente
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.status = "ativo"
        self.valor_total = self.calcular_valor_total()
        self.veiculo.disponivel = False

        # COMPOSIÇÃO: o Contrato instancia o Condutor.
        # Sem contrato, o condutor não existe.
        self.condutor = Condutor(nome_condutor, cnh_condutor)

    def calcular_valor_total(self):
        dias = (self.data_termino - self.data_inicio).days
        return dias * self.veiculo.valor_diaria

    def finalizar(self):
        self.status = "finalizado"
        self.veiculo.disponivel = True

    def cancelar(self):
        self.status = "cancelado"
        self.veiculo.disponivel = True


# Demonstração
cliente = Cliente("Maria Silva", "123.456.789-00", "(86) 99999-0000")
carro = Veiculo("ABC-1234", "Onix", 2023, 150.0)

contrato = Contrato(cliente, carro, date(2026, 10, 10), date(2026, 10, 15),
                    "João Souza", "12345678901")

print(contrato.condutor)                # João Souza (CNH: 12345678901)
print(contrato.valor_total)             # 750.0
print(contrato.condutor.validar_cnh())  # True

del contrato  # ao excluir o contrato, o condutor deixa de existir junto com ele
