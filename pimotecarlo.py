def montecarlopi(n): 
    import random 
    points_inside =0
    total_points =n

    r=1
    
    piestimate=0
    for i in range(1,n+1):
        x=random.random()
        y=random.random()
        # total_points +=1
        if ((x**2+y**2)<=1):
            points_inside += 1
            piestimate=4*(points_inside/total_points)
    return(piestimate)








