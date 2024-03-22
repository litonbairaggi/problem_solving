# Problem 3: Reverse Words in a String

string = "Hello Word!"
print("Reverse",string[::-1])


# Problem 2: Find Missing Number in Array
lists=[1,2,3,4,5,7,8,9,10]
print("Missing Element Of list", sum(range(lists[0],lists[-1]+1)) - sum(lists))


# Problem 1: Check Balanced Parentheses
def paraCheck( seq ):  
   while True:  
       if "()" in seq :  
           seq = seq.replace ( "()" , "" )  
       elif "{}" in seq :  
           seq = seq.replace ( "{}" , "" )  
       elif "[]" in seq :  
           seq = seq.replace ( "[]" , "" )  
       else :  
           return not seq  

seq = "([)]"
if not seq:
    print("Parentheses " +seq+ " is False")
print("Parentheses " +seq+ " is True")