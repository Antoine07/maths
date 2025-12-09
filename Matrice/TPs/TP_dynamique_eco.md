
# **Deux secteurs économiques en interaction**

Deux secteurs économiques :

* Industrie
* Services

Ils évoluent chaque année selon une règle fixe représentée par la matrice :

$$
A=
\begin{pmatrix}
0.8 & 0.1 \\
0.2 & 0.9
\end{pmatrix}.
$$

Le vecteur économique :

$$
X_n =
\begin{pmatrix}
\text{Industrie}_n \\
\text{Services}_n
\end{pmatrix}
$$

Dynamique :

$$
X_{n+1} = A X_n.
$$


# Données initiales

$$
X_0 = 
\begin{pmatrix} 
100 \\ 
50 
\end{pmatrix}.
$$


Calculez à la main:

$$
X_1 = A X_0
$$

Écrire explicitement :

$$
\begin{pmatrix}
0.8 & 0.1 \\
0.2 & 0.9
\end{pmatrix}
\begin{pmatrix}
100 \\
50
\end{pmatrix}
$$

Interpréter le résultat en mots :
**Qui influence qui ? Industrie sur Services ? L'inverse ?**


# **Évolution sur plusieurs années**

## **Calculez ensuite :**

`X_2 = A X_1`

`X_3 = A X_2`

1. L'industrie augmente-t-elle ?
2. Les services augmentent-ils ?
3. L'économie se stabilise-t-elle ?
4. À votre avis : si on continue encore 10 ans, que se passe-t-il ?

---

* est-ce que les deux secteurs convergent ?
* deviennent-ils proches ?
* l'un domine-t-il l'autre ?

---

### **Question ouverte (sans valeurs propres)**

Votre réponse doit être intuitive :

> Pourquoi une règle aussi simple que
> `X_{n+1} = A X_n`
> peut-elle suffire à prévoir l'évolution à long terme d'une économie simplifiée ?

---

Revenons à la matrice économique `A` 

$$
A=
\begin{pmatrix}
0.8 & 0.1 \\
0.2 & 0.9
\end{pmatrix}.
$$

###  Trouver un vecteur `v = (x,y)` tel que `A.v` soit **proportionnel** à `v`.

---

# Interprétation 

Interprétez les résultats

### **Pour la matrice suivante**

$$
B=
\begin{pmatrix}
2 & 0 \\
0 & 1
\end{pmatrix}
$$

1. Vérifier que `(1,0)` est un vecteur propre.
2. Vérifier que `(0,1)` est un vecteur propre.
3. Quelle est la valeur propre associée à chaque direction ?
4. Pourquoi dit-on que ce sont des "directions privilégiées" ?

### **Pour la matrice économique**

$$
A=
\begin{pmatrix}
0.8&0.1\\
0.2&0.9
\end{pmatrix}
$$

1. Vérifier que `(1,-1)` est un vecteur propre.
2. Déterminer sa valeur propre.
3. Interpréter ce vecteur propre en langage non technique.
4. Pourquoi cette direction est-elle importante pour comprendre l'évolution économique ?

---

### **Simulation Python**

```python
# TODO
```

Comparer le résultat avec `lambda v`
