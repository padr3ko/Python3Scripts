#This python script imports Input from the curtsies module (still trying to figure out whats with this name)
#prints out the keys being pressed

#running ubuntu 16.04
#found python 3(ver 3.5ish) sudo apt-cache search python3 -> sudo apt-get install [module name]
#found curtsies sudo apt-cache search curtsies -> sudo apt-get install [module name]



from curtsies import Input

#make global string variables
scannerInput = ""

#creating main method
def main():

	#with statement using Input method from curtsies module making a input_generator(input variable)
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			
			#specific that the local variable is actually global
			global scannerInput

			#if scanner input does not equal new line character add it to the string
			if str(e) != "\n":
				scannerInput += str(e)

			#if scanner input equals new line character, print string and clear the scannerInput string			
			if str(e) == "\n":
				print(scannerInput)
				scannerInput = ""

#before execution at indentation 0, python makes the __name__ variable and assigns the "current module" to that variable name, if it is the current file it will be __main__
if __name__ == '__main__':
	main()