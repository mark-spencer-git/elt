import pandas as pd
from datetime import datetime
import os
import warnings
warnings.simplefilter("ignore")

def extract(file):
    # effective date reads file naming
    df = pd.read_excel(file)
    return df