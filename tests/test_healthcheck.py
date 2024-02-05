class TestAdmin:
    def test_response(self, client, faker):
        response = client.get("/admin")
        assert response.status_code == 200
