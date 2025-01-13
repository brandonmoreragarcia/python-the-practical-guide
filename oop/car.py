class Car: 
    # top_speed = 100
    
    def __init__(self, top_speed=100):
        self.top_speed = top_speed
        self.warnings = []
    
    def drive(self):
        print(f'I am driving but not faster than {self.top_speed}')
        
car1 = Car()
car1.drive()
car1.warnings.append('one ticket')

car2 = Car(200)
car2.drive()

car3 = Car(300)
car3.drive()

print(car1.__dict__)