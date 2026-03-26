---
marp: true
theme: default
paginate: true
class: lead
html: true
---

# Covariance et correlation

## Cours

---

## Exercice 2 - Donnees

| X | 1 | 2 | 3 |
| - | - | - | - |
| Y | 2 | 4 | 5 |

Consigne :

1. Calculez $$\bar{x}$$
2. Calculez $$\bar{y}$$

<details>
<summary>Afficher la correction</summary>

$$
\bar{x}=2,\qquad \bar{y}=\frac{11}{3}
$$
</details>

---

## Exercice 2 - Covariance

Formule :

$$
\mathrm{Cov}(X,Y)=\frac{1}{3}\sum (x_i-\bar{x})(y_i-\bar{y})
$$

Travail a faire :

1. Calculez chaque terme $$(x_i-\bar{x})(y_i-\bar{y})$$
2. Deducez la covariance

<details>
<summary>Afficher la correction</summary>

Termes :

$$
\frac{5}{3},\ 0,\ \frac{4}{3}
$$

Donc :

$$
\mathrm{Cov}(X,Y)=\frac{1}{3}\left(\frac{5}{3}+0+\frac{4}{3}\right)=1
$$
</details>

---

## Exercice 2 - Correlation

$$
\rho=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}
$$

Consigne :

1. Calculez $$\sigma_X$$ et $$\sigma_Y$$
2. Calculez $$\rho$$
3. Interpretez le signe et l'intensite

<details>
<summary>Afficher la correction</summary>

$$
\sigma_X=\sqrt{\frac{2}{3}},\qquad \sigma_Y=\frac{\sqrt{14}}{3}
$$

$$
\rho=\frac{1}{\sigma_X\sigma_Y}\approx 0.98
$$

Interpretation : tres forte correlation lineaire positive.
</details>

---

## Exercice 4 - Lire un coefficient de correlation

Interpretez :

1. $$\rho = 0.92$$
2. $$\rho = -0.45$$
3. $$\rho = 0$$

<details>
<summary>Afficher la correction</summary>

1. $$\rho = 0.92$$ : lien lineaire tres fort positif
2. $$\rho = -0.45$$ : lien lineaire negatif modere
3. $$\rho = 0$$ : pas de lien lineaire detectable
</details>

---

## Rappel important

Correlation forte ne veut pas dire causalite.

Toujours verifier avec :

1. un nuage de points
2. le contexte metier / physique
3. des variables explicatives plausibles

---

## Resume

1. Covariance : sens global de variation commune
2. Correlation : intensite normalisee entre -1 et +1
3. Toujours completer avec une lecture graphique
