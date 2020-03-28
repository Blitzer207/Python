# file = open('C:\\Users\\sandr\\Desktop\\python\\.txt')
# text = file.read()
# print(text)
# file.close()

# read
# with open('C:\\Users\\sandr\\Desktop\\python\\trash.txt','read') as f:
##     print(f.read())

# write
with open('C:\\Users\\sandr\\Desktop\\python\\trash.txt',"a") as f: # a: append #'w'  recover original text
    f.write(" Goodbye world\n")



print(help(open))