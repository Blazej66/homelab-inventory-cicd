# homelab-inventory-cicd

![CI/CD](https://github.com/Blazej66/homelab-inventory-cicd/actions/workflows/ci.yml/badge.svg)

Simple Flask + PostgreSQL REST API for tracking homelab devices, fronted by Nginx and automated via GitHub Actions (`pytest` + Docker build & push to `ghcr.io`).

## Stack
* **API:** Python 3.12, Flask, Gunicorn, SQLAlchemy (`psycopg`)
* **DB & Proxy:** PostgreSQL 16, Nginx 1.27
* **CI/CD & Host:** GitHub Actions → GHCR → Debian 13 VM (Proxmox)

## Quick Start
```bash
docker compose pull
docker compose up -d
curl http://localhost:8080/health

Simple Flask + PostgreSQL REST API for tracking homelab devices, fronted by Nginx and automated via GitHub Actions (`pytest` + Docker build & push to `ghcr.io`).

## Stack
* **API:** Python 3.12, Flask, Gunicorn, SQLAlchemy (`psycopg`)
* **DB & Proxy:** PostgreSQL 16, Nginx 1.27
* **CI/CD & Host:** GitHub Actions → GHCR → Debian 13 VM (Proxmox)

## Quick Start
```bash
docker compose pull
docker compose up -d
curl http://localhost:8080/health
