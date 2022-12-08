str_1 = ""
some_list = ["Welcome", "To", "Bonus", "Tips"]
print(str_1.join(some_list))

# Use the above code instead of: 
str_1 = ""
some_list = ["Welcome", "To", "Bonus", "Tips"]
for x in some_list:
    str_1 += x
    print(x)
