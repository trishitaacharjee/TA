import boto3
print(boto3.Session().get_credentials())

sts = boto3.client("sts")
identity = sts.get_caller_identity()

print("AWS Identity Check Successful")
print(identity)
