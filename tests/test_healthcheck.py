class TestAdmin:
    def test_response(self, client):
        response = client.get("/admin")
        assert response.status_code == 301
