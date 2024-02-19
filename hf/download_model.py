import argparse
from huggingface_hub import snapshot_download 

def download_model(repo_id):
    local_dir = repo_id.replace("/", "_").lower()
    snapshot_download(repo_id=repo_id, local_dir=local_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('repo_id')
    args = parser.parse_args()
    download_model(args.repo_id)
