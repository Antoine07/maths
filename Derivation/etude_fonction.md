# **Étude complète d'une fonction – Limites, Continuité, Tableau de Variation et Tangente**

Ce chapitre complète l'étude de fonction commencée dans la partie sur la dérivation.
Il fournit toutes les notions nécessaires pour analyser correctement une fonction en mathématiques et en data science.

---

# Limites d'une fonction

La limite décrit **le comportement d'une fonction lorsqu'on s'approche d'un point**, ou lorsqu'on part vers l'infini.

## Limites aux bornes infinies

Pour une fonction polynomiale :

**Le terme de plus haut degré domine.**

Exemples :

1.

$$
f(x)=3x^3 - 2x \quad\Rightarrow\quad f(x)\to +\infty\text{ lorsque }x\to+\infty.
$$

2.

$$
g(x)= -5x^4 + x \quad\Rightarrow\quad g(x)\to -\infty\text{ lorsque }x\to+\infty.
$$

## Limites en un point

Elles permettent de repérer :

* les **asymptotes verticales**,
* les **discontinuités**.

Exemple :

$$
\frac{1}{x} \quad\Rightarrow\quad \lim_{x\to 0^+}=+\infty,\quad \lim_{x\to 0^-}=-\infty.
$$

→ On dit que (x=0) est une **asymptote verticale**.

---

# Asymptotes

## Asymptote verticale

Si :

$$
\lim_{x\to a^\pm} f(x)=\pm\infty
$$

alors (x=a) est une **asymptote verticale**.

---

## Asymptote horizontale

Si :

$$
\lim_{x\to\pm\infty} f(x)=L
$$

alors (y=L) est une **asymptote horizontale**.

Exemple :

$$
f(x)=2 + \frac{1}{x}
\Rightarrow y=2.
$$

---

## Asymptote oblique

Si :

$$
\lim_{x\to\infty} \big(f(x) - (ax+b)\big)=0
$$

alors (ax+b) est une asymptote oblique.

Exemple :

$$
f(x)=x + \frac{2}{x} \quad\Rightarrow\quad \text{asymptote } y=x.
$$

---

# Continuité d'une fonction

Une fonction est continue en un point (a) si :

$$
\lim_{x\to a} f(x) = f(a).
$$

Cas typiques de non-continuité :

* saut (fonction par morceaux mal raccordée),
* point isolé,
* asymptote verticale.

---

# Fonctions définies par morceaux

Très important en data science (ReLU, Huber, fonctions coûts).

## Exemple :

$$
f(x)=
\begin{cases}
x + 2 & x < 0 \\
x^2  & x \ge 0
\end{cases}
$$

Questions classiques :

1. La fonction est-elle continue ?
2. Est-elle dérivable ?
3. Étudier ses variations.

Ce type de fonction aide à comprendre :

* les "kinks" d'une fonction,
* les dérivées nulles ou non-existantes,
* les comportements mixtes.

---

# Tableau de signes (préparation aux variations)

Pour résoudre (f(x)>0), (f(x)<0), etc.

Exemple :

$$
f(x)=x(x-3)
$$

Racines : (0) et (3)

| Intervalle | $$-\infty, 0$$| (0, 3) | $$3, +\infty$$ |
| ---------- | ------------ | ------ | ------------ |
| Signe f(x) | –            | +      | +            |

---

#  Tangente à une courbe

