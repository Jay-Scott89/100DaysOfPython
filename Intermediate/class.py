# the syntax of a class is a class key word followed by its name and a semicolon. every inside the class has to be indented
class User: 
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Methods are functions when attached to an object. 
    def follow(self, user):
        user.followers += 1
        self.following += 1

# when using the class you can assigin it to a varibale as an object, you also need to include brackets. 
user_1 = User("001", "Jamie")
user_2 = User("002", "Mason")

user_1.follow(user_1)

print(user_1.following)
print(user_2.following)

# Adding attributes can be done like this. Its messy but possible
# user_1.id = "001" 
# user_1.username = "Jamie"

#Using a Constructor is a way to initialize the object to the starting values
# This is where the init function is uses. The init function will be called everytime a new object is created from the class 
class Car:
    def __init__(self, seats):
        self.seats = seats
    

my_car = Car(5)

