import base64
from io import BytesIO

import pytest
from faker import Faker
from rest_framework.test import APIClient

fake = Faker()

picture = base64.b64encode(fake.image())


@pytest.mark.django_db
class TestRequests:
    def test_create(self, client):
        client = APIClient()
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
                "picture_left": picture,
                "picture_right": picture,
                "picture_markings": picture,
                "picture_charger": picture,
            },
            format="json",
        )
        assert response.status_code == 201


@pytest.mark.django_db
class TestAnalysis:
    def test_create(self, client):
        client = APIClient()
        response = client.post(
            "/analyses/",
            {
                "picture": picture,
            },
            format="json",
        )
        assert response.status_code == 201
