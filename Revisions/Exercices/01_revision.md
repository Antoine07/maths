
# Vecteurs et opérations de base**

Un vecteur de dimension 2 se note :

$$
\vec{u} = \begin{pmatrix} a \ b \end{pmatrix}
$$

De dimension 3 :

$$
\vec{v} = \begin{pmatrix} x \ y \ z \end{pmatrix}
$$

---

##  Addition

$$
\begin{pmatrix} a \ b \end{pmatrix}
+
\begin{pmatrix} c \ d \end{pmatrix}
=

\begin{pmatrix} a+c \ b+d \end{pmatrix}
$$

##  Multiplication par un scalaire

$$
\lambda \begin{pmatrix} a \ b \end{pmatrix}
=

\begin{pmatrix} \lambda a \ \lambda b \end{pmatrix}
$$

##  Norme d'un vecteur

$$
|\vec{u}| = \sqrt{a^2 + b^2}
$$

Exemple :

$$
|(3,4)| = \sqrt{9 + 16} = 5.
$$

---

#  **Exercices vecteurs**

## 01 Exercice 

Calculer :

a)

$$
\begin{pmatrix}2\\
-1\end{pmatrix}
+
\begin{pmatrix}3\\
4\end{pmatrix}
$$

b)

$$
2 \begin{pmatrix}1\\
-5\end{pmatrix}
$$

c) Norme de $$(6,8)$$

---

# Matrices 2×2 : base du calcul matriciel

Une matrice 2×2 :

$$
A =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

agit sur un vecteur :

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=

\begin{pmatrix}
ax + by \\
cx + dy
\end{pmatrix}
$$

C'est uniquement une **combinaison linéaire** des composantes.

---

# Exemples courts

1.

$$
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}

\begin{pmatrix}
3 \\
 4
\end{pmatrix}
=

\begin{pmatrix}
11 \\
4
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
0.8 & 0 \\
0 & 0.9
\end{pmatrix}
\begin{pmatrix}
100 \\
50
\end{pmatrix}
=
\begin{pmatrix}
80 \ 45
\end{pmatrix}
$$

---

# **Exercices matrices**

Calculer :

a)

$$
\begin{pmatrix}
2 & 1\\
0 & 3
\end{pmatrix}

\begin{pmatrix}
4 \\
5
\end{pmatrix}
$$

b)

$$
\begin{pmatrix}
0.5 & 0.5 \\
0.1 & 0.9
\end{pmatrix}

\begin{pmatrix}
10 \\ 
20
\end{pmatrix}
$$

c)
Interpréter le résultat en termes de combinaison linéaire.

---

# **12. Matrices : opérations de base**

### Addition

$$
A+B=
\begin{pmatrix}
a+c & b+d  \\
e+g & f+h
\end{pmatrix}
$$

### Multiplication par un nombre

$$
\lambda A = (\lambda a_{ij})
$$

### Produit matriciel simple

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}

\begin{pmatrix}
p & q \\
r & s
\end{pmatrix}
=
\begin{pmatrix}
ap+br & aq+bs \\
cp+dr & cq+ds
\end{pmatrix}
$$

---

# Exercices matrices

Évaluer :

a)

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
+
\begin{pmatrix}
4 & 1 \\
0 & -2
\end{pmatrix}
$$

b)

$$
2
\begin{pmatrix}
3 & 0 \\
-1 & 4
\end{pmatrix}
$$

c)

$$
\begin{pmatrix}
1 & 0 \\
2 & 3
\end{pmatrix}

\begin{pmatrix}
4 & 1 \\
0 & 2
\end{pmatrix}
$$

---

# **Déterminant d'une matrice 2×2**

Le déterminant :

$$
\det(A)=ad-bc
$$

Exemples :

1.

$$
\det\begin{pmatrix}
2 & 3 \\
1 & 4
\end{pmatrix}
= 8 - 3 = 5
$$

2.

$$
\det\begin{pmatrix}
1 & 1  \\ 
2 & 2\end{pmatrix}
= 2 - 2 = 0
$$

---

# Exercices déterminant

Calculer :

a)

