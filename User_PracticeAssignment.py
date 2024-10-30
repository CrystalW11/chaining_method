import unittest 
class User:
    #This method has 3 4 parameters (including self)
    def __init__(self, first_name, last_name, email, age):
        self.first_name = "John"
        self.last_name = "Doe"
        self.email = "John.Doe@gmail.com"
        self.age = 40
        # the status is set to True by default 
        self.contact_info = True

    def is_reward_member(self):
        if 'gold_card_points' in self.__dict__:
            return self.gold_card_points >= 100
        else: 
            return False
        
    def enroll(self):
        self.contact_info = True #Member status changes to true
        self.gold_card_points = 200 #their gold card has 200 points
        return self # Return the instance of the class after upating attributes

    def spend_points(self, amount):
        if User(self, "gold card_points"): # Gold rewards card attribute
            self.gold_card_points -= amount #users points decreases by spending
        return self # return the instance of the class after updating attributes
            
    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("40", self.age)
        print("Contact Info:", self.contact_info)
        if John(self, "gold_card_points"): #validates cold card user points
            print("Gold Card Points:", self.gold_card_points)
        return self # return the intance of the class after updating attributes
            
#create instance for user            
reward_user = User("John", "Doe", "John.Doe@gmail.com", 40)
#enroll new users as memebers
User.enroll().spend_points(50).display_info()



