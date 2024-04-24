# MENU

#-------------------------------AWS-------------------------------#

   
# Criar VPC na AWS:
# Método: POST
# Endpoint: /aws/vpc
# Corpo da Requisição (JSON):
{
    "nome": "nome_vpc",
    "endereco": "endereco_vpc"
}
# Criar Subrede Privada na AWS:
# Método: POST
# Endpoint: /aws/Subrede Privada
# Corpo da Requisição (JSON):
{
    "nome": "nome_subrede_privada",
    "endereco": "endereco_subrede_privada"
}
# Criar Subrede Pública na AWS:
# Método: POST
# Endpoint: /aws/Subrede Pública
# Corpo da Requisição (JSON):
{
    "nome": "nome_subrede_publica",
    "endereco": "endereco_subrede_publica"
}
# Criar Gateway de Internet na AWS:
# Método: POST
# Endpoint: /aws/Gateway
# Corpo da Requisição (JSON):
{
    "nome": "nome_gateway"
}
# Criar Tabela de Rota na AWS:
# Método: POST
# Endpoint: /aws/Tabela de Rota
# Corpo da Requisição (JSON):
{
    "nome": "nome_tabela_rotas"
}
# Criar Grupo de Segurança Linux na AWS:
# Método: POST
# Endpoint: /aws/Grupo de Segurança Linux
# Corpo da Requisição (JSON):
{
    "nome": "nome_grupo_seguranca_linux"
}
# Criar Grupo de Segurança Windows na AWS:
# Método: POST
# Endpoint: /aws/Grupo de Segurança Windows
# Corpo da Requisição (JSON):
{
    "nome": "nome_grupo_seguranca_windows"
}
# Criar Instância EC2 Linux na AWS:
# Método: POST
# Endpoint: /aws/Máquina Virtual Windows
# Corpo da Requisição (JSON):
{
    "nome": "nome_maquina_virtual_windows",
    "usuario": "nome_usuario_windows",
    "senha": "senha_usuario_windows"
}
# Criar Instância EC2 Windows na AWS:
# Método: POST
# Endpoint: /aws/Máquina Virtual Linux
# Corpo da Requisição (JSON):
{
    "nome": "nome_maquina_virtual_linux",
    "usuario": "nome_usuario_linux",
    "senha": "senha_usuario_linux"
}
# Criar Balanceador de Carga na AWS:
# Método: POST
# Endpoint: /aws/Load Balancer
# Corpo da Requisição (JSON):
{
    "nome": "nome_balanceador_carga"
}
# Destruir Recursos na AWS:
# Método: POST
# Endpoint: /aws/Destruir Recursos
# Somente Rodar com o Endpoint