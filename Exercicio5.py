n1=int(input("Digite um número: ")) 
n2=int(input("Digite outro número: "))
operacao=input("Digite qual será a operação matemática: ")

if operacao == "+":
	print(n1 , "+" , n2 , "=" , n1+n2)
elif operacao == "-":
	print(n1 , "-" , n2 , "=" , n1-n2)
elif operacao == "*":
	print(n1 , "*" , n2 , "=" , n1*n2)
elif operacao == "/":
	print(n1 , "/" , n2 , "=" , n1/n2)
elif operacao == "**":
	print(n1 , "**" , n2 , "=" , n1**n2)
else :
	print("Operação Inválida")


