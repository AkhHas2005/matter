#Numbers list that saves
import os.path

class NumbersListController:
	def __init__(self):
		self.thisList = []
	
	def menu(self):
	    print("1. Load saved list from file")
	    print("2. View saved list")
	    print("3. View first number in list")
	    print("4. Add to list")
	    print("5. Remove first item of list")
	    print("6. Exit")
	
	def getChoice(self):
	    choice = 0
	    while choice not in [1,2,3,4,5,6]:
	        try:
	            choice = int(input("Enter your choice (1-5): "))
	        except:
	            print("Choice must be a number!")
	    return choice
	
	def loadList(self):
	    self.thisList = []
	    fileName = input("Enter the file name to load from (default=NumbersList): ")
	    fileName += ".txt"
	    file = open(fileName, 'r')
	    for line in file:
	        line = line.strip("\n")
	        self.thisList.append(int(line))
	    return self.thisList
	
	def addToList(self, thisList):
	    toAdd = True
	    while True:
	        number = int(input("Enter a number to add to the list: "))
	        thisList.append(number)
	        toAdd = input("Do you wish to add more numbers (Y/N)? ")
	        if toAdd.upper() == "Y":
	            print("You have chosen to add another number to the list!")
	        else:
	            break
	    return thisList
	
	def saveList(self, thisList):
	    check_file = True
	    num = 0
	    while check_file:
	        path = './NumbersList'+str(num)+'.txt'
	        check_file = os.path.isfile(path)
	        num += 1
	    file = open(path, 'w')
	    for number in thisList:
	        file.write(str(number)+"\n")
	    print("The file is called",path[2:])
	
	def main(self):
	    print("Welcome to the Number List controller - the list saves when you exit")
	    
	    while True:
	        self.menu()
	        choice = self.getChoice()
	        if choice == 1:
	            self.thisList = self.loadList()
	        elif choice == 2:
	            print(self.thisList)
	        elif choice == 3:
	            print(self.thisList[0])
	        elif choice == 4:
	            self.addToList(self.thisList)
	        elif choice == 5:
	            first = self.thisList[0]
	            self.thisList.remove(first)
	        else:
	            self.saveList(self.thisList)
	            exit()

if __name__ == "__main__":
    nlc = NumbersListController()
    nlc.main()
