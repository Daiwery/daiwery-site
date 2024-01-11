from core import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("profile", help="The profile from .aws/credentials")
parser.add_argument(
    "-bucket", default="",
    help="The name of the bucket (default: a single bucket is selected)"
)
args = parser.parse_args()

s3 = get_s3(args.profile)
args.bucket = get_bucket(s3, args.bucket)

for key in s3.list_objects(Bucket=args.bucket)["Contents"]:
    print(key["Key"])
