import sys

def main():
	for i in range(1, len(sys.argv)):
		print(sys.argv[i][0], end='')
	print()
	
if __name__ == "__main__":
	main()

