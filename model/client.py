class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento=data_nascimento
        self.endereco=endereco

    def to_dict(self):
        return {"cpf": self.cpf, "nome": self.nome,"data_nascimento": self.data_nascimento,"endereco":self.endereco}
