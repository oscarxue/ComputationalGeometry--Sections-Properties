#every polygon can be separated into many triangles therefore we can caclualte
#the area using the information from list of vertices

pts = [[1,1.5],[1,5, 2.5],[3.5,2.5],[3.4,2.4],[1.5,5.4]]  # coordinate points of vertices
# function of the area
def area(points):
# if statement to check if the first vertex and last vertex are the same, as they need to be a closure to make it a polygon
    if points[0] != points[-1]:
        points += points[:1]

# assigning x and y coordinates with the given points

    x = [c[0] for c in points]
    y = [c[1] for c in points]

#assigning the sum variable to be a given value
    sum = 0


#for loop to sum up green's theoream of area.
#the equation works counterclockwise according to the green's theorem
    for i in range(len(points) - 1):
        sum += x[i] * y[i+1] - x[i+1] * y[i]
    return sum/2


print(area(pts))


example_1 = [
    [0,0],[1.5,0],[2.5,-1],[3.5,0],[5,0],[5,2],[3.5,2],[2.5,3],[1.5,2],[0,2]
]


print(area(example_1))


#Green's theoream : sum of the rotational forces inside a closed surface is equal to the sum of all the
#individual forces around it.



#centroid area
#the centroid of an area is essentially the average position of the area.

def centroid(points):
    if points[0] != points[-1]:
        points += points[:1]
        # assigning x and y coordinates with the given points

    x = [c[0] for c in points]
    y = [c[1] for c in points]

    sum_x = 0
    sum_y = 0

#find the area of the points used in the polygon
    a_polygon = area(points)

#Use a for loop to find the sum of the xc and yc , we minus one from the points because we don't use the last point.
    for i in range(len(points) - 1):
        sum_x = (x[i+1]+x[i]) * (x[i]*y[i+1] - x[i+1]*y[i])
        sum_y =(y[i+1]+y[i]) * (x[i]*y[i+1] - x[i+1]*y[i])
    return sum_y/6*a_polygon, sum_x/6*a_polygon

section_centroid = centroid(pts)

print(section_centroid)











#calculating moment of inertia about xx and yy axis
#calculating product of inertia withrespect to xy axis about the centroid
#product of inertia measures rotational stability
def inertia():   #measures warping of beam
    if pts[0] != pts[-1]:
        pts = pts + pts[:1] , #:1 means the showing the first element of the array, same as [0]
        
            



