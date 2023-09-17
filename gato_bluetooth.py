import bluetooth
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 22
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print("Conexion realizada con: ", address)
while True:
	recvdata = client_socket.recv(1024)
	print("Informacion recibida: %s" % recvdata)
	if recvdata == "Q":
		print("Finalizado")
		break

client_socket.close()
server_socket.close()
