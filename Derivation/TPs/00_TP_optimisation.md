# TP Optimisation 

## Problème : optimisation d'un coût de production (maths + data + Python)

Une entreprise produit un bien.
Pour un niveau de production x (en milliers d'unités), son coût total est modélisé par :

$$
C(x) = 40x + 2000 - 500 e^{-0.5x}
$$

(1) Le terme 40x : coût linéaire.
(2) Le terme 2000 : coût fixe.
(3) Le terme 

$$
-500 e^{-0.5x}
$$

Apprentissage => plus on produit, plus on devient efficace, donc le coût baisse au début, mais cet effet s'atténue.

On veut répondre à une question data très courante :
Quel niveau de production minimise le coût moyen par unité ?
En effet, une entreprise cherche non pas seulement à réduire le coût total, mais surtout à réduire le coût par produit.

---

1. Étude mathématique

On étudie la fonction coût moyen :

$$
M(x) = \frac{C(x)}{x}
= 40 + \frac{2000}{x} - 500\frac{e^{-0.5x}}{x}.
$$

Objectif : trouver le minimum de M(x).

a) Domaine

x>0.

---

2. Dérivée de M(x) pour justifiez si il existe un nimimum.

2.1 Créez une fonction en Python pour trouver cette valeur si elle existe, utilisez la fonction `np.argmin` de Numpy.

```python
def M(x):
   pass
xs = np.linspace(0.1, 50, 10000)
Ms = M(xs)
```

3. Donnez la production optimal

