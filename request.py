import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    
    print("Escolha a opção:")
    print("1. Conversão de base")
    print("2. Operação binária")
    choice = input("Opção: ")

    if choice == '1':
        number = input("Digite o número: ")
        base_from = input("Base de origem: ")
        base_to = input("Base de destino: ")
        request = f"conversion,{number},{base_from},{base_to}"
    elif choice == '2':
        operation = input("Operação (add/sub): ")
        num1 = input("Primeiro número binário: ")
        num2 = input("Segundo número binário: ")
        request = f"operation,{operation},{num1},{num2}"
    else:
        print("Opção inválida")
        return

    client.send(request.encode())
    response = client.recv(4096).decode()
    print(f"Resposta: {response}")
    client.close()

if __name__ == "__main__":
    main()

