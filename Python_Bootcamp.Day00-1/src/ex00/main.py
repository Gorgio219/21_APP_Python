import sys

def main():
	if len(sys.argv) != 2 or sys.argv[1].isnumeric() != 1:
		print("Error: wrong argument.")
	amount_lines : int = int(sys.argv[1])
	for _ in range(amount_lines):
		string : str = input()
		if len(string) == 32 and string[:5] == '00000' and string[6] != '0':
			print(string)

if __name__ == "__main__":
	main()
