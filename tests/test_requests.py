import base64
from io import BytesIO

import pytest
from django.test import Client
from faker import Faker

fake = Faker()

picture_left = BytesIO(fake.image())
picture_left.name = "myimage.gif"
picture_right = BytesIO(fake.image())
picture_right.name = "myimage.gif"
picture_markings = BytesIO(fake.image())
picture_markings.name = "myimage.gif"
picture_charger = BytesIO(fake.image())
picture_charger.name = "myimage.gif"


@pytest.mark.django_db
class TestRequests:
    def test_create(self, client):
        client = Client()
        response = client.post(
            "/requests/",
            {
                "agent_identifier": "test",
                "assignment_service": "test",
                "agent_phone_number": "test",
                "agent_email": "test@test.com",
                "seizure_date": "2021-01-01",
                "weapon_type": "long",
                "weapon_length": 10,
                "weapon_barrel_length": 10,
                "picture_left": picture_left,
                "picture_right": picture_right,
                "picture_markings": picture_markings,
                "picture_charger": picture_charger,
            },
        )
        assert response.status_code == 201
