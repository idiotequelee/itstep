def isPalindrome(s):
	return s == s[::-1]

s = input().lower().replace(' ', '')
print(s)
ans = isPalindrome(s)
 
 #test 4

if ans:
	print("Yes")
else:
	print("No")
