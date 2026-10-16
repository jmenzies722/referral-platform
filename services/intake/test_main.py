"""Tests for ticket 001. `with TestClient(app)` runs the lifespan (startup/shutdown)."""

from fastapi.testclient import TestClient

from main import app


def test_healthz_ok():
    with TestClient(app) as client:
        r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_readyz_ok_after_startup():
    with TestClient(app) as client:
        r = client.get("/readyz")
    assert r.status_code == 200


def test_readyz_503_when_not_ready():
    with TestClient(app) as client:
        app.state.ready = False  # simulate shutdown having started
        r = client.get("/readyz")
    assert r.status_code == 503


def test_create_referral_returns_201_id_and_location():
    with TestClient(app) as client:
        r = client.post(
            "/referrals", json={"patient": "Jane Test", "specialty": "cardiology"}
        )
    assert r.status_code == 201
    referral_id = r.json()["id"]
    assert referral_id.startswith("ref_")
    assert r.headers["location"] == f"/referrals/{referral_id}"


def test_missing_patient_returns_422():
    with TestClient(app) as client:
        r = client.post("/referrals", json={"specialty": "cardiology"})
    assert r.status_code == 422
