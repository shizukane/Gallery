from django.test import TestCase
from .models import Image, Location, Category

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location = 'Mombasa')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.save_location()
        Location.delete_location(self.location.id)
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)
    
    def test_update_location(self):
        Location.update_location(self.location.id, 'Paris')
        self.assertEqual(self.location.location, 'Paris')

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category = 'Things')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
    
    def test_delete_category(self):
        Category.delete_category(self.category.id)
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)

    def test_update_category(self):
        Category.update_category(self.category.id, 'Animals')
        self.assertEqual(self.category.category, 'Animals')

class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(location = 'Paris')
        self.location.save_location()

        self.category = Category(category = 'Animals')
        self.category.save_category()

        self.img = Image(img_path = 'darolle.png', img_name = 'passport photo', img_desc ='passport sized photo of Joan', img_location= self.location, img_category = self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.img, Image))
    
    def test_save_image(self):
        self.img.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)
    
    def test_delete_image(self):
        self.img.save_image()
        Image.delete_image(self.img.id)
        images = Image.objects.all()
        self.assertEqual(len(images), 0)

    def test_get_image_by_id(self):
        self.img.save_image()
        image = Image.get_image_by_id(self.img.id)
        self.assertEqual(self.img.img_location, image)

    def test_search_image(self):
        self.img.save_image()
        image = Image.search_image(self.img.img_category)
        self.assertEqual(self.img, image)

    def test_update_image(self):
        self.img.save_image()
        Image.update_image(self.img.id, 'mark.jpg')
        self.assertEqual(self.img.img_path, 'mark.jpg')

    def test_update_description(self):
        self.img.save_image()
        Image.update_desc(self.img.id, 'passport sized photo of Mark')
        self.assertEqual(self.img.img_desc, 'passport sized photo of Mark')

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

