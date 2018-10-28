import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# bring in the six packs
df_train = pd.read_csv('./../dataset/train.csv')
# check the decoration
df_train.columns
