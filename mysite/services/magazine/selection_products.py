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
            print(f"{product} ---- {coefficient}")
            if coefficient >= 0.5:
                actual_products.append(product)
            
        return actual_products