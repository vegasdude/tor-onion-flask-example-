# tor-onion-flask-example

A minimal example of running a Flask web app as a Tor hidden service.

## Files
- `app.py` – simple Flask app
- `Dockerfile` – builds the Python app
- `docker-compose.yml` – runs Flask + Tor together
- `torrc` – Tor configuration
- `.gitignore` – prevents secrets and temporary files from being uploaded

## Notes
This is for educational and development use only.  
**Do not upload any private keys or real hidden service credentials to GitHub.**

## Run locally
```bash
docker-compose up
