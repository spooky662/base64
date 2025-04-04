# Tabela Base64
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
 
def base64_encode(data):
    # Se a entrada for string, converte para bytes
    if isinstance(data, str):
        data = data.encode('ascii')
    
    encoded = []
    padding = 0
    
    # Processa os dados em blocos de 3 bytes
    for i in range(0, len(data), 3):
        chunk = data[i:i+3]
        
        # Verifica se precisa de padding
        if len(chunk) < 3:
            padding = 3 - len(chunk)
            chunk += b'\x00' * padding  # Adiciona bytes nulos para completar
        
        # Converte os 3 bytes em um número de 24 bits
        value = (chunk[0] << 16) | (chunk[1] << 8) | chunk[2]
        
        # Divide em 4 grupos de 6 bits
        for j in range(4):
            # Pega os 6 bits mais significativos
            index = (value >> (18 - j * 6)) & 0x3F
            encoded.append(BASE64_CHARS[index])
    
    # Adiciona padding se necessário
    if padding > 0:
        encoded[-padding:] = ['='] * padding
    
    return ''.join(encoded)
 
# Exemplos de uso
print(base64_encode("Man"))  # Deve retornar "TWFu"
print(base64_encode("Ma"))   # Deve retornar "TWE="
print(base64_encode("M"))    # Deve retornar "TQ=="
print(base64_encode("Hello World!"))  # Deve retornar "SGVsbG8gV29ybGQh"
