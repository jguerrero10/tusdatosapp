from core.entities.user import User
from core.security.auth import hash_password


def test_get_speakers(client, db_session):
    # Crear usuarios locales
    local_speakers = [
        {"email": "speaker1@example.com", "full_name": "Speaker 1"},
        {"email": "speaker2@example.com", "full_name": "Speaker 2"},
    ]

    db_session.add_all([
        User(email=u["email"], full_name=u["full_name"], hashed_password=hash_password("pass"), is_speaker=True)
        for u in local_speakers
    ] + [
        User(email="user@example.com", full_name="Regular User", hashed_password=hash_password("pass"), is_speaker=False)
    ])
    db_session.commit()

    response = client.get("/api/v1/speakers")
    assert response.status_code == 200

    speakers = response.json()
    returned_emails = {s["email"] for s in speakers}
    for u in local_speakers:
        assert u["email"] in returned_emails
