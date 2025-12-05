# Cours : Le gradient d'une fonction de plusieurs variables

Nous passons maintenant de fonctions d'une variable (Terminale) à des fonctions **de deux variables** ou plus :

$$
f : \mathbb{R}^n \to \mathbb{R}.
$$

Le concept central pour étudier la variation locale de ces fonctions est le **gradient**.

---

# 1. Fonction de deux variables et dérivées partielles

Pour une fonction :

$$
f(x,y),
$$

on peut étudier séparément l'effet d'une variation de (x) (en gardant (y) fixe) et vice versa.

Définitions :

$$
f_x(x,y)=\frac{\partial f}{\partial x}, \qquad f_y(x,y)=\frac{\partial f}{\partial y}.
$$

Elles mesurent respectivement :

* comment (f) change quand on modifie (x) seul,
* comment (f) change quand on modifie (y) seul.

Exemple :

$$
f(x,y)=x^2 + 3y.
$$

$$
f_x = 2x,\qquad f_y = 3.
$$

---

# 2. Définition du gradient

Le gradient regroupe toutes les dérivées partielles en un seul vecteur :

$$
\nabla f(x,y)=
\begin{pmatrix}
f_x(x,y)\
f_y(x,y)
\end{pmatrix}.
$$

Pour une fonction de (n) variables :

$$
\nabla f(x_1,\dots,x_n)=
\begin{pmatrix}
\frac{\partial f}{\partial x_1}\
\vdots \
\frac{\partial f}{\partial x_n}
\end{pmatrix}.
$$

---

# 3. Interprétation géométrique

Le gradient représente la **direction de plus forte augmentation** de la fonction.

Important :

* Le gradient **pointe là où la fonction augmente le plus vite**.
* Sa norme représente la **vitesse maximale d'augmentation**.
* Il est **orthogonal aux courbes de niveau** (lignes où (f(x,y)=k)).

Exemple :
Pour

$$
f(x,y)=x^2 + y^2,
$$

$$
\nabla f = (2x,2y).
$$

Au point ((1,1)), le gradient vaut ((2,2)), orienté vers l'extérieur.
La fonction croît le plus vite en s'éloignant du centre.

---

# 4. Calcul du gradient : exemples

### Exemple 1

$$
f(x,y)=x^3 + xy.
$$

$$
f_x = 3x^2 + y, \qquad f_y = x.
$$

$$
\nabla f = (3x^2 + y,; x).
$$

---

### Exemple 2

$$
f(x,y,z)=x^2 + y^2 + 3z.
$$

$$
\nabla f = (2x,;2y,;3).
$$

---

### Exemple 3

$$
f(x,y)=e^{x+y}.
$$

$$
\nabla f=(e^{x+y}, e^{x+y}).
$$

---

# 5. Points critiques

Un point critique est un point où le gradient s'annule :

$$
\nabla f(x,y) = (0,0).
$$

Ce sont des candidats pour :

* minimum local,
* maximum local,
* point selle.

Exemple :

$$
f(x,y)=x^2 + y^2.
$$

$$
\nabla f=(2x,2y)=0 \Rightarrow (x,y)=(0,0).
$$

---

# 6. Lien avec l'approximation linéaire

Le gradient intervient dans l'approximation :

$$
f(x+\Delta x, y+\Delta y) \approx
f(x,y) + \nabla f(x,y) \cdot
\begin{pmatrix}
\Delta x\
\Delta y
\end{pmatrix}.
$$

Il sert donc à estimer rapidement la variation d'une fonction.

---

# 7. Rôle du gradient dans la pratique

Le gradient est utilisé :

* en optimisation (descente de gradient),
* en apprentissage automatique,
* en économie (analyse marginale),
* en physique (champ de température, potentiel…),
* pour étudier les surfaces (tangentes, courbes de niveau).

---

# Exercices d'entraînement

## Exercice 1

Calculer le gradient :

a) $$f(x,y)=x^2 - 3xy + y^2$$
b) $$g(x,y)=\ln(xy)$$ sur $$(x>0,y>0)$$
c) $$h(x,y)=\sqrt{x^2+y^2}$$

---

## Exercice 2

Trouver les points critiques :

a) $$f(x,y)=x^2 + y^2 - 4x$$
b) $$g(x,y)=x^3 - 3xy$$

---

## Exercice 3

Évaluer le gradient au point indiqué :

a) $$f(x,y)=x^2 + 2y^2$$, au point (1,2)
b) $$g(x,y)=e^{x-y}$$, au point (0,0)

---

## Exercice 4

Interprétation :
La fonction $$T(x,y)=20 - x^2 - y^2$$
représente une température.
Que signifie le gradient au point (1,1) ?
