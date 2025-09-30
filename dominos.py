#Dominos clone
import random
class Dominos:
    menu={
        "veg":{"Margerita": 129,"Cheese_and_corn":169,
               "Peppi_paneer":260,"Veg_Loaded":210,
               "Tomato_tangi":170},

       "non_veg":{"Pepper_barbeque":199,"Non_veg_loaded":169,
                  "Chicken_sausage":200},

        "snacks":{"garlic_bread":120,"Zingy":59,
                  "Chicken_cheese_balls":170},

        "desserts":{"Choco_lava":100,"Mousse cake":169},

        "drinks":{"Coke":90,"Pepsi":78,"Sprite":50}
    }  
    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False #to validate login state
        self.cart={}  #to store orders
        
        #main program
        while True:
            if not self.login_status:
                print("-----------Welcome to DOMINOS🍕 APP--------------")
                print("Login")
                ch=input("Do you want to Login? (y/n): ").lower()
                if ch=='y':
                    self.login()
            if self.login_status:
                print("User 👤:",self.name)
                print("Enter 1: Order")
                print("Enter 2: Show cart")
                print("Enter 3: Logout")
                choice=int(input("Enter choice: "))
                if choice==1:
                    self.order()
                elif choice==2:
                    self.show_cart()
                elif choice==3:
                    self.logout()
                else:
                    print("Invalid choice")
    @staticmethod
    def validate_otp(value):
        while True:
            og_otp=random.randint(1000,9999)
            print(f"An otp has been sent to {value}")
            print(f"Your dominos otp is:{og_otp}")
            otp=int(input("Enter otp: "))
            if otp==og_otp:
                print("Login successful✅")
                return True
            print("Incorrect otp enter correct otp...")

    def login(self):
        print("Enter 1: Login with Phone")
        print("Enter 2: Login with Email")
        ch=int(input("Enter choice: "))
        if ch==1:
            #phone no validation
            phno=int(input("Enter phno: "))
            if phno==self.phno:
                state=self.validate_otp(phno)  #True
                self.login_status=state
            else:
                print("Incorrect phno")

        elif ch==2:
            #email validation
            email=input("Enter email: ")
            if email==self.email:
                state=self.validate_otp(email)
                self.login_status=state
            else:
                print("Incorrect otp")

        else:
            print("Invalid choice")
    def order(self):
        print("-------Dominos Menu--------")
        for category in Dominos.menu :
            print(category)
        cat=input("Enter category: ")
        if cat in Dominos.menu:
            d=Dominos.menu[cat]
            for item in d:
                print(item,'              Rs.',d[item])
            item=input("Enter item: ")
            if item in d:
                q=int(input("Enter quantity: ")) #2
                if item in self.cart:
                    self.cart[item]+=d[item]*q  #var[key]=new val
                else:
                    self.cart[item]=d[item]*q
                print(f'{item} added to the cart')    
            else:
                print(f'{item} is not available❌')
        else:
            print(f'{cat} is not available❌')

    def show_cart(self):
        if self.cart!={}:
            total_bill = 0
            for item in self.cart:
                total_bill+=self.cart[item]
                print(item,"------------Rs.",self.cart[item])
            print("Total Bill:           Rs.",total_bill)
        else:
            print("Cart is Empty please order...")

        if self.cart!={}:
            ch=input("Do you want to place the order ?(y/n): ").lower()
            if ch=='y':
                print("Thank you👍for placing the order")
                print("Your order is on the way🛵")
                self.cart={}

    def logout(self):
        ch=input("Do yu want to logout? (y/n): ").lower()
        if ch=='y':
            self.login_status= False
            print("Logged out ✅")


ob=Dominos("Keerthana","keerthi07@gmail.com",8996342091)
