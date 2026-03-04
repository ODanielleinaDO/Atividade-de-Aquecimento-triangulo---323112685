Usuario_A = {"Python", "Jogos", "Música", "IA"}
Usuario_B = {"Java", "IA", "Música", "Caminhada"}


em_comum = Usuario_A.intersection(Usuario_B)


sugestao_para_A = Usuario_B.difference(Usuario_A)

print("Interesses em comum:")
print(em_comum)

print("\nSugestões para o Usuário A:")
print(sugestao_para_A)

