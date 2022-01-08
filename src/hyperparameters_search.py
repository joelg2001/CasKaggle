# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:29:33 2022

@author: joelg
"""
import sys
sys.path.insert(1, '../src')
from imports import *

def Hyperparam_search_KNC(X,y,n_splits,n_repeats,leaf_size,n_neighbors,p,search_type,name_save,algorithms=["auto"],weight=["uniform"]):
    x_t, x_v, y_t, y_v = train_test_split(X, y, train_size=0.7)
    cv = RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=n_repeats)
    hyperparameters = dict(leaf_size=leaf_size, n_neighbors=n_neighbors, p=p, algorithm=algorithms,weights=weight)
    knn_2 = KNeighborsClassifier()
    start_time = time.time()
    if (search_type=="Grid search"):
        clf = GridSearchCV(knn_2, hyperparameters, cv=cv,n_jobs=-1)
    else:
        clf = RandomizedSearchCV(knn_2, hyperparameters, n_iter=500, n_jobs=-1, cv=cv)
    best_model = clf.fit(x_t,y_t)
    pickle.dump(best_model, open(name_save, "wb"))
    print(search_type)
    print('Best leaf_size:', best_model.best_estimator_.get_params()['leaf_size'])
    print('Best p:', best_model.best_estimator_.get_params()['p'])
    print('Best n_neighbors:', best_model.best_estimator_.get_params()['n_neighbors'])
    print('Precision at best_score:',best_model.score(x_v,y_v))
    print("--- %s seconds ---" % (time.time() - start_time))
    
def Hyperparam_search_RF(X,y,n_splits,n_repeats,n_estimators,max_depth,min_samples_split,min_samples_leaf,bootstrap,search_type,name_save):
    x_t,x_v,y_t,y_v = train_test_split(X, y, test_size=0.7)
    cv = RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=n_repeats)
    hyperparameters = dict(n_estimators=n_estimators, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf,bootstrap=bootstrap)
    R_f=RandomForestClassifier()
    start_time = time.time()
    if (search_type=="Grid search"):
        clf = GridSearchCV(R_f, hyperparameters,n_jobs=-1, cv=cv)
    else:
        clf = RandomizedSearchCV(R_f, hyperparameters, n_iter=80, n_jobs=-1, cv=cv)
    best_model = clf.fit(x_t,y_t)
    pickle.dump(best_model, open(name_save, "wb"))
    print(search_type)
    print('Best leaf_size:', best_model.best_estimator_.get_params()['leaf_size'])
    print('Best p:', best_model.best_estimator_.get_params()['p'])
    print('Best n_neighbors:', best_model.best_estimator_.get_params()['n_neighbors'])
    print('Precision at best_score:',best_model.score(x_v,y_v))
    print("--- %s seconds ---" % (time.time() - start_time))

