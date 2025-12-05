# Cours de probabilités — Révision des notions fondamentales

---

# Univers et événements

Quand on réalise une expérience aléatoire (tirage, lancer d'un dé, choix aléatoire), plusieurs résultats sont possibles.

### Univers

Ensemble de tous les résultats possibles :

$$
\Omega = {\text{tous les cas possibles}}.
$$

Exemple : lancer un dé

$$
\Omega = {1,2,3,4,5,6}.
$$

### Événement

Un sous-ensemble de l'univers.

Exemples :

* A = "obtenir un nombre pair" = {2,4,6}
* B = "obtenir un nombre > 4" = {5,6}

---

# Probabilité d'un événement

Si tous les résultats sont équiprobables :

$$
P(A)=\frac{\text{nombre de cas favorables}}{\text{nombre de cas possibles}}.
$$

Exemples :
Dé équilibré :

$$(P(\text{pair}) = 3/6 = 1/2)$$
$$(P(6)=1/6)$$

---

# Probabilités sur plusieurs événements

###  Union

$$
P(A \cup B)=P(A)+P(B)-P(A \cap B).
$$

###  Intersection

$$
P(A \cap B)=P(A)\times P(B|A).
$$

###  Complémentaire

$$
P(\bar A)=1-P(A).
$$

Exemple simple :
$$P(\text{ne pas faire 6}) = 1 - 1/6 = 5/6.$$

---

# Indépendance

Deux événements sont indépendants si :

$$
P(A \cap B) = P(A)P(B).
$$

Exemples :

lancer deux dés → “faire 6 au premier” et “obtenir un nombre pair au second” sont indépendants ;
tirer deux fois **sans remise** dans un sac n'est **pas indépendant**.

---

# Variables aléatoires

Une variable aléatoire associe un nombre à chaque issue.

Exemples :

1. somme obtenue avec deux dés,
1. montant gagné dans un jeu,
1. nombre d'appels reçus par heure.

---

# Espérance

L'espérance est la **moyenne théorique** de la variable aléatoire.

Si (X) prend les valeurs (x_i) avec probabilité (p_i) :

$$
E(X)=\sum x_i p_i.
$$

Exemple : gain d'un jeu

* +3 € avec probabilité 0.4
* -1 € avec probabilité 0.6

$$
E(X)=3(0.4) + (-1)(0.6)=1.2 - 0.6 = 0.6.
$$

On gagne en moyenne **0,60 € par partie**.

---

#  Variance

$$
\mathrm{Var}(X)=E[(X-E(X))^2].
$$

Mesure la dispersion autour de l'espérance.

Exemple :
Si (X) vaut 1 ou -1 avec probabilité 1/2 :

$$
E(X)=0,
$$

$$
\mathrm{Var}(X)=1^2(1/2) + (-1)^2(1/2) = 1.
$$

---

#  Loi binomiale (B(n,p))

Situation :
on répète **n expériences indépendantes**, chacune ayant une probabilité (p) de succès.

La variable :

$$
X = \text{nombre de succès}
$$

suit une loi binomiale :

$$
P(X=k)=\binom{n}{k}p^k (1-p)^{n-k}.
$$

Propriétés :

1. Espérance : (E(X)=np)
1. Variance : (np(1-p))

Exemple :
On tire 10 fois à pile ou face, (X=) nombre de piles.

$$
P(X=7)=\binom{10}{7}(1/2)^{10}.
$$

---


# Exercices d'entraînement

## Exercice 1

Un sac contient 3 boules rouges et 5 boules bleues.
On tire une boule au hasard.

1. Probabilité d'obtenir une rouge.
2. Probabilité de **ne pas** obtenir une bleue.

---

## Exercice 2

On lance deux dés.

1. Probabilité d'obtenir une somme égale à 9.
2. Probabilité que les deux dés montrent le même nombre.

---

## Exercice 3

On lance un dé baisé où :

1. (P(6)=0.2)
1. toutes les autres faces ont la même probabilité.

1. Quelle est la probabilité d'obtenir 1 ?
2. Quelle est l'espérance du résultat ?

---

## Exercice 4

Une machine réussit une opération avec probabilité (p = 0.8).
On la teste 5 fois.

1. Probabilité d'obtenir exactement 4 succès.
2. Espérance du nombre de succès.

---

## Exercice 5

$$X \sim \mathcal{N}(50, 4^2)$$.

1. Probabilité approximative que (X) soit dans ([46,54]).
2. Interpréter ce résultat.


# Apparition expérimentale de la loi normale à partir de la loi de Bernoulli

La loi normale ne tombe pas du ciel : elle apparaît naturellement lorsque l'on **additionne beaucoup de petites variables aléatoires indépendantes**.

Un cas très simple :
la **somme** de (n) variables de Bernoulli.

---

## 1. Rappel : loi de Bernoulli

Une variable (X) suit une **loi de Bernoulli(p)** si :

* (X = 1) avec probabilité (p),
* (X = 0) avec probabilité (1 - p).

C'est le modèle d'un **succès/échec**.

Exemple : pile = 1, face = 0.

---

## 2. Somme de variables Bernoulli → loi binomiale

Si on additionne (n) variables Bernoulli(p) indépendantes :

$$
S_n = X_1 + X_2 + \cdots + X_n,
]

