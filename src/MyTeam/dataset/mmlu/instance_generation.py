from MyTeam.utils import ensure_dir
from MyTeam.dataset.mmlu.mmlu import instance_generation

import dataclasses
import tyro
import os.path as osp
import pandas as pd
 

@dataclasses.dataclass
class Args:
    """Args for download the MMLU dataset."""
    
    all_data_root: str = "/Users/xiransong/Code/MyTeam_Project/data"

    raw_csv: str = "dev.csv"

    instance_name: str = "instance-mmlu"

    subject: str = "all"

    num_samples: int = 10

    seed: int = 1999


def main():
    args = tyro.cli(Args)
    print(args)

    instance_dir = osp.join(args.all_data_root, "dataset", args.instance_name)
    ensure_dir(instance_dir)
    instance_csv = osp.join(instance_dir, args.instance_name + ".csv")

    instance_generation(
        raw_csv=osp.join(args.all_data_root, "dataset/raw-mmlu", args.raw_csv), 
        instance_csv=instance_csv, 
        subject=args.subject, num_samples=args.num_samples, seed=args.seed
    )


if __name__ == "__main__":
    main()
