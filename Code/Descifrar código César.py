def descifrar_codigo_cesar(texto_cifrado:str, corrimiento: int)->str:

    abecedario = "abcdefghijklmnopqrstuvwxyz"
    abecedario_mayusculas = abecedario.upper()
    texto_descifrado = ""

    corrimiento_en_cadena = 26 - corrimiento


    ordd = 0
    letra = ""

    for i in texto_cifrado:

        if i not in abecedario and i not in abecedario_mayusculas:
            texto_descifrado += i

        else:

            ordd = ord(i)
            letra = chr(ordd - corrimiento)

            if letra not in abecedario and letra not in abecedario_mayusculas:

                if i.isupper():

                    pos_letra_i = abecedario_mayusculas.find(i)
                    letra = abecedario_mayusculas[pos_letra_i+corrimiento_en_cadena]
                    texto_descifrado += letra     

                else:

                    pos_letra_i = abecedario.find(i)
                    letra = abecedario[pos_letra_i+corrimiento_en_cadena]
                    texto_descifrado += letra

            else:
                texto_descifrado += letra

    return texto_descifrado