from elt.configs.config import db, source, Connection
from elt.extract.extract import extract
from elt.load.load import load
from elt.transform.transform import transform
import pandas as pd
import os

def elt(file):
    print(file)
    con = Connection().con
    df = extract(file)
    load(con, df)
    transform(con)