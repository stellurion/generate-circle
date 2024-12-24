import random
import math


#range (0-100, 0-100)

def haversine_distance(dist1, dist2) -> int:
    pass

def euclid_distance(dist1, dist2) -> int:
    return math.sqrt((dist1[0] - dist2[0])**2 + (dist1[1] - dist2[1])**2)

def offset(limit, coords) -> tuple:
    offset = random.uniform(0, limit) #generate radius offset from center, always <= from center, so drawn will include circle
    theta = random.uniform(0, 2 * math.pi)
    return coords[0] + offset*math.cos(theta), coords[1] + offset*math.sin(theta)

def circle(guess, target, g, maxg) -> Tuple[tuple, int]:
    dist = euclid_distance(guess, target) * ((maxg-g)/g) #guess radius
    center = offset(dist, target)
    return center, dist

#make visualization for this