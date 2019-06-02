from tkinter import Tk, Label, Button, Entry, StringVar
#Creating a class for the GUI object which we pass the root(master) node
class MyFirstGUI:
	
	#constructor for class
	def __init__(self, master):

		#String Variables
		self.entryString = StringVar()
		self.labelString = StringVar()

		#set labelString to default
		self.labelString.set("My First Python GUI!")

		#Window/Frame Title
		self.master = master
		master.title("A simple GUI")

		#add a label to the master node
		self.label = Label(master, textvariable=self.labelString, font=("Helvetica", 20))
		self.label.pack()

		#add a greet button to the master node
		self.greet_button = Button(master, text="Greet", command=self.greet, font =("Helvetica", 15))
		self.greet_button.pack()

		#add a close button to the master node
		self.close_button = Button(master, text="Close", command=master.quit, font = ("Helvetica", 15))
		self.close_button.pack()

		#add textEntry Box
		self.entry = Entry(master, textvariable=self.entryString, font=("Helvetica", 20))
		self.entry.pack()

		#add button to get textFrom entry
		self.getText_button = Button(master, text="Get Entry", command=self.get, font = ("Helvetica", 20))
		self.getText_button.pack()


	#callback function for the green button
	def greet(self):
		print("What up nukka?!")

	def get(self):
		self.labelString.set(self.entryString.get())

root = Tk()
root.geometry("500x500")
my_gui = MyFirstGUI(root)
root.mainloop()