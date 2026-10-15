# Intake service v1: accept referrals, report health

**What:** A service that lets clinics send referrals and returns a referral ID so they can
track it. Python (FastAPI), in `intake/`. Synthetic data only.

## Endpoints
| Endpoint | Behaviour |
|---|---|
| `GET /healthz` | 200 `{"status":"ok"}` whenever the process is running. **No dependency checks** (liveness must never depend on downstream services). |
| `GET /readyz` | 200 when ready; **503 during startup and once shutdown begins**, so the pod drains from the load balancer before exiting. |
| `POST /referrals` | Body `{"patient": str, "specialty": str}` → **201 Created**, body `{"id": "<new id>"}`, header `Location: /referrals/<id>`. |

## Edge cases
- Missing or invalid fields → **422** (client error, via FastAPI request-model validation).
  Never 5xx for client mistakes: 5xx counts against the SLO and can page on-call.

## Decisions
- **Shutdown draining via a Kubernetes `preStop` sleep** (accepted 2026-10-15). uvicorn stops
  accepting connections before lifespan shutdown runs, so flipping readiness there is too late.
  The readiness flag is unit-tested here; the real drain is proven in step 1.7.
- In-memory storage for v1: data is lost on restart and not shared across pods. A DB/queue
  comes in Stage 6.
- Never log request bodies (synthetic PHI habit).

## Done when
- [ ] `pytest` passes: `/healthz` → 200 · `/readyz` → 200 when ready · valid POST → 201 + id +
      `Location` · POST missing `patient` → 422
- [ ] Running locally, `curl` shows the same results
- [ ] `/readyz` returns 503 once shutdown starts (verified with a test or a manual SIGTERM)
- [ ] Every line reviewed and explainable by Josh
