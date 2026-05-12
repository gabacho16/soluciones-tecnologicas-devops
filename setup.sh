#!/bin/bash

echo "Actualizando paquetes..."

sudo yum update -y

echo "Instalando dependencias esenciales..."

sudo yum install -y git vim docker python3

echo "Instalando pip para Python..."

sudo yum install -y python3-pip

echo "Instalando boto3..."

pip3 install boto3

echo "Iniciando Docker..."

sudo service docker start

echo "Agregando ec2-user al grupo docker..."

sudo usermod -aG docker ec2-user

echo "Verificando instalaciones..."

git --version
vim --version
docker --version
python3 --version
pip3 show boto3

echo "Configuración completada."
