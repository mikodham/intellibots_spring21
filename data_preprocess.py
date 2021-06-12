# import pandas as pd
import numpy as np
import csv
import pathlib
import os
import pprint

FILENAME = "master_data.csv"
with open(os.path.join(os.getcwd(), "Dataset", FILENAME), 'r', newline='') as f:
    # spamreader = csv.reader(f, delimiter=' ', quotechar='|')
    lis = [line.split('|') for line in f]
    pprint.pprint(lis)
    #  thewriter = csv.writer(f)
    #  thewriter.writerow(['sentences','#of heteronyms','#of different heteronyms','#heteronyms with different pos','source-site'])
