# This code will define two variables to nest within a third variable
# to create a sentence

c: str= "cats"  #This stores the first variable as a string
d: str= "dogs"  #This stores the second variable as a string
s = f"It's raining {c} and {d}."    #This variable uses and 'f' string to nest the previous two variables

print(s)    #This prints variable 's'
