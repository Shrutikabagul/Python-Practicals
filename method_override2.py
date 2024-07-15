class calculate:
    def add(self):
        print(5+5)

class calc(calculate):
    def add(self):
        print('Shrutika'+'Bagul')

print('The method add here is overridden in the code')

# Invoking Child class through object r
r = calc()
r.add()

# Invoking Parent class through object r
r = calculate()
r.add()
