class Gas:
    
    def __init__(self):
        self.id = 0
        self.pesagem = 0
        self.Vertex_removidos = 0
        self.DataInicialDeConsumo = 0
        self.DataDePesagem = 0
        self.Valor = 0
        self.PesoInicialDoConjunto = 0
        self.TaraDoBotijao = 0
        self.TaraDoRegistro = 0
        self.PesoAtualDoConjunto = 0
thiago = Gas()
thifany = Gas()
thiago.TaraDoRegistro = 14.7
thifany.TaraDoRegistro = 3.14
print("thiago.TaraDoRegistro = ", end="")
print(thiago.TaraDoRegistro)
print("thifany.TaraDoRegistro = ", end="")
print(thifany.TaraDoRegistro)
