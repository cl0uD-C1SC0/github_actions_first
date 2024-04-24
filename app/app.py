# Importações necessárias para o aplicativo Flask
from flask import Flask, jsonify, request
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger, swag_from
from flask_cors import CORS
import os, json
import subprocess


# Inicialização do aplicativo Flask
app = Flask(__name__)

# Configuração do CORS para permitir solicitações de todas as origens para determinados endpoints
CORS(app, resources={
    r"/awss/*": {"origins": "*"}
})

@app.route('/swagger.json')
def swagger_json():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "API Documentation"
    return jsonify(swag)


# Configuração da documentação Swagger UI
SWAGGER_URL = '/api/aws'  # URL para acessar a documentação Swagger
API_URL = '/static/swagger.json'  # URL onde sua API está disponível, que gera o JSON Swagger

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Documentation"
    }
)

# Registra a blueprint para a documentação Swagger
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Atualizar Nomes
def atualizar_nomes_tf(dados_variavel, diretorio):
    arquivo_variables_tf = os.path.join(diretorio, "variables.tf")
    with open(arquivo_variables_tf, 'r') as file:
        lines = file.readlines()

    variavel_existente = False
    for i, line in enumerate(lines):
        if line.strip().startswith(f'variable "{dados_variavel["nome"]}"'):
            variavel_existente = True
            # Encontrou a definição da variável, vamos verificar se o código existente está presente
            start_index = i
            end_index = None
            for j in range(i, len(lines)):
                if lines[j].strip() == '}':
                    end_index = j
                    break

            if end_index is not None:
                # O código existente está presente, vamos atualizar o valor padrão se necessário
                for k in range(i, end_index):
                    if lines[k].strip().startswith('default'):
                        lines[k] = f'  default     = "{dados_variavel["valor"]}"\n'
                        break
                else:
                    lines.insert(end_index, f'  default     = "{dados_variavel["valor"]}"\n')
            else:
                # Não foi encontrado o final da definição da variável, substituiremos toda a definição
                lines[i] = f'variable "{dados_variavel["nome"]}" {{\n'
                lines[i] += f'  description = "Descricao da variavel {dados_variavel["nome"]}"\n'
                lines[i] += f'  default     = "{dados_variavel["valor"]}"\n'
                lines[i] += '}\n'
            break

    if not variavel_existente:
        # Se a variável não existir, adicionamos uma nova entrada no final do arquivo
        nova_variavel = f'variable "{dados_variavel["nome"]}" {{\n'
        nova_variavel += f'  description = "Descricao da variavel {dados_variavel["nome"]}"\n'
        nova_variavel += f'  default     = "{dados_variavel["valor"]}"\n'
        nova_variavel += '}\n'
        # Adicionamos a nova variável apenas se não existir no arquivo
        lines.append(nova_variavel)

    with open(arquivo_variables_tf, 'w') as file:
        file.writelines(lines)

# Atualizar endereços
def atualizar_endereco_tf(dados_variavel, diretorio):
    arquivo_variables_tf = os.path.join(diretorio, "variables.tf")
    with open(arquivo_variables_tf, 'r') as file:
        lines = file.readlines()

    variavel_existente = False
    for i, line in enumerate(lines):
        if line.strip().startswith(f'variable "{dados_variavel["nome"]}"'):
            variavel_existente = True
            # Encontrou a definição da variável, vamos verificar se o código existente está presente
            start_index = i
            end_index = None
            for j in range(i, len(lines)):
                if lines[j].strip() == '}':
                    end_index = j
                    break

            if end_index is not None:
                # O código existente está presente, vamos atualizar o valor padrão se necessário
                for k in range(i, end_index):
                    if lines[k].strip().startswith('default'):
                        lines[k] = f'  default     = {dados_variavel["valor"]}\n'
                        break
                else:
                    lines.insert(end_index, f'  default     = "{dados_variavel["valor"]}"\n')
            else:
                # Não foi encontrado o final da definição da variável, substituiremos toda a definição
                lines[i] = f'variable "{dados_variavel["nome"]}" {{\n'
                lines[i] += f'  description = "Descricao da variavel {dados_variavel["nome"]}"\n'
                lines[i] += f'  default     = "{dados_variavel["valor"]}"\n'
                lines[i] += '}\n'
            break

    if not variavel_existente:
        # Se a variável não existir, adicionamos uma nova entrada no final do arquivo
        nova_variavel = f'variable "{dados_variavel["nome"]}" {{\n'
        nova_variavel += f'  description = "Descricao da variavel {dados_variavel["nome"]}"\n'
        nova_variavel += f'  default     = "{dados_variavel["valor"]}"\n'
        nova_variavel += '}\n'
        # Adicionamos a nova variável apenas se não existir no arquivo
        lines.append(nova_variavel)

    with open(arquivo_variables_tf, 'w') as file:
        file.writelines(lines)

