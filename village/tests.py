from django.test import TestCase
from .models import Profile ,Village , Events
# Create your tests here.
class ProfileTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.anitha= Profile(Profile_picture = 'passion.jpeg', user_bio ='Passion',location='Musanze',email='a@gmail.com')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.anitha,Profile))


    def test_save_profile(self):
        self.james = Profile(Profile_picture = 'passion.jpeg', user_bio ='Passion',location='Musanze',email='a@gmail.com')
        self.james.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    
    def test_update_profile(self):
        self.ange = Profile(Profile_picture = 'passion.jpeg', user_bio ='Passion',location='Musanze',email='a@gmail.com')
        self.ange.save_profile()
        cars =Profile.objects.filter(location='Musanze').first()
        update= Profile.objects.filter(id=cars.id).update(location='Burera')
        updated = Profile.objects.filter(location='Burera').first()
        self.assertNotEqual(cars.location , updated.location)

    def test_delete_profile(self):
        self.fina = Profile(Profile_picture = 'passion.jpeg', user_bio ='Passion',location='Musanze',email='a@gmail.com')
        self.fina.save_profile()
        nature = Profile.objects.filter(location='Musanze').first()
        tree = Profile.objects.filter(id =nature.id).delete()
        trees =Profile.objects.all()
        
# class VillageTestClass(TestCase):
#        # Set up method
#     def setUp(self):
#         self.gafuka= Village(village_image= 'passion.jpeg',location ='Burere',population=40)
        
#         # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.gafuka,Village))

#     def test_save_village(self):
#         self.gafuka= Village(village_image= 'passion.jpeg',location ='Burere',population=40)
#         self.quotes.save_project()
#         projects = Village.objects.all()
#         self.assertTrue(len(Village)>0)
    

#     def test_update_project(self):
#         self.gitega= Village(village_image= 'passion.jpeg',location ='kigali',population=4) 
#         self.gitega.save_village()
#         sector =Village.objects.filter(location ='kigali').first()
#         update= Village.objects.filter(id=sector.id).update(name ='Goals')
#         updated = Village.objects.filter(location ='kiyovu').first()
#         self.assertNotEqual(gitega.location , updated.location)

    # def test_delete_project(self):
    #     self.gafuka= Village(village_image= 'passion.jpeg',location ='Burere',population=40
    #     self.quotes.save_project()
    #     QUOTES = Village.objects.filter(name ='Quotes').first()
    #     quotes = Village.objects.filter(id =QUOTES.id).delete()
    #     quotes = Village.objects.all()
        