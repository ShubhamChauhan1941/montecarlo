def test_1(): 
	from math import pi 	
	from pimotecarlo import montecarlopi 
	xvalues=[10,100,1000,10000,100000,1000000]
	for n in xvalues:
		newmontecarlopi =montecarlopi(n)
		pi_math=pi	
		print(f"for n={n}, montecarlopi={newmontecarlopi} and math_pi={pi_math}") 
		error = abs(newmontecarlopi - pi_math) / pi_math
		er=error*100
		print(er)
		assert error < 2,f"Error for {n} points is larger than 20%: {er}"
			


