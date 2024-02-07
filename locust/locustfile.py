import os
import time

from locust import HttpUser, between, constant, task


class WebsiteUser(HttpUser):
    wait_time = constant(1)
    host = "http://localhost:8000"

    @task
    def upload(self):
        with open("revolver.jpg", "rb") as f:
            self.client.post(
                "/api/analyses/",
                files={"picture": f},
            )
