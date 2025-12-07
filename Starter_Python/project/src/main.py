from fastapi import FastAPI
from fastapi.responses import JSONResponse, StreamingResponse
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

app = FastAPI(title="TP – Analyse d'une fonction avec FastAPI")
from controllers.temperature_controller import router as temperature_router


app.include_router(temperature_router, prefix="/temperature-api")

# -----------------------------------------------------------
# 1. Modèle mathématique simple : T(x,y) = x² + 2y
#    ∇T(x,y) = (2x, 2)
# -----------------------------------------------------------

def T(x, y):
    return x**2 + 2*y

def grad_T(x, y):
    return np.array([2*x, 2.0])


# -----------------------------------------------------------
# 2. Endpoint REST : renvoie T(x,y) et son gradient
# -----------------------------------------------------------

@app.get("/temperature")
def compute_temperature(x: float, y: float):
    """
    Calcule la température T(x,y) et le gradient au point (x,y).
    Exemple d'appel :
    http://localhost:8000/temperature?x=1&y=2
    """
    value = T(x, y)
    gradient = grad_T(x, y).tolist()

    return JSONResponse({
        "inputs": {"x": x, "y": y},
        "temperature": value,
        "gradient": {
            "dT_dx": gradient[0],
            "dT_dy": gradient[1],
            "vector": gradient
        },
        "interpretation": (
            "Le gradient indique la direction de variation maximale. "
            "Ici, augmenter x ou y augmente la température."
        )
    })


# -----------------------------------------------------------
# 3. Endpoint REST : approximation linéaire
#    ΔT ≈ grad(T) ⋅ Δx
# -----------------------------------------------------------

@app.get("/variation")
def variation_temperature(x: float, y: float, dx: float, dy: float):
    """
    Approximation locale :
    ΔT ≈ ∇T(x,y) · (dx, dy)
    Exemple :
    http://localhost:8000/variation?x=1&y=2&dx=0.1&dy=-0.05
    """

    g = grad_T(x, y)
    delta_vec = np.array([dx, dy])
    delta_T_approx = float(g @ delta_vec)

    # Valeur réelle
    real = T(x + dx, y + dy) - T(x, y)

    return JSONResponse({
        "point": (x, y),
        "variation": {"dx": dx, "dy": dy},
        "delta_T_approx": delta_T_approx,
        "delta_T_real": real,
        "difference": real - delta_T_approx
    })


# -----------------------------------------------------------
# 4. Endpoint REST : renvoi d'un graphique PNG
# -----------------------------------------------------------

@app.get("/plot")
def plot_temperature():
    """
    Renvoie une carte de chaleur de T(x,y) = x² + 2y.
    Exemple :
    http://localhost:8000/plot
    """
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = T(X, Y)

    fig, ax = plt.subplots(figsize=(6, 5))
    c = ax.contourf(X, Y, Z, levels=20, cmap="coolwarm")
    plt.colorbar(c, ax=ax)
    ax.set_title("Carte de température : T(x,y) = x² + 2y")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")


# -----------------------------------------------------------
# 5. Lancement du serveur :
# -----------------------------------------------------------
# uvicorn main:app --reload
