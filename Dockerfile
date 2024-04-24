FROM ubuntu:22.04

# Atualizando pacotes
RUN apt update -y 

# Instalar Terraform
RUN apt-get install wget unzip curl -y

RUN wget https://releases.hashicorp.com/terraform/1.8.2/terraform_1.8.2_linux_amd64.zip

RUN unzip terraform_1.8.2_linux_amd64.zip

RUN mv terraform /usr/local/bin/

RUN terraform --version 

# Instalar o Python
RUN apt-get install python3.9 -y

RUN apt install python3-pip -y

# instalar awscli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install -i /usr/local/aws-cli -b /usr/local/bin

WORKDIR /work/
COPY app/ .

# Instalar os requisitos minimos (requirements.txt)
RUN python3 -m pip install -r requirements.txt

ENV AWS_ACCESS_KEY_ID="AKIAQ3EGRZIX3OWOGF44" 
ENV AWS_SECRET_ACCESS_KEY="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"
ENV AWS_DEFAULT_REGION="us-east-1"

# CORRETO:
# ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} 
# ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
# ENV AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}

RUN mkdir aws

RUN echo "[default]" >> aws/credentials
RUN echo "aws_access_key_id = $(echo $AWS_ACCESS_KEY_ID)" >> aws/credentials 
RUN echo "aws_secret_access_key = $(echo $AWS_SECRET_ACCESS_KEY)" >> aws/credentials


EXPOSE 8080

# Rodar a aplicação
CMD ["python3", "app.py"]