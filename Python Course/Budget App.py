class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.00

    def __repr__(self):
        header = self.name.center(30, "*")
        ledger = ""
        for item in self.ledger:
            ldesc = "{:<23}".format(item["description"])
            lamount = "{:>7}".format(item["amount"])
            ledger += "{} {:.2f}\n".format(ldesc[:23], float(lamount[:7]))
        total = "Total: {:.2f}".format(self.balance)
        return header + "\n" + ledger + total

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": self.amount, "description": description})
        self.balance += self.amount

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def withdraw(self, amount, description=""):
        self.amount = amount
        self.description = description
        if self.check_funds(amount):
            self.ledger.append({"amount": -abs(self.amount), "description": description})
            self.balance -= self.amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, object_instance):
        if self.withdraw(amount, f"Transfer to {object_instance.name}"):
            object_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

def create_spend_chart(categories):

    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    name = list(map(lambda category: category.name, categories))
    max_length = max(map(lambda name: len(name), name))
    name = list(map(lambda name: name.ljust(max_length), name))
    for x in zip(*name):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")

a = Category("food")
b = Category("entertainment")
a.deposit(900, "deposit")
a.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
a.transfer(20, b)
print(a)
