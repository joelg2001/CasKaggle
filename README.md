# Pràctica Kaggle APC UAB 2021-22
### Nom: Joel Guevara Lopez
### DATASET: Smart Grid Stability
### URL: [kaggle] https://www.kaggle.com/pcbreviglieri/smart-grid-stability
## Resum
Aquest conjunt de dades correspon a una versió augmentada del "Conjunt de dades simulat d'estabilitat de la xarxa elèctrica",
creat per Vadim Arzamasov (Karlsruher Institut für Technologie, Karlsruhe, Alemanya) i donat al Repositori d'aprenentatge
automàtic de la Universitat de Califòrnia (UCI), on actualment està allotjat.

Tenim 60000 dades amb 14 atributs. Un d'ells, "stabf" és una variable categòrica binària.
Les dades estan normalitzades des de l'origen.

### Objectius del dataset
Volem aconseguir classificar a partir dels atributs donats si una xarxa és estable o no, per fer-ho aplicarem models de classificació
sobre les dades prèviament obtingudes per poder predir si una futura xarxa serà estable o no.

## Experiments
Per poder aprendre el funcionament del dataset, ha sigut necessari primer realitzar una matriu de correlacions per poder observar quines variables
poden ser les que ens ajudin a poder fer la classificació de les dades. També seria útil fer un enfrontament atribut contra atribut per poder analitzar
possibles outlayers o possibles transformacions a les dades.

Serà necessari provar si les possibles transformacions de les dades com PCAs sobre 2 variables, 3 o limitant la variància de les dades ajudaria a poder
escollir un bon model.

Durant aquesta pràctica hem realitzat diferents experiments.

Totes aquestes proves poden ser vistes en el notebook Preprocessing_Dataset.

### Preprocessat
Per fer el preprocessat s'ha aplicat primerament un label encoder per poder imposar la variable binària en l'atribut stabf.

A continuació s'han eliminat dades que no aporten informació a la classificació a partir de l'ús d'un features selection automatitzat
que decideix quines variables seran les millors per poder fer la classificació. Els atributs escollits han sigut: g1, g2, g3, g4.

A banda, s'ha utilitzat un PCA en dues dimensions i un PCA amb una variància limitada al 95%, per provar si aportaria un millor model.
Pels PCA també s'han observat correlacions amb la variable a classificar, i a través d'aquestes es pot predir que el PCA en 2 dimensions
pot ser una gran transformació i que la de la variància no.

### Recerca de hiperparametres aplicades.

| Model | Tipus de recerca | Prepocessing | Hiperparametres | Precisio | Temps |
| -- | -- | -- | -- | -- | -- |
| KNeighbors | Grid Search | Features selection | Leaf_size=1, p=1, n_neighbors=1 | 0.6717 | 20.418s |
| KNeighbors | Random Search | Features selection | Leaf_size=1, p=1, n_neighbors=1 | 0.672 | 20.156s |
| KNeighbors | Grid Search | PCA 2 dimensions | Leaf_size=1, p=1, n_neighbors=1 | 0.9996 | 20.149s |
| KNeighbors | Random Search | PCA 2 dimensions | Leaf_size=1, p=1, n_neighbors=1 | 0.9986 | 33.900s |
| KNeighbors | Grid Search | PCA 2 dimensions | Leaf_size=1, p=2, n_neighbors=1 | 0.9996 | 1535.434s |
| KNeighbors | Random Search | PCA 2 dimensions | Leaf_size=49, p=2, n_neighbors=1 | 0.9993 | 256.387s |
| Random Forest | Grid Search | Features selection | n_estimators=350, max_depth= None, Bootstrap=False | 0.7164 | 218.617s |
| Random Forest | Random Search | Features selection | n_estimators=1100, max_depth= None, Bootstrap=False | 0.7125 | 259.891s |
| Random Forest | Grid Search | Features selection | n_estimators=850, max_depth= None, Bootstrap=True | 0.7241 | 349.115s |
| Random Forest | Random Search | Features selection | n_estimators=600, max_depth= None, Bootstrap=True | 0.7249 | 337.977s |
| Random Forest | Grid Search | Features selection | n_estimators=600, max_depth= None, Bootstrap=True | 0.7233 | 1042.655s |
| Random Forest | Random Search | Features selection | n_estimators=850, max_depth= None, Bootstrap=True | 0.7256 | 1048.072s |

### Millors models
| Model | Prepocessing | Hiperparametres | Precisio | Temps |
| -- | -- | -- | -- | -- |
| KNeighbors | PCA 2 dimensions | Leaf_size=1, p=1, n_neighbors=1 | 0.9983 | 0.3695s |
| KNeighbors | PCA 2 dimensions | Leaf_size=1, p=1, n_neighbors=1 | 0.9993 | 0.3750s |
| KNeighbors | PCA 2 dimensions | Leaf_size=1, p=2, n_neighbors=1 | 0.9993 | 0.4339s |
| KNeighbors | PCA 2 dimensions | Leaf_size=49, p=2, n_neighbors=1 | 1.0 | 0.4019s |

## Demo
S'han creat dues petites demostracions que mostren com el programa troba els millors models en una mostra més petita, tot
fet des de un notebook autoexecutable.
(Codis: Demostration_Code_FDataset, Demostration_Code_PCA)

També s'adjunta un creador dels millors models de classificació considerats, ajuda a poder visualitzar el temps i aplicar-los.

## Conclusions
S'ha acabat aconseguint models de classificació pràcticament perfectes, sense realitzar overfitting en les dades.
Això és perquè probablement la classificació que es buscava estava calculada a partir d'alguna fórmula que tenia en consideració
els atributs donats.

El millor model per velocitat i precisió és KNeighbors amb PCA 2 dimensions i els atributs Leaf_size=1, p=2, n_neighbors=1.

## Idees per treballar en un futur

Es podria provar altres mètodes que no requereixin d'aplicar un PCA en dues dimensions per considerar un bon classificador. Aplicar
transformacions a les dades, recerques més profundes d'hiperparametres, aplicar models diferents...
