import socket


def format_data(weight):
    if weight:
        formatted = "Current weight is " + str(weight) + "g"
        print(formatted)
        return formatted



def run_server(server_ip=socket.gethostname(), server_port=80):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started. Waiting for client to connect ")
        s.bind((server_ip, server_port))
        s.listen(5)
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:

                data = conn.recv(1024).decode('utf-8')

                if str(data) == "Data_Request":

                    print("Ok Sending data.")

                    my_data = "Some Test data: US,+00418.53,  g"

                    print("Sending test data: " + str(my_data))

                    encoded_data = my_data.encode('utf-8')

                    conn.sendall(encoded_data)

                if not data:
                    break
                else:
                    pass


def main():
    run_server()


if __name__ == '__main__':
    main()