Lorsqu'on connaît la dérivée `f'(a)`, l'équation de la tangente à la courbe en (x=a) est :

$$
y = f(a) + f'(a)(x-a).
$$

Exemple :

Pour $$f(x)=x^2$$, tangente en (x=1) :

$$
f(1)=1,\quad f'(1)=2
$$

$$
y = 1 + 2(x-1).
$$

Cette formule sera utilisée plus tard pour l'**approximation linéaire**.

---

# Méthode complète d'étude d'une fonction

Pour étudier une fonction (méthode standard) :

### Étape 1 — Domaine de définition

Repérer les valeurs interdites.

### Étape 2 — Limites et asymptotes

Sortie utile à l'infini ou à un point critique.

### Étape 3 — Dérivée

$$
f'(x)
$$

### Étape 4 — Étude du signe de (f')

Déterminer les intervalles de croissance/décroissance.

### Étape 5 — Tableau de variation

Présenter clairement les résultats.

### Étape 6 — Dérivée seconde

Convexité, points d'inflexion.

### Étape 7 — Tangente éventuelle

En un point d'intérêt.

---

# Exercices 

## Exercice 1 — Limites et asymptotes

Étudier les limites et asymptotes éventuelles de :

a) $$f(x)=\frac{2x+1}{x-3}$$
b) $$g(x)=3 + \frac{1}{x^2}$$
c) $$h(x)=x + \frac{4}{x}$$

---

## Exercice 2 — Continuité et dérivabilité

Étudier la continuité et la dérivabilité de :

$$
f(x)=
\begin{cases}
x+1 & x<1 \\
x^2 & x\ge 1
\end{cases}
$$

---

## Exercice 3 — Tableau de variations complet

Étudier $$f(x)=x^3 - 6x$$ 

1. Limites $$\pm \infty$$
2. Dérivée
3. Signe de la dérivée
4. Tableau de variation

---

## Exercice 4 — Convexité

Étudier la convexité de :

a) $$f(x)=x^4 - x$$
b) $$g(x)=e^x$$
c) $$h(x)=\ln(x)$$

---

## Exercice 5 — Tangente et approximation

Pour $$f(x)=\sqrt{x+4}$$ 

Trouver la tangente en (x=0) et comparer numériquement (via NumPy) :

$$
f(x)\approx f(0)+f'(0)x
$$

---

# Extension NumPy / visualisation

* échantillonner une fonction :

  ```python
  x = np.linspace(-5, 5, 400)
  f = x**3 - 6*x
  ```
* tracer la fonction et sa dérivée :

  ```python
  f1 = 3*x**2 - 6
  plt.plot(x, f, label="f")
  plt.plot(x, f1, label="f'")
  plt.legend()
  ```
* valider les variations observées graphiquement.

---

# **Étude de fonction avec NumPy et Matplotlib**

Même si l'étude de fonction est théorique, les outils numériques sont très utiles pour :

* visualiser les variations,
* comprendre la convexité,
* identifier maxima et minima,
* comparer dérivée analytique et dérivée numérique.

Pour cela, on utilise :

### **Fonctions NumPy utiles**

| Fonction                          | Rôle                                          |
| --------------------------------- | --------------------------------------------- |
| `np.linspace(a, b, n)`            | Crée un vecteur de n points entre a et b      |
| `np.diff(x)`                      | Approximation de la dérivée : (x_{i+1} - x_i) |
| `np.gradient(x)`                  | Dérivée numérique lissée                      |
| `np.sin(x), np.exp(x), np.log(x)` | Fonctions usuelles                            |
| `x**2, x**3`                      | Puissances rapides                            |
| `np.where(condition)`             | Sélection d'indices                           |

### **Fonctions Matplotlib utiles**

| Fonction                    | Rôle                                 |
| --------------------------- | ------------------------------------ |
| `plt.plot(x, y)`            | Tracer une courbe                    |
| `plt.axhline(0)`            | Ligne horizontale (repère pour f'=0) |
| `plt.grid()`                | Grille                               |
| `plt.legend()`              | Légende                              |
| `plt.figure(figsize=(...))` | Taille du graphique                  |

---

# **Méthode générale (numérique) d'étude de fonction**

Pour une fonction ( f(x) ) sur un intervalle ([a,b]), on peut :

### **1. Créer un échantillon de points :**

```python
x = np.linspace(a, b, 400)
```

### **2. Calculer la fonction :**

```python
f = x**3 - 3*x  # exemple
```

### **3. Calculer la dérivée numérique :**

```python
f1 = np.gradient(f, x)
```

### **4. Calculer la dérivée seconde :**

```python
f2 = np.gradient(f1, x)
```

Voir un exemple complet à tester dans un Notebook
[code Numpy](../Starter_Python/project/notebooks/Examples/ex_etude_fonction.ipynb)

---

# **Exercices numériques avec NumPy**


#**Étude complète d'une fonction**

Étudier numériquement la fonction :

[
f(x) = x^4 - 2x^2 + 3
]

Travail demandé :

1. Générer un vecteur `x` entre –3 et 3.
2. Calculer `f(x)`, puis sa dérivée `f'(x)` avec `np.gradient`.
3. Tracer les deux courbes.
4. Repérer graphiquement :

   * les extremums,
   * les intervalles où f croît / décroît.

---

#**Exercice NumPy 2 — Convexité**

Tracer sur un même graphique :

[
f(x)=e^{x}, \qquad f''(x)=e^{x}.
]

Questions :

1. La dérivée seconde est-elle positive ?
2. Que conclure sur la convexité ?
3. Pourquoi cette fonction n'a-t-elle pas de minimum ?

---

#**Exercice NumPy 3 — Étude d'une fonction oscillante**

Étudier :

[
f(x)=\sin(x) - 0.1x
]

1. Tracer f, f' et f''.
2. Repérer les points où f'=0 (maximums locaux).
3. Expliquer pourquoi la fonction finit par décroître sur (\mathbb{R}).

---

#**Exercice NumPy 4 — Comparaison analytique / numérique**

Fonction :

[
f(x)=\log(x)
]

Travail :

1. Calculer la dérivée analytique (f'(x)=1/x),
2. Calculer la dérivée numérique avec `np.gradient`,
3. Tracer les deux sur le même graphique,
4. Expliquer pourquoi l'erreur numérique augmente près de (x=0).

---

#**Exercice NumPy 5 — Sensibilité d'une fonction**

Étudier :

[
f(x)=x e^{-x}
]

1. Tracer f.
2. Calculer f' numériquement.
3. Repérer la zone où f est le plus sensible (dérivée la plus grande en valeur absolue).
4. Interpréter.

---

# 💡 **Pourquoi ces exercices sont importants pour une filière data ?**

Parce qu'ils introduisent très tôt ce que les étudiants verront dans :

* optimisation (descente de gradient),
* traitement du signal (bruit, dérivation),
* machine learning (surfaces de perte),
* modélisation mathématique.

NumPy devient alors un **outil de validation visuelle**, ce qui forme de meilleures intuitions qu'une étude purement symbolique.

---

Si tu veux, je peux te préparer :

✅ Un **Notebook Jupyter complet** avec les corrections
ou
✅ Une **séance avec FastAPI** pour générer automatiquement les graphiques des études de fonctions.
