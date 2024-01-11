from core import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("profile", help="The profile from .aws/credentials")
args = parser.parse_args()

s3 = get_s3(args.profile)

buckets = s3.list_buckets()["Buckets"]
for bucket in buckets:
    print(bucket["Name"])

