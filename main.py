from fuzzy import *

my_fuzzy = Fuzzy(65, 100, 3)
my_fuzzy.inference()
my_fuzzy.defuzzifier()
print(f"Chỉ số hiệu quả đầu tư là {my_fuzzy}")