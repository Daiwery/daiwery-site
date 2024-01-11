SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
alias list_buckets="python3 $SCRIPT_DIR/list_buckets.py"
alias list_objects="python3 $SCRIPT_DIR/list_objects.py"
alias download="python3 $SCRIPT_DIR/download.py"
alias sync="python3 $SCRIPT_DIR/sync.py"
alias upload_file="python3 $SCRIPT_DIR/upload_file.py"