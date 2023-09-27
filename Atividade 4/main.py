import csv

class Inventory():
    def __init__(self, csv_filename):
        """
        Inicializa a classe Inventory.

        Parâmetros:
        - csv_filename (str): O nome do arquivo CSV que contém os dados do inventário.

        Atributos:
        - rows (list): Uma lista que armazena todas as linhas do arquivo CSV (excluindo o cabeçalho).
        - header (list): Uma lista que armazena o cabeçalho do arquivo CSV.
        - id_to_row (dict): Um dicionário que mapeia IDs de laptop para suas respectivas linhas de dados.
        - prices (set): Um conjunto de preços únicos de laptops.
        - rows_by_price (list): Uma lista de linhas de dados de laptops ordenadas por preço.
        """
        with open(csv_filename) as csv_file:
            reader = csv.reader(csv_file)
            self.rows = list(reader)

        self.header = self.rows[0]
        self.rows = self.rows[1:]

        for row in self.rows:
            row[-1] = int(row[-1])

        self.id_to_row = {}
        for row in self.rows:
            self.id_to_row[row[0]] = row

        self.prices = set()
        for row in self.rows:
            self.prices.add(row[-1])

        def row_price(row):
            return row[-1]

        self.rows_by_price = sorted(self.rows, key=row_price)

    def get_laptop_from_id(self, laptop_id):
        """
        Retorna os detalhes de um laptop com base em seu ID.

        Parâmetros:
        - laptop_id (str): O ID do laptop a ser pesquisado.

        Retorna:
        - Um dicionário com os detalhes do laptop ou None se o laptop não for encontrado.
        """
        for row in self.rows:
            if row[0] == laptop_id:
                return row
        return None

    def get_laptop_from_id_fast(self, laptop_id):
        """
        Retorna os detalhes de um laptop com base em seu ID de forma mais rápida usando o mapeamento ID-linha.

        Parâmetros:
        - laptop_id (str): O ID do laptop a ser pesquisado.

        Retorna:
        - Um dicionário com os detalhes do laptop ou None se o laptop não for encontrado.
        """
        return self.id_to_row.get(laptop_id)

    def check_promotion_dollars(self, dollars):
        """
        Verifica se é possível comprar um laptop com a quantia de dinheiro especificada.

        Parâmetros:
        - dollars (int): A quantia de dinheiro para verificar.

        Retorna:
        - True se for possível comprar um laptop com a quantia, False caso contrário.
        """
        for row in self.rows:
            if row[-1] == dollars:
                return True
            for second_row in self.rows:
                if row[-1] + second_row[-1] == dollars:
                    return True
        return False

    def check_promotion_dollars_fast(self, dollars):
        """
        Verifica se é possível comprar um laptop com a quantia de dinheiro especificada de forma mais eficiente.

        Parâmetros:
        - dollars (int): A quantia de dinheiro para verificar.

        Retorna:
        - True se for possível comprar um laptop com a quantia, False caso contrário.
        """
        if dollars in self.prices:
            return True

        for price in self.prices:
            if dollars - price in self.prices:
                return True

    def find_first_laptop_more_expensive(self, price):
        """
        Encontra o índice do primeiro laptop mais caro que o preço especificado.

        Parâmetros:
        - price (int): O preço de referência.

        Retorna:
        - O índice do primeiro laptop mais caro que o preço, ou -1 se nenhum for encontrado.
        """
        for row in self.rows_by_price:
            if row[-1] > price:
                return self.rows_by_price.index(row)
        return -1

    def find_laptop_within_price_range(self, min_price, max_price):
        """
        Encontra laptops dentro de um intervalo de preço específico.

        Parâmetros:
        - min_price (int): O preço mínimo do intervalo.
        - max_price (int): O preço máximo do intervalo.

        Retorna:
        - Um dicionário com os detalhes dos laptops dentro do intervalo de preço especificado.
        """
        laptops_in_range = {}
        for row in self.rows_by_price:
            if row[-1] >= min_price and row[-1] <= max_price:
                laptops_in_range[row[0]] = row
        return laptops_in_range

    def find_laptop_with_RAM_and_storage(self, ram, storage):
        """
        Encontra laptops com RAM e armazenamento específicos.

        Parâmetros:
        - ram (str): A quantidade de RAM desejada.
        - storage (str): A capacidade de armazenamento desejada.

        Retorna:
        - Um dicionário com os detalhes dos laptops que correspondem aos critérios de RAM e armazenamento.
        """
        laptops = {}
        for row in self.rows:
            if ram in row[7] and storage in row[8]:
                laptops[row[0]] = row
        return laptops

    def find_laptop_within_RAM_range(self, min_ram, max_ram):
        """
        Encontra laptops com RAM dentro de um intervalo específico.

        Parâmetros:
        - min_ram (str): A quantidade mínima de RAM desejada.
        - max_ram (str): A quantidade máxima de RAM desejada.

        Retorna:
        - Um dicionário com os detalhes dos laptops dentro do intervalo de RAM especificado.
        """
        laptops = {}
        minimum_ram_value = self.extract_numeric_value(min_ram)
        maximum_ram_value = self.extract_numeric_value(max_ram)
        if maximum_ram_value < minimum_ram_value:
            return 'Valores inválidos'
        for row in self.rows:
            ram_value = self.extract_numeric_value(row[7])
            if ram_value is not None and minimum_ram_value <= ram_value <= maximum_ram_value:
                laptops[row[0]] = row
        return laptops

    def find_laptop_within_storage_range(self, min_storage, max_storage):
        """
        Encontra laptops com armazenamento dentro de um intervalo específico.

        Parâmetros:
        - min_storage (str): A capacidade mínima de armazenamento desejada.
        - max_storage (str): A capacidade máxima de armazenamento desejada.

        Retorna:
        - Um dicionário com os detalhes dos laptops dentro do intervalo de armazenamento especificado.
        """
        laptops = {}
        minimum_storage_value = self.extract_numeric_value(min_storage)
        maximum_storage_value = self.extract_numeric_value(max_storage)
        if maximum_storage_value < minimum_storage_value:
            return 'Valores inválidos'
        for row in self.rows:
            storage_value = self.extract_numeric_value(row[8])
            if storage_value is not None and minimum_storage_value <= storage_value <= maximum_storage_value:
                laptops[row[0]] = row
        return laptops

