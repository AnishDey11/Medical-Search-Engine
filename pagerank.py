import json


def calculate_pagerank():

    with open("links.json", "r", encoding="utf-8") as file:
        links = json.load(file)

    pages = list(links.keys())

    n = len(pages)

    damping = 0.85
    tolerance = 0.0001

    rank = {}

    for page in pages:
        rank[page] = 1 / n

    while True:

        new_rank = {}

        for page in pages:

            contribution = 0

            for source in pages:

                if page in links[source]:

                    contribution += (
                        rank[source] /
                        len(links[source])
                    )

            new_rank[page] = (
                (1 - damping) / n
                + damping * contribution
            )

        difference = 0

        for page in pages:

            change = abs(
                new_rank[page] - rank[page]
            )

            if change > difference:
                difference = change

        rank = new_rank

        if difference < tolerance:
            break

    return rank



    