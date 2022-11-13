# The Elegance of List Comprehension 

# instead of doing this 
L = []
for ch in "mihirchakma":
    L.append(ch)

print(L)


# use the one-liner list comprehension
L = [ch for ch in "mihirchakma"]

print(L)