# Exibir IP público maquina Linux
output "IP_Publico_Linux" {
 description = "IP Publico da Instancia EC2 linux"
 value       = aws_instance.linux.public_ip
}

# Exibir IP público maquina Windows
output "IP_Publico_Windows" {
 description = "IP Publico da Instancia EC2 linux"
 value       = aws_instance.windows.public_ip
}