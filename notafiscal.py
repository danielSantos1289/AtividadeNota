"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal
from datetime import date

def escrever_linha(caractere,tamanho):
    return caractere * tamanho

class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor += item._valorUnitario * item._quantidade
        self._valorNota=valor

    def imprimirNotaFiscal(self):
        max_size = 111
        caractere = "-"
        print(escrever_linha(caractere,max_size))
        linha = "NOTA FISCAL" + (" " * (max_size-21)) + date.today().strftime("%m/%d/%Y")
        print(linha)
        linha = "Cliente: " + str(self._cliente._codigo) + " Nome: " + self._cliente._nome
        print(linha[0:(max_size-1)])
        linha = "CPF/CNPJ: " + self._cliente._cnpjcpf
        print(linha[0:(max_size-1)])
        print(escrever_linha(caractere,max_size))
        print("ITENS")
        print(escrever_linha(caractere,max_size))
        linha = "Seq  " + "Descrição" + " " * 51 + "QTD" + " " * 10 + "Valor Unit" + " " * 13 + "Preço"
        print(linha)
        print(escrever_linha(caractere,4) + " " + escrever_linha(caractere,56) + escrever_linha(" ",4) + escrever_linha(caractere,5) + escrever_linha(" ",7) + escrever_linha(caractere,12) + escrever_linha(" ",4) + escrever_linha(caractere,18))
        total = 0
        for item in self._itens:
            seq = str(item._sequencial).zfill(3)
            desc = item._descricao
            qtd = str(item._quantidade)
            vlr = "{:.2f}".format(item._valorUnitario)
            preco = "{:.2f}".format(item._valorUnitario * item._quantidade)
            total += item._valorUnitario * item._quantidade
            print(seq + escrever_linha(" ",(5-len(seq)))+ desc + escrever_linha(" ",(60-len(desc))) + escrever_linha(" ",(5-len(qtd))) + qtd + escrever_linha(" ",(7)) + escrever_linha(" ",(12-len(vlr))) + vlr + escrever_linha(" ",(4)) + escrever_linha(" ",(18-len(preco))) + preco)
        print(escrever_linha(caractere,max_size))
        print("Valor Total: {:.2f}".format(total))
