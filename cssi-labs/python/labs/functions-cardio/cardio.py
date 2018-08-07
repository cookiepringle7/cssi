

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s = "Exercise1"

print "The original string  is : ", s

print "The reversed string(using recursion) is : ", reverse(s)
