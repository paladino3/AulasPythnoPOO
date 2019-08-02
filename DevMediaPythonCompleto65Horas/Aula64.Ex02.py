import socket


host  = socket.gethostname()
port = 9999


mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    packet = input("Packt>>> ")
    print("\nSending packet...")
    mySocket.sendto(packet.encode('ascii'), (host,port))
    print("PAcket send \n")

    received = mySocket.recv(1024)

    print("Packet received:")
    print("Containing:")
    print("\t" + received.decode('ascii') + ("\n"))

mySocket.close()