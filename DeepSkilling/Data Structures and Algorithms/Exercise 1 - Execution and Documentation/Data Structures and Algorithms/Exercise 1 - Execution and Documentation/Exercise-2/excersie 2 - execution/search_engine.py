class ProductSearchEngine:
    def __init__(self, products):
        self.products = products

    def search(self, query):
        if not query:
            return self.products

        q = query.strip().lower()
        results = []

        for product in self.products:
            haystack = " ".join(
                [
                    str(product.get("name", "")).lower(),
                    str(product.get("category", "")).lower(),
                ]
            )
            if q in haystack:
                results.append(product)

        return results
