provider "aws" {
 region = "us-east-1"
 shared_config_files=["./aws/config"]
 shared_credentials_files=["./aws/config"]
}

resource "aws_instance" "ec2_instance" {
  ami           = "ami-07caf09b362be10b8"
  instance_type = "t2.micro"
  subnet_id     = "<subnet_id>" # ID da Subnet
  vpc_security_group_ids = ["${aws_security_group.instance_sg.id}"]

  key_name = "vockey"

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker
              service docker start
              usermod -a -G docker ec2-user
              docker push <substituir_aqui>/apicontainer:${var.github_sha}
              docker run -d -p 8080:8080 --name api-container <substituir_aqui>/apicontainer:${var.github_sha}
              EOF

  tags = {
    Name = "EC2_Instance-alpine-5"
  }
}

resource "aws_security_group" "instance_sg" {
  name        = "instance_sg-5"
  description = "Allow SSH and HTTP inbound traffic"
  vpc_id      = "<vpc-id>"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

variable "github_sha" {}

output "public_ip" {
  value = aws_instance.ec2_instance.public_ip
}
