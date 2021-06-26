# Deploying EC2 instance
import boto3
def create_instance():
ec2_client = boto3.client("ec2", region_name="us-east-1")
ec2.create_tags(Resources=[instance.id], Tags=[{'Key': 'Name','Value': myinstance1,}] # will provide the name to our EC2 instance
instances = ec2_client.run_instances(
ImageId="ami-0dbd8c88f9060cf71",
MinCount=10,
MaxCount=10,
InstanceType="t3.micro",
KeyName="ec2-key-pair")
print(instances["Instances"][0]["InstanceId"])

#Copy the instance id and save it for reference.
  
# creating s3 buckets
s3 = boto3.client('s3')
s3.create_bucket(Bucket='$Arsh-mys3bucket1')
s3.create_bucket(Bucket='$Arsh-mys3bucket2')
s3.create_bucket(Bucket='$Arsh-mys3bucket3')
s3.create_bucket(Bucket='$Arsh-mys3bucket4')
s3.create_bucket(Bucket='$Arsh-mys3bucket5')
s3.create_bucket(Bucket='$Arsh-mys3bucket6')
s3.create_bucket(Bucket='$Arsh-mys3bucket7')
s3.create_bucket(Bucket='$Arsh-mys3bucket8')
s3.create_bucket(Bucket='$Arsh-mys3bucket9')
s3.create_bucket(Bucket='$Arsh-mys3bucket10')
print("Buckets created succesfully")
 
