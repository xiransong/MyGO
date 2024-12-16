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

    print("hello world!")

    # parse config

    # init dataset
    
    # init agents and team


    # inference

    # evaluation



if __name__ == "__main__":
    main()
