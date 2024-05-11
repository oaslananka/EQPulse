import socket
import pandas as pd

def collect_data(host='localhost', port=12345):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = []
    try:
        while True:
            raw_data = s.recv(1024)
            if not raw_data:
                break
            formatted_data = process_data(raw_data)
            data.append(formatted_data)
    finally:
        s.close()
    return pd.DataFrame(data)

def process_data(raw_data):
    # This function processes the raw data and converts it to a suitable format.
    return eval(raw_data.decode())

if __name__ == "__main__":
    df = collect_data()
    df.to_csv('real_time_data.csv', index=False)