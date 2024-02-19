import argparse
import joblib

from huggingface_hub import hf_hub_download


def download_model(repo_id):
    local_dir = repod_id.replace("/", "_").lower()
    hf_hub_download(repo_id=repo_id, local_dir=local_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('repo_id')
    args = parser.parse_args()
    download_model(args.repo_id)