# ----------------------------------------------------AWS-----------------------------------------------------------#
    
@app.route('/login', methods=['POST', 'OPTIONS'])
def fazer_login_aws():

    terraform_dir = './awss/'
    
    try:
        subprocess.run('terraform init', shell=True, cwd=terraform_dir)
        return jsonify({"message": "Login realizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao fazer login na AWS: {e}"}), 500
    
@app.route('/aws/vpc', methods=['POST'])
def criar_vpc():
    dados = request.json
    nome_vnet = dados['nome']
    endereco_usuario = dados['endereco']
    endereco_vnet = "\"" + endereco_usuario + "\""
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_vpc", "valor": nome_vnet}, terraform_dir)
    atualizar_endereco_tf({"nome": "endereco_vpc", "valor": endereco_vnet}, terraform_dir)
    
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_vpc.vpc'], cwd=terraform_dir, check=True)
        return jsonify({"message": "VPC criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar VPC: {e}"}), 500
    
# Função para criar Subrede Pública na AWS
@app.route('/aws/Subrede Pública', methods=['POST'])
def criar_subrede_publica_aws():
    dados = request.json
    nome_subrede_publica = dados['nome']
    endereco_subrede_publica = dados['endereco']
    endereco_subpub = "\"" + endereco_subrede_publica + "\""
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_subrede_publica_aws", "valor": nome_subrede_publica}, terraform_dir)
    atualizar_endereco_tf({"nome": "endereco_subrede_publica_aws", "valor": endereco_subpub}, terraform_dir)
    
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_subnet.Subrede_Publica'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Subrede Pública criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Subrede Pública: {e}"}), 500
    
    # Endpoint para criar uma Subrede Privada na AWS

@app.route('/aws/Subrede Privada', methods=['POST'])
def criar_subrede_privada_aws():
    dados = request.json
    nome_subrede_privada = dados['nome']
    endereco_subrede_privada = dados['endereco']
    endereco_subpri = "\"" + endereco_subrede_privada + "\""
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_subrede_privada_vpc", "valor": nome_subrede_privada}, terraform_dir)
    atualizar_endereco_tf({"nome": "endereco_subrede_privada_vpc", "valor": endereco_subpri}, terraform_dir)
    
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_subnet.Subrede_Privada'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Subrede Privada criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Subrede Privada: {e}"}), 500

# Função para criar Gateway de Internet na AWS
@app.route('/aws/Gateway', methods=['POST'])
def criar_gateway_internet_aws():
    dados = request.json
    nome_gateway = dados['nome']
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_gateway", "valor": nome_gateway}, terraform_dir)
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_internet_gateway.igw'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Gateway de Internet criado com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Gateway de Internet: {e}"}), 500

# Função para criar Tabela de Rotas na AWS
@app.route('/aws/Tabela de Rota', methods=['POST'])
def criar_tabela_rotas_aws():
    dados = request.json
    nome_tabela_rotas = dados['nome']
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_tabela_rotas", "valor": nome_tabela_rotas}, terraform_dir)

    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_route_table.public', '-target=aws_route_table_association.public'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Tabela de Rotas criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Tabela de Rotas: {e}"}), 500

