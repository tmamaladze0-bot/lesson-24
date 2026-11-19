import socket


HOST = "127.0.0.1"
PORT = 5060

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    message = "hello socket"
    client.sendall(message.encode("utf-8"))
    data = client.recv(1024)
    reply = data.decode("utf-8")
    print(f"პასუხი: {reply}")