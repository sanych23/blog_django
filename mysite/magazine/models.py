from django.db import models
from services.magazine.selection_products import ProductsSelection


class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    description = models.TextField()
    count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    old_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey("ProductCategory", on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField("TagProduct", related_name='products')

    def main_image_path(self):
        image_path = self.Images.filter(main_image=1).get().image_path
        return image_path

    def similar_products(self):
        all_products = []
        tags = self.tags.all()

        for tag in tags:
            secondary_products = tag.products.all()
            all_products += [product for product in secondary_products if product not in all_products]

        actual_products = ProductsSelection().get_similar_products(tags, all_products)
        return actual_products
    
    def recomended_product(self):
        return 
    
    def __str__(self) -> str:
        return f"{self.title}"


class TagProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self) -> str:
        return f"{self.title}"


class ProductsRating(models.Model):
    pass


class ProductImages(models.Model):
    image_path = models.CharField(max_length=255, null=True)
    product = models.ForeignKey("Products", on_delete=models.DO_NOTHING, null=True, related_name="Images")
    main_image = models.BooleanField(default=False)


class Cart(models.Model):
    pass
