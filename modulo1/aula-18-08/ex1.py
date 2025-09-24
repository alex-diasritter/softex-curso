lanche = 15
cod = "123"
nomeProd = "lanche"
precoFinal = 0

while True:
        prod = input("Nome do produto: ")
        if nomeProd == prod:
            break
        print("Produto não encontrado, tente novamente.")

codClient = input("Código de desconto: ")
if codClient == cod:
    print("Cupom com desconto aceito")
    precoFinal = lanche * 0.9
    print(f"Preço final: {precoFinal}")  
else:
    print("Cupom inexistente, preço final R$15,99")
        
        
