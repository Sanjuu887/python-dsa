"""
Problem 4 — Email Validator
Scenario

A website allows users to register using an email address.

Before registration, the system must validate the email.

Requirements

Ask user:

Enter Email:
Rules
Rule 1

Email must contain:

@
Rule 2

Email must contain:

.
Rule 3

Email length must be at least:

8 characters
Rule 4

Email should not contain spaces.

Example:

sanjay @gmail.com

Invalid.

Rule 5

Email should contain only ONE:

@

Example:

sanjay@@gmail.com

Invalid.

Output

If all conditions satisfy:

Valid Email

Otherwise:

Invalid Email

Also print the reason(s).

Example:

Invalid Email
Missing @

OR

Invalid Email
Contains Spaces

OR

Invalid Email
More than one @
Example Test Case 1

Input:

sanjay@gmail.com

Output:

Valid Email
Example Test Case 2

Input:

sanjaygmail.com

Output:

Invalid Email
Missing @
Example Test Case 3

Input:

sanjay@@gmail.com

Output:

Invalid Email
More than one @
Example Test Case 4

Input:

san jay@gmail.com

Output:

Invalid Email
Contains Spaces
Topics Covered

✅ Strings
✅ String Traversal
✅ Conditions
✅ Validation Logic
✅ Counting Characters
✅ Functions (optional)
"""
email=input("Enter your email : ")
if len(email)==0 or len(email)<=8 or "@" not in email or  "." not in email or email.count("@")>=2 or " " in email or email[0]=="@" or email[-1]=="@":
    print("\nInvalid email..\n")
    if len(email)==0:
        print("empty email\n")
    else:
        if len(email)<=8:
            print("email is less than 8 characters..\n")
        if "@" not in email:
            print("@ is missing\n")
        if email.count("@")>=2:
            print("@ is more than 1\n")
        if "." not in email:
            print(". is missing\n")
        if " " in email:
            print("space is there\n")
        if "@"==email[0] or email[-1]=="@":
            print("@ invalid place\n")
else:
    print("\nvalid mail")



    
    
        

