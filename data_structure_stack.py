#!/usr/bin/env python3


# stack 实现栈

stack = []

# 进栈
def pushit():
	stack.append(input("Enter new string: ").strip())

# 出栈
def popit():
	if len(stack) == 0:
		print("cannot pop from an empty stack!")
	else:
		print("Removed [", stack.pop(), "]")

# 遍历栈
def viewstack():
	print(stack)


CMDs = {"u": pushit, "o": popit, "v": viewstack}

def showmenu():
	pr = """
	p(U)sh
	p(O)p
	(V)iew
	(Q)uit
		Enter choice: """

	while True:
		while True:
			try:
				choice =input(pr).strip()[0].lower()
			except (EOFError, KeyboardInterrupt,IndexError):
				choice = "q"
			print("\nYou Picked: [%s]" % choice)
			if choice not in "uovq":
				print("Invalid option, try again")
			else:
				break

		if choice == "q":
			break
		CMDs[choice]()


if __name__ == "__main__":
	showmenu()


