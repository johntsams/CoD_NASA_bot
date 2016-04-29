import socket               # Import socket module 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name ip addr
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port


s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from \n', addr
   c.send('Thank you for connecting \n')
   userdata = input(enter in text ) #string data type         #http://www.tutorialspoint.com/python3/python_strings.htm
   c.send(userdata)                 # Data or whatever
   c.close()                # Close the connection
  

   
# http://www.binarytides.com/python-socket-programming-tutorial/
# https://docs.python.org/2/library/socket.html
