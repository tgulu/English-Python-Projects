
# recursive string reversal

def reverse_string(str1, newstr = ""):
	if len(str1) == 0:
		return newstr
	else:
		return reverse_string(str1[:-1], newstr + str1[-1])
			
words = "This is my song"
print(reverse_string(words))


# Single line reverse string
def strings_reverse(x):
  return x[::-1]

mytxt = strings_reverse("I wonder how this text looks like backwards")

print(mytxt)


# Two pointer String List Reversal
def reverse_stringer(self, s: List[str]) -> None:
    def help(lp, rp):
        if lp<rp:
            s[lp],s[rp] = s[rp],s[lp]
            help(lp +1, rp -1)
            
    help(0, len(s)-1)


s = ["h","e","l","l","o"]

obj = reverse_stringer(s)
print(obj)