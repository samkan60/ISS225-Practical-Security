#program to insert string in the middle of another string

#create function with two arguments, the string and inserted string
def insert_string(str, str2):
	return str[:2] + str2 + str[2:]
    #slice initial string and concatenate with input string

print(insert_string('[[]]', 'Python'))
print(insert_string('{{}}', 'PHP'))

