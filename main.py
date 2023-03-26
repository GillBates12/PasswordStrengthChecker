import string

password = input("Type your password to check strength: ")

uppercase = any([1 if c in string.ascii_uppercase else 0 for c in password])
lowercase = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [uppercase, lowercase, special, digits]

length = len(password)

score = 0

with open('/Users/pablorizo/Downloads/10k most common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password is too common. Score automatically is 0. Try again.")
    exit()

if length >= 8:
    score += 1
if length >= 12:
    score += 1
if length >= 16:
    score += 3

if sum(characters) > 0:
    score += 1
if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 2

if score < 5:
    print(f"The score is quite low, try again. Score {str(score)} / 10")
elif score == 5:
    print(f"The score is ok, try again. Score {str(score)} / 10")
elif 5 < score < 8:
    print(f"The score is pretty good! It will be tough trying to hack you. Score {str(score)} / 10")
elif score >= 8:
    print(f"Perfect score! Might as well give up hackers. Score {str(score)} / 10")