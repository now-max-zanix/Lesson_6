import random

def write_to_file(data):
    with open("./text.txt","wb") as f:
        f.write(data)
    
def read_from_file():
    try:
        with open("./text.txt", "rb") as f:
            data = f.read()
            return data
    except FileNotFoundError:
        print("<Not found file>")

def xor_encryption():
    message = input("Введите сообщение (Enter - чтение из файла):")
    key = input("\nВведите ключ (Enter - ключ сгенерируется автоматически):")

    if not message:
        message = read_from_file()

    if not key:
        key = "".join(
            random.choice(
                "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            )
            for i in range(random.randint(1, len(message)))
        )
        print(f"Ключ сгененрировался:\n{key}")

    result = bytearray()
    if type(message) == str:
        message = bytearray(message, "utf-8")
    key = bytearray(key, "utf-8")

    for i in range(len(message)):
        result.append(message[i] ^ key[i % len(key)])
    write_to_file(result)
xor_encryption()

