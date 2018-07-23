import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from latrineapp.models import Place, Resource, Feedback


class Command(BaseCommand):
    help = 'Loads data from every page of RefugeRestrooms.org public API and saves into the database.'

    def handle(self, *args, **options):
        api_page_number = 1
        dataset_length = 1
        while dataset_length > 0:  # iterating over each page of the API
            url = "https://www.refugerestrooms.org:443/api/v1/restrooms/search.json?page={}&per_page=100&query=portland" \
            .format(api_page_number)
            resp = requests.get(url)
            resp.raise_for_status()  # HTTP error handling
            restrooms = resp.json()
            dataset_length = len(restrooms)
            if dataset_length == 0:
                break
            for restroom in restrooms:  # iterating over each result on a page
                if not restroom["longitude"] or not restroom["latitude"]:  # skipping corrupted coordinates
                    continue
                try:
                    new_place = Place(
                                organization=restroom["name"],
                                address="{}, {}, {}".format(restroom["street"], restroom["city"], restroom["state"]),
                                lat=restroom["latitude"],
                                lng=restroom["longitude"],
                                short_description=restroom["directions"],
                                gender="unisex: {}".format(str(restroom["unisex"]).lower())
                                )
                    new_resource = Resource(
                                        facility_type="restrooms",
                                        accessible=restroom["accessible"],
                                        changing_table=restroom["changing_table"],
                                        created_at=datetime(int(restroom["created_at"][:4]), int(restroom["created_at"][5:7]), int(restroom["created_at"][8:10]), int(restroom["created_at"][11:13]), int(restroom["created_at"][14:16]), int(restroom["created_at"][17:19])),
                                        updated_at=datetime(int(restroom["updated_at"][:4]), int(restroom["updated_at"][5:7]), int(restroom["updated_at"][8:10]), int(restroom["updated_at"][11:13]), int(restroom["updated_at"][14:16]), int(restroom["updated_at"][17:19])),
                                        place=new_place
                                        )
                    new_feedback = Feedback(
                                   upvote=restroom["upvote"],
                                   downvote=restroom["downvote"],
                                   comment=restroom["comment"],
                                   resource=new_resource
                                   )
                    new_place.save()
                    new_resource.save()
                    new_feedback.save()
                    new_resource.feedback.add(new_feedback)
                    new_place.resources.add(new_resource)
                except IntegrityError:
                    self.stdout.write("Duplicate found. {} will not be saved to the database.".format(restroom["name"]))
            self.stdout.write("Page {} of the API; {} records have been analyzed.".format(api_page_number, dataset_length))
            api_page_number += 1
