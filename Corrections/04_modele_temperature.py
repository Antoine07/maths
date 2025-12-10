import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
#  Données de l'exercice
# -----------------------------
T = np.array([
    8.0, 8.2, 8.5, 9.0, 9.3, 9.5, 10.1, 10.4, 
    10.6, 11.0, 11.2, 11.4, 11.7, 12.0, 12.1, 
    12.5, 12.6, 12.9, 13.0, 13.1, 13.4, 13.5, 
    13.7, 14.0, 14.2, 14.3, 14.5, 14.8, 15.0, 15.2
])

# Vecteur des jours t = 1 à 30
t = np.arange(1, len(T) + 1)


# -----------------------------
#  Ajustement linéaire
# -----------------------------
a, b  = np.polyfit(t, T, 1)   # ajustement degré 1

# Modèle estimé
T_model = a * t + b

# -----------------------------
#  Affichage des résultats
# -----------------------------
print("Modèle linéaire obtenu :  T(t) = a t + b")
print(f"a = {a:.4f}  (pente : variation quotidienne moyenne)")
print(f"b = {b:.4f}")

# Température prédite pour les jours du mois
print("\nPrévision du jour 35 :", a * 35 + b)

# -----------------------------
#  Graphique
# -----------------------------
plt.figure(figsize=(10,5))
plt.scatter(t, T, color="blue", label="Températures observées")
plt.plot(t, T_model, color="red", linewidth=2, label="Modèle linéaire")

plt.title("Évolution de la température moyenne – Modèle linéaire")
plt.xlabel("Jour du mois")
plt.ylabel("Température (°C)")
plt.grid(alpha=0.3)
plt.legend()
plt.show()