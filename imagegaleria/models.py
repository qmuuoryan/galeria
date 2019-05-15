from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length =30)


    def save_Location(self):
            self.save()

    # def delete_Location(self):
    #         self.delete()


    def __str__(self):
            return self.location_name


class Category(models.Model):
    category_name = models.CharField(max_length =30)


    def save_category(self):
            self.save()

    def delete_category(self):
            self.delete()

    def __str__(self):
            return self.category_name


class Image(models.Model):
    image_name = models.CharField(max_length = 70)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category )
    photo = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(pk=id)
        return cls.objects.get(id=image_id)

    @classmethod
    def update_image(cls,id,name,description,location,category):
        image = cls.objects.get(pk=image_id)
        image = cls(name=name,description=description,location=location,category=category)
        image.save()

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def search_by_category(cls,search_term):
        result_search = cls.objects.filter(category_name__icontains=search_term)
        return result_search    