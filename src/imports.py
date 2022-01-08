# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:50:49 2022

@author: joelg
"""
import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import make_regression
import numpy as np
import time
import pandas as pd
#matplotlib notebook
from matplotlib import pyplot as plt
import scipy.stats
import math
import pickle
import seaborn as sns
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as sm1
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
#%matplotlib inline
from mpl_toolkits.mplot3d import axes3d, Axes3D
from sklearn import svm, datasets, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans
#%matplotlib widget
import sklearn
from sklearn.datasets import make_regression
from sklearn.metrics import f1_score, precision_recall_curve, average_precision_score, roc_curve, auc
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import RepeatedStratifiedKFold
from scipy.stats import loguniform
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.cluster import KMeans
from sklearn.metrics import completeness_score
pd.set_option('display.float_format', lambda x: '%.3f' % x)
