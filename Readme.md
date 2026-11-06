# FinTech Transaction Scoring Engine

A mock high-availability payment processing API built for enterprise Kubernetes environments. 

## Tech Stack
* **App:** Python (FastAPI), Docker
* **Infrastructure as Code:** Terraform
* **Orchestration:** Kubernetes (Minikube)
* **Observability:** Prometheus & Grafana
* **CI/CD:** GitHub Actions

## Features
* Processes payment JSON payloads with mock approval/decline logic.
* Exposes `/metrics` for Prometheus scraping.
* Fully provisioned via Terraform.
* Secured with Kubernetes RBAC (least privilege principles).
* Automated CI/CD pipeline via GitHub Actions.
