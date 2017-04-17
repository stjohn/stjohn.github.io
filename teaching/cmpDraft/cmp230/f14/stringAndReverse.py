
def main():
    s = input("Enter string: ")
    l = len(s)
    for i in range(l):
        print(s[i],s[l-i-1])
    print("Thank you for using my program!")

main()
