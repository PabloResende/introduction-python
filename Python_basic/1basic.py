'''this is a DocString
this is a pound, used to comment(# = is a pound)
can be used to comment
on multiple lines'''

print(123)# Display things on the screen

print(12, 34)# 12,34
print(12, 34, sep="-")# 12-34
print(9, 10, sep="joao" )# SEP adds the character inside the quotation marks\
# in place of the spaces

# \r\n = CRLF breaks the line
print(32, 35, end='\r\n##')# ##32 35##
print(32, 35, end='##\r\n')# 32 35
print(32, 35, end='\r\n38')

print('pablo') # works with both common quotation
print("pablo") # marks and double quotation marks

print("pablo  ou \'PABLO\'")
# a backslash is used as the ESCAPE character\
#  to use quotation marks inside quotation marks

#But it gets better:
print('pablo ou "PABLO"')
#or
print("pablo ou 'PABLO'")