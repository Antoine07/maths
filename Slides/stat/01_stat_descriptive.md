---
marp: true
theme: default
paginate: true
class: lead
html: true
---

# Statistiques descriptives

## Cours

---

## Objectifs

1. Calculer moyenne, mediane, variance, ecart-type
2. Lire un tableau d'effectifs
3. Determiner le quartile Q1

---

## Exercice 1 - Ages

Donnees :

```text
12, 15, 14, 13, 16, 15
```

---

## Exercice 1 - Moyenne

Consigne :

1. Calculez la moyenne de la serie
2. Interpretez le resultat

<details>
<summary>Afficher la correction</summary>

$$
\bar{x}=\frac{12+15+14+13+16+15}{6}=\frac{85}{6}\approx 14.17
$$

Interpretation : age moyen du groupe = 14.17 ans.
</details>

---

## Exercice 1 - Mediane

Serie triee :

```text
12, 13, 14, 15, 15, 16
```

Consigne :

1. Identifiez les deux valeurs centrales
2. Calculez la mediane

<details>
<summary>Afficher la correction</summary>

Il y a 6 valeurs, donc mediane = moyenne des 2 valeurs centrales :

$$
\text{Mediane}=\frac{14+15}{2}=14.5
$$
</details>

---

## Exercice 1 - Ecart-type

Consigne :

$$
\bar{x}=\frac{1}{n}\sum x_i,\qquad
\text{Var}=\frac{1}{n}\sum(x_i-\bar{x})^2,\qquad
\sigma=\sqrt{\text{Var}}
$$

Calculez ensuite la variance et l'ecart-type.

<details>
<summary>Afficher la correction</summary>

Avec $$\bar{x}\approx 14.17$$ :

$$
\sum (x_i-\bar{x})^2 \approx 10.85
$$

$$
\text{Var}=\frac{10.85}{6}\approx 1.81
$$

$$
\sigma=\sqrt{1.81}\approx 1.35
$$
</details>

---

## Exercice 3 - Tailles

Donnees :

```text
160, 170, 175, 150, 165
```

Tableau d'effectifs :

| Taille   | 150 | 160 | 165 | 170 | 175 |
| -------- | --- | --- | --- | --- | --- |
| Effectif | 1   | 1   | 1   | 1   | 1   |

---

## Exercice 3 - Moyenne et dispersion

Consigne :

1. Calculez la moyenne
2. Calculez la variance
3. Calculez l'ecart-type

<details>
<summary>Afficher la correction</summary>

$$
\bar{x}=\frac{150+160+165+170+175}{5}=164
$$

$$
\text{Var}=\frac{(150-164)^2+(160-164)^2+(165-164)^2+(170-164)^2+(175-164)^2}{5}=74
$$

$$
\sigma=\sqrt{74}\approx 8.60
$$
</details>

---

## Exercice 3 - Quartile Q1

Donnees triees :

```text
150, 160, 165, 170, 175
```

Consigne : determinez $$Q_1$$ avec la methode vue en cours.

<details>
<summary>Afficher la correction</summary>

$$
Q_1=155
$$
</details>

---

## Aide methode

Methode interpolation :

$$
r=\frac{n+1}{4}
$$

Puis interpolation entre les deux valeurs encadrant le rang.

Ne pas afficher le resultat final sur cette slide.

<details>
<summary>Afficher la correction</summary>

Avec $$n=5$$ :

$$
r=\frac{n+1}{4}=\frac{6}{4}=1.5
$$

Interpolation entre 150 et 160 :

$$
Q_1=150+0.5(160-150)=155
$$
</details>

---

## Resume

1. Moyenne : niveau global
2. Mediane : valeur centrale robuste
3. Ecart-type : dispersion autour de la moyenne
4. Quartiles : position de la serie en 4 parties
