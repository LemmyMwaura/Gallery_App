from django.test import TestCase
from .models import Image, Location, Category
class TestGalleryApp(TestCase):
    @classmethod
    def setUpTestData(cls):
        '''
        Sets up the default ID field for the Object below in the database. (Django doesn't reset auto ID fields 
        for each test case)
        Saves the new objects id.
        '''
        cls.obj_id = Image.objects.create(
            image='/image/location', 
            description='a cool image',
        ).pk 

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
        self.location_2 = Location(name='Mombasa')
        self.category_2 = Category(name='Coding')
        self.location_2.save_location()
        self.category_2.save_category()

        self.image_2 = Image(
            image='/image/route', 
            description='coding is cool', 
            location=Location.objects.get(name='Mombasa'), 
            category=Category.objects.get(name='Coding')
        )
        self.image_2.save_image()

        images = Image.objects.all()
        locations = Location.objects.all()
        Categories = Category.objects.all()

        self.assertEqual(len(images), 3)
        self.assertEqual(len(locations), 2)
        self.assertEqual(len(Categories), 2)

    def test_delete_objects(self):
        '''
        test_delete_image test case to test if the image object is removed from
        the db.
        '''
        # Images
        self.image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)

        # locatiom
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)

        # category
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)

    def test_update_image(self):
        '''
        test_update_image test case to test if the image object to be updated is queried
        '''
        new_image = Image.update_image(self.obj_id)
        self.assertEqual(new_image.id, 1)

    def test_get_image_by_id(self):
        '''
        test_update_image test case to test if the image object can be queried by its ID
        '''
        get_image_by_id = Image.get_image_by_id(self.obj_id)
        self.assertEqual(get_image_by_id.id, 1)

    def test_search_image(self):
        '''
        test_filter_by_location test case to test if the image object is filtered by its category
        '''
        all_instances_of_category = Image.search_image('Fashion')
        self.assertEqual(len(all_instances_of_category), 1)

    def test_filter_by_location(self):
        '''
        test_filter_by_location test case to test if the image object is filtered by its location
        '''
        all_instances_of_location = Image.filter_by_location('Nairobi')
        self.assertEqual(len(all_instances_of_location), 1)
