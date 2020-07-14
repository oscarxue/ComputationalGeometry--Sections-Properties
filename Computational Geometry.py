#every polygon can be separated into many triangles therefore we can caclualte
#the area using the information from list of vertices

pts = [[1,1.5],[1,5, 2.5],[3.5,2.5],[3.4,2.4],[1.5,5.4]]  # coordinate points of vertices
# function of the area
def area(points):
# if statement to check if the first vertex and last vertex are the same, as they need to be a closure to make it a polygon
    if points[0] != points[-1]:
        points = points + points[:1]

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



