class Veiculo():
    def __init__(self, placa, ano, marca_modelo, cor):
        self.placa = placa
        self.ano = ano
        self.marca_modelo = marca_modelo
        self.cor = cor

    def __str__(self):
        return '{} {} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor)

    def __repr__(self):
        return '{} {} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor)


class HashTable:
    def __init__(self):
        self.size = 29
        self.table = [None] * self.size

    def hash_function(self, key):
        placa_int = int(''.join(filter(str.isdigit, key)))
        return placa_int % self.size

    def insert(self, veiculo):
        key = veiculo.placa
        value = veiculo
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None and self.table[hash_value][0] != key:
            hash_value = (hash_value + 1) % self.size
        if self.table[hash_value] is None:
            self.table[hash_value] = (key, value)
        else:
            print('Placa já foi inserida na tabela')

    def search(self, key):
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                return self.table[hash_value][1]
            hash_value = (hash_value + 1) % self.size
        return None

    def delete(self, key):
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                self.table[hash_value] = "APAGADO"
                return True
            hash_value = (hash_value + 1) % self.size
        return False

    def display(self):
        for i in range(self.size):
            print('{}: {}'.format(i, self.table[i]))


def menu():
    tabela = HashTable()
    while True:
        print(f'''{"MENU":=^24}
-[1] Inserir veículo.
-[2] Buscar veículo por placa.
-[3] Deletar veículo por placa.
-[4] Mostrar tabela completa.
-[5] Sair.
{"="*24}''')

        opcao = input('Insira a opção desejada: ')

        if opcao == '1':
            placa = input('Insira a placa do veículo: ')
            ano = input('Insira o ano do veículo: ')
            marca_modelo = input('Insira a marca e modelo do veículo: ')
            cor = input('Insira a cor do veículo: ')
            veiculo = Veiculo(placa, ano, marca_modelo, cor)
            tabela.insert(veiculo)
        elif opcao == '2':
            placa = input('Insira a placa do veículo: ')
            veiculo = tabela.search(placa)
            if veiculo is not None:
                print(veiculo)
            else:
                print('Veículo não encontrado.')
        elif opcao == '3':
            placa = input('Insira a placa do veículo: ')
            if tabela.delete(placa):
                print('Veículo excluído com sucesso.')
            else:
                print('Veículo não encontrado.')
        elif opcao == '4':
            tabela.display()
        elif opcao == '5':
            break
        else:
            print('Opção inválida.')


menu()
