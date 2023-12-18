class UserClass:
    def __init__(self, currentUser, externalUser):
        self.currentUser = currentUser
        self.externalUser = externalUser
    
    def sayHi(self):
        print("Hi!")

    
    def getName(self):
        print(self.currentUser)
        print(self.externalUser)    

    def getPath(self):
        current_user = self.currentUser

        if self.currentUser.lower() == "david":
            print("davey in the shire")

        elif self.currentUser.lower() == "frodo":
            print("frodo in the shire")

        elif self.currentUser.lower() == "sam":
            print("sam in the shire")
        
        else: 
            print("user not found")

