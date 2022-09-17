
x = False
y = 50
z = 23
p = "Hello python"

# if else condition
if x :
    print('sum = ', y+z)
else :
    print('result not')

# ternary operator
print(y if y > z else z,'is large value')


# switch statement
def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"

print(switch("JavaScript"))   
print(switch("PHP"))   
print(switch("Java")) 
