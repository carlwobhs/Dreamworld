print('Dreamworld - are you eligible to take the rides')

height = float(input('Enter your height: '))#float or decimal
age = int(input('Enter your age: ')) #turning to number integer

if(height > 150):
    print('Stratosfear, Family Carts, Scorpion Karts')
if(height > 120):
    print('Fearfall, Invader, Corkscrew Rollercoaster... ')
if(height > 90 and age > 5):
    print('Los Banditos')
    if(age > 8):
        print('Robot Riot')
if(height > 80):
    print('Log flume, Gold Rush, Family Karts,Dogems')
elif(height < 80 and age >=3 and age <= 8):
    print('Fortress of Fun')

