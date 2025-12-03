# **La dérivée seconde en dimension 1**

Considérons une fonction d'une variable :
$$
f : \mathbb{R} \to \mathbb{R}.
$$

## **1. Définition**

La **dérivée seconde** est la dérivée de la dérivée première :
$$
f''(x) = \frac{d}{dx}\left(f'(x)\right).
$$

Elle mesure **comment la pente change** quand on se déplace le long de l'axe des (x).

---

## **2. Interprétation géométrique**

* La **dérivée première** ( f'(x) ) = la **pente** du graphe de (f).
* La **dérivée seconde** ( f''(x) ) = la **variation** de cette pente.

Autrement dit :

* **Si ( f''(x) > 0 )** → la pente **augmente** → le graphe se courbe **vers le haut** (∪).
  Même si la pente ( f'(x) ) est négative au départ, elle **devient de moins en moins négative**, puis positive : elle **augmente continuellement**.

* **Si ( f''(x) < 0 )** → la pente **diminue** → le graphe se courbe **vers le bas** (∩).
  Même si la pente est positive au départ, elle **devient de moins en moins positive**, puis négative : elle **diminue continuellement**.

Le signe de ( f'' ) indique **comment évolue la pente**,
et cette évolution dicte la **courbure** de la fonction.

# **Rappel — Convexité / Concavité en dimension 1**

Pour une fonction $$f : \mathbb{R} \to \mathbb{R}$$ deux fois dérivable :

* **( f''(x) > 0 )** sur un intervalle → ( f ) est **convexe** sur cet intervalle (cuvette ∪).
* **( f''(x) < 0 )** sur un intervalle → ( f ) est **concave** sur cet intervalle (dôme ∩).
* **( f''(x) = 0 )** → critère insuffisant à ce point; observer les signes autour.

# **Rappel sur le point d'inflexion** est un point où **la courbure du graphe change de signe**

> C'est un point où la fonction passe d'une forme **concave** (∩) à **convexe** (∪),
> ou inversement.

Soit une fonction deux fois dérivable ( f ).

Un point ( x_0 ) est un **point d'inflexion** si :

1. $$f''(x_0) = 0$$ (condition nécessaire),
2. $$f''$$ **change de signe** en ( x_0 ) (condition essentielle).

Cela signifie :

* soit $$f'' < 0$$ avant et $$f'' > 0$$ après → ∩ devient ∪,
* soit $$f'' > 0$$ avant et $$f'' < 0$$ après → ∪ devient ∩.

---

# Interprétation géométrique

C'est un point où la forme du graphe :

* **se renverse**,
* passe d'un "dôme" à une "cuvette", ou l'inverse.

Visuellement, c'est un point où la courbe a une **tangente qui traverse le graphe**.


# **Exercice 1 — Étude du signe de ( f'' ) et de la courbure**

On considère la fonction :
$$
f(x) = x^3 - 3x.
$$

1. Calculer ( f'(x) ) puis ( f''(x) ).
2. Étudier le signe de ( f''(x) ).
3. Déterminer sur quels intervalles la fonction se courbe **vers le haut** et **vers le bas**.
4. Expliquer ce que cela signifie pour l'évolution de la pente.

**Objectif :**
Identifier les zones convexes (∪), concaves (∩) et comprendre comment la pente change.

---

# **Exercice 2 — Interprétation de la pente et de la dérivée seconde**

Soit la fonction :
$$
g(x) = -x^2 + 4x.
$$

1. Calculer la pente ( g'(x) ).
2. Calculer la dérivée seconde ( g''(x) ).
3. Déterminer si la pente **augmente** ou **diminue** sur ℝ.
4. Conclure sur la forme du graphe : **cuvette** (∪) ou **dôme** (∩).
5. Indiquer si le sommet de la parabole est un **maximum** ou un **minimum**.

**Objectif :**
Vérifier la relation :

( g'' < 0 ) ↔ pente qui diminue ↔ dôme ↔ maximum.


---

# **Exercice 3 - Interprétation de la pente et de la dérivée seconde**

On considère la fonction :
$$
f(x) = x^4 - 2x^2 + 3.
$$

1. Calculer ( f'(x) ).
2. Calculer ( f''(x) ).
3. Étudier le signe de ( f''(x) ).
4. Déterminer sur quels intervalles ( f ) est **convexe** et sur quels intervalles elle est **concave**.
5. Repérer les éventuels **points d'inflexion**.

---


## **3. Rôle pour étudier les extrema**

Pour un **point critique** où $$f'(x_0) = 0$$

* Si $$f''(x_0) > 0$$ → **minimum local**.
---
* Si $$f''(x_0) < 0$$ → **maximum local**.
---
* Si $$f''(x_0) = 0$$ → test insuffisant (on doit analyser plus finement).
---

Ainsi, la dérivée seconde joue en dimension 1 exactement le rôle que la **hessienne** jouera en dimension supérieure.

---

## **4. Exemple simple**

Prenons :
$$
f(x)=x^2
$$

$$f'(x)=2x$$
$$f''(x)=2$$

Comme $$f''(x)=2>0$$ partout, la fonction est **convexe** et possède un **minimum en ( x=0 )**.

---

## **5. Lien avec la hessienne**

En dimension 1 :
$$
H_f = (f''(x)),
$$
c'est-à-dire que la hessienne **se réduit exactement à la dérivée seconde**.

Ce que vous faites avec ( f'' ) en dimension 1, vous le ferez avec la **hessienne** en dimension supérieure :

* étudier la courbure,
* déterminer min/max/selle,
* analyser la convexité.

---

# ✔︎ Exemple simple

Pour
$$
f(x)=x^3,
$$
on a :
$$
f''(x)=6x.
$$

* ( f''(x) < 0 ) si ( x < 0 ) → concave (∩)
* ( f''(x) > 0 ) si ( x > 0 ) → convexe (∪)

→ En ( x = 0 ), le signe change : c'est un **point d'inflexion**.


> **Un point d'inflexion est un point où la courbe change de forme : de concave à convexe ou de convexe à concave.**


# **Qu'est-ce que le gradient ?**

**Idée générale :**
Le gradient est un outil qui décrit **comment une fonction varie** quand on se déplace dans l'espace.

Pour une fonction à plusieurs variables
$$
f(x,y,\dots)
$$
le gradient est le vecteur :
$$
\nabla f = \left(
\frac{\partial f}{\partial x},,
\frac{\partial f}{\partial y},\dots
\right)
$$

**À retenir :**

* Chaque composante du gradient → la pente selon une variable.
* Le gradient pointe vers la **direction où la fonction augmente le plus vite**.

**Exemple simple :**
$$
f(x,y) = x^2 + y^2
$$
$$
\nabla f = (2x,, 2y)
$$

---

# **Interprétation géométrique**

Imaginez une colline représentée par une fonction ( f(x,y) ).

* Le gradient vous indique **la direction la plus raide pour monter**.
* Le vecteur opposé au gradient indique **la direction la plus raide pour descendre**.

**Idée clé :**
Le gradient est **perpendiculaire** aux courbes de niveau (lignes où la fonction est constante).

**Exemple visuel (à imaginer) :**
Pour ( f(x,y) = x^2 + y^2 ) :

* les courbes de niveau sont des cercles,
* le gradient pointe toujours *vers l'extérieur* (plus on s'éloigne du centre, plus ( f ) augmente).

---

# **Comment calcule-t-on un gradient ?**

1. On dérive ( f ) par rapport à chaque variable.
2. On range ces dérivées dans un vecteur.

**Exemple 1**
$$
f(x,y) = x^2 + xy
$$
$$
f_x = 2x + y, \quad f_y = x
$$
$$
\nabla f = (2x + y,\ x)
$$

**Exemple 2**
$$
f(x,y,z) = x^2 + y^2 + 3z
$$
$$
\nabla f = (2x,\ 2y,\ 3)
$$

**Remarque :**
Si une variable n'apparaît pas → la dérivée par rapport à elle est 0.

---

# **Pourquoi le gradient est-il utile ?**

Le gradient permet de comprendre **comment une fonction se comporte localement**.

### Applications mathématiques essentielles :

* Trouver des **points critiques** (là où le gradient vaut 0).
* Étudier les **minimums et maximums** locaux.
* Comprendre la **géométrie** et la **courbure** d'une fonction.

### Exemple : point critique

$$
f(x,y) = x^2 + y^2
$$
$$
\nabla f = (2x, 2y)
$$
Annuler le gradient →
$$
2x = 0,\quad 2y = 0
$$
→ point critique : ((0,0)), qui est un **minimum**.


Voici la **suite naturelle du cours**, exactement dans le même style que ce que vous avez commencé :
→ **un exemple détaillé**
→ **une introduction progressive à la hessienne**
→ **explication de son rôle dans l'étude d'un point critique.**

---

# **Exemple complet : étude locale de** ( f(x,y) = x^2 + y^2 )

Dans cet exemple, on utilise le gradient pour trouver un point critique, puis la hessienne pour comprendre **la nature** de ce point.

### **1. Calcul du gradient**

On a :
$$
\nabla f = (2x,\ 2y)
$$

Le point critique s'obtient en annulant le gradient :
$$
2x=0,\quad 2y=0 \quad \Rightarrow \quad (0,0).
$$

**Conclusion :**
((0,0)) est le seul point où la fonction peut avoir un minimum, un maximum ou un point selle.
Mais *quel est-il* ?
→ Le **gradient ne permet pas d'y répondre**.
→ Il faut examiner la **hessienne**.

---

# **Introduction à la hessienne**

La **hessienne** est l'outil qui permet d'étudier la **courbure** d'une fonction de plusieurs variables, exactement comme la dérivée seconde en dimension 1.

Pour une fonction à deux variables
$$
f(x,y),
$$
la hessienne est la matrice :
$$
H_f(x,y)
========

\begin{pmatrix}
f_{xx} & f_{xy} \
f_{yx} & f_{yy}
\end{pmatrix},
$$
où :

* (f_{xx}) mesure la courbure selon l'axe (x),
* (f_{yy}) mesure la courbure selon (y),
* (f_{xy}) et (f_{yx}) mesurent la manière dont les deux variables interagissent.

**Idée géométrique :**
La hessienne décrit **comment la surface se courbe autour d'un point**.

---

# **Calcul de la hessienne dans notre exemple**

Pour
$$
f(x,y)=x^2+y^2,
$$
les dérivées secondes sont :

$$
f_{xx}=2,\quad f_{yy}=2,\quad f_{xy}=0.
$$

Donc :
$$
H_f(x,y) =
\begin{pmatrix}
2 & 0 \
0 & 2
\end{pmatrix}.
$$

Cette matrice a deux propriétés essentielles :

1. **Elle est diagonale.**
   → les directions principales sont simplement les axes (x) et (y).

2. **Ses valeurs propres sont positives :**
   $$
   \lambda_1 = 2,\quad \lambda_2 = 2.
   $$

---

# **Interprétation : rôle du hessien sur la nature du point critique**

La hessienne permet de trancher :

* Si toutes les valeurs propres sont **positives**, la surface est **courbée vers le haut** → **minimum local**.
* Si elles sont **négatives**, la surface est **courbée vers le bas** → **maximum local**.
* Si elle change de signe → **point selle**.

Dans notre cas :
$$
\lambda_1 = \lambda_2 = 2 > 0.
$$

→ la hessienne est **définie positive**
→ la fonction est **localement convexe**
→ le point critique ((0,0)) est un **minimum**.

### **Image mentale :**

La surface est un bol parfaitement symétrique.
La hessienne « voit » cette courbure et conclut qu'on est au fond du bol.

---

# **Résumé de la démarche**

| Étape | Outil           | Rôle                         |
| ----- | --------------- | ---------------------------- |
| 1     | Gradient        | trouver les points critiques |
| 2     | Hessienne       | analyser la courbure locale  |
| 3     | Valeurs propres | déterminer min / max / selle |
