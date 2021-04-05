import pandas as pd
import os

def spotonify_file(filepath, exp_time):
    data = pd.read_csv(filepath)
    columnNames = ['frame', 't', 'trajectory', 'x', 'y']
    for label in list(data):
        print(label)
        if label not in columnNames:
            data.drop(columns = [label], inplace = True)

    data['t'] = data['frame'] * exp_time
    data['y'] /= 10
    data['x'] /= 10
    data = data[columnNames]
    return data

def batch_process(inpath, outpath, exp_time):
    for filename in os.listdir(inpath):
        data = spotonify_file(inpath + filename, exp_time)
        data.to_csv(outpath + filename[:-4] + '_spoton.csv')
