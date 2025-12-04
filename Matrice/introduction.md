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
\end{pmatrix}.
$$

Il représente une direction et une intensité dans l'espace.

### 2. Matrices

Une matrice est un tableau de nombres.

$$
A=
\begin{pmatrix}
1 & 3\\
2 & -1
\end{pmatrix}.
$$

Elle représente une transformation linéaire : elle prend un vecteur en entrée et produit un nouveau vecteur.

---

## II. Multiplication matrice–vecteur

Pour une matrice (A) et un vecteur (x), le produit (Ax) est défini par :

$$
Ax =
\begin{pmatrix}
a_{11}x_1 + a_{12}x_2 \\
a_{21}x_1 + a_{22}x_2
\end{pmatrix}.
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
\end{pmatrix}.
$$

$$
Ax=
\begin{pmatrix}
1\cdot 2 + 2\cdot 1\\
3\cdot 2 + 1\cdot 1
\end{pmatrix}
=

\begin{pmatrix}
4\\
7
\end{pmatrix}.
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
\end{pmatrix}.
$$

Multiplie la coordonnée (x) par 3, laisse (y) inchangé.

### 2. Compression

$$
A=
\begin{pmatrix}
0.5 & 0\\
0 & 0.5
\end{pmatrix}.
$$

Réduit toutes les directions d'un facteur 2.

### 3. Réflexion (symétrie)

$$
A=
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix}.
$$

Symétrie par rapport à l'axe (x).

### 4. Cisaillement (shear)

$$
A=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$

Incline les vecteurs vers la droite.

### 5. Rotation

$$
A=
\begin{pmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{pmatrix}.
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
a_{ij} = a_{ji}.
$$

Exemple :

$$
S=
\begin{pmatrix}
2 & 1\\
1 & 3
\end{pmatrix}.
$$

Les matrices symétriques possèdent des propriétés géométriques fortes, notamment l'existence de vecteurs propres orthogonaux.

---

## V. Vecteurs propres et valeurs propres

### 1. Définition

Pour une matrice carrée (A), un vecteur non nul (v) est un vecteur propre s'il existe un réel $$\lambda$$ tel que :

$$
A v = \lambda v.
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
\end{pmatrix}.
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
\end{pmatrix}.
$$

### 3. Interprétation géométrique

Une matrice possède généralement plusieurs directions privilégiées : ses vecteurs propres.
Ce sont les directions où la transformation agit de manière la plus simple.

Cette notion sera essentielle plus tard pour :

* analyser les directions principales d'une fonction (via une Hessienne),
* comprendre des données (ACP),
* étudier la stabilité de systèmes,
* optimiser des critères.


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
\end{pmatrix}.
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

1. Montrer que (v = (1,0)^T) est un vecteur propre.
2. Trouver (\lambda).
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
