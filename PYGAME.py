print('Hello')

StartGame = input('Start game? (Yes/No) ')

score = 0

if StartGame.lower() != 'yes' :
    print('Why Not :(')
    quit
else:
    print('Welcome to the Cybersecurity Quiz! ')
    print('There are 10 questions in total! Enjoy :) ')

print('Qn 1. Which of the following are Cyber Attacks? ')
print('a) Man in the Middle attack')
print('b) Phishing')
print('c) Denial of Service attack ')
print('d) All of the above')
Answer1 = input ('Answer: ')

if Answer1.lower() == 'd':
    print('Correct!')
    score = + 1

else:
    print('Incorrect!')
    print('The answer is d!')

print('Qn 2. Which of the following are cybersecurity practices? ')
print('a) Using multi-factor authentication to secure accounts')
print('b) Using simple passwords')
print('c) Opening suspicious links')
print('d) Not installing software updates')
Answer1 = input ('Answer: ')


if Answer1.lower() == 'a':
    print('Correct!')
    score = + 1

else:
    print('Incorrect!')
    print('The answer is a!')


print('Qn 3 What is the purpose of a firewall? ')
print('a) To burn so brightly the viruses die')
print('b) To store and protect sensitive data')
print('c) To monitor and control network traffic')
print('d) To detect and remove viruses')
Answer1 = input ('Answer: ')


if Answer1.lower() == 'c':
    print('Correct!')
    score = + 1

else:
    print('Incorrect!')
    print('The answer is c!')

print('Qn 4 What is strong password?  ')
print('a) A combination of lowercase, uppercase, numbers and special characters')
print('b) The name of your favourite TV show')
print('c) qwerty123456')
print('d) Yor birthday')
Answer1 = input ('Answer: ')


if Answer1.lower() == 'a':
    print('Correct!')
    score = + 1

else:
    print('HOW DID YOU GET THAT WRONG?!')
    print('The answer is a! (Obviously)')



print('Qn 5 What is the purpose of a VPN? ')
print('a) Maintain online privacy')
print('b) Watch your favourite Netflix show from other regions')
print('c) Protects sensitive information from being intercepted')
print('d) All of the above')
Answer1 = input ('Answer: d')


if Answer1.lower() == 'd':
    print('Correct!')
    score = + 1

else:
    print('Incorrect!')
    print('The answer is d!')

print('Qn 6 What is phishing? ')
print('a) To catch phish (Yum yum)')
print('b) Computer virus that spreads through clicking on suspicious ads')
print('c) To trick victims into revealing sensitive information by posing as a trustworthy source')
print('d) Stealing sensitive information of those who visits a unsecure website')
Answer1 = input('Answer: ')

if Answer1.lower() == 'c':
    print('Correct!')
    score = + 1

else:
    print('Incorrect!')
    print('The answer is c!')



print('Qn 7 Which of the following are NOT indicative of a phishing email?')
print('a) Email contains mismatched sender information')
print('b) Email looks professional')
print('c) Email has high levels of grammatical error')
print('d) Email contains urgent language')
Answer1 = input('Answer: ')

if Answer1.lower() == 'b':
        print('Correct!')
        score = + 1

else:
        print('Incorrect!')
        print('The answer is b!')


print('Qn 8 What is a brute-force attack? ')
print("a) Method where hacker tries all possible password combinations to gain access to victim's device")
print('b) Breaking and entering')
print('c) Taking apart a device physically to obtain sensitive information')
print('d) Smashing the device to pieces')
Answer1 = input('Answer: ')

if Answer1.lower() == 'a':
        print('Correct!')
        score = + 1

else:
        print('Incorrect!')
        print('The answer is a!')


print('Qn 9 What is 2FA? ')
print('a) 2-factor Authentication')
print('b) 2-factor Authorisation')
print('c) 2-factor Access')
print('d) 2-factor Authenticity')
Answer1 = input('Answer: ')

if Answer1.lower() == 'a':
        print('Correct!')
        score = + 1

else:
        print('Incorrect!')
        print('The answer is a!')


print('Qn 10 What virus did David L. Smith create in 1999? ')
print('a) Melissa Virus')
print('b) Stuxnet')
print('c) Deathworm')
print('d) Smith Vius')
Answer1 = input('Answer: ')

if Answer1.lower() == 'a':
        print('Correct!')
        score = + 1

else:
        print('Incorrect!')
        print('The answer is a!')


print('Congratulations! You got ' + str(score) + '!!!')


