#TODO read about Spec cypher

def get_masterkey(key:str) -> list:
    masterkey = []
    for i in range((len(message)//len(key))+1):
        masterkey += key
    return masterkey

def vernam_encrypt(message:list, masterkey:list) -> list:
    cypher_text = []
    for i in range(len(message)):
        cypher_text.append(masterkey[i] ^ message[i])
    return cypher_text

def vernam_decrypt(cypher_text:list, masterkey:list) -> list:
    plain_text = []
    for i in range(len(cypher_text)):
        plain_text.append(masterkey[i] ^ cypher_text[i])
    return plain_text


if __name__ == '__main__':  
    with open('input.txt') as f:
        message = f.read()

    key = input('Insert the masterkey: ')
    while len(key) < 2:
        key = input('Please, insert the more long masterkey: ')

    masterkey = get_masterkey(key)
    masterkey = [ord(i) for i in masterkey]

    message = list(message)
    message = [ord(i) for i in message]

    cypher_text = vernam_encrypt(message, masterkey)

    with open('bin_output.txt', 'w') as f:
        for i in range(len(cypher_text)):
            f.write(chr(cypher_text[i]))


    plain_text = vernam_decrypt(cypher_text, masterkey)

    with open('output.txt', 'w') as f:
        for i in range(len(plain_text)):
            f.write(chr(plain_text[i]))
