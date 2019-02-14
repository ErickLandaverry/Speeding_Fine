#The speeding fine in some small town in the countryside outside Metropolis is $50 plus $5 for each mph over the speed limit. There is also a penalty of $200 for any speed over 90 mph.   Write a program that accepts a speed limit and clocked speed as input and prints "legal" if the speed is legal, or the fine amount and "illegal" if the speed is not legal. 


def main():
  speed = int(input("What is your speed?: "))
  speed_limit = int(input("What is the speed limit?: "))

  if speed > 90:
    print("Really!? Well, you are going to be fined $200 for driving over 90 mph and you will get a ticket of $", 50+((speed-speed_limit)* 5))
  
  elif speed > speed_limit:
    print("You were pulled over for speeding. Your ticket will be $" , 50 + ((speed-speed_limit) * 5))

  else:
    print("Keep driving! Your speed is legal.")
  
main()