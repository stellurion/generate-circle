import random
import math

def haversine_distance(dist1, dist2) -> int:
    R = 6371
    lat1, lon1 = math.radians(dist1[0]), math.radians(dist1[1])
    lat2, long2 = math.radians(dist2[0]), math.radians(dist2[1])

    a = math.sin(lat2-lat1)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2-lon1)/2)** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R*c

def euclid_distance(dist1, dist2) -> int:
    return math.sqrt((dist1[0] - dist2[0])**2 + (dist1[1] - dist2[1])**2)

def haversine_offset(limit, coords) -> tuple:
    pass

def euclid_offset(limit, coords) -> tuple:
    offset = random.uniform(0, limit) #generate radius offset from center, always <= from center, so drawn will include circle
    theta = random.uniform(0, 2 * math.pi)
    return coords[0] + offset*math.cos(theta), coords[1] + offset*math.sin(theta)

def euclid_circle(guess, target, g, maxg) -> Tuple[tuple, int]:
    dist = euclid_distance(guess, target) * ((maxg-g)/g) #guess radius
    center = euclid_offset(dist, target)
    return center, dist