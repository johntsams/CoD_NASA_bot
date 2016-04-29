import socket               # Import socket module
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(14,GPIO.out)
GPIO.setup(15,GPIO.out)
GPIO.setup(18,GPIO.out)
GPIO.setup(23,GPIO.out)
GPIO.setup(24,GPIO.out) 
GPIO.setup(25,GPIO.out)
GPIO.setup(8,GPIO.out)
GPIO.setup(7,GPIO.out)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
# for ipv4 addr

host = socket.gethostname() # Get local machine name  this is going to be changed to the #controlling computers ip addr

port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)

drivemotorl =  GPIO.PWM(14,400)
drivemotorr =  GPIO.PWM(15,400)

binactuatirl = GPIO.PWM(18,400)
binactuatir = GPIO.PWM(23,400)

steer = GPIO.PWM(24,400)

ballscrew = GPIO.PWM(25,400)

conveyor = GPIO.PWM(8,400)

augur = GPIO.PWM(7,400)

#name.start(dutycycle)
#name.ChangeDutyCycle(dutycycle)
#name.stop() stops pwm output

s.close                     # Close the socket when done

# http://www.binarytides.com/python-socket-programming-tutorial/
# https://docs.python.org/2/library/socket.html
