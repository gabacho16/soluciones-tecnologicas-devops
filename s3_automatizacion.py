import boto3
from datetime import datetime

s3 = boto3.client('s3')

bucket_name = 'devops-bucket-126765947646'

# Crear archivo local
file_name = 'archivo_prueba.txt'

with open(file_name, 'w') as file:
    file.write('Archivo de prueba para automatizacion S3')

print("Archivo local creado correctamente")

# Subir archivo al bucket
s3.upload_file(
    file_name,
    bucket_name,
    f'pruebas/{file_name}'
)

print("Archivo subido a S3 correctamente")

# Listar objetos del bucket
response = s3.list_objects_v2(Bucket=bucket_name)

print("\nObjetos en el bucket:\n")

if 'Contents' in response:
    for obj in response['Contents']:
        print(f"Nombre: {obj['Key']}")
        print(f"Tamaño: {obj['Size']} bytes")
        print(f"Última modificación: {obj['LastModified']}")
        print("-" * 40)
else:
    print("El bucket está vacío")
