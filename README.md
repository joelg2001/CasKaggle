# Pràctica Kaggle APC UAB 2021-22
### Nom: Joel Guevara Lopez
### DATASET: Smart Grid Stability
### URL: [kaggle] https://www.kaggle.com/pcbreviglieri/smart-grid-stability
## Resum
Aquest conjunt de dades correspon a una versió augmentada del "Conjunt de dades simulat d'estabilitat de la xarxa elèctrica", 
creat per Vadim Arzamasov (Karlsruher Institut für Technologie, Karlsruhe, Alemanya) i donat al Repositori d'aprenentatge 
automàtic de la Universitat de Califòrnia (UCI), on actualment està allotjat.

Tenim 60000 dades amb 14 atributs. Un d'ells, "stabf" és una variable categorica binaria. 
Les dades estan normalizades desde el origen.

### Objectius del dataset
Volem aconseguir classificar a partir dels atributs donats si una xarxa és estable o no, per fer-ho aplicarem models de classificació
sobre les dades previament obtingudes per poder predir si una futura xarxa serà estable o no.

## Experiments
Per poder aprendre el funcionament del dataset, ha sigut necessari primer realizar una matriu de correlacions per poder observar quines variables
poden ser les que ens ajudin a poder fer la classificaciò de les dades. També seria util fer un enferentament atribut contra atribut per poder observar
possibles outlayers o possibles transformacions a les dades.

Serà necessari provar si les posibles transformacions de les dades com PCAs sobre 2 variables, 3 o limitant la variancia de les dades ajudaria a poder
escollir un bon model.

Durant aquesta pràctica hem realitzat diferents experiments.

Totes aquestes proves poden ser observades en el notebook Preprocessing_Dataset.

### Preprocessat
Per fer el preprocessat s'ha aplicat primerament un label encoder per poder imposar la variable binaria en el atribut stabf. 

A continuació s'han eliminat dades que no aporten informació a la classificació a partir del us de un features selection automatizat
que decideix quines variables seràn les millors per poder fer la classificació. Els atributs escollits han sigut: g1, g2, g3, g4.

A banda, s'ha utilitzar un PCA en dues dimensions i un PCA amb una variancia limitada al 95%, per probar si aportaria un millor model.
Per els PCA també s'han observar correlacions amb la variable a classificar, i a traves d'aquestes es pot preedir que el PCA en 2 dimensions
pot ser una gran transoformacio i que la de la variancia no.



### Model
| Model | Hiperparametres | Mètrica | Temps |
| -- | -- | -- | -- |
| [Random Forest](link) | 100 Trees, XX | 57% | 100ms |
| Random Forest | 1000 Trees, XX | 58% | 1000ms |
| SVM | kernel: lineal C:10 | 58% | 200ms |
| -- | -- | -- | -- |
| [model de XXX](link al kaggle) | XXX | 58% | ?ms |
| [model de XXX](link al kaggle) | XXX | 62% | ?ms |
## Demo
Per tal de fer una prova, es pot fer servir amb la següent comanda
``` python3 demo/demo.py --input here ```
## Conclusions
El millor model que s'ha aconseguit ha estat...
En comparació amb l'estat de l'art i els altres treballs que hem analitzat....
## Idees per treballar en un futur
Crec que seria interesant indagar més en...
## Llicencia
El projecte s’ha desenvolupat sota llicència ZZZz.
