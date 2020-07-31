import socket
import subprocess
from PBL.Controller import scaleController


def format_sensor_data(data):
    # example input: "US,+00418.53,  g"
    if data:
        weight = data.split(",")[1]
        weight = data[1:]
        print("Current weight is " + str(weight) + "g")
        return weight


def run_server(server_ip=socket.gethostname(), server_port=80):
    sc = scaleController.ScaleController()
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
                    print("Reading weight from sensor...")
                    current_weight = sc.getWeight()
                    #current_weight = format_sensor_data(sensor_output)
                    print("Ok. Sending data.")

                    encoded_data = current_weight.encode('utf-8')
                    conn.sendall(encoded_data)

                if not data:
                    break
                else:
                    pass


def main():
    while True:
        run_server()


if __name__ == '__main__':
    main()