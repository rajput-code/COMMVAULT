import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Create an EC2 instance
response = ec2.run_instances(
    ImageId='ami-051f7e7f6c2f40dc1',  
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='harsh',  
    SecurityGroupIds=['sg-0406ef29c0b4a5ae4'],  # Replace with your security group ID
)

# Wait for the instance to be running
instance_id = response['Instances'][0]['InstanceId']
waiter = ec2.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])

public_ip = '34.197.28.120'  # Replace with your Elastic IP address
ec2.associate_address(InstanceId=instance_id, PublicIp=public_ip)

s3 = boto3.client('s3', region_name='us-east-1')  # Replace 'us-east-1' with your preferred region

# Specify the bucket name (must be globally unique within the specified region)
bucket_name = 'bucket-198'

# Create the S3 bucket
s3.create_bucket(Bucket=bucket_name)