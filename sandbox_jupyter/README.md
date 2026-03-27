# Sandbox JupyterLab (Docker Compose)

## Prerequis

- Docker
- Docker Compose v2 (`docker compose`)

## Lancer le sandbox

Depuis la racine du projet :

```bash
cd sandbox_jupyter
docker compose up -d --build
```

JupyterLab sera disponible sur :

- http://localhost:8888
- Sans token (authentification desactivee)

## Arreter

```bash
cd sandbox_jupyter
docker compose down
```

## Notes

- Le dossier projet complet est monte dans `/workspace` (volume `../:/workspace`).
- Stack Python installee : `numpy`, `pandas`, `jupyterlab`.
