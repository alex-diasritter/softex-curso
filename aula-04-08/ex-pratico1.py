password = input("\nDigite sua senha: ")
password2 = input("Digite sua senha novamente: ")

finalPassword = password == password2

print ("\nSenhas iguais!" if finalPassword == True else "\nSenhas diferentes.")

#-----------------------------------
age1 = input("\nDigite a sua idade: ")
age2 = input("\nDigite sua idade novamente: ")

age1Int = int(age1)
age2Int = int(age2)

finalAge = age1Int == age2Int

print ("\nIdades iguais!" if finalAge == True else "\nIdades diferentes.")
