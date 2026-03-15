email = input("Enter Your Email: ")
count = 0
if 6 <= len(email) <= 254: #Length if Gmail should be in range 6 to 254
    if email[0].isalpha():#First letter should be alpha 
        if ("@" in email) and (email.count("@")==1 ):# '@' symbol contains exactly one 
            if email.endswith(("@gmail.com", "@gmail.org", "@gmail.net", "@gmail.edu", "@gmail.in")):
                for i in email: #Only lowercase letters, numbers, and symbols (_ . @)") are allowed
                    if i == i.isspace():
                        count=1
                    elif i.isalpha():
                        if i == i.upper():
                            count=1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i =="." or i =="@":
                        continue
                    else:
                        count = 1

                if count == 1:
                        print("Invalid email. Please use only lowercase letters, numbers, and allowed symbols (_ . @)")
                else:
                    print("The Email ({}) has been successfully validated.".format(email))
            else:
                 print("Invalid Email domain.\nPlease use a valid Gmail domain such as @gmail.com, @gmail.org, @gmail.net, @gmail.edu, or @gmail.in")
        else:
            print("Invalid Email. Please make sure your email contains exactly one '@' symbol.")
    else:
        print("Invalid Email.\nThe first character should not be: space . _ @ % + -")
else:
    print("Invalid Email: length is Invalid ")
