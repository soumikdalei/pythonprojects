import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','*','(',')','*','+']
numbers=['0','1','2','3','4','5','6','7','8','9']
print("Welcome to the random password generator")
nr_letters=int(input("How many words do you want in your password? "))
nr_symbols=int(input("How many symbols do you want in your password? "))
nr_number=int(input("How many numbers do you want in your password? "))
#Easy Method
password=""
for char in range(1,nr_letters+1):
    password+=random.choice(letters)
for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)
for char in range(1,nr_number+1):
    password+=random.choice(numbers)
print(password)
#hard One

password_list=[]
password1=""
for char in range(1,nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))
for char in range(1,nr_number+1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
for char in password_list:
    password1+=char
print(f"Your password is {password1}")




