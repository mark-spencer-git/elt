import pandas as pd
import warnings
warnings.simplefilter("ignore")

def extract(file):
    # effective date reads file naming
    df = pd.read_excel(file)
    return df