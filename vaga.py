class cliente (object):
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        self.enderecos=[]
    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        self.nome=novo_nome
    def get_idade(self):
        return self.idade
    def set_idade(self,nova_idade):
        self.idade=nova_idade
    def inserir_endereco(self,cidade,estado):
       endereco1=endereco(cidade,estado)
       self.enderecos.append(endereco1)
    def inserir_endereco2(self,cidade,estado):
       endereco2=endereco(cidade,estado)
       self.enderecos.append(endereco2)
    def mostrar_enderecos(self):
        if self.enderecos == []:
            print("Não ha endereço cadastrado")
        else:
            for endereco1 in self.enderecos:
                print(endereco1.get_cidade(), endereco1.get_estado())
    def mostrar_enderecos2(self):
        for endereco2 in self.enderecos:
            print(endereco2.get_cidade(), endereco2.get_estado())
class endereco(cliente):
    def __init__(self, cidade, estado):
        self.cidade=cidade
        self.estado=estado
    def get_cidade(self):
        return self.cidade
    def get_estado(self):
        return self.estado
if __name__== '__main__':
    cliente1=cliente("João cleiton",33)
    print('Nome:', cliente1.get_nome())
    print('Idade:', cliente1.get_idade())
    cliente1.inserir_endereco("cidade1","estado1")
    cliente1.mostrar_enderecos()
    cliente2=cliente("John vasco", 99)
    print("Nome:",cliente2.get_nome())
    print("Idade:",cliente2.get_idade())
    cliente2.inserir_endereco("cidade2","estado2")
    cliente2.mostrar_enderecos()