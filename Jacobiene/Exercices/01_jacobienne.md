# **EXERCICES À FAIRE À LA MAIN (1 à 5)**

---

## **Exercice 1 — Jacobienne simple (2→2)**

Soit
$$
f(x,y)=
\begin{pmatrix}
x^2 + y\\
x - y^2
\end{pmatrix}
$$

1. Calculer $$J_f(x,y)$$
2. Évaluer $$J_f(1,2)$$

---

## **Exercice 2 — Fonction linéaire (3→2)**

Soit

$$
f(x,y,z)=
\begin{pmatrix}
2x - y + 3z\\
x + 4y
\end{pmatrix}
$$

1. Calculer la jacobienne.
2. Pourquoi la jacobienne est-elle constante ?

---

## **Exercice 3 — Approximation linéaire (2→2)**

Soit
$$
f(x,y)=
\begin{pmatrix}
x^2 - y\\
3x + y^2
\end{pmatrix}
$$

Au point ((1,1)), on prend (\Delta x = 0.05), $$\Delta y = -0.1$$

1. Calculer $$J_f(1,1)$$
2. Calculer $$\Delta f \approx J_f,\Delta x$$
3. Comparer avec $$f(1.05,0.9)$$

---

## **Exercice 4 — Fonction économique (2→1)**

Soit le profit :

$$
P(q,r) = q^2 r + 3q
$$

1. Calculer le gradient (ici la jacobienne est 1×2).
2. Interpréter économiquement les dérivées partielles.

---

## **Exercice 5 — Changement de variables (simple) (2→2)**

Soit

$$
F(u,v) = (x,y) = (u+v, u-v)
$$

1. Calculer la jacobienne (J_F(u,v)).
2. L'interpréter comme transformation du plan.

---

---

# **EXERCICES AVEC NUMPY (6 à 10)**

---

## **Exercice 6 — Jacobienne numérique (2→2)**

Soit
$$
f(x,y) = (x^2 + y, e^x y)
$$

Calculer **numériquement** la jacobienne au point ((1,2)).

👉 Utiliser :
`np.gradient` ou une **approximation par différences finies** :

$$
\frac{f(x+h)-f(x)}{h}
$$

---

## **Exercice 7 — Vérification de l'approximation linéaire**

Même fonction :

$$
f(x,y) = (x^2 + y,; e^x y)
$$

1. Calculer une approximation NumPy de (J_f(1,2))
2. Calculer (\Delta f \approx J_f \Delta x) pour
   $$\Delta x = (0.01, -0.02)$$
3. Vérifier avec
   `f(np.array($$1,2]) + delta) - f(np.array($$1,2]))`

👉 Utiliser :

1. `numpy.array`
1. calculs vectoriels
1. méthode des différences finies

---

## **Exercice 8 — Jacobienne d'un modèle linéaire (3→3)**

Soit

$$
F(x)=Ax \quad\text{avec}\quad
A=
\begin{pmatrix}
2 & 1 & 0\\
0 & 3 & -1\\
1 & 0 & 1
\end{pmatrix}
$$

1. Vérifier avec NumPy que la jacobienne est **égale à A**.
2. Vérifier pour plusieurs points aléatoires.

👉 Utiliser :

1. `np.dot`
1. `np.random.randn`

---

## **Exercice 9 — Champ vectoriel (2→2)**

Soit

$$
f(x,y)=
\begin{pmatrix}
\sin(xy)\
x^2 + y
\end{pmatrix}
$$

Approximations numériques de :

$$
J_f(0.5,, 1)
$$

👉 Utiliser :

1. une fonction Python
1. un calcul de dérivée numérique avec `h = 1e-5`
1. `np.zeros((2,2))`

---

## **Exercice 10 — Jacobienne sur grille 2D**

Soit

$$
f(x,y)=x^2 - y^3
$$

1. Créer une grille NumPy :
   `x = np.linspace(-2,2,200)`
   `y = np.linspace(-2,2,200)`
2. Calculer :

   $$
   \frac{\partial f}{\partial x},\quad \frac{\partial f}{\partial y}
   $$

   sur toute la grille.

👉 Utiliser :

1. `np.meshgrid`
1. `np.gradient`

But : visualiser le champ vectoriel (quiver) $$\nabla f$$ 
