import random
import math

# //formula: 
# //1. grab current distance from destination. shrink it by number of guesses ratio (maxguesses-guess)/maxguesses
# //2. use the above as the radius. 
# //3. generate a number from [0-radius]. use this number to offset from the destination in any direction and get a random point

#range (0-100, 0-100)

coord = tuple(map(int, input().split()))
dest = (random.randint(1, 100), random.randint(1, 100))

distance =  math.sqrt((coord[1]-dest[1])**2 + (coord[0]-dest[0])**2)
radius = random.randint(1, distance)
angle = random.randint(0, 360)

center = (coord )

#center radius must be greater than center > distance




#or just make offset circle