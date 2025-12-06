
$$
v^\top H v \ge 0
$$


---

# Convexité via la condition générale $$(v^\top H v \ge 0)$$

---

# Pourquoi utiliser un critère général ?

En dimension 1 et 2, on utilise :

1. $$f''(x) > 0$$ en 1D
1. $$\det(H) > 0$$ et $$f_{xx} > 0$$ en 2D

Mais **dans les dimensions supérieures**, il n'existe PLUS de critère simple type "déterminant positif”.

Donc on utilise le critère **universel** :

---

# Théorème fondamental

Soit $$f : \mathbb{R}^n \to \mathbb{R}$$ deux fois différentiable.

Alors :

> **f est convexe si et seulement si son Hessien est semi-défini positif :**

$$
v^\top H(x), v \ge 0 \quad \forall v \in \mathbb{R}^n,\ \forall x.
$$

### Signification intuitive

1. (v) = **une direction quelconque** dans l'espace.
1. (v^\top H v) = **courbure de f dans cette direction**.

👉 Si la courbure est positive dans *toutes* les directions :
la fonction est courbée vers le haut → **convexe**.

---

# Exemple concret en dimension 3 (matrice 3×3)

Considérons la fonction :

$$
f(x,y,z) = x^2 + y^2 + z^2
$$

C'est l'extension naturelle du bol parabolique 2D.

---

## 🟩 3.1. Calcul du Hessien

Les dérivées secondes :

$$
f_{xx}=2,\quad f_{yy}=2,\quad f_{zz}=2,
\quad f_{xy}=f_{xz}=f_{yz}=0.
$$

Donc :

$$
H =
\begin{pmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{pmatrix}
= 2I_3.
$$

---

## 🟩 3.2. Test de convexité général

Prenons **un vecteur arbitraire** :

$$
v = \begin{pmatrix} a \ b \ c \end{pmatrix}
$$

Calculons :

$$
v^\top H v
=
\begin{pmatrix}
a & b & c
\end{pmatrix}
\begin{pmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{pmatrix}
\begin{pmatrix}
a \ b \ c
\end{pmatrix}
$$

Effectuons la multiplication :

$$
v^\top H v = 2a^2 + 2b^2 + 2c^2
$$

Ce nombre est toujours **≥ 0**.

### Vérification du critère :

$$
2(a^2 + b^2 + c^2) \ge 0 \quad \forall (a,b,c)
$$

1. Courbure positive dans toutes les directions
1. Donc la fonction est **strictement convexe**

---

# Interprétation géométrique claire

Dans l'espace 3D :

1. la surface (z = f(x,y,z)) n'est plus visible directement (car f dépend de 3 variables),
1. mais on sait que **quel que soit le plan** que l'on coupe, on obtient une parabole tournée vers le haut.

### Ce que dit le critère $$v^\top H v \ge 0$$ 

Dans *toute* direction de l'espace (a,b,c), la fonction :

1. s'incurve vers le haut,
1. ne peut jamais faire de "creux inversés” ni de selles,
1. se comporte comme une parabole.

---

# Exemple d'une fonction NON convexe en 3D

Considérons :

$$
g(x,y,z) = x^2 + y^2 - z^2
$$

Hessien :

$$
H_g =
\begin{pmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & -2
\end{pmatrix}
$$

Posons :

$$
v = (0,0,1)
$$

Alors :

$$
v^\top H_g v = -2 < 0
$$

👉 Il existe **une direction où la courbure est négative**.
👉 Donc **g n'est pas convexe**.
👉 C'est une **surface selle**, même en dimension 3.

---

# Ce que ce critère permet de comprendre (au-delà du 2×2)

1. Il est **général** et valable pour **toutes les dimensions**
1. Il fonctionne même pour des fonctions complexes
1. Il généralise ce que vous faites déjà en 2D
1. C'est la base théorique de l'optimisation moderne (machine learning)
