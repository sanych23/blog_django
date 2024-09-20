from difflib import SequenceMatcher


class ProductsSelection:
    def similarity_coefficient(self, main_tags, product_tags):
        similary = 0
        coef_one_sim = 1 / len(main_tags)

        for tag in main_tags:
            if tag in product_tags:
                similary += coef_one_sim

        return similary


    def get_similar_products(self, main_product_tags, products):
        actual_products = list()

        for product in products:
            coefficient = self.similarity_coefficient(main_product_tags, product.tags.all())
            # print(f"{product} ---- {coefficient}")
            if coefficient >= 0.5:
                actual_products.append(product)
            
        return actual_products
    


class RecomendedProduct:
    def get_recomdended_products(self, main_product, products):
        recomended = list()
        for product in products:
            similary = [
                SequenceMatcher(None, product.title, main_product.title).ratio(),
                SequenceMatcher(None, product.short_description, main_product.short_description).ratio(),
                SequenceMatcher(None, product.description, main_product.description).ratio(),
            ]
            similary_koef = sum(similary) / len(similary)
            print(f"{product.title} --- {similary_koef}")
            if similary_koef >= 0.5:
                recomended.append(product)
        # print(recomended)
        return recomended
