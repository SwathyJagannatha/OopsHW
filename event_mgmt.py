# Task 2: Event Management System Enhancement

# Problem Statement: Use the existing Event class by adding an attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date,number_of_participants):
        self.name = name
        self.date = date
        self.number_of_participants = number_of_participants
        print(f"existing participants count is {self.number_of_participants}")
    
    def add_participant(self):
        print("1 Participant is being added to system")
        self.number_of_participants += 1
        print(f"Total number of participants is {self.number_of_participants}")
        pass

    def add_more_participants(self,cnt):
        print("Number of participants before adding new members:",self.number_of_participants)
        self.number_of_participants += cnt
        print(f"Total number of participants is {self.number_of_participants} as {cnt} participants were added!")
        pass

    def get_participant_count(self):
        print("The existing count of participants is:")
        print(self.number_of_participants)

    def delete_participant(self):
        user_ip = input("Do you want to delete participant?")

        if user_ip == "yes":
            if self.number_of_participants < 1:
                print("Existing count of participants is",{self.number_of_participants})
                print("Sorry, there are no participants to delete in the system!!")
                return

            self.number_of_participants -= 1
            print(f"Total number of participants currently is {self.number_of_participants}")  

    def delete_more_participants(self,count):
        user_ip = input("Do you want to delete participant?")

        if user_ip == "yes":
            if (self.number_of_participants - 10) < 1:
                print(f"Existing count of participants is {self.number_of_participants}")
                print(f"Sorry,there are less than {count} participants in the system!!")
                return

            self.number_of_participants -= count
            print(f"Total number of participants currently is {self.number_of_participants} as {count} partcipants were deleted")  

#First Event

print("Birthday Party\n")
event_bparty = Event("Birthday Party","07/24/2024",5)  
event_bparty.add_participant()

event_bparty.get_participant_count()

# extra method

event_bparty.add_more_participants(10)
event_bparty.get_participant_count()

event_bparty.delete_participant()
event_bparty.get_participant_count()

event_bparty.delete_more_participants(11)
event_bparty.get_participant_count()

event_bparty.delete_more_participants(11)
event_bparty.get_participant_count()

# 2nd Event
print("Christmas Party\n")
event_chparty = Event("Christmas Party","12/25/2024",10)  
event_chparty.add_participant()

event_chparty.get_participant_count()

# extra method

event_chparty.add_more_participants(10)
event_chparty.get_participant_count()

event_chparty.delete_participant()
event_chparty.get_participant_count()

event_chparty.delete_more_participants(11)
event_chparty.get_participant_count()

event_chparty.delete_more_participants(21)
event_chparty.get_participant_count()



    
