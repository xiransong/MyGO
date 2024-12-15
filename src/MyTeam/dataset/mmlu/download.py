from MyTeam.utils import ensure_dir
from MyTeam.dataset.mmlu.mmlu import download

import dataclasses
import tyro
import os.path as osp
 

@dataclasses.dataclass
class Args:
    """Args for download the MMLU dataset."""
    
    all_data_root: str = "/Users/xiransong/Code/MyTeam_Project/data"


def main():
    args = tyro.cli(Args)
    print(args)

    cache_dir = osp.join(args.all_data_root, "dataset/raw-mmlu")
    ensure_dir(cache_dir)
    download(cache_dir)


if __name__ == "__main__":
    main()
