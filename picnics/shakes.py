import math
import random
import datetime

print("Square root of 36:", math.sqrt(36))
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print("Power of 2^3:", math.pow(2, 3))

# Generate a random number between 1 and 100
print("Random number between 1 and 100:", random.randint(1, 100))

# Shuffle a list of numbers
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled numbers:", numbers)

 
# Random choice from a list
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry'])) 

 
today = datetime.date.today()
print("Today's date is:", today)

now = datetime.datetime.now()
print("Current time:", now.strftime("%H:%M:%S")) 