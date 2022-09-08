import os
import pickle
#import csv

file_path = os.path.join(os.getcwd(),'mydata.txt')

#
# sth1 = "Khoa"
#
# sth2 = 21
#
# sth3 = "Malkkke"
#


# Writing to file
#
# with open(file_path, 'w') as f:
#
#     f.write(sth1 + '\n')
#
#     f.write(str(sth2)+ '\n')
#
#     f.write(sth3)




#Loading from file
#
# with open(file_path, 'r') as f:
#
#     data = f.read().splitlines()
#
#     print(data)


class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def print_info(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Price: ", self.price)


    def __str__(self):
        string = "Car brand: %s"%(self.brand)
        return string


car_list = [("Toyota","Innova",100),("Toyota","Fortuner",2000),("Ford","STh",1222),("Mazda","LV",12221)]





cars = [Car(brand,model,price) for brand, model, price in car_list]




sth = pickle.dumps(cars)
#with open(file_path, 'wb') as f:
    #sth = pickle.dump(cars,f)


sth2 = "12345"

print(size(sth2))


#
# with open(file_path, 'wb') as f:
#     pickle.dump(cars,f)

#
# with open(file_path,'rb') as f:
#     cars = pickle.load(f)
#
#
#
# for x in cars:
#     x.print_info()
#     print("\n")
#
# car1 = Car("Toyota","Fortuner",1000)
#
# car2 = Car("Ford", "sth", 2000)


#Writing class to file using pickle
# with open(file_path,'wb') as f:
#     pickle.dump(car1,f)
#     pickle.dump(car2,f)

#
# with open(file_path,'rb') as f:
#     car1 = pickle.load(f)
#     car2 = pickle.load(f)
#
# car1.print_info()
# car2.print_info()
