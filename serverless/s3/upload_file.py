from core import *
import argparse
import mimetypes

parser = argparse.ArgumentParser()
parser.add_argument("profile", help="The profile from .aws/credentials")
parser.add_argument(
    "-bucket", default="",
    help="The name of the bucket (default: a single bucket is selected)"
)
parser.add_argument("path", help="Path to file")
parser.add_argument("key", help="The key")
args = parser.parse_args()

s3 = get_s3(args.profile)
args.bucket = get_bucket(s3, args.bucket)

content_type = mimetypes.guess_type(args.key)[0]
s3.upload_file(args.path, args.bucket, args.key, ExtraArgs={"ContentType": content_type})
