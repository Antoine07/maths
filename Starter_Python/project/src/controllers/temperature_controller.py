"""
TP Températures – Correction complète (Version Controller)

Ce fichier contient :

- La génération et le nettoyage de données de température
- Le calcul de la dérivée numérique
- Trois endpoints REST (via APIRouter)
    /temperature
    /interval
    /plot

À importer dans main.py via :
    from controllers.temperature_controller import router
    app.include_router(router, prefix="/temperature-api")
"""

import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse


# --------------------------------------------------------------------
# ROUTER FASTAPI
# --------------------------------------------------------------------
router = APIRouter(tags=["TP Températures"])


# --------------------------------------------------------------------
# 1. GÉNÉRATION DES DONNÉES DE TEMPÉRATURE
# --------------------------------------------------------------------

N_HOURS = 48
t = np.arange(0, N_HOURS, 1)

np.random.seed(0)
noise = np.random.normal(loc=0.0, scale=0.5, size=t.size)

T_raw = 10 + 5 * np.sin((2 * np.pi / 24) * t) + noise


# --------------------------------------------------------------------
# 2. NETTOYAGE DES DONNÉES
# --------------------------------------------------------------------

T_clean = T_raw.copy()
outlier_mask = (T_clean < -5) | (T_clean > 35)
outlier_indices = np.where(outlier_mask)[0]

for i in outlier_indices:
    if i == 0:
        T_clean[i] = T_clean[i + 1]
    elif i == len(T_clean) - 1:
        T_clean[i] = T_clean[i - 1]
    else:
        T_clean[i] = 0.5 * (T_clean[i - 1] + T_clean[i + 1])


# --------------------------------------------------------------------
# 3. MATRICE DES DONNÉES
# --------------------------------------------------------------------
M = np.column_stack((t, T_clean))


# --------------------------------------------------------------------
# 4. DÉRIVÉE NUMÉRIQUE
# --------------------------------------------------------------------
dT = np.diff(T_clean)
t_dT = t[:-1]

idx_up = int(np.argmax(dT))
idx_down = int(np.argmin(dT))

hour_up = t_dT[idx_up]
hour_down = t_dT[idx_down]

stable_indices = np.where(np.abs(dT) < 0.1)[0]
stable_hours = t_dT[stable_indices]


# --------------------------------------------------------------------
# UTILITAIRE
# --------------------------------------------------------------------
def get_temperature_and_derivative(hour: int):
    if hour < 0 or hour >= N_HOURS:
        raise ValueError("Heure hors intervalle [0, 47].")

    temp = float(T_clean[hour])
    deriv = float(dT[hour]) if hour < N_HOURS - 1 else None
    return temp, deriv


# --------------------------------------------------------------------
# ENDPOINT 1 : /temperature
# --------------------------------------------------------------------
@router.get("/temperature")
def temperature_endpoint(t: int):
    if t < 0 or t >= N_HOURS:
        raise HTTPException(status_code=400, detail="t doit être dans [0, 47].")

    temp, deriv = get_temperature_and_derivative(t)

    return JSONResponse({
        "heure": t,
        "temperature": temp,
        "derivee_approx": deriv,
        "commentaire": (
            "La dérivée approx représente ΔT entre t et t+1."
            if deriv is not None
            else "Pas de dérivée possible à t = 47 (pas de point suivant)."
        )
    })


# --------------------------------------------------------------------
# ENDPOINT 2 : /interval
# --------------------------------------------------------------------
@router.get("/interval")
def interval_endpoint(t1: int, t2: int):
    if t1 < 0 or t2 < 0 or t1 >= N_HOURS or t2 >= N_HOURS:
        raise HTTPException(status_code=400, detail="t1 et t2 doivent être dans [0, 47].")

    if t2 < t1:
        raise HTTPException(status_code=400, detail="t2 doit être ≥ t1.")

    slice_values = T_clean[t1:t2 + 1]

    return JSONResponse({
        "t1": t1,
        "t2": t2,
        "nb_points": len(slice_values),
        "temperature_moyenne": float(np.mean(slice_values)),
        "temperature_min": float(np.min(slice_values)),
        "temperature_max": float(np.max(slice_values)),
    })


# --------------------------------------------------------------------
# ENDPOINT 3 : /plot
# --------------------------------------------------------------------
@router.get("/plot")
def plot_endpoint():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax1 = axes[0]
    ax1.plot(t, T_clean, marker="o")
    ax1.set_title("Température nettoyée")
    ax1.set_xlabel("Heure")
    ax1.set_ylabel("°C")
    ax1.grid(True)

    ax2 = axes[1]
    ax2.plot(t_dT, dT, marker="o", color="red")
    ax2.set_title("Dérivée numérique")
    ax2.set_xlabel("Heure")
    ax2.set_ylabel("ΔT (°C)")
    ax2.grid(True)

    fig.suptitle("Évolution de la température et de sa dérivée", fontsize=14)

    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    plt.close(fig)
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")
