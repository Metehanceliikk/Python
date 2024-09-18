import math

points=[(1,5),(7,3),(2,4),(8,7),(3,4)]

def euclideanDistance(point_1,point_2):
    
    x1,x2=point_1
    y1,y2=point_2

    return math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))

distances=[]

for i in range(len(points)):
    for k in range(i+1,len(points)):
        distance=euclideanDistance(points[i],points[k])
        distances.append(distance) 

       
min_distance=min(distances)
print(f"Minimum Öklid Mesafesi {min_distance}")