$$
\det\begin{pmatrix}
3 & 2  \\
1 & -1\end{pmatrix}
$$

b)

$$
\det\begin{pmatrix}5 & 1  \\
0 & 3
\end{pmatrix}
$$

c)
Interpréter le cas où le déterminant vaut 0.

---

# **Matrices 3×3 (niveau accessible)**

Une matrice 3×3 :

$$
A=
\begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
$$

agit sur un vecteur 3D de manière naturelle :

$$
A\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
=
\begin{pmatrix}
ax+by+cz \\
dx+ey+fz \\
gx+hy+iz
\end{pmatrix}
$$

---

# Exercices 3×3

Calculer :

a)

$$
\begin{pmatrix}
1 & 0 & 2 \\
-1 & 3 & 0 \\
0 & 4 & 1
\end{pmatrix}

\begin{pmatrix}
2  \\ 
1  \\
3
\end{pmatrix}
$$

b)

$$
\det
\begin{pmatrix}
1 & 1 & 0 \\
0 & 2 & 1 \\
3 & 0 & 1
\end{pmatrix}
$$

---

#  **Premier contact avec les vecteurs propres**

Une matrice (A) peut parfois "étirer" un vecteur **sans changer sa direction** :

$$
A v = \lambda v
$$

1. (v) = vecteur propre
1. (\lambda) = valeur propre

---

Soit :

$$
A =
\begin{pmatrix}
2 & 0 \\
0 & 3
\end{pmatrix}
$$

On cherche (v = (x,y)) tel que :

$$
\begin{pmatrix}
2x  \\
3y
\end{pmatrix}
=
\lambda
\begin{pmatrix}
x  \\
y
\end{pmatrix}
$$

On obtient deux solutions :

1. si $$x \neq 0$$, alors $$\lambda = 2$$ et vecteur propre ((1,0))
1. si $$y \neq 0$$, alors $$\lambda = 3$$ et vecteur propre (0,1)

---

# Exercices vecteurs propres

Trouver les valeurs propres et un vecteur propre de :

a)

$$
\begin{pmatrix}
4 & 0 \\
0 & 1
\end{pmatrix}
$$

b)

$$
\begin{pmatrix}
3 & 1 \\
0 & 3
\end{pmatrix}
$$

---

#  **Exercices récapitulatifs**


a) Développer $$(x-2)^2$$
b) Factoriser $$x^2 - 9$$

## matrices

a)

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}

\begin{pmatrix}
5  \\
6
\end{pmatrix}
$$

b)

$$
2A + B
$$

avec

$$
A=
\begin{pmatrix}
1&0 \\
2&3
\end{pmatrix},
\quad
B=
\begin{pmatrix}
4&1 \\
0&2
\end{pmatrix}
$$

## déterminants

Calculer à la main avec la méthode proposée ci-dessous

$$
\det\begin{pmatrix}
2 & 0 & 1 \\
1 & -1 & 3 \\
0 & 2 & 1
\end{pmatrix}
$$

---
# **Déterminant 3×3 : mnémonique “+ − +”**

Pour

$$
A=
\begin{pmatrix}
a & b & c\\
d & e & f\\
g & h & i
\end{pmatrix}
$$

on développe selon la première ligne :

$$
\det(A)
=
+ a \begin{vmatrix} e & f \\ h & i \end{vmatrix}
- b \begin{vmatrix} d & f \\ g & i \end{vmatrix}
+ c \begin{vmatrix} d & e \\ g & h \end{vmatrix}
$$

### 🔹 Règle à retenir :

* **a** → mineur → **+**
* **b** → mineur → **−**
* **c** → mineur → **+**

C'est le mnémonique :

$$
\color{blue}{+; -; +}
$$


Mais on peut faire ça rapidement avec `Numpy`

```python
import numpy as np

A = np.array([
    [2, 0, 1],
    [1, -1, 3],
    [0, 2, 1]
])

detA = np.linalg.det(A)
print(detA)
```

## vecteurs et norme

a) Calculer $$|(4,-3)|$$

b) Écrire un vecteur unitaire dans la même direction
