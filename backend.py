from relevance import calculate_relevance
from pagerank import calculate_pagerank
import json


def get_page_overview(page):
    path = f"pages/{page}.txt"

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read().strip()
    except FileNotFoundError:
        return "Document not found."

    sentences = content.split(".")

    for sentence in sentences:
        sentence = sentence.strip()

        if sentence:
            overview = sentence

            if len(overview) > 250:
                overview = overview[:250] + "..."

            return overview + "."

    return content[:250] + "..."


def search(query):
    relevance, details = calculate_relevance(query)

    pagerank = calculate_pagerank()

    max_pagerank = max(pagerank.values()) if pagerank else 0

    results = []

    for page in relevance:
        relevance_score = relevance[page]
        page_rank_score = pagerank.get(page, 0)

        if max_pagerank > 0:
            normalized_pagerank = page_rank_score / max_pagerank
        else:
            normalized_pagerank = 0

        final_score = (
            0.7 * relevance_score
            + 0.3 * normalized_pagerank
        )

        results.append({
            "page": page,
            "overview": get_page_overview(page),
            "relevance": relevance_score,
            "pagerank": page_rank_score,
            "normalized_pagerank": normalized_pagerank,
            "final_score": final_score,
            "terms": details[page]
        })

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results


def get_page_content(page):
    path = f"pages/{page}.txt"

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def get_page_rank_data():
    pagerank = calculate_pagerank()

    max_pagerank = max(pagerank.values()) if pagerank else 0

    rows = []

    for page, value in pagerank.items():

        if max_pagerank > 0:
            normalized = value / max_pagerank
        else:
            normalized = 0

        rows.append({
            "page": page,
            "pagerank": value,
            "normalized": normalized
        })

    rows.sort(
        key=lambda x: x["pagerank"],
        reverse=True
    )

    return rows


def get_graph():
    with open("links.json", "r", encoding="utf-8") as file:
        return json.load(file)



    