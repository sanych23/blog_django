

class SeedExtension:
    def delete(self):
        self.model.objects.all().delete()


