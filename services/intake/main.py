"""Intake service: accepts referrals from clinics and reports its own health.

Ticket 001. Synthetic data only.
"""

import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# In-memory store for v1: lost on restart and not shared across pods (see ticket 001).
REFERRALS: dict[str, dict] = {}


class ReferralIn(BaseModel):
    """What a clinic sends. Missing or wrong-typed fields → automatic 422."""

    patient: str
    specialty: str


class ReferralOut(BaseModel):
    """What we send back."""

    id: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ready = True  # startup finished: ready for traffic
    yield
    # Shutting down. Real draining is handled by the Kubernetes preStop hook (ticket 001).
    app.state.ready = False


app = FastAPI(title="intake", lifespan=lifespan)
app.state.ready = False  # not ready until lifespan startup has run


@app.get("/healthz")
def healthz() -> dict:
    """Liveness: the process is up. No dependency checks, by design."""
    return {"status": "ok"}


@app.get("/readyz")
def readyz() -> JSONResponse:
    """Readiness: should this pod receive traffic right now?"""
    if app.state.ready:
        return JSONResponse({"status": "ready"})
    return JSONResponse(
        {"status": "not ready"}, status_code=status.HTTP_503_SERVICE_UNAVAILABLE
    )


@app.post("/referrals", status_code=status.HTTP_201_CREATED, response_model=ReferralOut)
def create_referral(referral: ReferralIn, response: Response) -> ReferralOut:
    """Store a referral and return its new ID. Never log the body (PHI habit)."""
    referral_id = f"ref_{uuid.uuid4().hex[:12]}"
    REFERRALS[referral_id] = referral.model_dump()
    response.headers["Location"] = f"/referrals/{referral_id}"
    return ReferralOut(id=referral_id)
