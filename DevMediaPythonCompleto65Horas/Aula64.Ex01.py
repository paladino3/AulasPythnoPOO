import socket


host  = socket.gethostname()
port = 9999


mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.bind((host,port))

while True:
    packet, address = mySocket.revfrom(1024)
    print("Packet received: ")
    print("From host: ",address[0])
    print("Host port ",address[1])
    print("Length: ",len(packet))
    print("Containing: ")
    print("\t" + packet.decode('ascii'))

    print("\nEcho data to client...")
    mySocket.sendto(packet,address)
    print("Packet sent\n")

mySocket.close()