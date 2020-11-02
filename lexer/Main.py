import sys
from Lexer import Lexer

def main():
	if len(sys.argv) < 2:
		print("usage main.py filename")
	else:
		l = Lexer(sys.argv[1])
		#lexer.scanfile(sys.argv[1])

if __name__ == "__main__":
    main()