import sys
import re

def main():
	with open('m.txt') as f:
		s = str(f.read())
	arr = s.split('\n')
	if(len(arr) != 3):
		print("Error")
	count = 0
	for i in range(len(arr)):
		if(len(arr[i]) != 5):
			print("Error")
			break
		if(i == 0 and re.match(r'[*][^*][^*][^*][*]', arr[i])):
			count += 1
		if(i == 1 and re.match(r'[*][*][^*][*][*]', arr[i])):
			count += 1
		if(i == 2 and re.match(r'[*][^*][*][^*][*]', arr[i])):
			count += 1
	print("True" if count == 3 else "False")
	
if __name__ == "__main__":
	main()

