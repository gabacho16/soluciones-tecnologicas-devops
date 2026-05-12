import boto3
from datetime import datetime, timedelta

REGION = "us-east-1"

ec2 = boto3.client("ec2", region_name=REGION)
cloudwatch = boto3.client("cloudwatch", region_name=REGION)
s3 = boto3.client("s3")
autoscaling = boto3.client("autoscaling", region_name=REGION)


def listar_instancias():
    print("\n===== INSTANCIAS EC2 =====")

    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            state = instance["State"]["Name"]

            print(f"ID: {instance_id}")
            print(f"Tipo: {instance_type}")
            print(f"Estado: {state}")
            print("-" * 40)


def reporte_cpu():
    print("\n===== REPORTE CPU EC2 =====")

    response = ec2.describe_instances()

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=24)

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]

            if state == "running":

                metrics = cloudwatch.get_metric_statistics(
                    Namespace="AWS/EC2",
                    MetricName="CPUUtilization",
                    Dimensions=[
                        {
                            "Name": "InstanceId",
                            "Value": instance_id
                        }
                    ],
                    StartTime=start_time,
                    EndTime=end_time,
                    Period=3600,
                    Statistics=["Average"]
                )

                datapoints = metrics["Datapoints"]

                print(f"\nInstancia: {instance_id}")

                if datapoints:
                    for data in datapoints:
                        timestamp = data["Timestamp"]
                        cpu = round(data["Average"], 2)

                        print(f"{timestamp} -> CPU Promedio: {cpu}%")
                else:
                    print("No hay métricas disponibles.")


def listar_buckets():
    print("\n===== BUCKETS S3 =====")

    response = s3.list_buckets()

    for bucket in response["Buckets"]:

        bucket_name = bucket["Name"]

        print(f"\nBucket: {bucket_name}")

        try:
            objects = s3.list_objects_v2(Bucket=bucket_name)

            if "Contents" in objects:
                for obj in objects["Contents"]:
                    print(f" - {obj['Key']}")
            else:
                print(" Bucket vacío")

        except Exception as e:
            print(f"Error accediendo al bucket: {e}")


def listar_autoscaling():
    print("\n===== AUTO SCALING GROUPS =====")

    response = autoscaling.describe_auto_scaling_groups()

    groups = response["AutoScalingGroups"]

    if groups:
        for group in groups:

            print(f"\nNombre: {group['AutoScalingGroupName']}")
            print(f"Min Size: {group['MinSize']}")
            print(f"Max Size: {group['MaxSize']}")
            print(f"Desired Capacity: {group['DesiredCapacity']}")
            print("-" * 40)

    else:
        print("No existen Auto Scaling Groups.")


if __name__ == "__main__":

    listar_instancias()
    reporte_cpu()
    listar_buckets()
    listar_autoscaling()
