# generate-circle
Given a start location and target location, create a randomly generated circle around the target in relation to the remaining distance and tries. Developed at LA Hacks 2024.

# algorithm
1. grab current distance from destination. shrink it by number of guesses ratio (max_guesses - guess)/max_guesses
2. use the above as the radius. 
3. generate an offset of random direction and [0-radius] from the target.
4. use new offset point as the center and the original distance as the radius for your circle hint


# TODO
implement visualization    
implement generation on map using leaflet
