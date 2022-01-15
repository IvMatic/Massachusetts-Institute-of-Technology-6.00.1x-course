"""
@author: ivan matic
"""

'''
Write a program that prints the number of times the string 'bob' occurs in s. For example,
if s = 'azcbobobegghakl', then your program should print 2

'''


s = 'azcbobobegghakl'
count = 0

for i in range(len(s)):
    if s[i:i+3] =='bob':
        count += 1
print('number of bob is:' + str(count))
