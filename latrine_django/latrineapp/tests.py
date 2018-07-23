import json
from io import StringIO
from django.core.management import call_command
from django.test import TestCase, TransactionTestCase
from django.test import Client
from django.utils import timezone
from .models import Place, Resource, Feedback


class PlaceTestCase(TestCase):
    def setUp(self):
        """Creating instances of all models."""
        self.place = Place.objects.create(
            organization="Rose Haven",
            website="http://rosehaven.org",
            short_description="Rose Haven offers various facilities to women and children in need.",
            address="627 NW 18th Ave., Portland, OR 97209",
            phone="503-248-6364",
            lat="45.527666",
            lng="-122.689642",
            gender="women, children",
            image="")

        self.now = timezone.now().strftime('%Y-%m-%d %H:%M')
        self.past = (timezone.now() - timezone.timedelta(days=1)).strftime('%Y-%m-%d %H:%M')

        self.resource1 = Resource.objects.create(created_at=self.past, updated_at=self.now, facility_type="showers", hours="Monday, Tuesday and Thursday, from 9am-4pm.", short_description="Private shower facilities for women and children in need.", place=self.place)
        self.resource2 = Resource.objects.create(created_at=self.past, updated_at=self.now, accessible=False, changing_table=True, facility_type="restrooms", hours="24h", short_description="Accessible restrooms.", place=self.place)

        self.feedback1 = Feedback.objects.create(upvote=3, comment="Safe place!", resource=self.resource1)
        self.feedback2 = Feedback.objects.create(downvote=2, comment="Not safe!", resource=self.resource1)
        self.feedback3 = Feedback.objects.create(comment="Good experience.", resource=self.resource2)

        self.c = Client()

    def test_model_fields(self):
        """Test that we can create a place with multiple resources and feedback."""
        self.assertTrue(isinstance(self.place, Place))
        self.assertTrue(isinstance(self.resource1, Resource))
        self.assertTrue(isinstance(self.resource2, Resource))
        self.assertTrue(isinstance(self.feedback1, Feedback))
        self.assertTrue(isinstance(self.feedback2, Feedback))
        self.assertTrue(isinstance(self.feedback3, Feedback))

        self.assertEqual(self.place.organization, "Rose Haven")
        self.assertEqual(self.place.website, "http://rosehaven.org")
        self.assertEqual(self.place.short_description, "Rose Haven offers various facilities to women and children in need.")
        self.assertEqual(self.place.address, "627 NW 18th Ave., Portland, OR 97209")
        self.assertEqual(self.place.phone, "503-248-6364")
        self.assertEqual(self.place.lat, "45.527666")
        self.assertEqual(self.place.lng, "-122.689642")
        self.assertEqual(self.place.gender, "women, children")
        self.assertNotEqual(self.place.image, "test")

        self.assertEqual(self.resource1.facility_type, "showers")
        self.assertEqual(self.resource1.hours, "Monday, Tuesday and Thursday, from 9am-4pm.")
        self.assertEqual(self.resource1.short_description, "Private shower facilities for women and children in need.")
        self.assertEqual(self.resource1.place, self.place)
        self.assertEqual(self.resource1.updated_at, self.now)
        self.assertEqual(self.resource1.created_at, self.past)
        self.assertNotEqual(self.resource1.created_at, self.now)
        self.assertEqual(self.resource2.facility_type, "restrooms")
        self.assertEqual(self.resource2.hours, "24h")
        self.assertEqual(self.resource2.short_description, "Accessible restrooms.")
        self.assertEqual(self.resource2.place, self.place)
        self.assertNotEqual(self.resource2.accessible, True)
        self.assertEqual(self.resource2.changing_table, True)

        self.assertEqual(self.feedback1.comment, "Safe place!")
        self.assertEqual(self.feedback1.resource, self.resource1)
        self.assertEqual(self.feedback1.upvote, 3)
        self.assertNotEqual(self.feedback1.resource, self.resource2)
        self.assertNotEqual(self.feedback1.downvote, 3)
        self.assertEqual(self.feedback2.comment, "Not safe!")
        self.assertEqual(self.feedback2.resource, self.resource1)
        self.assertEqual(self.feedback2.downvote, 2)
        self.assertNotEqual(self.feedback2.resource, self.resource2)
        self.assertEqual(self.feedback3.comment, "Good experience.")
        self.assertEqual(self.feedback3.resource, self.resource2)
        self.assertNotEqual(self.feedback3.resource, self.resource1)

    def test_api_get_all_places(self):
        """Test AllPlaces ApiView."""
        response = self.c.get('/places/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 400)

        expected_response = {'address': '627 NW 18th Ave., Portland, OR 97209',
                             'gender': 'women, children',
                             'image': None,
                             'lat': 45.527666,
                             'lng': -122.689642,
                             'organization': 'Rose Haven',
                             'phone': '503-248-6364',
                             'resources': [{'created_at': self.past, 'updated_at': self.now, 'accessible': False, 'changing_table': False, 'facility_type': 'showers',
                                            'feedback': [{'comment': 'Safe place!',
                                                          'downvote':0, 'upvote': 3},
                                                         {'comment': 'Not safe!',
                                                          'downvote':2, 'upvote':0}],
                                            'hours': 'Monday, Tuesday and Thursday, from 9am-4pm.',
                                            'short_description': 'Private shower facilities for women and '
                                                                 'children in need.'},
                                           {'created_at': self.past, 'updated_at': self.now,  'accessible': False, 'changing_table': True, 'facility_type': 'restrooms',
                                            'feedback': [{'comment': 'Good experience.',
                                                          'downvote':0, 'upvote':0}],
                                            'hours': '24h',
                                            'short_description': 'Accessible restrooms.'}],
                             'short_description': 'Rose Haven offers various facilities to women and '
                                                  'children in need.',
                             'website': 'http://rosehaven.org'}

        self.assertEqual(json.loads(json.dumps(response.data[0])), expected_response)

    def test_get_resources(self):
        """Test ResourceList ApiView."""
        response1 = self.c.get('/places/restrooms/')
        response2 = self.c.get('/places/showers/')
        response3 = self.c.get('/places/showers+restrooms/')
        response4 = self.c.get('/places/showers+restrooms+test/')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response4.status_code, 404)

        self.assertEqual(len(response1.data), 1)
        self.assertEqual(len(response2.data), 1)
        self.assertEqual(len(response3.data), 1)


class RefugeRestrooms(TransactionTestCase):
    """Testing the visual output of the custom management command get_restrooms."""
    def test_command_output(self):
        print("Testing custom management command *get_restrooms*. Be patient - it will take a bit longer than the rest of the unit tests...")
        out = StringIO()
        call_command('get_restrooms', stdout=out)
        self.assertIn('Page 1 of the API; 100 records have been analyzed.', out.getvalue())
        self.assertIn('Page 7 of the API;', out.getvalue())  # there will always be at least 7 pages
        self.assertNotIn('404', out.getvalue())
