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
    
    


            
