
## **Modèle de diffusion d'un produit sur deux marchés**

On étudie la manière dont la notoriété d'un nouveau produit se propage sur deux marchés, notés A et B.
On note :

$$
X_n =
\begin{pmatrix}
a_n \\
b_n
\end{pmatrix}
\quad\text{le niveau de notoriété au bout de n mois}.
$$

Le modèle retenu est :

$$
X_{n+1} = M X_n,
\qquad
M=
\begin{pmatrix}
1.20 & -0.2 \\
0.3 & 0.70
\end{pmatrix},
\qquad
X_0=
\begin{pmatrix}
120 \\
60
\end{pmatrix}.
$$

1. Calculer explicitement `X1 = M.X0`.
2. Calculer ensuite `X2 = M.X1`.
3. Interpréter brièvement l'évolution observée entre `n=0`, `n=1`, `n=2`.

---

## **Valeurs propres et vecteurs propres**

1. Calculer les valeurs propres de la matrice `M`.
2. Déterminer un vecteur propre pour chacune d'elles.
3. Justifier que la matrice est diagonalisable.
4. Expliquer pourquoi on peut écrire :

$$
X_0 = \alpha v_1 + \beta v_2.
$$

## **Expression générale de `Xn`**

1. En utilisant les résultats précédents, établir que :

$$
X_n = \alpha, \lambda_1^n v_1 + \beta, \lambda_2^n v_2.
$$

2. En déduire quels comportements apparaissent pour :

- la norme `|Xn|`,
- la proportion `an / bn`,

lorsque `n tend vers l'infini`.

## Interprétation économique

Rédigez une analyse de vos résultats.
