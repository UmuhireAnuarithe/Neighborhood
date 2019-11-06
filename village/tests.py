from django.test import TestCase
from .models import Profile ,Village , Events ,Business
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
        
class VillageTestClass(TestCase):
       # Set up method
    def setUp(self):
        self.gafuka= Village(village_image= 'passion.jpeg',location ='Burere',population=40)
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gafuka,Village))

    def test_save_village(self):
        self.gafuka= Village(village_image= 'passion.jpeg',location ='Burere',population=40)
        self.gafuka.save_village()
        hoods = Village.objects.all()
        self.assertTrue(len(hoods)>0)
    

    def test_update_project(self):
        self.gitega= Village(village_image= 'passion.jpeg',location ='kigali',population=4) 
        self.gitega.save_village()
        sector =Village.objects.filter(location ='kigali').first()
        update= Village.objects.filter(id=sector.id).update(location ='kiyovu')
        updated = Village.objects.filter(location ='kiyovu').first()
        self.assertNotEqual(sector.location , updated.location)

    def test_delete_project(self):
        self.gitega= Village(village_image= 'passion.jpeg',location ='Burere',population=40)
        self.gitega.save_village()
        cell = Village.objects.filter(location ='Burere').first()
        cells = Village.objects.filter(id =cell.id).delete()
        cells = Village.objects.all()
        

class BusinessTestClass(TestCase):
       # Set up method
    def setUp(self):
        self.guhinga = Business(business_image= 'passion.jpeg',name ='Burere',description='beans',owner='umuhire')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.guhinga,Business))

    def test_save_business(self):
        self.guhinga = Business(business_image= 'passion.jpeg',name ='Burere',description='beans',owner='umuhire')
        
        self.guhinga.save_business()
        hoods = Business.objects.all()
        self.assertTrue(len(hoods)>0)
    

    def test_update_Village(self):
        self.guhinga = Business(business_image= 'passion.jpeg',name ='Burere',description='beans',owner='umuhire')
        self.guhinga.save_business()
        sector =Business.objects.filter(owner='umuhire').first()
        update= Business.objects.filter(id=sector.id).update(owner='anuarithe')
        updated = Business.objects.filter(owner='anuarithe').first()
        self.assertNotEqual(sector.owner , updated.owner)

    def test_delete_project(self):
        self.guhinga = Business(business_image= 'passion.jpeg',name ='Burere',description='beans',owner='umuhire')
        self.guhinga.save_business()
        cell = Business.objects.filter(owner='umuhire').first()
        cells = Business.objects.filter(id =cell.id).delete()
        cells = Business.objects.all()
        
class EventsTestClass(TestCase):
       # Set up method
    def setUp(self):
        self.meeting = Events(event_image= 'passion.jpeg',name ='Burere',description='youth meeting')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.meeting,Events))

    def test_save_events(self):
        self.meeting = Events(event_image= 'passion.jpeg',name ='Burere',description='youth meeting')
        self.meeting.save_events()
        events = Events.objects.all()
        self.assertTrue(len(events)>0)
    
def test_update_events(self):
        self.meeting = Events(event_image= 'passion.jpeg',name ='Burere',description='youth meeting')
        self.meeting.save_events()
        sector =Events.objects.filter(name ='Burere').first()
        update= Events.objects.filter(id=sector.id).update(name ='kigali')
        updated = Events.objects.filter(name ='kigali').first()
        self.assertNotEqual(sector.name , updated.name)

    def test_delete_events(self):
        self.meeting = Events(event_image= 'passion.jpeg',name ='Burere',description='youth meeting')
        self.meeting.save_events()
        sector =Events.objects.filter(name ='Burere').first()
        cells = Events.objects.filter(id =sector.id).delete()
        cells = Events.objects.all()
        
    