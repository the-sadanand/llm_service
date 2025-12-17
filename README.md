# 🚀 Containerized LLM Serving API (FastAPI + Docker)

A **production-style, thread-safe LLM inference service** built using Python, FastAPI, Hugging Face Transformers, and Docker.  
This project demonstrates **real-world ML system design**, including authentication, concurrency handling, and containerized deployment.

---

## 📌 Project Overview

Large Language Models (LLMs) are computationally expensive and **not thread-safe by default**.  
This project exposes an LLM through a REST API while solving real production problems such as:

- Safe concurrent access to the model
- API key–based authentication
- Lazy model loading
- Clean Docker-based deployment
- Robust input validation

The service is designed for **CPU-based inference**, focusing on **correctness, stability, and clarity**.

---

## 🧠 Key Features

- REST API built with :contentReference[oaicite:0]{index=0}
- Text generation using :contentReference[oaicite:1]{index=1}
- Thread-safe inference using a global lock
- API key authentication via headers
- Input validation using Pydantic
- Dockerized deployment using :contentReference[oaicite:2]{index=2}
- Swagger UI for API testing
- Health check endpoint
- Concurrency-safe behavior (no corrupted or blank outputs)

---

## 📂 Project Structure

llm-service/
│
├── app/
│ ├── main.py # FastAPI entrypoint & routes
│ ├── model.py # Lazy-loaded LLM + inference lock
│ ├── auth.py # API key authentication
│ └── schemas.py # Request/response models
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## ⚙️ Technologies Used

- Python 3.10
- FastAPI
- Hugging Face Transformers
- PyTorch (CPU)
- Uvicorn
- Docker & Docker Compose
- Postman / curl for testing

---

## 🧩 Prerequisites

Before running the project, make sure you have:

- **Docker Desktop** installed
- Minimum **8 GB RAM** (recommended)
- Stable internet connection (for first-time model download)

Verify Docker installation:

```bash
docker --version
docker compose version
