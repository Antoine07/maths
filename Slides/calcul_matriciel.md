---
marp: true
theme: default
paginate: true
class: lead
---

# Calcul Matriciel

## 1. Définition

Une matrice est un tableau de nombres organisé en lignes et en colonnes :

$$
A=
\begin{pmatrix}
1 & 3\\
2 & -1
\end{pmatrix}.
$$

Une matrice sert à représenter des opérations linéaires, à effectuer des calculs, et à manipuler des systèmes.

---

# 2. Vecteurs et produit matrice–vecteur

Un vecteur colonne :

$$
x=
\begin{pmatrix}
2\\
-1
\end{pmatrix}.
$$

Le produit (Ax) se calcule ligne par colonne.

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

---

# 3. Produit matrice–matrice

Si (A) est (m \times n) et (B) est (n \times p), alors (AB) est (m \times p).

Exemple :

$$
A=
\begin{pmatrix}
1 & 3\\
2 & 1
\end{pmatrix},
\quad
B=
\begin{pmatrix}
2 & 0\\
1 & 4
\end{pmatrix}.
$$

$$
AB=
\begin{pmatrix}
1\cdot 2 + 3\cdot 1 & 1\cdot 0 + 3\cdot 4\\
2\cdot 2 + 1\cdot 1 & 2\cdot 0 + 1\cdot 4
\end{pmatrix}
=
\begin{pmatrix}
5 & 12\\
5 & 4
\end{pmatrix}.
$$

---

# 4. Matrice identité

$$
I=
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}.
$$

Elle vérifie :

$$
AI = IA = A.
$$

---

# 5. Inverse d'une matrice : méthode de la matrice augmentée

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

## Exemple complet

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

# 6. Vérification

$$
A A^{-1} =
\begin{pmatrix}
2 & 1\\
1 & 1
\end{pmatrix}
\begin{pmatrix}
1 & -1\
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

---

## Exercice 1 — Produit matrice–vecteur

Calculer (Ax).

$$
A=
\begin{pmatrix}
3 & -1\\
2 & 4
\end{pmatrix},
\quad
x=
\begin{pmatrix}
1\
3
\end{pmatrix}.
$$

---

## Exercice 2 — Produit matrice–matrice

Calculer (AB).

$$
A=
\begin{pmatrix}
2 & 5\\
1 & 3
\end{pmatrix},
\quad
B=
\begin{pmatrix}
1 & 0\\
4 & 2
\end{pmatrix}.
$$

---

## Exercice 3 — Matrices symétriques

Dire si les matrices suivantes sont symétriques.

1.

$$
\begin{pmatrix}
4 & 2\\
2 & 7
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

## Exercice 5 — Application simple

Une population se transforme selon :

$$
\begin{pmatrix}
x'\\
y'
\end{pmatrix}
=

\begin{pmatrix}
2 & 1\\
0 & 3
\end{pmatrix}
\begin{pmatrix}
x\
y
\end{pmatrix}.
$$

1. Calculer l'évolution de
   $$
   (x,y) = (1,2).
   $$
2. Interpréter le rôle du coefficient 1 dans la première ligne.

---

## [Retour au plan](https://antoine07.github.io/maths/)
