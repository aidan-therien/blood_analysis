#blood_analysis.py
def HDL_analysis(HDL_result):
	if HDL_reuslt >= 60:
		return "Good"
	elif 40 <= HDL_result <60:
		return "Borderline"
	else:
		retun "Bad"


def HDL_interface():
	#input should be HDL = 66
	print("HDL Interface")
	print("Please input the result in the following format: ")
	print(" HDL=## where ## is the result")
	HDL_input = input("Result: ")
	HDL_result = HDL_input.split("=")
	HDL_status = HDL_analysis(int(HDL_result[1]))
	print(HDL_status)
	pass

def interface():
	keep_running = True
	print("My blood analysis calculator")
	while keep_running:
		print("Options: ")
		print("9-quit")
		choice = input("Choose an option: ")
		if choice ==9:
			keep_running = False;
	if name__ == "__main__":
		interface()
