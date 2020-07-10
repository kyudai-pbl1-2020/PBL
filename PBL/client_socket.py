import socket

def send_data_request(server_ip=socket.gethostname(),server_port = 80, input='Data_Request'):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # define socket TCP
        s.connect((server_ip, server_port))

        input = input.encode('utf-8')

        # send request ti server
        s.sendall(input)

        # Get the Data from Server and process the Data
        data = s.recv(1024).decode('utf-8')

        return data


def main():
    data = send_data_request()
    print(data)

if __name__ == "__main__":
    main()