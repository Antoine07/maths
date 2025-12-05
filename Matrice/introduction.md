# **Matrices, vecteurs, transformations et vecteurs propres**

---

## I. Vecteurs et matrices

### 1. Vecteurs

Un vecteur est un ensemble ordonné de nombres.

$$
x =
\begin{pmatrix}
2\\
-1
\end{pmatrix}
$$

Il représente une direction et une intensité dans l'espace.

### 2. Matrices

Une matrice est un tableau de nombres.

$$
A=
\begin{pmatrix}
1 & 3\\
2 & -1
\end{pmatrix}
$$

Elle représente une transformation linéaire : elle prend un vecteur en entrée et produit un nouveau vecteur.

---

## II. Multiplication matrice–vecteur

Pour une matrice (A) et un vecteur (x), le produit (Ax) est défini par :

$$
Ax=
\begin{pmatrix}
a_{11}x_1 + a_{12}x_2 \\
a_{21}x_1 + a_{22}x_2
\end{pmatrix}
$$

Exemple :

$$
A=
\begin{pmatrix}
1 & 2\\
3 & 1
\end{pmatrix},
\quad
x=
\begin{pmatrix}
2\\
1
\end{pmatrix}
$$

d'où :

$$
Ax=
\begin{pmatrix}
1\cdot 2 + 2\cdot 1 \\
3\cdot 2 + 1\cdot 1
\end{pmatrix}
=
\begin{pmatrix}
4 \\
7
\end{pmatrix}
$$

Interprétation : la matrice transforme le vecteur en l'étirant, le tournant ou le comprimant.


## III. Transformations linéaires

Une matrice carrée représente une transformation linéaire de l'espace vers lui-même.

Voici les transformations fondamentales.

### 1. Étirement

$$
A=
\begin{pmatrix}
3 & 0\\
0 & 1
\end{pmatrix}
$$

Multiplie la coordonnée (x) par 3, laisse (y) inchangé.

### 2. Compression

$$
A=
\begin{pmatrix}
0.5 & 0\\
0 & 0.5
\end{pmatrix}
$$

Réduit toutes les directions d'un facteur 2.

### 3. Réflexion (symétrie)

$$
A=
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix}
$$

Symétrie par rapport à l'axe (x).

### 4. Cisaillement (shear)

$$
A=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}
$$

Incline les vecteurs vers la droite.

### 5. Rotation

