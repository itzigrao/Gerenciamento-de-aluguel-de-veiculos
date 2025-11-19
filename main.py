import datetime

class Veiculo:
    def __init__(self, placa, modelo, categoria, tarifa_diaria):
        self.__placa = placa
        self.__modelo = modelo
        self.__categoria = categoria
        self.__tarifa_diaria = tarifa_diaria
        self.__status = "disponivel"
        self.__veiculos_registrados = []


    def detalhes (self):
        print(" ----Detalhes do Veiculo----")
        print(f" Placa: {self.placa}")
        print(f" Modelo: {self.__modelo}")
        print(f" Categoria: {self.__categoria}")
        print(f" Tarifa diaria: {self.__tarifa_diaria}")
        print(f" Status: {self.__status}")

    def alugar (self):
        if self.__status == "disponivel":
            self.__status == "ocupado"
            print(f" O veiculo de placa {self.__placa}, foi alugado")
            return True
        else:
            print(f" Veiculo de placa {self.__placa} esta indisponivel.")
            return False

    def devolver (self):
        if self.__status == "disponivel":
            print(f" ERRO, veiculo de placa {self.__placa} consta disponivel")
        else:
            self.__status == "disponivel"
            print(f"Veículo de placa {self.__placa} foi devolvido com sucesso!")


    
    def calcular_valor_aluguel(self, dias):
        print(" calcular valor do aluguel")
        if dias <= 0:
            dias = 1
        return self.tarifa_diaria * dias

    @property
    def placa (self):
        return self.__placa
    
    @property
    def modelo (self):
        return self.__modelo
    

    @property
    def status (self):
        return self.__status


    @property
    def tarifa_diaria (self):
        return self.__tarifa_diaria
    

    
class Carro(Veiculo):
    def __init__(self, placa, modelo, categoria, tarifa_diaria, numero_portas):
        super().__init__(placa, modelo, categoria, tarifa_diaria)
        self.__numero_portas = numero_portas

    def detalhes(self):
        super().detalhes()
        print(" Tipo: carro")
        print(f" Numero de portas: {self.__numero_portas}")


    def calcular_valor_aluguel(self, dias):
        valor_base = super().calcular_valor_aluguel(dias)
        if self.__categoria == "luxo":
            taxa_luxo = 150.00
            print(f" Taxa extra para carros de luxo de R$150,00")
            return valor_base + taxa_luxo
        return valor_base
    @property
    def numero_portas (self):
        return self.__numero_portas

class Moto(Veiculo):
    def __init__(self, placa, modelo, categoria, tarifa_diaria, cilindradas):
        super().__init__(placa, modelo, categoria, tarifa_diaria)
        
        self.__cilindradas = cilindradas

    def detalhes(self):
        super().detalhes()
        print(" Tipo: Moto")
        print( f"Clindradas: {self.__cilindradas}")
    

    def calcular_valor_aluguel(self, dias):
        valor_base = super().calcular_valor_aluguel(dias)
        if dias >=10:
            print(" Desconto de 10% para alugueis de moto por mais de 30 dias!")
            desconto = valor_base * 0.10
            return valor_base - desconto
        return valor_base
    
        

    @property
    def cilindradas (self):
        return self.__cilindradas
    
    

