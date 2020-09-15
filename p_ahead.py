point_ahead = 20
point_ahead = point_ahead - 3

has_ball = True

if has_ball == True:
    point_ahead = point_ahead + 0.5
else:
    point_ahead = point_ahead - 0.5

point_ahead = point_ahead**2

seconds_left = 12
if point_ahead > seconds_left:
    print ('Lead team is safe')
else:
    print ('Lead team is not safe')

    
