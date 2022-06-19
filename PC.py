''' Crie uma classe para armazenar as informações de um computador. O computador deve ter os seguintes atributos:

-Modelo
-Fabricante
-Processador
-Memória RAM
-Tamanho do HD
-Espaço ocupado do HD
-Está ligado?

Sua classe também deve ter os seguintes métodos:

-liga() -> altera o status de "Está ligado" para True #ok
-desliga() -> altera o status de "Está ligado" para False #ok
-limparHD() -> recebe por parâmetro o tamanho do espaço que deseja liberar do HD
-ocuparHD() -> recebe por parâmetro o tamanho do espaço que deseja ocupar do HD

Lembre-se de manter as boas práticas na hora de criar os atributos, e certifique-se de que o valor passado nos métodos "limparHD" e "ocuparHD" sejam válidos!
 '''

class PC:
    def __init__(self, modelo, fabricante, processador, ram, hd_tamanho, hd_ocupado, ligado = False ):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador = processador
        self.ram = ram
        self.hd_tamanho = hd_tamanho
        self.hd_ocupado = hd_ocupado
        self.ligado = ligado

    def ligar(self):
        if not self.ligado:
            self.ligado = True
        return self.ligado

    def desligar(self):
        if self.ligado:
            self.ligado = False
        return self.ligado
    
    def limpar_HD(self,valor):
        #HD_livre = self.hd_tamanho - self.hd_ocupado
        if self.ligado and (valor) <= self.hd_ocupado:
            self.hd_ocupado -= valor
            return self.hd_ocupado
        else:
            return self.hd_ocupado
    
    def ocupar_HD(self,valor):
        HD_livre = self.hd_tamanho - self.hd_ocupado
        if self.ligado and (valor) <= HD_livre:
            self.hd_ocupado += valor
            return self.hd_ocupado
        else:
            return self.hd_ocupado

