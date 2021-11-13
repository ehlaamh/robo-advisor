OldMin = -80
OldMax = 120
NewMax = 13
NewMin=0
 
	
def new(OldValue):
    NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
    return NewValue
    
a= new(45)
print(a)