from unicodedata import category
from django.test import TestCase
from .models import Image, Location, Category
class TestGalleryApp(TestCase):
    def setUp(self):
        '''
        The setup method will run before each test case
        '''
        self.location = Location.objects.create(name='Nairobi')
        self.category = Category.objects.create(name='Fashion')
        self.image = Image.objects.create(
            image='/image/location', 
            description='a cool image', 
            location=Location.objects.get(name='Nairobi'), 
            category=Category.objects.get(name='Fashion')
        )

    def tearDown(self):
        '''
        The teardown method does the cleanup after each test has run.
        '''
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_instance(self):
        '''
        Test the instance of each object
        '''
        self.assertTrue(isinstance(self.image, Image))
        self.assertTrue(isinstance(self.location, Location))
        self.assertTrue(isinstance(self.category, Category))

    def test_save_objects(self):
        '''
        test_save_image test case to test if the image object is saved into
        the db.
        '''
        # images
        self.image.save_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)

        # location
        self.location.save_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 1)

        # categories
        self.category.save_category()
        Categories = Category.objects.all()
        self.assertEqual(len(Categories), 1)

    def test_delete_objects(self):
        '''
        test_delete_image test case to test if the image object is removed from
        the db.
        '''
        # Images
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 0)

        # locatiom
        self.location.save_location()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)

        # category
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)

    def test_update_image(self):
        '''
        test_update_image test case to test if the image object to be updated is queried
        '''
        self.image.save()
        new_image = Image.update_image(1)
        self.assertEqual(new_image.id, 1)

    # def get_image_by_id():
    #     pass

    def test_search_image(self):
        '''
        test_filter_by_location test case to test if the image object is filtered by its category
        '''
        self.image.save()
        self.category.save()
        self.location.save()
        all_instances_of_category = Image.search_image('Fashion')
        self.assertEqual(len(all_instances_of_category), 1)

    def test_filter_by_location(self):
        '''
        test_filter_by_location test case to test if the image object is filtered by its location
        '''
        self.image.save()
        self.category.save()
        self.location.save()
        all_instances_of_location = Image.filter_by_location('Nairobi')
        self.assertEqual(len(all_instances_of_location), 1)
    
        

        
