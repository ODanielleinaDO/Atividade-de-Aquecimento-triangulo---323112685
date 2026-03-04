
RH = {"ver_salario", "editar_perfil"}
TI = {"acesso_servidor", "editar_perfil"}


cargo_rh = input("O funcionário é do RH? (s/n): ").lower()
cargo_ti = input("O funcionário é da TI? (s/n): ").lower()

permissoes_funcionario = set()

if cargo_rh == "s":
    permissoes_funcionario = permissoes_funcionario | RH

if cargo_ti == "s":
    permissoes_funcionario = permissoes_funcionario | TI

print("\nPermissões do funcionário:")
print(permissoes_funcionario)

permissoes_necessarias = {
    "ver_salario",
    "editar_perfil",
    "acesso_servidor"
}


if permissoes_necessarias.issubset(permissoes_funcionario):
    print("Usuário pode abrir o arquivo confidencial.")
else:
    print("Usuário NÃO pode abrir o arquivo confidencial.")