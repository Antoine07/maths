# **TP – Dynamique économique et vecteurs propres**

---



### **Contexte : deux secteurs économiques qui interagissent**

Une économie est caractérisée par deux secteurs :

1. Industrie
2. Services

Chaque année, une partie de chaque secteur se transforme en l'autre.

On modélise cette interaction par la matrice :

$$
A=
\begin{pmatrix}
0.7 & 0.2 \\
0.1 & 0.8
\end{pmatrix}.
$$

Le vecteur économique au temps (n) est :

$$
X_n =
\begin{pmatrix}
\text{Industrie}_n \\
\text{Services}_n
\end{pmatrix}.
$$

La dynamique est :

$$
X_{n+1} = A X_n.
$$

---

# **Données initiales**

Au début :

$$
X_0 =
\begin{pmatrix}
1000 \\
500
\end{pmatrix}.
$$

---


## **Calculs itératifs**

Calculez à la main :

1. `X_1 = AX_0`
2. `X_2 = AX_1`
3. `X_3 = AX_2`

Questions d'analyse :

1. L'industrie augmente-t-elle ou diminue-t-elle ?
1. Les services augmentent-ils ou diminuent-ils ?
1. Les proportions entre les deux se rapprochent-elles d'une structure stable ?

---

## **Valeurs propres**

Calculez les valeurs propres de `A` en résolvant :

$$
\det(A - \lambda I) = 0.
$$

Vous devez obtenir deux valeurs propres réelles.


## **Vecteurs propres**

Pour chaque valeur propre `lambda`, résolvez :

$$
(A - \lambda I)v = 0.
$$

Trouvez deux vecteurs propres (non nuls).

## **Matrices (P) et (D)**

Construisez :

1. la matrice (P) contenant les vecteurs propres en colonnes,
1. la matrice diagonale (D) contenant les valeurs propres dans le même ordre.

Vérifiez la relation :

$$
A P = P D.
$$


## **Interprétation économique**

Expliquez :

1. ce que signifie le **vecteur propre associé à la plus grande valeur propre**,
2. ce que signifie le **second vecteur propre**,
3. quelle sera la **structure économique de long terme**,
4. pourquoi cette structure est indépendante de l'état initial.

# **Vérifiez avec Python vos calculs**

Comparez avec le module `Numpy`

```python
# TODO
```

