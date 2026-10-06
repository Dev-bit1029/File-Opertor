from datetime import datetime

dt = datetime.now()


print()

class Manager :
    
    def __init__(self):
        try :
            file = open("data.txt","x")
            file.close()
        except:
            print()
    def add_entry(self):
        try :
            
            file = open("data.txt","a")
            data = input("Enter your Journal Entry : \n")
            
            file.write(data)
            file.close()
            
            print(" Entry Added Successfully  ")
            
        except:
            print()
        
    def view_entry(self):
        try:
            file = open("data.txt","r")
            data = file.read()
            file.close()
            print(data)
        except:
            print()           
    def Search_entry(self):
        
        try:
            file = open("data.txt","r")
            data = input("Enter A Keyword Or Date To Search :- ").split()
            
            for x in file:
                if any(keyword in x for keyword in data):
                    print(x, str(dt))
                else:
                    print("No Entry Found")
            file.close()
            

        except:
            print()
            
    def delete_entry(self):
        try:
            file = open("data.txt","w")
            file.write("")
            file.close()
            print("Successfully Deleted All Entry ")
            
        except:
            print()
            
obj = Manager()





while True:
    print("Welcome To Personal Journal Manager !")
    
    print("1. Add A New Entry")
    print("2. View All Entry")
    print("3. Search Entry ")
    print("4. Deleted All Entry ")
    print("5. Exit.....")
    
    
    choice = int(input("Enter Your Choice Between (1-5):- "))
    
    if choice == 1:
        obj.add_entry()
        
    elif choice == 2:
        obj.view_entry()
        
    elif choice == 3 :
        obj.Search_entry()
        
    elif choice == 4:
        obj.delete_entry()
        
    elif choice == 5:
        print("Thank you For Using Personal Journal Manager....")
        break
