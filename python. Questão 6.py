convidados = ["Homem de Ferro", "Hulk", "Capitão America", "Homem Aranha", "Gavião Arqueiro"]

mensagem = "Prezado(a) %s, gostaríamos de convidá-lo(a) para um jantar em nossa casa."

for convidado in convidados:
    print(mensagem % convidado)

convidados_nao_poderao_ir = ["Capitão America", "Gavião Arqueiro"]

for convidado in convidados_nao_poderao_ir:
    print(f"{convidado} não poderá comparecer ao jantar.")

convidados[2] = "Homem Aranha."
convidados[4] = "Homem de Ferro"

print("Nova lista de convidados:")
for convidado in convidados:
    print(convidado)

for convidado in convidados:
    print(mensagem % convidado)