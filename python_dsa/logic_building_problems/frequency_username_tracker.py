"""
Problem 9 — Username Frequency Tracker
Scenario

You are building a social media analytics tool.

The system tracks how many times each username appears.

Requirements

Ask user:

How many usernames do you want to enter?

Take usernames one by one.

Example:

sanjay
rahul
sanjay
ravi
rahul
sanjay
After all usernames are entered

Print frequency of every username.

Example:

sanjay : 3
rahul : 2
ravi : 1
Also Print
1. Total Usernames Entered

Example:

Total Usernames : 6
2. Total Unique Usernames

Example:

Unique Usernames : 3
3. Most Frequent Username

Example:

Most Frequent Username : sanjay
Frequency : 3
4. Least Frequent Username

Example:

Least Frequent Username : ravi
Frequency : 1
5. Search Username

Ask:

Enter Username To Search:

If found:

rahul appears 2 times

If not found:

Username Not Found
Validation Rules
Rule 1

Username cannot be empty.

Example:

""

Output:

Invalid Username

Ask again.

Rule 2

Searching should not be case-sensitive.

Example:

Stored:

Sanjay

Search:

sanjay

Output:

sanjay appears 1 time
Sample Input
6

sanjay
rahul
sanjay
ravi
rahul
sanjay
Expected Output
sanjay : 3
rahul : 2
ravi : 1

Total Usernames : 6

Unique Usernames : 3

Most Frequent Username : sanjay
Frequency : 3

Least Frequent Username : ravi
Frequency : 1
What This Problem Tests

✅ Dictionaries

✅ Frequency Counting

✅ Strings

✅ Searching

✅ Highest / Lowest Pattern

✅ Validation
"""
usernames = {}

n = int(input("How many usernames do you want to enter : "))

for i in range(n):

    while True:

        username = input("Enter Username : ").lower()

        if len(username) == 0:
            print("Invalid Username")
        else:
            break

    if username in usernames:
        usernames[username] += 1
    else:
        usernames[username] = 1


print("\n----- Username Frequency -----")

for username, frequency in usernames.items():
    print(username, ":", frequency)


print("\nTotal Usernames :", n)

print("Unique Usernames :", len(usernames))


names = list(usernames.keys())

most_frequent = names[0]
least_frequent = names[0]

for username in names:

    if usernames[username] > usernames[most_frequent]:
        most_frequent = username

    if usernames[username] < usernames[least_frequent]:
        least_frequent = username


print("\nMost Frequent Username :", most_frequent)
print("Frequency :", usernames[most_frequent])

print("\nLeast Frequent Username :", least_frequent)
print("Frequency :", usernames[least_frequent])


search = input("\nEnter Username To Search : ").lower()

if search in usernames:
    print(search, "appears", usernames[search], "times")
else:
    print("Username Not Found")