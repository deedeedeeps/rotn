def encrypt_rotx(PT):
    plain_text = PT.lower()
    number = int(input('input rot: '))
    text = "abcdefghijklmnopqrstuvwxyz"
    final = ""
    finalencrypted = ''
    rotation = text[number:] + text[:number]

    
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            final = rotation[text.index(plain_text[i])]
            finalencrypted += final
        else:
            finalencrypted += plain_text[i]
    print(finalencrypted)

def decrypt_rotx(ET):
    encrypted_text = ET.lower()
    number = int(input('input rot: '))
    text = "abcdefghijklmnopqrstuvwxyz"
    final = ""
    finaldecrypted = ''
    rotation = text[number:] + text[:number]

    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            final = text[rotation.index(encrypted_text[i])]
            finaldecrypted += final
        else:
            finaldecrypted += encrypted_text[i]
    print(finaldecrypted)
            
                       
