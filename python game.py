print("WELCOME TO CAR RACING GAME")
print("--------------------------")
player=input("Enter your name: ")
distance=0
speed=20
fuel=100
print("\nGame started!")
print("Controls: ")
print("A= Slow down")
print("D= Speed up")
print("S=stop")
print("Q=Quit")
while True:
    print("\n-------------------")
    print("Player:",player)
    print("Distance:",distance,"km")
    print("Speed:",speed,"km/h")
    print("Fuel:",fuel,"%")
    print("-----------------------")
    if distance>=100:
        print("\n Congratulations!")
        print("You completed the race!")
        print("You completed the race!")
        print("Final distance:",distance,"km")
        break
    if fuel<=0:
        print("\n out of fuel!")
        print("Game over!")
        break
    move=input("Enter your move: ").lower()
    if move=="d":
      speed+=10
      if speed>100:
        speed=100
        distance+=speed//10
        fuel-=5
        print("You increased your speed!")
    elif move=="a":
      speed-=10
    if speed<10:
       speed=10
       distance+=speed//20
       fuel-=2
       print("You slowed down")
    elif move=="s":
       print("You slowed down")
    elif move=="q":
       print("\n you left the race")
       break
    else:
       print("Invalid command!")
print("\n THanks for playing!")





num = int(input('Enter a number'))
if num>=0:
   if num ==0:
      print('Zero')
   else:
      print('A Positive number')
else:
   print('A negative number') 

a=1
while a<=5:
      print(a)
      a+=1
print('end')      

















































































