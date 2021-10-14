class Calculator:
    def __init__(self) -> None:
        pass

    def add(self, liczba_a, liczba_b) -> int:
        return liczba_a + liczba_b

    def difference(self, liczba_a, liczba_b) -> int:
        return liczba_a - liczba_b

    def multiply(self, liczba_a, liczba_b) -> int:
        return liczba_a * liczba_b

    def divide(self, liczba_a, liczba_b) -> int:
        return liczba_a / liczba_b

klasa = Calculator()
print(klasa.add(23,21))
print(klasa.difference(23,21))
print(klasa.multiply(23,21))
print(klasa.divide(23,21))