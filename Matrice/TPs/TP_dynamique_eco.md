
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


## **Tracer l'évolution de l'industrie et des services**

(au choix : tableau, courbe, etc.)

Interpréter simplement :

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


#  **Partie 2 — Valeurs propres et vecteurs propres**


#  Une matrice qui étire l'espace différemment selon les directions

On considère maintenant une matrice  :

$$
B=
\begin{pmatrix}
2 & 0 \\
0 & 1
\end{pmatrix}.
$$

Elle transforme un vecteur `(x,y)` en :

$$
(x,y) ;\longrightarrow; (2x,, y)
$$

Donc :

* elle **double** la composante `x`,
* elle laisse **inchangée** la composante `y`.


### Quelles directions ne tournent pas ?

Un vecteur propre est **une direction qui ne change pas**, sauf pour l'étirement.

$$
B \begin{pmatrix} 1 \\ 0 \end{pmatrix}
=
\begin{pmatrix} 2 \\ 0 \end{pmatrix}
= 2 \begin{pmatrix} 1\\0 \end{pmatrix}.
$$

1. même direction, juste étirée.
1. C'est un **vecteur propre**.
1. La **valeur propre** associée est :

$$
\lambda = 2.
$$

### Axe vertical `(0,1)`

$$
B \begin{pmatrix} 0 \\ 1 \end{pmatrix}
=
\begin{pmatrix} 0 \\ 1 \end{pmatrix}
= 1 \begin{pmatrix} 0\\1 \end{pmatrix}.
$$

1. direction intacte.
1. C'est un vecteur propre.
1. Valeur propre associée :

$$
\lambda = 1.
$$

**Conclusion simple :**

* L'axe horizontal est **doublé**.
* L'axe vertical est **conservé**.

Ce sont les **deux directions spéciales** de la matrice.

# Application économique intuitive

Revenons à la matrice économique `A` 

$$
A=
\begin{pmatrix}
0.8 & 0.1 \\
0.2 & 0.9
\end{pmatrix}.
$$

###  Trouver un vecteur `v = (x,y)` tel que `A v` soit **proportionnel** à `v`.

On peut tester des vecteurs simples :

`v = (1,1)`

$$
A \begin{pmatrix} 1 \\ 1 \end{pmatrix}
=
\begin{pmatrix} 0.8 + 0.1 \\ 0.2 + 0.9 \end{pmatrix}
=
\begin{pmatrix} 0.9 \\ 1.1 \end{pmatrix}
$$

Ce vecteur n'est **pas** proportionnel à `(1,1)`, ce n'est **pas un vecteur propre**.

`v = (1,0)`

$$
A \begin{pmatrix} 1 \\ 0 \end{pmatrix}
=
\begin{pmatrix} 0.8 \ 0.2 \end{pmatrix}.
$$

Le résultat n'est pas un multiple de ((1,0)) → **pas bon**.

### • Essai 3 : (v = (1,-1))

$$
A \begin{pmatrix} 1 \\ -1 \end{pmatrix}
=
\begin{pmatrix} 0.8 - 0.1 \\ 0.2 - 0.9 \end{pmatrix}
\begin{pmatrix} 0.7 \\ -0.7 \end{pmatrix}
=
0.7 \begin{pmatrix} 1 \\ -1 \end{pmatrix}.
$$

🎉 **C'est proportionnel !**

Donc `(1,-1)` est un **vecteur propre**.
La valeur propre est : `lambda = 0.7`

---

# Interprétation 

Le vecteur propre `(1,-1)` signifie :

> "Si l'industrie augmente d'une unité et les services diminuent d'une unité,
> l'année suivante ils changent dans la **même direction**, juste réduits par 0.7”.

C'est une combinaison **stable** dans le temps.

### En clair :

* l'opposition “industrie – services” évolue toujours de la même façon.
* c'est une **tendance fondamentale** du modèle.

---

# Résumé

* Une matrice peut **tourner, étirer, comprimer** des vecteurs.
* Certaines directions **ne tournent jamais** → ce sont les vecteurs propres.
* Sur ces directions, la matrice se contente de **multiplier** :

  * multiplier par 2 → croissance
  * multiplier par 0.7 → décroissance
  * multiplier par 1 → stabilité totale

Les valeurs propres disent :

> "De combien cette direction spéciale est-elle amplifiée ou réduite ?"

---

### **Pour la matrice suivante**

$$
B=\begin{pmatrix}2&0\\0&1\end{pmatrix}
$$

1. Vérifier que `(1,0)` est un vecteur propre.
2. Vérifier que `(0,1)` est un vecteur propre.
3. Quelle est la valeur propre associée à chaque direction ?
4. Pourquoi dit-on que ce sont des "directions privilégiées" ?

### **Pour la matrice économique du TP 1**

$$
A=\begin{pmatrix}0.8&0.1\\0.2&0.9\end{pmatrix}
$$

1. Vérifier que `(1,-1)` est un vecteur propre.
2. Déterminer sa valeur propre.
3. Interpréter ce vecteur propre en langage non technique.
4. Pourquoi cette direction est-elle importante pour comprendre l'évolution économique ?

---

### **Simulation Python**

```python
import numpy as np

A = np.array([[0.8, 0.1],
              [0.2, 0.9]])

v = np.array([1., -1.])
print(A @ v)
```

Comparer le résultat avec `lambda v`
