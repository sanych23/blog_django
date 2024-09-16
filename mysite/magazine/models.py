from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    description = models.TextField()
    # main_image_product = models.CharField(max_length=255)
    count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    old_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey("ProductCategory", on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField("TagProduct", null=True)

    def main_image_path(self):
        image_path = self.Images.filter(main_image=1).get().image_path
        return image_path

    def similar_products(self):
        products = []
        tags = self.tags.all()
        for tag in tags:
            products += tag.products_set.all()
        return products
        # print(self.tags.all())
    
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
