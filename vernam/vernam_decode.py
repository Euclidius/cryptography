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


one_letter_enc = []
for i in range(0, len(encrypted_ord)//lenght, lenght):
    
    one_letter_enc.append(encrypted[i])

print(letters)