class Cliente:
            
    def __init__ (self, nome, cpf, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__historico = []




    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome: # Validação simples
            self.__nome = novo_nome
        else:
            print("ERRO: Nome não pode ser vazio.")

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nascimento(self):
        return self.__nascimento

    @property
    def historico(self):
        """Retorna uma CÓPIA da lista, para evitar modificação externa."""
        return self.__historico.copy()
    

    def exibir_detalhes(self):
        print("---Detalhes do Cliente---")
        print(f"Nome: {self.nome}")
        print(f" cpf: {self.cpf}")
        print(f" Data de nascimento: {self.nascimento}")
        print(f" Totalm de contratos: {len(self.historico)}")


    def adicionar_contrato(self, contrato):
        print(" ADICIONAR CONTRATO AO HISTÓRICO DE CONTRATOS")
        self.__historico.append(contrato)
        print(f"Novo contrato adicionado ao histórico do cliente {self.nome}.")

class Contratos_aluguel: #Um contrato é um documento que liga um objeto cliente específico a um objeto veículo específico.
    def __init__(self, cliente, veiculo, data_inicio, data_termino):
        self.__cliente = cliente
        self.__veiculo = veiculo
        self.__data_inicio = data_inicio
        self.__data_termino = data_termino
        self.__data_termino_real = None #para saber qual é o dia exato do termino, comeca com (None)
        self.__ativo = True # Variavel para saber se o contrato esta ativo, comeca ativo
        self.__valor_total = self.calcular_valor_total(self.__data_termino)

    @property
    def cliente(self):
        return self.__cliente

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def ativo(self):
        return self.__ativo
        
    @property
    def valor_total(self):
        return self.__valor_total



    def calcular_valor_total (self, data_fim):

        dias = (data_fim - self.__data_inicio).days
        if dias <= 0:
            dias = 1

        return self.__veiculo.calcular_valor_aluguel(dias)
    
    def exibir_detalhes (self):
        print("---Detalhes---")
        print(f" Contrato (ativo: {self.ativo})")
        print(f" Cliente: {self.cliente.nome} Cpf: {self.cliente.cpf}")
        print(f" Veículo: {self.veiculo.modelo}, Placa: {self.veiculo.placa}")
        print(f" O valor total previsto é de: {self.valor_total:.2f}")

    def encerrar_contrtao (self, data_devolucao):
        if self.__ativo:
            self.__ativo = False
            self.__data_termino_real = data_devolucao

            self.__valor_total = self.calcular_valor_total(self.__data_termino_real)

            self.__veiculo.devolver()
            print(f" Contrato encerrado no valor total de R${self.valor_total:.2f}")

        else:
            print("ERRO, contrato ja foi encerrado!")






class SistemaGerenciamento:
    def __init__(self):
        self.__veiculos = []
        self.__clientes = []
        self.__contratos = []
        

    def cadastrar_carro(self, placa, modelo, categoria, tarifa_diaria, portas):
        novo_carro = Carro( placa, modelo, categoria, tarifa_diaria, portas)
        self.__veiculos.append(novo_carro)
        print(f'O veiculo do modelo: {modelo} e da placa: {placa} foi cadastrado com sucesso!')

    def cadastrar_moto (self, placa, modelo, categoria, tarifa_diaria, cilindradas):
        nova_moto = Moto(self, placa, modelo, categoria, tarifa_diaria, cilindradas)
        self.__moto.append(nova_moto)
        print(f'A moto de placa: {placa}, e modelo {modelo} foi cadastrada com sucesso!')


    def buscar_veiculo_placa (self, placa):
        print("---Busca por placa---")
        for veiculo in self.__veiculos:
            if veiculo.placa == placa:
                return veiculo
        return None
    
    def cadastrar_cliente(self, nome, cpf, nascimento):
        novo_cliente = Cliente(nome, cpf, nascimento)
        self.__clientes.append(novo_cliente)
        print(f'Cliente de nome {nome} foi cadastrado com sucesso!')

    def buscar_cliente_cpf (self, cpf):
        print('---Busca por cliente---')
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def listar_veiculos_disponiveis(self):
        encontrou_algum = False # variavel boolena
        for veiculo in self.__veiculos:
            if veiculo.status == 'disponivel':
                veiculo.detalhes()
                encontrou_algum = True
        if not encontrou_algum:
            print('Nenhum veículo dísponivel no momento! ')

    def listar_clientes (self):
        for cliente in self.__clientes:
            cliente.exibir_detalhes()

    def listar_contratos_ativos(self):
        print('---contratos ativos')
        encontrou_algum = False
        for i, contrato in enumerate(self.__contratos):
            if contrato.ativo:
                print(f"ID do contrato {i}")
                contrato.exibir_detalhes()
                encontrou_algum = True
        if not encontrou_algum:
            print('NENHUM CONTRATO ATIVO')
        return encontrou_algum

    


    
    


            
    

