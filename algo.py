# //all measurements and math is done in meters

# //call ONCE to get destination point
# export function generateRandomPoint(coordinates, search_distance) {
#     //conversion radius in meters to degrees /111139, and then choose random ratio to shorten radius (to go along circle)
#     x = centerX + r * cos(theta)
#     y = centerY + r * sin(theta)

# }

# export function getOffsetRadius(distance, maxguess, guess) {
#     return distance * (maxguess-guess)/maxguess //radius
# }
# //this way, circles are always rewarded based on how much you have left, with it narrowing based on your guesses
# //should gurantee less overlap, because of the randomized angle
# export function generateOffsetPoint(destination, radius) { //radius comes from getOffsetRadius
#     var offset = Math.random() + radius //offset spin off destination

#     var angle = Math.random()*Math.PI*2; //radians 
#     var centerlat = destination[0] * Math.PI / 180
#     var centerlon = destination[1] * Math.PI / 180

#     var deltalat = offset * Math.cos(angle) / 111.111
#     var deltalon = offset * Math.sin(angle) / (111.111 * Math.cos(centerlat))

#     return [centerlat + deltalat, centerlon + deltalon]
# }

# //haversine formula
# export function distanceToLocation(from, to) {
#     var R = 6371 * 1000; //radius in meters
#     var lat1 = from[0] * Math.PI/180
#     var lat2 = to[0] * Math.PI/180
#     var lat = (to[0] - from[0]) * (Math.PI/180)
#     var lon = (to[1] - from[1]) * (Math.PI/180)
#     var a = Math.sin(lat/2) * Math.sin(lat/2) + Math.cos(lat1) * Math.cos(lat2) * Math.sin(lon/2) * Math.sin(lon/2) 
#     var d = R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
#     return d; //distance in meters
# }
