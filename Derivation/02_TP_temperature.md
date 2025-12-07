#  **TP : Analyse de données de température + mini API NumPy / FastAPI**

##  Objectifs du TP

Dans cet exercice, vous allez :

1. **simuler des données de température** sur 48 heures ;
2. **nettoyer** ces données ;
3. **construire une matrice NumPy** représentant les mesures ;
4. **calculer la dérivée numérique** de la température ;
5. **analyser les zones où la température monte / descend** ;
6. **produire des graphiques** ;
7. **exposer vos résultats dans une mini API FastAPI**.

---

# **Fonctions NumPy autorisées pour ce TP**

Pour guider votre travail, vous êtes autorisés à utiliser **uniquement** les fonctions suivantes :

### Création de vecteurs et matrices

* `np.array`
* `np.arange`
* `np.linspace`
* `np.zeros`, `np.ones`
* `np.column_stack`
* `np.vstack`

### Calculs numériques

* Opérations vectorisées `+`, `-`, `*`, `/`, `**`
* `np.sin`, `np.cos`
* `np.abs`
* `np.diff`
* `np.mean`

###  Extraction / filtrage

* Masques booléens :
  `mask = (T < seuil)`
  `T[mask] = valeur`
* `np.where`

### Affichage / informations

* `.shape`
* `T[:10]` (slicing)
* `print`

### (pour le graphique) Matplotlib :

* `plt.plot`
* `plt.scatter`
* `plt.figure`
* `plt.subplot`
* `plt.grid`
* `plt.show`

Ces fonctions suffisent pour réaliser tout le TP.

---

#  **Génération des données**

Vous devez :

1. Créer un vecteur `t` contenant les heures de 0 à 47.

2. Simuler une température réaliste à l’aide :

   * d’une **sinusoïde** (variation jour/nuit),
   * d’un **bruit aléatoire** (variations naturelles).

3. Visualiser les 10 premières valeurs.

> *But : obtenir une série temporelle bruitée.*

---

# **Nettoyage des données**

1. Identifier les valeurs aberrantes :

   * température < −5
   * température > 35
2. Créer un masque booléen.
3. Remplacer toute valeur aberrante par la moyenne de ses deux voisins immédiats.

> *But : obtenir une série réaliste et continue.*

---

# 🧭 **Étape 3 — Construction d’une matrice NumPy**

Créer une matrice ( M ) de taille 48 × 2 :

$$
M =
\begin{pmatrix}
t_0 & T_0 \
t_1 & T_1 \
\vdots & \vdots \
t_{47} & T_{47}
\end{pmatrix}
$$

Pour cela, utilisez **uniquement** :

* `np.column_stack((t, T))`

Puis afficher :

* la forme `M.shape`,
* les 5 premières lignes.

> *But : représenter proprement les données sous forme tabulaire.*

---

# **Dérivée numérique**

On calcule une dérivée discrète :

$$
T'(t_i) \approx T(t_{i+1}) - T(t_i)
$$

Vous devez :

1. Utiliser `np.diff` pour obtenir toutes les variations ;
2. Créer un vecteur des heures correspondantes ;
3. Visualiser les 10 premières valeurs de la dérivée.

> *But : mesurer l’évolution locale de la température.*

---

# **Analyse**

À partir du vecteur `dT` :

1. Trouvez l’heure où la température monte **le plus vite**.
2. Trouvez l’heure où elle baisse **le plus vite**.
3. Déterminez les heures où la température est **quasi stable**, c’est-à-dire :

$$
|T'(t)| < 0.1
$$

> *But : interpréter les résultats physiques.*

---

#  **Graphiques**

Créer deux graphiques :

1. **Température nettoyée** vs temps
2. **Dérivée numérique** vs temps

Chaque graphique doit contenir :

* un titre,
* des axes nommés,
* une grille,
* une ou deux séries (selon le cas).

🎯 *But : visualiser proprement vos résultats.*

---

# **Mini API FastAPI**

Créer un fichier `main.py` avec trois endpoints :

---

###  **Endpoint 1 – `/temperature`**

Entrées : `t` (heure)

Retourner en JSON :

* heure demandée,
* température correspondante,
* dérivée correspondante (approx).

---

### **Endpoint 2 – `/interval`**

Entrées : `t1`, `t2`

Retourner :

* liste des températures entre t1 et t2,
* moyenne,
* minimum,
* maximum.

---

### **Endpoint 3 – `/plot`**

Retourner un **PNG** généré avec Matplotlib :

* soit la courbe des températures,
* soit la courbe de dérivée,
* soit les deux superposées (au choix).

> *But : relier l’analyse mathématique à un service REST simple.*

---

# **Questions de réflexion**

Ajouter dans votre rapport :

1. Pourquoi la dérivée numérique est-elle une **approximation** de la dérivée réelle ?
2. Pourquoi le bruit rend-il la dérivée plus irrégulière ?
3. Quelles limites a le nettoyage par moyenne locale ?
4. Comment améliorer l’analyse (ex : moyenne glissante) ?
5. Comment généraliser ce TP à des données météo réelles ?
