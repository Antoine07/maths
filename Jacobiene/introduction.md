# **À quoi sert la jacobienne ?**

La jacobienne sert à décrire **comment une fonction multivariée à valeurs vectorielles varie localement**.
C'est l'outil qui généralise la dérivée lorsque :

$$
f : \mathbb{R}^n \to \mathbb{R}^m.
$$

Elle permet de :

* mesurer la **sensibilité** d'un système à plusieurs entrées,
* **approximer** la variation de la sortie lorsque l'on modifie légèrement les paramètres,
* obtenir la **meilleure approximation linéaire** de la fonction autour d'un point,
* analyser des modèles économiques, physiques ou statistiques dépendant de plusieurs variables.

En résumé :

> La jacobienne est la matrice qui indique comment de petites variations des entrées produisent de petites variations des sorties.

---

# **2. Définition**

Soit
$$
f(x_1,\dots,x_n) = (f_1(x),\dots,f_m(x)).
$$

La jacobienne est la matrice :

$$
J_f(x)=
\begin{pmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \
\vdots & & \vdots \
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{pmatrix}.
$$

Chaque ligne correspond aux dérivées partielles d'une composante de (f).

---

# **3. Interprétation**

Près d'un point (x_0), une petite variation (\Delta x) produit une variation approximative :

$$
\Delta f \approx J_f(x_0),\Delta x.
$$

La jacobienne joue donc le rôle de dérivée pour les fonctions vectorielles.

---

# **4. Approximation linéaire**

On utilise :

$$
f(x_0+\Delta x) \approx f(x_0) + J_f(x_0),\Delta x.
$$

Cette formule permet d'évaluer rapidement l'effet de petites variations d'input sur les outputs du modèle.

---

# **5. Exemple**

On considère :
$$
f(a,b)=
\begin{pmatrix}
a^2 + 3b \
2a - b^2
\end{pmatrix}.
$$

### a) Jacobienne générale

$$
J_f(a,b)=
\begin{pmatrix}
2a & 3 \
2 & -2b
\end{pmatrix}.
$$

### b) Jacobienne au point ((2,1))

$$
J_f(2,1)=
\begin{pmatrix}
4 & 3 \
2 & -2
\end{pmatrix}.
$$

### c) Approximation linéaire

Variations :
$$
\Delta a=0.1,\quad \Delta b=-0.05.
$$

$$
\Delta x=
\begin{pmatrix}
0.1 \ -0.05
\end{pmatrix}.
$$

$$
\Delta f \approx
\begin{pmatrix}
4 & 3\
2 & -2
\end{pmatrix}
\begin{pmatrix}
0.1 \ -0.05
\end{pmatrix}
=

\begin{pmatrix}
0.25 \ 0.30
\end{pmatrix}.
$$

### d) Vérification

$$
f(2.1,0.95)=
\begin{pmatrix}
7.26 \ 3.2975
\end{pmatrix},
\quad
f(2,1)=
\begin{pmatrix}
7 \ 3
\end{pmatrix}.
$$

Variation réelle :
$$
\Delta f_{\text{réel}}=
\begin{pmatrix}
0.26 \ 0.2975
\end{pmatrix}.
$$

L'approximation linéaire correspond très bien.

---

# **6. Synthèse**

1. La jacobienne est la **dérivée matricielle** d'une fonction vectorielle.
1. Elle indique **comment chaque sortie dépend de chaque variable d'entrée**.
1. Elle permet d'estimer les variations via $$\Delta f \approx J_f,\Delta x$$.
1. Elle est indispensable en optimisation, économie, statistiques, modèles physiques.


# Exercice : estimation d'une fonction économique à deux variables

On considère la fonction suivante, représentant un **coût de production** en fonction de deux paramètres numériques :

$$
f(a,b)=
\begin{pmatrix}
a^2 + 3b \
2a - b^2
\end{pmatrix}.
$$

On souhaite estimer la variation de (f) lorsqu'on modifie légèrement (a) et (b).

---

## Données numériques

On travaille au point :
$$
(a,b) = (2,; 1).
$$

Les variations sont :

* $$(\Delta a = 0{,}1)$$,
* $$(\Delta b = -0{,}05)$$.

---

## **Questions**

### 1. Calculez la jacobienne $$J_f(a,b)$$.

### 2. Évaluez cette jacobienne au point ((2,1)).

### 3. Utilisez l'approximation linéaire

$$
\Delta f \approx J_f(a,b),\Delta(a,b)
$$
pour estimer numériquement :
$$
f(a+\Delta a,, b+\Delta b) - f(a,b).
$$

### 4. Vérifiez votre approximation en calculant **réellement**

$$
f(2{,}1,; 0{,}95)
$$
et comparez les deux résultats.
