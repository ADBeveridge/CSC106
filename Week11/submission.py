# prog
def username():
	user = input("Enter username: ")
	return user

def sum3(x,y,z):
	res = x + y + z
	return res

print("this is your main function: ", __name__)

if __name__ == "__main__":
	print(username())
	print(sum3(1,2,3))


# prog2

import prog

print(prog.sum3(2,3,4))

# Learned the difference in execution between a library and a runner file. 
