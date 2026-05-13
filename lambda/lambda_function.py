import json
import random

def lambda_handler(event, context):

    mensajes = [
        "Microservicio DevOps ejecutado correctamente",
        "AWS Lambda funcionando exitosamente",
        "Pipeline serverless completado",
        "Respuesta generada desde Lambda",
        "Proyecto DevOps desplegado correctamente"
    ]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "mensaje": random.choice(mensajes),
            "servicio": "microservicio-devops"
        })
    }
