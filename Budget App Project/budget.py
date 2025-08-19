class Category:

    def __init__(self,name):
        """Initialize a Category with a name and empty ledger"""
        self.name = name
        self.ledger = [] 

    def deposit(self, amount, description = ""):
        self.ledger.append({
            'amount': amount, 
            'description': description
            })

    def withdraw(self, amount, description = ""):

        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount, 
                "description": description
            })
            return True
        return False

    def get_balance(self):

        return sum(item['amount'] for item in self.ledger)

    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            #withdraw from this category
            self.withdraw(amount,f'Transfer to {other_category.name}')
            #deposit to this category
            other_category.deposit(amount,f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self,amount):

        return amount <= self.get_balance()

    def __str__(self):

        title = f"{self.name:*^30}\n"

        items =""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"

            items += f"{desc:<23}{amt:>7}\n"

        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total


def create_spend_chart(categories):
    spent = []

    for category in categories:
        total =0
        for entry in category.ledger:
            if entry["amount"] < 0:
                total += -entry["amount"]
        spent.append(total)
    total_spent = sum(spent)
    percentage = [int((s/total_spent)*100) // 10 * 10 for s in spent]
    chart = "Percentage spent by category\n"

    #Chart bar from 100 down to 0
    for i in range(100,-1,-10):
        chart += str(i).rjust(3) + "| "
        for percent in percentage:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    #Bot line

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    names = [c.name for c in categories]

    max_len= max(len(n) for n in names) if names else 0
    for i in range(max_len):
        line = "     " #5 spaces indent
        for n in names:
            ch = n[i] if i < len(n) else " "
            line += ch + "  "
        chart += line + ("\n" if i < max_len - 1 else "")

    return chart
