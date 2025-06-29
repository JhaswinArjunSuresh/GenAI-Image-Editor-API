from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_edit_image():
    response = client.post("/edit_image", json={
        "user_prompt": "A futuristic city skyline at sunset",
        "mask_description": "Replace sky with stars"
    })
    assert response.status_code == 200
    data = response.json()
    assert "generated_image_path" in data