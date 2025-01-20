import numpy as np
import pandas as pd
import os.path as osp


def download(dir):
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
        df.to_csv(osp.join(dir, key + ".csv"), index=True)


def instance_generation(
        raw_csv, instance_csv, 
        subject='all', num_samples=100, seed=1999):
    df = pd.read_csv(raw_csv, index_col=0)

    if subject != 'all':
        assert subject in df['subject'].unique(), "subject should be one of these: {}".format(df['subject'].unique())
        df = df.loc[df['subject'] == subject]
    
    if num_samples == -1:  # use all the samples (for the subject)
        pass
    else:
        idx = np.arange(len(df))
        np.random.seed(seed)
        np.random.shuffle(idx)
        df = df.loc[df.index[idx[:num_samples]]]

    df.to_csv(instance_csv, index=True)
    print(df)


class MMLU_Dataset:

    def __init__(self):
        pass


class MMLU_Evaluator:

    def __init__(self):
        pass
