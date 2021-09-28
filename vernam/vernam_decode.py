from string import ascii_letters

with open('bin_output.txt') as f:
    encrypted = f.read()

encrypted = list(encrypted)
encrypted_ord = [ord(i) for i in encrypted]

for key in range(1, 21):
    shifted_text = []
    letters = {}
    
    for j in range(len(encrypted_ord)-key):
        shifted_text.append(encrypted_ord[j + key])
    
    shift_xor_encrypt = []
    for i in range(len(shifted_text)):
        shift_xor_encrypt.append(int(shifted_text[i]) ^ int(encrypted_ord[i]))
    
    unique_letters = []
    for i in range(len(shift_xor_encrypt)):
        if shift_xor_encrypt not in unique_letters:
            unique_letters.append(shift_xor_encrypt[i])

    sum = 0
    for i in range(len(unique_letters)):
        letters[unique_letters[i]] = shift_xor_encrypt.count(unique_letters[i])
        a = shift_xor_encrypt.count(unique_letters[i])
        sum += (a * (a-1))/2
    
    maybe_values = sum / len(shifted_text)
    print(maybe_values)
    
lenght = int(input("Print the len of the key: "))

#letters in the text but mod key
mod_keys = {}
test_keys = {}
for i in range(lenght):
    mod_keys[i] = []
    test_keys[i] = []


#раскидал буквы по длине одинаковым символам ключа 
for i in range(len(encrypted)):
    mod_keys[i%lenght].append(encrypted_ord[i])   

key = []

#для каждого ключа
for k in mod_keys.keys():
    #для каждой буквы
    for i in ascii_letters:
        #для каждого значения списка в ключа
        for j in range(len(mod_keys[k])):
            if mod_keys[k][j] ^ ord(i) < 13 or mod_keys[k][j] >32:
                test_keys[k].append(mod_keys[k][j] ^ ord(i))
                key.append(i)
            else:
                key.remove(i)
                break


print(key)