def print_age():
    name , age = input("Enter your name") , int(input("Enter your age"))
    
    for i in range(int(input("Enter a number"))):
        print("Hello ",name,"!, You will turn 100 in the year",(2017-age)+100," :) \n")
def main():
    print_age()
if __name__ == '__main__':
    main()
