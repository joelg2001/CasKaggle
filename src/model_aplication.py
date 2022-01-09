# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 13:07:13 2022

@author: joelg
"""
import sys
sys.path.insert(1, '../src')
from imports import *

def apply_models(particions,X,y,ret=False):
    for part in particions:
        x_t, x_v, y_t, y_v = train_test_split(X, y, train_size=part)

        #Creem el regresor logístic
        logireg = LogisticRegression(C=2.0, fit_intercept=True, penalty='l2', tol=0.001)

        # l'entrenem
        logireg.fit(x_t, y_t)
        problr = logireg.predict_proba(x_v)
        print ("Correct classification Logistic        ", part, "% of the data: ", logireg.score(x_v, y_v))

        #Creem el svm
        svc = svm.SVC(C=10.0, kernel='rbf', gamma=0.9, probability=True)

        # l'entrenem 
        svc.fit(x_t, y_t)
        probsvc = svc.predict_proba(x_v)
        print ("Correct classification SVM             ", part, "% of the data: ", svc.score(x_v, y_v))

        #Creem el svm lineal
        svcl = svm.SVC(C=10.0, kernel='linear', gamma=0.9, probability=True)

        # l'entrenem 
        svcl.fit(x_t, y_t)
        probsvcl = svcl.predict_proba(x_v)
        print ("Correct classification SVML            ", part, "% of the data: ", svcl.score(x_v, y_v))

        #Creem el svm poly deg=3
        svcp = svm.SVC(C=10.0, kernel='poly', gamma=0.9, probability=True)

        # l'entrenem 
        svcp.fit(x_t, y_t)
        probsvcp = svcp.predict_proba(x_v)
        print ("Correct classification SVMP deg3       ", part, "% of the data: ", svcp.score(x_v, y_v))

        #Creem el svm poly deg=2
        svcp2 = svm.SVC(C=10.0, kernel='poly', degree=2, gamma=0.9, probability=True)

        # l'entrenem 
        svcp2.fit(x_t, y_t)
        probsvcp2 = svcp2.predict_proba(x_v)
        print ("Correct classification SVMP deg2       ", part, "% of the data: ", svcp2.score(x_v, y_v))


        #Creem el svm sigmoid
        svcs= svm.SVC(C=10.0, kernel='sigmoid', gamma=0.9, probability=True)

        # l'entrenem 
        svcs.fit(x_t, y_t)
        probsvcs = svcs.predict_proba(x_v)
        print ("Correct classification SVMS            ", part, "% of the data: ", svcs.score(x_v, y_v))

        #####

        #random forests gini

        clf = RandomForestClassifier(max_depth=2, random_state=0)
        clf.fit(x_t, y_t)
        probclf = clf.predict_proba(x_v)
        print ("Correct classification RFC             ", part, "% of the data: ", clf.score(x_v, y_v))

        #random forests entropy with n_e=1000 and md=5

        clfe = RandomForestClassifier(n_estimators=1000, max_depth=5, random_state=0,criterion="entropy")
        clfe.fit(x_t, y_t)
        probclfe = clfe.predict_proba(x_v)
        print ("Correct classification RFC etpy        ", part, "% of the data: ", clfe.score(x_v, y_v))

        #####

        #KNN ball_tree

        KNNbt = KNeighborsClassifier(n_neighbors=3,algorithm="ball_tree")
        KNNbt.fit(x_t, y_t)
        probKNNbt = KNNbt.predict_proba(x_v)
        print ("Correct classification KNN BT          ", part, "% of the data: ", KNNbt.score(x_v, y_v))

        #KNN kd_tree

        KNNkd = KNeighborsClassifier(n_neighbors=3,algorithm="kd_tree")
        KNNkd.fit(x_t, y_t)
        probKNNkd = KNNkd.predict_proba(x_v)
        print ("Correct classification KNN KD          ", part, "% of the data: ", KNNkd.score(x_v, y_v))

        #KNN brute

        KNNbrt = KNeighborsClassifier(n_neighbors=3,algorithm="brute")
        KNNbrt.fit(x_t, y_t)
        probKNNbrt = KNNbrt.predict_proba(x_v)
        print ("Correct classification KNN BRT         ", part, "% of the data: ", KNNbrt.score(x_v, y_v))

        #####

        #KNN ball_tree weights = distance

        KNNbtwd = KNeighborsClassifier(n_neighbors=3,algorithm="ball_tree",weights="distance")
        KNNbtwd.fit(x_t, y_t)
        probKNNbtwd = KNNbtwd.predict_proba(x_v)
        print ("Correct classification KNN BT wd=d     ", part, "% of the data: ", KNNbtwd.score(x_v, y_v))

        #KNN kd_tree weights = distance

        KNNkdwd = KNeighborsClassifier(n_neighbors=3,algorithm="kd_tree",weights="distance")
        KNNkdwd.fit(x_t, y_t)
        probKNNkdwd = KNNkdwd.predict_proba(x_v)
        print ("Correct classification KNN KD wd=d     ", part, "% of the data: ", KNNkdwd.score(x_v, y_v))

        #KNN brute weights = distance

        KNNbrtwd = KNeighborsClassifier(n_neighbors=3,algorithm="brute",weights="distance")
        KNNbrtwd.fit(x_t, y_t)
        probKNNbrtwd = KNNbrtwd.predict_proba(x_v)
        print ("Correct classification KNN BRT wd=d    ", part, "% of the data: ", KNNbrtwd.score(x_v, y_v))    
        
        print("\n")
    if ret:
        return[problr,probsvc,probsvcl,probsvcp,probsvcp2,probsvcs,probclf,probclfe,probKNNbt,probKNNkd,probKNNbrt,probKNNbtwd,probKNNkdwd,probKNNbrtwd],x_t, x_v, y_t, y_v