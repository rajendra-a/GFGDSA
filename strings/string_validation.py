# The string must have below constrainst 
# String must have the length greater than or equal to 10 chars
# Strin must contain at least 1 numeric character
# String must contain at least 1 uppercase
# String must contain at least 1 lowercase
# String must contain at least 1 special char  from @#$*_

def string_validation(s):
    if len(s) < 10:
        return 0
    upper = 0 
    lower = 0
    numeric = 0
    special = 0
    for i in range(0,len(s)):
        if(s[i].islower()):
            lower = 1
        elif(s[i].isupper()):
            upper = 1
        elif(s[i].isdigit()):
            numeric = 1
        elif(s[i] in "@#$*-"):
            special = 1
    if lower == 1 and upper == 1 and numeric == 1 and special == 1:
        return 1
    else:
        return 0
