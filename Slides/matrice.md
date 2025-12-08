---
marp: true
theme: default
paginate: true
class: lead
---

## **Matrices, vecteurs, transformations et vecteurs propres**

---

## Introduction 

D'où viennent les équations ou matrices

## **Dimension 1 : décroissance simple**

On modélise une quantité qui diminue de 20 % à chaque période
(population, prix, signal…).

Relation réelle :

$$
x_{\text{nouveau}} = 0.8 , x_{\text{ancien}}
$$

---

Ici :

1. le coefficient **0.8** exprime une perte de 20 %,
1. la « transformation » est simplement **une matrice 1×1** :
  $$
  [0.8]
  $$

Ce modèle dit juste : *chaque période, on garde 80 % de la valeur précédente*.

---

# Dimension 2 : industrie et services

Deux secteurs se stimulent mutuellement :

1. l'industrie génère +0.7 de nouvelle industrie et +0.1 de services,
1. les services génèrent +0.2 d'industrie et +0.8 de services.

Alors :

$$
\begin{pmatrix}
\text{Ind}*{n+1} \\
\text{Serv}*{n+1}
\end{pmatrix}
=

\begin{pmatrix}
0.7 & 0.1 \\
0.2 & 0.8
\end{pmatrix}
\begin{pmatrix}
\text{Ind}_n \\
\text{Serv}_n
\end{pmatrix}
$$

La matrice traduit simplement :

1. comment **chaque secteur influence l'autre**,
1. et comment chacun **s'auto-alimente**.

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

---

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

---

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

---

### 2. Compression

$$
A=
\begin{pmatrix}
0.5 & 0\\
0 & 0.5
\end{pmatrix}
$$

Réduit toutes les directions d'un facteur 2.

---

### 3. Réflexion (symétrie)

$$
A=
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix}
$$

Symétrie par rapport à l'axe (x).

---

### 4. Cisaillement (shear)

$$
A=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}
$$

Incline les vecteurs vers la droite.

---

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

1. (v) est une direction préservée,

1. 

$$
\lambda
$$ 

est le facteur d'étirement dans cette direction.

---

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

---

### 3. Interprétation géométrique

Une matrice possède généralement plusieurs directions privilégiées : ses vecteurs propres.
Ce sont les directions où la transformation agit de manière la plus simple.

Si l'on observe deux données comme la taille et le poids, les vecteurs propres indiquent les directions dans lesquelles ces données varient le plus ensemble. Par exemple, on peut découvrir qu'une augmentation de taille s'accompagne souvent d'une augmentation de poids : cette relation correspond à une direction propre. Les vecteurs propres servent donc à repérer les tendances naturelles dans les données.

---

Cette notion sont essentielles dans:

1. analyser les directions principales d'une fonction (via une Hessienne),
1. comprendre des données (ACP),
1. étudier la stabilité de systèmes,
1. optimiser des critères.

---

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

Les solutions 

$$
\lambda_1, \lambda_2, \dots
$$ 

sont les **valeurs propres**.

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

---

Donc :

$$
A P = P D.
$$

Et comme (P) est inversible :

$$
A = P D P^{-1}
$$

---

# Résumé

> On diagonalise une matrice en construisant la base de ses vecteurs propres : dans cette base, la matrice devient diagonale, ce qui donne


$$
A = P D P^{-1}
$$


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

## Remarque en statistiques

La covariance mesure comment deux variables varient ensemble : positive si elles montent ou descendent ensemble, négative si l'une monte quand l'autre descend.

La matrice de covariance est diagonalisée :
→ Les vecteurs propres = axes principaux
→ Les valeurs propres = variances importantes


> **(A) et (D) font la même chose : (A) le fait dans la base normale, (D) le fait dans la base des vecteurs propres où tout est plus simple.**

---


# Inverse d'une matrice : méthode de la matrice augmentée

Une matrice (A) est inversible s'il existe $$(A^{-1})$$ tel que :

$$
A A^{-1} = I.
$$

Pour trouver (A^{-1}), on utilise **la matrice augmentée** :

$$
(A \mid I),
$$

et on applique des opérations élémentaires pour transformer :

$$
(A \mid I) ;\longrightarrow; (I \mid A^{-1}).
$$

---

## Exemple 

Soit

$$
A=
\begin{pmatrix}
2 & 1\\
1 & 1
\end{pmatrix}.
$$

On forme :

$$
\left(
\begin{array}{cc|cc}
2 & 1 & 1 & 0\\
1 & 1 & 0 & 1
\end{array}
\right).
$$

Étape 1 : rendre le pivot en haut à gauche égal à 1 (on échange les lignes) :

$$
\left(
\begin{array}{cc|cc}
1 & 1 & 0 & 1\\
2 & 1 & 1 & 0
\end{array}
\right).
$$

---

Étape 2 : annuler la deuxième ligne, première colonne :

L2 ← L2 – 2 L1

$$
\left(
\begin{array}{cc|cc}
1 & 1 & 0 & 1\\
0 & -1 & 1 & -2
\end{array}
\right).
$$

---

Étape 3 : normaliser la deuxième ligne

L2 ← –L2

$$
\left(
\begin{array}{cc|cc}
1 & 1 & 0 & 1\\
0 & 1 & -1 & 2
\end{array}
\right).
$$

---

Étape 4 : annuler le 1 au-dessus (colonne 2)

L1 ← L1 – L2

$$
\left(
\begin{array}{cc|cc}
1 & 0 & 1 & -1\\
0 & 1 & -1 & 2
\end{array}
\right).
$$

Résultat :

$$
A^{-1}=
\begin{pmatrix}
1 & -1\\
-1 & 2
\end{pmatrix}.
$$

---

# Vérification

$$
A A^{-1} =
\begin{pmatrix}
2 & 1\\
1 & 1
\end{pmatrix}
\begin{pmatrix}
1 & -1\\
-1 & 2
\end{pmatrix}
=

\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}.
$$

L'inverse est correctement trouvé.


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

---

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

---

## Exercice 3 — Vecteur propre simple

Pour

$$
A=
\begin{pmatrix}
4 & 0\\
0 & 1
\end{pmatrix},
$$

1. Montrer que 

$$
v = (1,0)^T
$$

est un vecteur propre.
2. Trouver 

$$
\lambda
$$

3. Trouver un autre vecteur propre évident.

---

## Exercice 4 — Transformation linéaire

Décrire géométriquement la transformation réalisée par :

$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix}.
$$

---

## Exercice 4 — Inverse par matrice augmentée

Utiliser exclusivement la méthode de Gauss-Jordan pour trouver l'inverse.

$$
A=
\begin{pmatrix}
1 & 2\\
3 & 4
\end{pmatrix}.
$$

---

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

---

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

---

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

---

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

1. si les cellules immunitaires augmentent,
1. les cellules tumorales diminuent (et inversement).

→ **Comportement secondaire**, opposé des dynamiques.

---

# TP dynamique économique

[Dynamique économique](https://github.com/Antoine07/maths/tree/main/Derivation/TPs/TP_dynamique_eco.md)

---

## [Retour au plan](https://antoine07.github.io/maths/)