$$
A=
\begin{pmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{pmatrix}
$$

Rotation de tout l'espace d'un angle (\theta).

---

## IV. Matrices particulières : matrices symétriques

Une matrice est symétrique si :

$$
A = A^T,
$$
c'est-à-dire :
$$
a_{ij} = a_{ji}
$$

Exemple :

$$
S=
\begin{pmatrix}
2 & 1\\
1 & 3
\end{pmatrix}
$$

Les matrices symétriques possèdent des propriétés géométriques fortes, notamment l'existence de vecteurs propres orthogonaux.

---

## V. Vecteurs propres et valeurs propres

### 1. Définition

Pour une matrice carrée (A), un vecteur non nul (v) est un vecteur propre s'il existe un réel $$\lambda$$ tel que :

$$
A v = \lambda v
$$

* (v) est une direction préservée,
* $$\lambda$$ est le facteur d'étirement dans cette direction.

### 2. Exemple simple

$$
A=
\begin{pmatrix}
3 & 0\\
0 & 2
\end{pmatrix}.
$$

Alors :

$$
A
\begin{pmatrix}
1\\
0
\end{pmatrix}
=
\begin{pmatrix}
3\\
0
\end{pmatrix}
= 3
\begin{pmatrix}
1\\
0
\end{pmatrix}
$$

Donc $$(1,0)^T$$ est un vecteur propre, valeur propre $$\lambda = 3$$.

De même :

$$
A
\begin{pmatrix}
0\\
1
\end{pmatrix}
=
2
\begin{pmatrix}
0\\
1
\end{pmatrix}
$$

### 3. Interprétation géométrique

Une matrice possède généralement plusieurs directions privilégiées : ses vecteurs propres.
Ce sont les directions où la transformation agit de manière la plus simple.

Si l'on observe deux données comme la taille et le poids, les vecteurs propres indiquent les directions dans lesquelles ces données varient le plus ensemble. Par exemple, on peut découvrir qu'une augmentation de taille s'accompagne souvent d'une augmentation de poids : cette relation correspond à une direction propre. Les vecteurs propres servent donc à repérer les tendances naturelles dans les données.

Cette notion sont essentielles dans:

* analyser les directions principales d'une fonction (via une Hessienne),
* comprendre des données (ACP),
* étudier la stabilité de systèmes,
* optimiser des critères.


#  Comment obtenir

$$
A = P D P^{-1}
$$

La diagonalisation consiste à **réécrire la matrice A dans une base formée de ses vecteurs propres**.

Voici les étapes exactes.

---

# 1. Trouver les valeurs propres

On résout :

$$
\det(A - \lambda I) = 0
$$

Les solutions $$\lambda_1, \lambda_2, \dots$$ sont les **valeurs propres**.

---

# 2. Trouver les vecteurs propres

Pour chaque valeur propre $$(\lambda)$$, on résout :

$$
(A - \lambda I)v = 0.
$$

Les solutions non nulles sont les **vecteurs propres**.

---

# 3. Construire la matrice (P)

On met **chaque vecteur propre comme colonne** :

$$
P = [v_1 ; v_2 ; \dots ; v_n].
$$

Si la matrice est diagonalisable, (P) est **inversible**.

---

# 4. Construire la matrice diagonale (D)

On place les valeurs propres **dans le même ordre que les vecteurs propres de (P)** :

$$
D =
\begin{pmatrix}
\lambda_1 & 0 & \cdots \\
0 & \lambda_2 & \cdots \\
\vdots & & \ddots
\end{pmatrix}.
$$

---

# 5. Alors on obtient automatiquement :

$$
A P = P D
$$

Pourquoi ?

Parce que :

$$
A v_i = \lambda_i v_i
\quad\text{pour chaque vecteur propre } v_i.
$$

Écrit sous forme matricielle :

$$
A[v_1 ; v_2 ;\dots; v_n]
=

[v_1 ; v_2 ;\dots; v_n]
\begin{pmatrix}
\lambda_1 & 0 & \dots \\
0 & \lambda_2 & \dots \\
\vdots & & \ddots
\end{pmatrix}.
$$

Donc :

$$
A P = P D.
$$

Et comme (P) est inversible :

$$
A = P D P^{-1}.
$$

---

# Résumé

> On diagonalise une matrice en construisant la base de ses vecteurs propres : dans cette base, la matrice devient diagonale, ce qui donne
> $$A = P D P^{-1}$$.


---

### 4. Théorèmes importants

**Matrices symétriques réelles.**
Toute matrice symétrique réelle admet une famille complète de vecteurs propres réels, mutuellement orthogonaux, qui forment une base de l'espace.

**Matrices diagonalisables.**
Toute matrice diagonalisable possède suffisamment de vecteurs propres pour former une base.
Ces vecteurs propres ne sont pas nécessairement orthogonaux.

**Autres matrices.**
Une matrice qui n'est pas diagonalisable ne possède pas assez de vecteurs propres pour former une base (et peut même ne pas en posséder du tout).


---

## VI. Combinaison linéaire et base de vecteurs propres

De nombreuses matrices, notamment les matrices symétriques, peuvent être diagonalisées :

$$
A = P D P^{-1},
$$

où (D) est diagonale, formée des valeurs propres.

Cette idée servira plus tard pour :

1. lire facilement la structure d'une transformation,
2. identifier les directions principales d'un problème.

Diagonaliser, c'est trouver les axes naturels du problème.

---

## Une remarque en statistiques

La covariance mesure comment deux variables varient ensemble : positive si elles montent ou descendent ensemble, négative si l'une monte quand l'autre descend.

La matrice de covariance est diagonalisée :
→ Les vecteurs propres = axes principaux
→ Les valeurs propres = variances importantes


> **(A) et (D) font la même chose : (A) le fait dans la base normale, (D) le fait dans la base des vecteurs propres où tout est plus simple.**


---

# Exercices

## Exercice 1 — Produit matrice–vecteur

Calculer (Ax) :

$$
A=
\begin{pmatrix}
2 & -1\\
4 & 3
\end{pmatrix},
\quad
x=
\begin{pmatrix}
1\\
2
\end{pmatrix}
$$

## Exercice 2 — Symétrie

Dire si les matrices suivantes sont symétriques :

1.

$$
\begin{pmatrix}
5 & 2\\
2 & 1
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
0 & 3\\
-3 & 0
\end{pmatrix}
$$

## Exercice 3 — Vecteur propre simple

Pour

$$
A=
\begin{pmatrix}
4 & 0\\
0 & 1
\end{pmatrix},
$$

1. Montrer que $$v = (1,0)^T$$ est un vecteur propre.
2. Trouver $$\lambda$$
3. Trouver un autre vecteur propre évident.

## Exercice 4 — Transformation linéaire

Décrire géométriquement la transformation réalisée par :

$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix}.
$$

## Application - Trouvez les vecteurs propres

Utilisez Python pour trouver les vecteurs propres de la matrice suivante:

$$
A=
\begin{pmatrix}
4 & 1 & 2\\
0 & 3 & 5\\
1 & 0 & 2\\
\end{pmatrix}.
$$

Testez le programme suivant

```python
import numpy as np

A = np.array([
    [4, 1, 2],
    [0, 3, 5],
    [1, 0, 2]
])

# Calcul des valeurs propres et vecteurs propres
valeurs_propres, vecteurs_propres = np.linalg.eig(A)

print("Valeurs propres :")
print(valeurs_propres)

print("\nVecteurs propres :")
print(vecteurs_propres)
```

Vérifiez pour une matrice `2x2` que vous obtentez par le calcul et à l'aide de Python les vecteurs propres.

## Exercice **Interaction entre deux types de cellules**

Deux types de cellules interagissent :

1. (x) : cellules immunitaires
1. (y) : cellules tumorales

On modélise leurs influences respectives par :

$$
A=
\begin{pmatrix}
4 & 2\\
2 & 4
\end{pmatrix}.
$$

Cette matrice décrit comment les deux populations agissent l'une sur l'autre dans un modèle simplifié.

---
Sans utilisez Python répondez aux questions suivantes:

1. Calculez les valeurs propres de (A).
2. Trouvez les vecteurs propres associés.
3. Construisez les matrices (P) et (D).
4. Interprétez biologiquement les deux vecteurs propres.


Vérifiez l'ensemble de vos calcules à l'aide de Python.


##  **Interprétation biologique**

$$
(1,1)
\quad\text{avec}\quad
\lambda_1 = 6
$$

Cela décrit **une évolution conjointe** où les deux populations cellulaires augmentent ou diminuent *ensemble*.

→ **Comportement dominant**, coopération forte.

---

###  Deuxième vecteur propre

$$
(1,-1)
\quad\text{avec}\quad
\lambda_2 = 2
$$

Cela décrit une **relation opposée** :

* si les cellules immunitaires augmentent,
* les cellules tumorales diminuent (et inversement).

→ **Comportement secondaire**, opposé des dynamiques.
