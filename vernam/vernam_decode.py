with open('bin_output.txt') as f:
    encrypted = f.read()

encrypted = list(encrypted)
encrypted = [ord(i) for i in encrypted]

for key in range(2, 21):
    shifted_text = []
    letters = {}
    
    for j in range(len(encrypted)-key):
        shifted_text.append(encrypted[j + key])
    
    shift_xor_encrypt = []
    for i in range(len(shifted_text)):
        shift_xor_encrypt.append(int(shifted_text[i]) ^ int(encrypted[i]))
    
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
    
length = int(input("Print the len of the key: "))
print(length)