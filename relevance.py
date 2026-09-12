import json
import math


def load_hashmaps():

    with open("forward_hashmap.json", "r", encoding="utf-8") as file:
        forward_hashmap = json.load(file)

    with open("backward_hashmap.json", "r", encoding="utf-8") as file:
        backward_hashmap = json.load(file)

    return forward_hashmap, backward_hashmap


def calculate_tf(word, page, forward_hashmap):

    words = forward_hashmap[page]

    total_words = len(words)

    if total_words == 0:
        return 0

    count = words.count(word)

    return count / total_words


def calculate_idf(word, backward_hashmap, total_documents):

    df = len(backward_hashmap.get(word, []))

    if df == 0:
        return 0

    return math.log(total_documents / df)


def calculate_tfidf(
    word,
    page,
    forward_hashmap,
    backward_hashmap
):

    total_documents = len(forward_hashmap)

    tf = calculate_tf(
        word,
        page,
        forward_hashmap
    )

    idf = calculate_idf(
        word,
        backward_hashmap,
        total_documents
    )

    return tf * idf


def calculate_relevance(query):

    forward_hashmap, backward_hashmap = load_hashmaps()

    query_words = query.lower().split()

    relevance = {}

    details = {}

    for page in forward_hashmap:

        score = 0

        details[page] = {}

        for word in query_words:

            tf = calculate_tf(
                word,
                page,
                forward_hashmap
            )

            idf = calculate_idf(
                word,
                backward_hashmap,
                len(forward_hashmap)
            )

            tfidf = tf * idf

            score += tfidf

            details[page][word] = {
                "tf": tf,
                "idf": idf,
                "tfidf": tfidf
            }

        relevance[page] = score

    return relevance, details



    