# Função para criar Grupo de Segurança Linux na AWS
@app.route('/aws/Grupo de Segurança Linux', methods=['POST'])
def criar_grupo_seguranca_linux_aws():
    dados = request.json
    nome_grupo_seguranca_linux = dados['nome']
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_grupo_seguranca_linux_aws", "valor": nome_grupo_seguranca_linux}, terraform_dir)

    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_security_group.Grupo_de_Seguranca_LInux'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Grupo de Segurança criado com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Grupo de Segurança: {e}"}), 500

# Função para criar Grupo de Segurança Windows na AWS
@app.route('/aws/Grupo de Segurança Windows', methods=['POST'])
def criar_grupo_seguranca_windows_aws():
    dados = request.json
    nome_grupo_seguranca_windows = dados['nome']
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_grupo_seguranca_windows_aws", "valor": nome_grupo_seguranca_windows}, terraform_dir)

    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_security_group.Grupo_de_Seguranca_Windows'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Grupo de Segurança criado com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Grupo de Segurança: {e}"}), 500

# Função para criar instância EC2 Linux na AWS
@app.route('/aws/Máquina Virtual Windows', methods=['POST'])
def criar_instancia_ec2_windows_aws():
    dados = request.json
    nome_maquina_virtual_windows = dados['nome']
    nome_usuario_windows = dados ['usuario']
    senha_usuario_winodws = dados['senha']
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_maquina_virtual_windows_aws", "valor": nome_maquina_virtual_windows}, terraform_dir)
    atualizar_nomes_tf({"nome": "nome_usuario_windows_aws", "valor": nome_usuario_windows}, terraform_dir)
    atualizar_nomes_tf({"nome": "senha_usuario_windows_aws", "valor": senha_usuario_winodws}, terraform_dir)
    
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_instance.windows'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Instância EC2 Linux criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Instância EC2 Linux: {e}"}), 500

# Função para criar instância EC2 Windows na AWS
@app.route('/aws/Máquina Virtual Linux', methods=['POST'])
def criar_instancia_ec2_linux_aws():
    dados = request.json
    nome_maquina_virtual_linux = dados['nome']
    nome_usuario_linux = dados ['usuario']
    senha_usuario_linux = dados['senha']
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_maquina_virtual_linux_aws", "valor": nome_maquina_virtual_linux}, terraform_dir)
    atualizar_nomes_tf({"nome": "nome_usuario_linux_aws", "valor": nome_usuario_linux}, terraform_dir)
    atualizar_nomes_tf({"nome": "senha_usuario_linux_aws", "valor": senha_usuario_linux}, terraform_dir)
    
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_instance.linux'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Instância EC2 Windows criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Instância EC2 Windows: {e}"}), 500

# Criar Load Balancer AWS
@app.route('/aws/Load Balancer', methods=['POST'])
def criar_load_balancer_aws():
    dados = request.json
    nome_load_balancer = dados['nome']
    
    terraform_dir = './awss/'
    
    atualizar_nomes_tf({"nome": "nome_load_balancer_aws", "valor": nome_load_balancer}, terraform_dir)

    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', 
                        '-target=aws_lb.loadb',
                        '-target=aws_internet_gateway.igw',
                        '-target=aws_route_table_association.public',
                        '-target=aws_security_group.lb_sg',
                        '-target=aws_lb_target_group.grupo_de_destino',
                        '-target=aws_lb_listener.lb_listener',
                        '-target=aws_instance.Linuxlb',
                        '-target=aws_lb_target_group_attachment.grupo_target'
                        ], cwd=terraform_dir, check=True)
        print("LoadBalancer criado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar Load Balancer: {e}")

# Endpoint para destruir recursos na AWS
@app.route('/aws/destruir-recursos', methods=['POST'])
def destruir_recursos_aws():
    terraform_dir = './awss/'
    try:
        subprocess.run(['terraform', 'destroy', '-auto-approve'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Recursos na AWS destruídos com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao destruir recursos na AWS: {e}"}), 500

# Inicialização do servidor Flask
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, port=port, host='0.0.0.0')