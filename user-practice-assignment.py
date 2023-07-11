class User:

    def __init__(self, first, last, email, age):
        self.first = first
        self.last = last
        self.email = email
        self.age = age
        self.is_rewards_member = False # * is set to default
        self.gold_card_points = 0 # * is set to default


    def display_info(self): # print on separate lines
        print(f"{self.first} {self.last}\n{self.email}\n{self.age}\n")

    def enroll(self):
        if self.is_rewards_member == True:
            print(f"User is already enrolled.\n")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = self.gold_card_points + 200
            print(f"\n{self.first} {self.last} is now enrolled, and their points currently amount to: {self.gold_card_points}.\n")
            return self.gold_card_points
        # if self.is_rewards_member == False:    
        #     self.is_rewards_member = True
        #     self.gold_card_points = self.gold_card_points + 200
        #     print(f"{self.first} {self.last}'s enrollment status is currently: {self.is_rewards_member}, and their points currently amount to: {self.gold_card_points}.\n")
        #     return self.gold_card_points
        # elif self.is_rewards_member == True:
        #     print(f"User is already enrolled.")
        #     return True

    def spend_points(self,amount):
        if self.is_rewards_member == True and self.gold_card_points > amount:
            self.gold_card_points = self.gold_card_points - amount
            print(f"{self.first} {self.last}'s points decreased by: {amount} to: {self.gold_card_points}.\n")
        elif self.is_rewards_member == False:
            print(f"{self.first} {self.last} is not enrolled yet and therefore has 0 points.\n")
        else:
            print(f"User does not have enough points to spend.")

user_01 = User("Benjamin", "Sisko", "bestcommander@starfleet.space", 40)
user_02 = User("Erica", "Ortegas", "bestpilot@starfleet.space", 26)
user_03 = User("Kathryn", "Janeway", "bestcaptain@starfleet.space", 45)

# user_01.display_info() 
user_03.spend_points(25)
# user_01.spend_points(50)
# user_02.enroll()
# user_02.spend_points(80)
# user_01.display_info()
# user_02.display_info() 
# user_03.display_info() 
# user_01.enroll()
# user_01.enroll()
# user_02.enroll()
# user_02.enroll()
user_03.spend_points(80)
user_03.enroll()
user_03.spend_points(80)
user_03.spend_points(80)
user_03.spend_points(80)