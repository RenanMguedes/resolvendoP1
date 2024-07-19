import socket

def base_conversion(number, base_from, base_to):
    if base_from == 16 and base_to == 10:
        return str(int(number, 16))
    elif base_from == 10 and base_to == 2:
        return bin(int(number))[2:]
    else:
        return "Conversão não suportada"

def binary_operations(operation, num1, num2):
    if operation == 'add':
        result = int(num1, 2) + int(num2, 2)
    elif operation == 'sub':
        result = int(num1, 2) - int(num2, 2)
    else:
        return "Operação não suportada"
    
    result_bin = bin(result & 0xff)[2:]
    return result_bin.zfill(8)

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    params = request.split(',')

    if params[0] == 'conversion':
        number, base_from, base_to = params[1], int(params[2]), int(params[3])
        response = base_conversion(number, base_from, base_to)
    elif params[0] == 'operation':
        operation, num1, num2 = params[1], params[2], params[3]
        response = binary_operations(operation, num1, num2)
    else:
        response = "Requisição não suportada"

    client_socket.send(response.encode())
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Servidor aguardando conexões...")

    while True:
        client_socket, addr = server.accept()
        print(f"Conexão aceita de {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
