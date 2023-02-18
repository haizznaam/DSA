def reverse(s,n=1,res=''):
    if n == len(s):
        return res + s[0]
    else:
        res += s[-n]
    return reverse(s,n+1,res)

s = "hello world"
print(reverse(s))