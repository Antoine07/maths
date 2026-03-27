---
marp: true
theme: default
paginate: true
class: lead
html: true
---

# Statistiques descriptives avec NumPy

## Cours + corrections detaillees

---

## Objectifs

1. Utiliser `np.mean`, `np.median`, `np.var`, `np.std`, `np.percentile`
2. Distinguer population totale et echantillon
3. Comprendre l'impact de `ddof`
4. Calculer et interpreter `Q1`

---

## Convention importante : population vs echantillon

Population totale (on a tous les individus) :

1. variance population : `np.var(x, ddof=0)`
2. ecart-type population : `np.std(x, ddof=0)`

Echantillon (on estime une population) :

1. variance echantillon : `np.var(x, ddof=1)`
2. ecart-type echantillon : `np.std(x, ddof=1)`

---

## Exercice 1 - Ages

Donnees :

```python
import numpy as np
ages = np.array([12, 15, 14, 13, 16, 15], dtype=float)
```

---

## Exercice 1 - Moyenne et mediane

Consigne :

1. Calculez la moyenne avec NumPy
2. Calculez la mediane avec NumPy
3. Interpretez les 2 valeurs

<details>
<summary>Afficher la correction</summary>

```python
mean_age = np.mean(ages)
median_age = np.median(ages)

print(mean_age)    # 14.166666666666666
print(median_age)  # 14.5
```

$$
\bar{x}=\frac{85}{6}\approx 14.17,\qquad \text{Mediane}=14.5
$$

Interpretation : l'age central (mediane) est legerement au-dessus de la moyenne.
</details>

---

## Exercice 1 - Variance et ecart-type (population)

Consigne :

1. Calculez la variance population avec `ddof=0`
2. Calculez l'ecart-type population avec `ddof=0`
3. Comparez avec `ddof=1`

<details>
<summary>Afficher la correction</summary>

```python
var_pop = np.var(ages, ddof=0)
std_pop = np.std(ages, ddof=0)

var_sample = np.var(ages, ddof=1)
std_sample = np.std(ages, ddof=1)

print(var_pop, std_pop)        # 1.805555... 1.343709...
print(var_sample, std_sample)  # 2.166666... 1.471960...
```

Population totale :

$$
\text{Var}=\frac{1}{n}\sum (x_i-\bar{x})^2\approx 1.81,\qquad
\sigma\approx 1.35
$$

`ddof=1` donne une dispersion un peu plus grande car on corrige le biais d'echantillonnage.
</details>

---

## Exercice 3 - Tailles

Donnees :

```python
tailles = np.array([160, 170, 175, 150, 165], dtype=float)
```

Tableau d'effectifs :

| Taille   | 150 | 160 | 165 | 170 | 175 |
| -------- | --- | --- | --- | --- | --- |
| Effectif | 1   | 1   | 1   | 1   | 1   |

---

## Exercice 3 - Moyenne et dispersion (NumPy)

Consigne :

1. Calculez moyenne, variance, ecart-type (population)
2. Donnez les interpretations

<details>
<summary>Afficher la correction</summary>

```python
m = np.mean(tailles)
v = np.var(tailles, ddof=0)
s = np.std(tailles, ddof=0)

print(m, v, s)  # 164.0 74.0 8.602325267...
```

$$
\bar{x}=164,\qquad \text{Var}=74,\qquad \sigma\approx 8.60
$$

Interpretation : les tailles s'ecartent en moyenne d'environ 8.6 cm autour de 164 cm.
</details>

---

## Exercice 3 - Quartiles avec NumPy

Consigne :

1. Triez la serie
2. Calculez `Q1` avec la methode du cours (rang `(n+1)/4`)
3. Comparez avec la methode par defaut de NumPy

<details>
<summary>Afficher la correction</summary>

```python
x = np.sort(tailles)
q1_weibull = np.percentile(x, 25, method="weibull")  # methode (n+1)/4
q1_linear  = np.percentile(x, 25, method="linear")   # defaut NumPy

print(q1_weibull)  # 155.0
print(q1_linear)   # 160.0
```

Avec la methode du cours :

$$
r=\frac{n+1}{4}=\frac{6}{4}=1.5,
\qquad
Q_1=150+0.5(160-150)=155
$$

Point cle : pour etre coherent avec la correction du cours, utiliser `method="weibull"`.
</details>

---

## Resume des fonctions NumPy

1. `np.mean(x)` : moyenne
2. `np.median(x)` : mediane
3. `np.var(x, ddof=0)` : variance population
4. `np.std(x, ddof=0)` : ecart-type population
5. `np.percentile(x, 25, method="weibull")` : `Q1` version cours
