##########################################################################
## Modify the variables so that all of the statements evaluate to True. ##
##########################################################################

var1 = 3
var6 = 3.22
var2 = "kantanand"
var3 = [1,2,3]
var4 = (0,1,'Hello, Python!')
var5 = { "happy": "birthday", "egg": "salad" }

############################################
## Don't edit anything below this comment ##
############################################

# integers
print(type(var1) is int)
print(type(var6) is float)
print(var1 < 35)
print(var1 <= var6)

# strings
print(type(var2) is str)
print(var2[5] == 'n' and var2[0] == "p")

# lists
print(type(var3) is list)
print(len(var3) == 5)

# tuples
print(type(var4) is tuple)
print(var4[2] == "Hello, Python!")

# dictionaries
print(type(var5) is dict)
print("happy" in var5)
print(7 in var5.values())
print(var5.get("egg") == "salad")
print(len(var5) == 3)
var5["tuna"] = "fish"
print(len(var5) == 3)
