from fuzzywuzzy import fuzz



def search_engine(query: str, data: list, threshold: int =50) -> list:
    """
    Search engine for the data.
    """
    results: list = []

    if len(query) <= 1:
        threshold = 10

    elif len(query) <= 3:
        threshold = 40

    for choice in data:
        similarity = fuzz.ratio(query, choice)
        if similarity >= threshold:
            results.append(choice)

    return results

