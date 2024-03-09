def test_pi1(xvalues,n): 
    from math import pi 
    from pimotecarlo import montecarlopi 
    xvalues=[]
    x=10**6
    er=0.02

    for i in range(10,x+1):
        xvalues.append(i)
        for n in xvalues: 
            newmontecarlopi =montecarlopi(n)
            pi_math=pi
            error = abs(newmontecarlopi - pi_math) / pi_math
            if error > 0.2:
                print(f"Error for {n} points is larger than 20%: {error}")