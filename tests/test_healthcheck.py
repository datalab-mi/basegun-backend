class TestHealthcheck:
    def test_response(self, client):
        response = client.get("/api/")
        assert response.status_code == 200
