>>> point_ahead = 15
>>> point_ahead = point_ahead - 3
>>> has_ball = True
>>> if has_ball == True:
	point_ahead = point_ahead + 0.5
else:
	point_ahead = point_ahead - 0.5

	
>>> point_ahead = point_ahead**2
>>> sec_left = 10
>>> if point_ahead > sec_left:
	print ('Lead is safe')
else:
	print ('Lead is not safe')
