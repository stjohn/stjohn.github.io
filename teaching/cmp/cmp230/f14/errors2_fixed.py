# errors2.py-- modified from Zelle
# recursions.py
#   A collection of simple recursive functions from Zelle, 2nd Edition
#   (Some also include looping counterparts).

def fact(n):
    # returns factorial of n
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def reverse(s):
    # returns reverse of string s
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]

def anagrams(s):
    # returns a list of all anagrams of string s
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                    ans.append(w[:pos]+s[0]+w[pos:])
        return ans

def loopFib(n):
    # returns the nth Fibonacci number
    curr = 1
    prev = 1
    for i in range(n-2):
        curr, prev = curr+prev, curr
    return curr

def main():
    n = eval(input("Enter a number: "))
    s = input("Enter a string: ")
    print(str(n)+"!= ", fact(n), "or", loopFib(n))
    print(s, "reversed is: ", reverse(s))
    print("\n anagrams: ", anagrams(s))

main()
