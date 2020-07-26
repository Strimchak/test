import boto3


def newinstance():
    print("Creating new instance\nInput instance parameters:")
    ImageId = input("ImageId: ")
    MinCount = input("MinCount: ")
    MaxCount = input("MaxCount: ")
    KeyName = input("KeyName: ")
    InstanceType = input("InstanceType: ")
    SG_id = input("SecurityGroupId: ")
    SubnetId = input("SubnetId: ")

    ec2 = boto3.resource("ec2", region_name="eu-north-1")
    print(ec2)
    ec2.create_instances(ImageId=ImageId, MaxCount=int(MaxCount), MinCount=int(
        MinCount), KeyName=KeyName, InstanceType=InstanceType, SecurityGroupIds=[SG_id], SubnetId=SubnetId)
    print("\n")


def deleteinstance():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            state = instance["State"]
            if state['Name'] == 'running':
                print(instance["InstanceId"])
    id = input("Input instance id to delete: ")
    response = ec2.terminate_instances(
        InstanceIds=[id])
    print("\n")


def showinstance():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            state = instance["State"]
            x = "None"
            if state['Name'] == 'running':
                x = instance["PublicIpAddress"]
            print(instance["InstanceId"], state['Name'], x)
    print("\n")
