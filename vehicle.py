# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

class Vehicle:
    # adding few extra attributes for constructor
    def __init__(self,reg_num,type,owner,color_variants,class_name):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
        self.class_name = class_name
        self.color_variants = color_variants
        pass

    def update_owner(self,owner_name):
        print("Vehicle details before owner update:")
        self.display_info()
        print("Owner update in progress::\n")
        self.owner = owner_name

        print("Vehicle details after owner update:")
        self.display_info()

    def display_info(self):
        print("Vehicle specifications:")
        print(f"""----------- Vehicle -------------
                   Type : {self.type}
    Registration_number : {self.registration_number}
                  Owner : {self.owner}
              """)
        
    def show_info(self,mileage):
        print("Vehicle Mileage Info:")
        print(f"Vehicle from {self.class_name} has mileage of {mileage} mph")

veh_1 = Vehicle("7AKN145","Car-Honda Civic","Hermione","Black","Car Family")
#accesing class atrributes
print(veh_1.class_name)
print(veh_1.color_variants)

veh_1.update_owner("Emma Watson")
veh_1.display_info()
veh_1.show_info(30)

veh_1 = Vehicle("6AGN148","Car-Rolls Royce","Damon Salvatore","Maroon","Car Family")
#accesing class atrributes
print(veh_1.class_name)
print(veh_1.color_variants)

veh_1.update_owner("Ian Somerhalder")
veh_1.display_info()
veh_1.show_info(25)


