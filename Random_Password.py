import random
difficulty = input ("How complex do you want yor password be? weak or strong?")
if difficulty == "strong":
    password = ''
    characters = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLINOPQRSTUVUXYZ!@#$%^&*()_+-=[]\;'
    origin = input("Do you want to set a original password? yes or no")
    if origin == "yes":
        pa = input("Set the original password")
        length = input("how long do you want your password?(original+random)")
        for i in range (int (length)):
            randchar = random. choice (characters)
            password = password + randchar
        print ("strong password with original password: " + pa + password)
    if origin == "no":
        password = ''
        characters = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLINOPQRSTUVUXYZ！@#¥%……&*（）_`~+-=「」｜：“；'
        length = input("how long do you want your password?")
        for i in range(int(length)):
            randchar = random.choice(characters)
            password = password + randchar
        print("strong password" + password)
if difficulty == "weak":
    password = ''
    characters = 'abcdefghijklmnopqrstuvwxyz'
    origin = input("Do you want to set a original password? yes or no")
    if origin == "yes":
        pa = input("Set the original password")
        length = input("how long do you want your password?(original+random)")
        for i in range (int (length)):
            randchar = random. choice (characters)
            password = password + randchar
        print ("weak password with original password: "+ origin + password)
    if origin == "no":
        password = ''
        characters = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLINOPQRSTUVUXYZ！@#¥%……&*（）_`~+-=「」｜：“；'
        length = input("how long do you want your password?")
        for i in range(int(length)):
            randchar = random.choice(characters)
            password = password + randchar
        print("weak password" + password)