alors (S_n \sim \text{Binom}(n, p)).

Plus (n) est grand :

* la distribution devient moins "discrète",
* sa forme se rapproche **très fortement** d'une loi normale.

---

## 3. Approche expérimentale avec NumPy

Voici un code Python que tes étudiants peuvent exécuter :

```python
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
p = 0.5         # probabilité du succès
n = 30          # nombre de Bernoulli additionnés
N = 100000      # nombre d'expériences simulées

# Simulation : N lois binomiales
samples = np.random.binomial(n, p, size=N)

# Histogramme normalisé
plt.hist(samples, bins=30, density=True, alpha=0.6)

# Ajout de la loi normale approchée
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(min(samples), max(samples), 200)
normal = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sigma**2))

plt.plot(x, normal)
plt.xlabel("Valeur observée")
plt.ylabel("Densité")
plt.title("Approche expérimentale de la loi normale")
plt.show()
```

---

## 4. Ce qu'on observe

Quand on trace l'histogramme des valeurs simulées :

* il commence à prendre **une forme en cloche**,
* centrée autour de (np),
* avec une largeur proportionnelle à (\sqrt{np(1-p)}).

Et lorsque l'on superpose la courbe normale, elle correspond presque parfaitement.

---

## 5. Pourquoi cela fonctionne ?

C'est une illustration du :

# Thème : Théorème Central Limite (TCL)

Le TCL affirme que :

> **La somme de nombreuses petites variables indépendantes tend vers une distribution normale**,
> même si les variables de départ ne sont pas normales.

Dans notre cas :

* Les Bernoulli sont très loin d'être normales (0 ou 1 uniquement !)
* Pourtant, leur somme s'approche d'une loi normale.

C'est une des raisons pour lesquelles la loi normale apparaît partout en statistique.

---

## 6. Exemple numérique simple à expliquer aux étudiants

Prenons (n = 30) tirages Bernoulli(0.5).

* moyenne théorique :

$$
\mu = np = 15
$$

* écart-type :

[
\sigma = \sqrt{np(1-p)} = \sqrt{30 \cdot 0.5 \cdot 0.5} \approx 2.74
$$

Le graphique issu du code montre :

1. un pic autour de 15,
1. une forme symétrique,
1. une cloche très proche de la densité normale.


#  Loi normale (résumé)

Beaucoup de phénomènes réels suivent une forme “courbe en cloche”.

Une variable (X) suit une loi normale :

$$
X \sim \mathcal{N}(\mu, \sigma^2),
$$

où :

$$\mu$$ = moyenne
$$\sigma$$ = écart-type

Propriétés essentielles :

68 % des valeurs dans $$[\mu - \sigma, \mu + \sigma]$$
95 % dans $$[\mu - 2\sigma, \mu + 2\sigma]$$
99.7 % dans $$[\mu - 3\sigma, \mu + 3\sigma]$$