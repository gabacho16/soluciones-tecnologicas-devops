import boto3
import time

dynamodb = boto3.resource('dynamodb')

table_name = 'devops-tabla'

# Crear tabla
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

print("Creando tabla DynamoDB...")

table.wait_until_exists()

print("Tabla creada correctamente")

# Insertar registro
table.put_item(
    Item={
        'id': '1',
        'nombre': 'ServidorDevOps',
        'status': 'activo'
    }
)

print("Registro insertado correctamente")

# Modificar status
table.update_item(
    Key={
        'id': '1'
    },
    UpdateExpression='SET #st = :nuevo_estado',
    ExpressionAttributeNames={
        '#st': 'status'
    },
    ExpressionAttributeValues={
        ':nuevo_estado': 'inactivo'
    }
)

print("Registro actualizado correctamente")

# Eliminar registro
table.delete_item(
    Key={
        'id': '1'
    }
)

print("Registro eliminado correctamente")
