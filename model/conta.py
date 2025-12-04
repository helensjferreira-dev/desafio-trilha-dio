class Conta:
    contador=1
    def __init__(self,cpf):
        self.agencia = "0001"
        self.numero= Conta.contador
        self.cpf=cpf
        self.saldo=0
        self.extrato=""
        self.numero_saques = 0
        

        Conta.contador+=1 #incrementar para a proxima

    def to_dict(self):
        return {"agencia": self.agencia,"numero": self.numero,"cpf": self.cpf, "saldo":self.saldo,"extrato":self.extrato,"numero_saques": self.numero_saques}
