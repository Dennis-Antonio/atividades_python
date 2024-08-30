def incrementar_contador():
    global contador 
    contador += 1
    print(f"Contador atualizado: {contador}")
    
    mensagem = "Este é o valor atual do contador." 
    print(mensagem)  

incrementar_contador()

print(mensagem)