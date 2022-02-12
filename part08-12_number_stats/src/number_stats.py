class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) == 0:
            return 0
        return self.get_sum() / self.count_numbers()


print("Please type in integer numbers:")
nums = NumberStats()
evens = NumberStats()
odds = NumberStats()

while True:
    num = int(input())
    if num == -1:
        break

    nums.add_number(num)

    if num % 2 == 0:
        evens.add_number(num)
    else:
        odds.add_number(num)

print("Sum of numbers:", nums.get_sum())
print("Mean of numbers:", nums.average())
print("Sum of even numbers:", evens.get_sum())
print("Sum of odd numbers:", odds.get_sum())
