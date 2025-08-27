frase = input("Digite uma palavra: ")

codificada = frase.lower().replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")

print("\nFrase Codificada: " + codificada)

decodificada = frase.lower().replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u")

print("\nFrase Decodificada: " + decodificada)

