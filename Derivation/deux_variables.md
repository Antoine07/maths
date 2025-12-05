# Fonctions à deux variables

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

# 3. Dérivée directionnelle

On peut dériver dans **n'importe quelle direction** $$((u_1,u_2))$$.

L'idée intuitive :

variation selon l'axe (x)

$$
f_x
$$ 

variation selon l'axe (y)

$$
f_y
$$

dérivée directionnelle = combinaison des deux

---

# 4. Gradient

Le gradient regroupe toutes les dérivées partielles dans un vecteur :

$$
\nabla f(x,y)=
\begin{pmatrix}
f_x(x,y)\\
f_y(x,y)
\end{pmatrix}.
$$

Rôle essentiel :

> Le gradient pointe vers la direction où la fonction augmente le plus vite.

Exemple :

$$
f(x,y)=x^2+y^2
\quad \Rightarrow \quad
\nabla f = (2x, 2y).
$$

Au point (1,1), le gradient vaut (2,2) : la fonction augmente le plus rapidement vers la diagonale.

---

# 5. Point critique

Un point critique d'une fonction à deux variables est un point où :

$$
\nabla f(x,y) = (0,0)
$$

Exemple :

$$
f(x,y)=x^2+y^2
\quad \Rightarrow \quad
\nabla f = (2x,2y).
$$

Le seul point critique est (0,0).

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
f_{xx} & f_{xy} \\
f_{yx} & f_{yy}
\end{pmatrix}.
$$

Cette matrice sert à déterminer :

* minimum local,
* maximum local,
* point selle.

---

# **Hessien et convexité**

Pour une fonction f(x,y), le **Hessien** est :

$$
H_f(x,y)=
\begin{pmatrix}
f_{xx} & f_{xy} \\
f_{yx} & f_{yy}
\end{pmatrix}
$$

Critères :

1. Si le Hessien est **défini positif** → ( f ) est **strictement convexe**.
1. Si le Hessien est **défini négatif** → ( f ) est **strictement concave**.
1. Si le Hessien est **indéfini** → ni convexe ni concave.
1. Si semi-défini → convexité faible.

Pour un Hessien  $$2 \times 2$$  

1. Positif si : $$f_{xx} > 0$$ et $$\det(H_f) > 0$$
1. Négatif si : $$f_{xx} < 0$$ et $$\det(H_f) > 0$$
1. Indéfini si : $$\det(H_f) < 0$$

---

# **Exemple 1**

$$
f(x,y) = 3x^2 + y^3 - xy
$$

### Dérivées partielles premières

Déjà données :

$$
f_x = 6x - y, \qquad f_y = 3y^2 - x
$$

### Dérivées secondes

$$
f_{xx} = 6,\quad f_{yy} = 6y,\quad f_{xy} = f_{yx} = -1
$$

### Hessien

$$
H_f(x,y) =
\begin{pmatrix}
6 & -1 \\
-1 & 6y
\end{pmatrix}
$$

### Déterminant

$$
\det(H_f) = 6 \cdot 6y - 1 = 36y - 1
$$

### Analyse

* Si $$y > \frac{1}{36}$$, alors $$\det(H_f) > 0$$ et $$f_{xx} = 6 > 0$$ ⇒ **Hessien défini positif** ⇒ **fonction convexe** dans cette région.
* Si $$y < \frac{1}{36}$$ ⇒ Hessien indéfini ⇒ **ni convexe ni concave**.
* Si $$y = \frac{1}{36}$$ ⇒ passage limite (semi-défini).

➡️ Convexité **selon la zone du plan**, non globale.

---

# **Exemple 2**

$$
f(x,y) = e^{x+y}
$$

### Dérivées partielles premières

Déjà données :

$$
f_x = e^{x+y},\quad f_y = e^{x+y}
$$

### Dérivées secondes

$$
f_{xx} = e^{x+y},\quad f_{yy} = e^{x+y},\quad f_{xy} = e^{x+y}
$$

### Hessien

$$
H_f(x,y) =
e^{x+y}
\begin{pmatrix}
1 & 1 \\
1 & 1
\end{pmatrix}
$$

### Déterminant

$$
\det(H_f) = e^{2(x+y)}(1\cdot 1 - 1\cdot 1) = 0
$$

Le Hessien est **semi-défini positif** (matrice positive mais de rang 1).

### Conclusion

$$f(x,y) = e^{x+y}$$ est :

* **Convexe** (car exponentielle d'une fonction affine).
* **Pas strictement convexe** car le Hessien n'est pas strictement positif (déterminant nul).

---

# **Exemple 3**

$$
f(x,y) = \ln(xy),\quad x>0,\ y>0
$$

### Dérivées partielles premières

Déjà données :

$$
f_x = \frac{1}{x},\quad f_y = \frac{1}{y}
$$

### Dérivées secondes

$$
f_{xx} = -\frac{1}{x^2},\quad
f_{yy} = -\frac{1}{y^2},\quad
f_{xy} = 0
$$

### Hessien

$$
H_f(x,y) =
\begin{pmatrix}
-\frac{1}{x^2} & 0 \\
0 & -\frac{1}{y^2}
\end{pmatrix}
$$

### Déterminant

$$
\det(H_f) = \frac{1}{x^2 y^2} > 0
$$

Et $$f_{xx} < 0$$

### Conclusion

* Hessien **défini négatif**
* Donc $$f(x,y) = \ln(xy)$$ est **strictement concave** sur  $$x>0,\ y>0$$.

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
