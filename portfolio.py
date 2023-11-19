from termcolor import cprint


class Portfolio:
    def __init__(self, name):
        self.name = name
        self.capacity = 1
        self.size = None
        self.symbols = []
        self.symbol = None
        self.portfolio = {}
        self.total = []

    def __str__(self):
        return f"{self.portfolio}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        self._name = name

    # Getter for symbol
    @property
    def symbol(self):
        return self._symbol

    # Setter for symbol
    @symbol.setter
    def symbol(self, symbol):
        if isinstance(symbol, int) or isinstance(symbol, float):
            raise ValueError("Ticker symbol cannot be a number or float")
        elif symbol in self.symbols:
            raise ValueError("Ticker symbol already selected")
        elif symbol == "":
            raise ValueError("Ticker symbol cannot be empty")
        self._symbol = symbol

    def deposit(self, symbol, value):
        if not isinstance(value, int):
            raise ValueError("Please enter an integer value")
        elif value / 100 <= 0:
            raise ValueError("Cannot allocate negative or 0 %")
        elif (
            value / 100 > self.capacity or value / 100 + sum(self.total) > self.capacity
        ):
            raise ValueError("Cannot allocate over 100%")

        self.size = value / 100
        self.symbol = symbol
        self.portfolio[self.symbol] = self.size
        self.total = [v for v in self.portfolio.values()]
        self.symbols = [k for k in self.portfolio.keys()]

    @classmethod
    def get(cls):
        while True:
            name = input("Name your portfolio: ").upper()
            if name != "":
                return cls(name)
            else:
                cprint("Portfolio name cannot be empty.", "light_red")
                continue
        
