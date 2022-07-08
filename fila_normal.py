class filanormal:
    codigo= 0
    fila = []
    clientesatendido = []
    senhatual = ""

    def gerasenhaatual(self):
        self.senhatual = f'NM{self.codigo}'

    def resetafila(self):
        if self.codigo >- 100:
            self.codigo=0
        else:
            self.codigo+=1
    def atualizafila(self):
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhatual)
    def chamacliente(self, caixa):
        cliente_atual = self.fila.pop(0)
        self.clientesatendido.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, dirija-se ao caixa')
