import sys
from runtime.router import route_command

def main():
    route_command(sys.argv)

if __name__ == '__main__':
    main()
