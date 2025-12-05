# Dérivation

## 1. Définition intuitive de la dérivée

La dérivée d’une fonction (f) en un point (x) mesure **la pente de la courbe** de (f) à ce point.
On l’interprète comme la vitesse de variation :

$$
f'(x) = \text{pente de la tangente au point } x.
$$

Si :

* (f'(x) > 0) : la fonction **augmente** (pente positive).
* (f'(x) < 0) : la fonction **diminue** (pente négative).
* (f'(x) = 0) : la courbe a une **tangente horizontale** (candidats aux extremums).

---

## 2. Fonction dérivable

Une fonction est dérivable sur un intervalle si sa pente existe en tout point.
Notation :

$$
f : I \to \mathbb{R}, \quad f'(x) \text{ existe pour tout } x \in I.
$$

---

# 3. Règles de dérivation

### 3.1. Dérivées usuelles

$$
(x^n)' = nx^{n-1}
$$

$$
(\sqrt{x})' = \frac{1}{2\sqrt{x}}
$$

$$
(e^x)' = e^x
$$

$$
(\ln(x))' = \frac{1}{x}
$$

### Fonctions trigonométriques

$$
(\sin x)' = \cos x
$$

$$
(\cos x)' = -\sin x
$$

---

### 3.2. Règles de calcul

1. **Somme**

$$
(f+g)' = f' + g'
$$

2. **Produit**

$$
(fg)' = f'g + fg'
$$

3. **Quotient**

$$
\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2} \qquad (g \neq 0)
$$

4. **Composition** (chaîne)

$$
f(g(x))' = f'(g(x)) \cdot g'(x)
$$

# 4. Dérivée et sens de variation

Pour étudier une fonction, on :

1. calcule sa dérivée (f'),
2. étudie le signe de (f'),
3. remplit un tableau de variation.

Règle fondamentale :

* (f'(x) > 0) : (f) **croît**,
* (f'(x) < 0) : (f) **décroît**,
* (f'(x) = 0) : points critiques (minima, maxima possibles).

---

# 5. Dérivée seconde et courbure (rappel utile)

La dérivée seconde est la dérivée de la dérivée :

$$
f''(x) = (f'(x))'.
$$

Elle indique la **courbure** :

* (f''(x) > 0) : la courbe est **convexe** (pente augmente),
* (f''(x) < 0) : la courbe est **concave** (pente diminue).

---

# 6. Exemples corrigés

## Exemple 1 : $$(f(x) = x^3 - 3x)$$

1. Dérivée :

$$
f'(x) = 3x^2 - 3.
$$

2. Signe :

$$
f'(x)=0 \iff 3x^2-3=0 \iff x^2=1 \iff x=\pm 1.
$$

3. Variation :

* $$(f'>0) pour (x<-1)$$
* $$(f'<0) pour (-1<x<1)$$
* $$(f'>0) pour (x>1)$$

La fonction décroît puis croît → minimum local en (x=1), maximum local en (x=-1).

---

## Exemple 2 : Fonction avec quotient

$$f(x)=\frac{x^2-1}{x} (sur \mathbb{R}\setminus{0})$$

$$
f'(x)=\frac{2x^2 - (x^2 - 1)}{x^2} = \frac{x^2 + 1}{x^2}.
$$

Comme $$x^2+1>0$$, on obtient :

$$
f'(x) > 0 \quad \text{pour tout } x\neq 0.
$$

La fonction est **strictement croissante** sur chaque intervalle de son domaine.

---

## Exemple 3 : Composition

$$(f(x) = e^{3x})$$

$$
f'(x) = 3 e^{3x}.
$$

Toujours positif → fonction strictement croissante.

---

# 7. Exercices d’entraînement

## Exercice 1

Dériver :

a) $$f(x)=x^4 - 2x^2 + 1$$

b) $$g(x)=\sqrt{x}(x^2+3)$$

c) $$h(x)=\frac{3x+1}{x-2}$$

---

## Exercice 2

Étudier les variations de :

a) $$f(x)=x^3+3x^2$$

b) $$g(x)=\ln(x) - x$$

c) $$h(x)=e^{-x}$$

---

## Exercice 3

Trouver les maxima/minima de :

a) $$f(x)=x^2 - 4x +1$$

b) $$g(x)=x + \frac{1}{x})$$ sur $$\mathbb{R}^{+}$$

c) $$h(x)=\sin x + x$$

---

## Exercice 4

Étudier la convexité de :

a) $$f(x)=x^4$$

b) $$g(x)=x e^x$$

c) $$h(x)=\ln(x)$$
