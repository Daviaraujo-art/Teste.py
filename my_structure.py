class NumberStorage:
    def __init__(self):
        self.numbers = {}

    def add_number(self, number):
        status = self.numbers.get(number, "NAO_ADICIONADO")
        if status == "NAO_ADICIONADO":
            self.numbers[number] = "unico"
        else:
            self.numbers[number] = "repetido"

    def get_numbers(self):
        return self.numbers