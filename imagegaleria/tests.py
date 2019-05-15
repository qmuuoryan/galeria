from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
# category test class
class Category_test(TestCase):
    def setUp(self):
        self.Art=Category(id=1,category_name="Art")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.Art,Category))

    def test_save_category(self):
        self.Art.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_category(self):
        self.Art.delete_category()
        category= Category.objects.all()
        self.assertTrue(len(category) < 1)

# location test class
class LocationTestClass(TestCase):
    def setUp(self):
        self.prestige= Location(id=1 ,location_name= 'prestige')

    def test_instance(self):
        self.assertTrue(isinstance(self.prestige,Location))
    
    def test_save_method(self):
        self.prestige.save_Location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # def test_delete_Location(self):
    #     self.prestige.delete_Location()
    #     locations= Location.objects.all()
    #     self.assertTrue(len(location) < 1)    
               