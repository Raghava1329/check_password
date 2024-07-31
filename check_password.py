def ragh(passcode):
    if len(passcode) < 8:
        return "weak"
    A= False
    a= False
    num= False
    sp= False
    sp_c= "!@#$%^&*~"
    for char in passcode:
        if char.isupper():
            A = True
        elif char.islower():
            a = True
        elif char.isdigit():
            num = True
        elif char in sp_c:
            sp = True
    if A==True:
        if a==True:
            if num==True:
                if sp==True:
                    return "strong"
    else:
        return "weak"
passcode = input("Enter a passcode: ")
print(ragh(passcode))