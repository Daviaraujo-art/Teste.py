class NumberStorage:
    def _init_(self):
        self.numbers = {}
        

    def add_number(self, number):
        status = self.numbers.get(number, "one time appeared")
        if status == "one time appeared":
            self.numbers[number] = "unique"
        else:
            self.numbers[number] = "repeated"
        

    def get_numbers(self):
        return self.numbers

storage = NumberStorage()
