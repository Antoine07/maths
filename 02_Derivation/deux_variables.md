# Cours : Fonctions à deux variables

On étudie maintenant des fonctions qui prennent **deux variables d'entrée** :

$$
f : \mathbb{R}^2 \to \mathbb{R}, \qquad f(x,y).
$$

Exemples :

* $$f(x,y)=x^2+y^2$$
* $$f(x,y)=\frac{x}{y}$$
* $$f(x,y)=e^{x+y}$$

Ce type de fonction apparaît dans :

* les probabilités,
* l'économie (coût, profit),
* la physique (température en un point),
* l'optimisation.

---

# 1. Représentation d'une fonction à deux variables

Une fonction (f(x,y)) peut être représentée :

1. En **surface 3D**, où l'axe vertical est (z=f(x,y)).
2. Avec des **courbes de niveau**, lignes où (f(x,y)=k).

Exemple :
Pour $$f(x,y)=x^2+y^2$$, les courbes de niveau sont des cercles.

---

# 2. Dérivées partielles

La dérivée partielle mesure comment (f) varie **en faisant varier une seule variable**, l'autre étant fixée.

Définitions :

$$
f_x(x,y)=\frac{\partial f}{\partial x}, \qquad f_y(x,y)=\frac{\partial f}{\partial y}.
$$

Exemples :

### Exemple 1

$$
f(x,y)=x^2+3y.
$$

Alors :

$$
f_x=2x, \qquad f_y=3.
$$

### Exemple 2

$$
f(x,y)=xy^2.
$$

$$
f_x=y^2, \qquad f_y=2xy.
$$

---

# 3. Dérivée directionnelle (idée simple)

On peut dériver dans **n'importe quelle direction** $$((u_1,u_2))$$.

L'idée intuitive :

$$f_x=$$ variation selon l'axe (x)
$$f_y=$$ variation selon l'axe (y)

dérivée directionnelle = combinaison des deux

---

# 4. Gradient

Le gradient regroupe toutes les dérivées partielles dans un vecteur :

$$
\nabla f(x,y)=
\begin{pmatrix}
f_x(x,y)\
f_y(x,y)
\end{pmatrix}.
$$

Rôle essentiel :

> Le gradient pointe vers la direction où la fonction augmente le plus vite, c'est très important dans tout problème de data de préciser une tendance.

Exemple :

$$
f(x,y)=x^2+y^2
\quad \Rightarrow \quad
\nabla f = (2x, 2y).
$$

Au point ((1,1)), le gradient vaut ((2,2)) : la fonction augmente le plus rapidement vers la diagonale.

---

# 5. Point critique

Un point critique d'une fonction à deux variables est un point où ( c'est classique ) :

$$
\nabla f(x,y) = (0,0)
$$

Exemple :

$$
f(x,y)=x^2+y^2
\quad \Rightarrow \quad
\nabla f = (2x,2y).
$$

Le seul point critique est ((0,0)).

---

# 6. Dérivées secondes et Hessienne 

On définit :

$$
f_{xx},\ f_{yy},\ f_{xy},\ f_{yx}.
$$

On les regroupe dans la **matrice hessienne** :

$$
H_f(x,y)=
\begin{pmatrix}
f_{xx} & f_{xy} \
f_{yx} & f_{yy}
\end{pmatrix}.
$$

Cette matrice sert à déterminer :

* minimum local,
* maximum local,
* point selle.

---

# 7. Exemples corrigés

### Exemple 1

$$
f(x,y)=3x^2 + y^3 - xy.
$$

$$
f_x=6x - y,
\qquad
f_y=3y^2 - x.
$$

### Exemple 2

$$
f(x,y)=e^{x+y}.
$$

$$
f_x=e^{x+y}, \qquad f_y=e^{x+y}.
$$

### Exemple 3

$$
f(x,y)=\ln(xy)
\quad (x>0, y>0).
$$

$$
f_x = \frac{1}{x}, \qquad f_y=\frac{1}{y}.
$$

---

# 8. Exercices

## Exercice 1

Calculer les dérivées partielles :

a) $$f(x,y)=x^3+y^2$$
b) $$g(x,y)=xy + 3x$$
c) $$h(x,y)=\sqrt{x^2+y^2}$$

---

## Exercice 2

Trouver le gradient de :

a) $$f(x,y)=x^2 - y$$
b) $$g(x,y)=xy^2 - 3y$$

---

## Exercice 3

Trouver les points critiques :

a) $$f(x,y)=x^2 + y^2 - 4x$$
b) $$g(x,y)=x^2 - y^2$$

---

## Exercice 4

Interpréter les dérivées partielles pour la fonction :

$$
f(x,y)=3x + 2y.
$$

Question :
Quelle variable influence le plus la fonction ?
