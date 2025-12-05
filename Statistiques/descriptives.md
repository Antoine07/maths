# Cours de statistiques — Révision des notions de base

---

# 1. Population, échantillon, variable

### Population

Ensemble de tous les individus étudiés.
Exemple : tous les élèves d'un lycée.

### Échantillon

Sous-ensemble extrait de la population.
Exemple : 50 élèves choisis au hasard.

### Variable

Ce que l'on mesure :

* **Quantitative** : âge, taille, revenu.
* **Qualitative** : couleur, catégorie socio-pro, type d'habitation.

---

# 2. Série statistique et fréquences

Pour une variable quantitative, on manipule souvent :

* les **effectifs** : nombre d'individus ayant telle valeur ;
* les **fréquences** : proportion.

Exemple :
Taille (en cm) d'un groupe de 6 personnes :
168, 172, 172, 180, 165, 175.

Effectifs :

| Taille   | 165 | 168 | 172 | 175 | 180 |
| -------- | --- | --- | --- | --- | --- |
| Effectif | 1   | 1   | 2   | 1   | 1   |

Fréquence = effectif total/6.

---

# 3. Moyenne

La moyenne d'une série de valeurs $$(x_1,\dots,x_n)$$ est :

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^n x_i.
$$$

Exemple :

$$
168 + 172 + 172 + 180 + 165 + 175 = 1032.
$$$

$$
\bar{x} = \frac{1032}{6} = 172.
$$$

---

# 4. Médiane

La médiane est la valeur qui **partage l'échantillon en deux**.

Étapes :

1. ranger les valeurs dans l'ordre croissant.
2. si (n) est impair : médiane = valeur du milieu ;
3. si (n) est pair : moyenne des deux valeurs centrales.

Exemple (6 valeurs rangées) :

165, 168, 172, 172, 175, 180
Milieu entre 172 et 172 → médiane = 172.

---

# 5. Quartiles (rappel bref)

* (Q_1) : 25 % des données en dessous
* (Q_2) : médiane
* (Q_3) : 75 % en dessous

Ils servent à mesurer la répartition et construire les boîtes à moustaches.

---

# 6. Variance et écart-type

La variance mesure **la dispersion** autour de la moyenne.

$$
\mathrm{Var}(X)=\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2.
$$$

L'écart-type est la racine carrée de la variance :

$$
\sigma = \sqrt{\mathrm{Var}(X)}.
$$

### Exemple rapide

Données : 1, 3, 5.

Moyenne = 3.

$$
(1-3)^2 = 4,\quad (3-3)^2 = 0,\quad (5-3)^2 = 4.
$$$

$$
\text{Var} = \frac{4+0+4}{3} = \frac{8}{3}.
$$$

$$
\sigma = \sqrt{8/3}.
$$$

---

# 7. Covariance

La covariance mesure **comment deux variables évoluent ensemble**.

$$
\mathrm{Cov}(X,Y)=\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}).
$$$

Interprétation :

* positive → (X) et (Y) augmentent ensemble ;
* négative → quand (X) monte, (Y) descend ;
* proche de 0 → variables peu liées.

---

# 8. Corrélation

La corrélation est une version **normalisée** de la covariance :

$$
\rho = \frac{\mathrm{Cov}(X,Y)}{\sigma_X \sigma_Y}.
$$$

Elle est comprise entre -1 et 1 :

* $$\rho = 1$$ : tendance parfaitement croissante ;
* $$\rho = -1$$ : tendance parfaitement décroissante ;
* $$\rho = 0$$ : pas de relation linéaire.

---

# 9. Représentations graphiques utiles

* histogramme : répartition des valeurs
* nuage de points : relation entre deux variables
* boîte à moustaches : dispersion, quartiles
* courbe cumulative : proportion croissante

---

# 10. Exercices

## Exercice 1

On observe les âges suivants :
12, 15, 14, 13, 16, 15.

1. Calculer la moyenne.
2. Trouver la médiane.
3. Trouver l'écart-type.

---

## Exercice 2

Deux variables sont observées :

| X | 1 | 2 | 3 |
| - | - | - | - |
| Y | 2 | 4 | 5 |

1. Calculer la covariance.
2. Trouver la corrélation.

---

## Exercice 3

On a les tailles (cm) :
160, 170, 175, 150, 165.

1. Représenter les effectifs.
2. Calculer moyenne et écart-type.
3. Trouver le quartile (Q_1).

---

## Exercice 4

Donner une interprétation simple des valeurs de corrélation suivantes :

a) $$\rho = 0.92$$
b) $$\rho = -0.45$$
c) $$\rho = 0$$