def find_laptop_with_RAM_range_and_storage_range(self, min_ram, max_ram, min_storage, max_storage):
    """
    Encontra laptops com RAM e armazenamento dentro de intervalos específicos.

    Parâmetros:
    - min_ram (str): A quantidade mínima de RAM desejada.
    - max_ram (str): A quantidade máxima de RAM desejada.
    - min_storage (str): A capacidade mínima de armazenamento desejada.
    - max_storage (str): A capacidade máxima de armazenamento desejada.

    Retorna:
    - Um dicionário com os detalhes dos laptops que correspondem aos critérios de RAM e armazenamento.
    """
    laptops = {}
    minimum_ram_value = self.extract_numeric_value(min_ram)
    maximum_ram_value = self.extract_numeric_value(max_ram)
    minimum_storage_value = self.extract_numeric_value(min_storage)
    maximum_storage_value = self.extract_numeric_value(max_storage)
    if maximum_ram_value < minimum_ram_value and maximum_storage_value < minimum_storage_value:
        return 'Valores inválidos'
    for row in self.rows:
        ram_value = self.extract_numeric_value(row[7])
        storage_value = self.extract_numeric_value(row[8])
        if (ram_value is not None and
            storage_value is not None and
            minimum_ram_value <= ram_value <= maximum_ram_value and
            minimum_storage_value <= storage_value <= maximum_storage_value):
            laptops[row[0]] = row
    return laptops

def extract_numeric_value(self, text):
    """
    Extrai um valor numérico de uma string que contém texto e números.

    Parâmetros:
    - text (str): A string que contém o valor numérico.

    Retorna:
    - O valor numérico extraído como um int, ou None em caso de erro na conversão.
    """
    try:
        if 'TB' in text:
            numeric_value = int(''.join(filter(str.isdigit, text))) * 1000
        else:
            numeric_value = int(''.join(filter(str.isdigit, text)))
        return numeric_value
    except ValueError:
        return None


# Criando uma instância da classe Inventory com o arquivo 'laptops.csv'
inventory = Inventory('laptops.csv')

# Exemplo de uso: Encontrar laptops com armazenamento entre '256GB' e '1TB'
print(inventory.find_laptop_within_storage_range('256GB', '1TB'))
