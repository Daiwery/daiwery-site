from core import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("profile", help="The profile from .aws/credentials")
parser.add_argument(
    "-bucket", default="",
    help="The name of the bucket (default: a single bucket is selected)"
)
parser.add_argument("path", help="Path to file")
parser.add_argument("key", help="The key (auto adds the file name if key like a dir-path)")
args = parser.parse_args()

if os.path.basename(args.key) == "":
    args.key = os.path.join(args.key, args.path)

s3 = get_s3(args.profile)
args.bucket = get_bucket(s3, args.bucket)

s3.upload_file(args.path, args.bucket, args.key, Callback=ProgressUploadPercentage(args.path))
print()
