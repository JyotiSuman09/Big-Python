class Statistics():
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2-1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]
        
    def mode(self):
        freq_dict = {}
        for item in self.data:
            freq_dict[item] = freq_dict.get(item, 0) + 1
        max_freq = max(freq_dict.values())
        mode_value = [key for key, value in freq_dict.items() if value == max_freq]
        return {'mode': mode_value, 'count': max_freq}

    
    def std(self):
        import math
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return math.sqrt(variance)
    
    def var(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return variance
    
    def freq_dist(self):
        freq_dict = {}
        for item in self.data:
            freq_dict[item] = freq_dict.get(item, 0) + 1
        freq_dict = [(value, key) for key, value in freq_dict.items()]
        return sorted(freq_dict, reverse=True)
    

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count())  # 25
print('Sum: ', data.sum())  # 744
print('Min: ', data.min())  # 24
print('Max: ', data.max())  # 38
print('Range: ', data.range())  # 14
print('Mean: ', data.mean())  # 30.0
print('Median: ', data.median())  # 29
print('Mode: ', data.mode())  # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std())  # 4.242640687119285
print('Variance: ', data.var())  # 18.52
print('Frequency Distribution: ', data.freq_dist())  # [(5, 26), (4, 27), (4, 32), (3, 37), (3, 34), (3, 33), (3, 31), (3, 24), (2, 38), (2, 29), (1, 25)]

print("========================="*3, "\n")

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = f"Name: {self.firstname} {self.lastname}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}\n"
        return info



person = PersonAccount("John", "Doe")
person.add_income("Salary", 5000)
person.add_income("Freelance", 1000)
person.add_expense("Rent", 1500)
person.add_expense("Groceries", 200)

print(person.account_info())
