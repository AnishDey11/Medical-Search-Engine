# Medical Research Search Engine

A simple web-based medical search engine built using **Python, FastAPI, HTML, CSS, and JavaScript**.

It searches five medical research pages using **TF-IDF relevance** and **PageRank**, then combines both scores to rank the results.

## Features

- Forward HashMap: `Page → Words`
- Backward HashMap: `Word → Pages`
- TF-IDF based relevance
- PageRank based page importance
- Search results with document overview
- Clickable pages to view full content
- Analysis page with relevance, PageRank, graph, and final ranking
- Final ranking using:

  `Final Score = 0.7 × Relevance + 0.3 × Normalized PageRank`

## Project Structure

    Medical-Search_Engine/
    │
    ├── app.py
    ├── backend.py
    ├── relevance.py
    ├── pagerank.py
    ├── forward_hashmap.json
    ├── backward_hashmap.json
    ├── links.json
    │
    ├── pages/
    │   ├── P1.txt
    │   ├── P2.txt
    │   ├── P3.txt
    │   ├── P4.txt
    │   └── P5.txt
    │
    └── templates/
        ├── index.html
        ├── page.html
        └── analysis.html

## Formulas

    TF = Term occurrences / Total words in document

    DF = Number of documents containing the term

    IDF = log(N / DF)

    TF-IDF = TF × IDF

    Relevance = Sum of TF-IDF values of query terms

    PageRank:
    PR(i) = (1 - d) / N + d × Σ(PR(j) / L(j))

    where j → i

    d = 0.85

    N = Total number of pages

    L(j) = Number of outgoing links from page j

    Initial PageRank:
    PR(i) = 1 / N

    Convergence condition:
    max |PR_new - PR_old| < 0.0001

    Normalized PageRank:
    Normalized PageRank = PageRank / Maximum PageRank

    Final Score:
    Final Score = 0.7 × Relevance + 0.3 × Normalized PageRank

## Run Locally

    python -m venv venv
    .\venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    python -m uvicorn app:app --reload

Open:

    http://127.0.0.1:8000

## Deployment on Render

Build Command:

    pip install -r requirements.txt

Start Command:

    uvicorn app:app --host 0.0.0.0 --port $PORT

## Technologies

Python, FastAPI, Uvicorn, Jinja2, HTML, CSS, JavaScript, JSON, TF-IDF, PageRank

