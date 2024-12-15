import pandas as pd
import os.path as osp


def download(cache_dir):
    splits = {
        'test': 'all/test-00000-of-00001.parquet', 
        'validation': 'all/validation-00000-of-00001.parquet', 
        'dev': 'all/dev-00000-of-00001.parquet', 
        'auxiliary_train': 'all/auxiliary_train-00000-of-00001.parquet'
    }
    for key in splits:
        url = "hf://datasets/cais/mmlu/" + splits[key]
        print("download " + url)
        df = pd.read_parquet(url)
        df.to_csv(osp.join(cache_dir, key + ".csv"), index=False)


def instance_generation(df, num_sample):
    pass



class MMLU_Dataset:

    def __init__(self):
        pass


class MMLU_Evaluator:

    def __init__(self):
        pass
