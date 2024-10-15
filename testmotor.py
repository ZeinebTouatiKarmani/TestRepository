from motor import Motor

motor1=Motor() #instance1
motor2=Motor() #instance2
motor3=Motor() #instance3


motor1.speed=25
motor1.acceleration=10
motor1.maxSpeed=60
motor1.pinA=1
motor1.pinB=2
print (motor1.forward())
print (motor1.speed)