class Car:
    
    def __init__(self, mark: str, color: str, year: int):
        self.mark = mark
        self.color = color
        self.year = year
    
    def horn(self):
        print(f'Машина {self.mark} делает "Би-би-биииии"')

my_car = Car('Mazda', 'Black', 2019)
new_car = Car('Tesla', 'Bloo', 2000)

my_car.horn()
new_car.horn()

print(my_car.mark)
print(new_car.mark)
