#!/usr/bin/env python
# -*- coding: latin-1 -*-

# adaptaci�n del c�digo de Otabek Yorkinov
# https://www.datatechnotes.com/2020/07/classification-example-with-ridge-classifier-in-python.html

from sklearn.linear_model import RidgeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay 
from sklearn.model_selection import cross_val_score
import time
start_time = time.time()

#obteniendo los datos aleatorios
x, y = make_classification(n_samples=5000, n_features=10, 
                           n_classes=3, 
                           n_clusters_per_class=1)
#dividir entre train y test
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.15)

#entrenando
rc = RidgeClassifier()
RidgeClassifier(alpha=1.0, class_weight=None, copy_X=True, fit_intercept=True,
                max_iter=None, normalize=True, random_state=None, solver='auto',
                tol=0.001)
rc.fit(xtrain, ytrain)

#obteniendo el reporte
ypred = rc.predict(xtest) 
 
print(classification_report(ytest, ypred))

#matriz de confusi�n
cm = confusion_matrix(ytest, ypred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=rc.classes_)
disp.plot()
plt.savefig('matriz1.png')

tiempo=(time.time() - start_time)
print(f'Tiempo de proceso: {tiempo:.6f}')