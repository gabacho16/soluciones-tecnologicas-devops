#!/bin/bash

echo "Creando usuario devops_user..."

sudo useradd devops_user

echo "Asignando contraseña al usuario..."

echo "devops_user:DevOps123!" | sudo chpasswd

echo "Creando grupo developers..."

sudo groupadd developers

echo "Agregando usuario al grupo developers..."

sudo usermod -aG developers devops_user

echo "Asignando permisos sobre el entorno..."

sudo chown -R devops_user:developers ~/environment

echo "Restaurando permisos para ec2-user..."

sudo chown -R ec2-user:ec2-user ~/environment

echo "Gestión de usuarios completada."
