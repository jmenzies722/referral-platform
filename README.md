# Referral Platform

A learning project built and operated like production: a small system that accepts referral
documents, processes them, and routes them, with reliability, security, and AI-platform
practices applied end to end. **Synthetic data only.**

## Layout
| Path | What lives there |
|---|---|
| `services/` | Application services (`intake/` first) |
| `deploy/` | Kubernetes manifests / Helm charts |
| `infra/` | Terraform (AWS, from Stage 8) |
| `docs/tickets/` | Specs, one per change |
| `docs/adr/` | Architecture decision records |
| `docs/runbooks/` | One runbook per alert |
| `docs/postmortems/` | Blameless postmortems from game days |

## How we work
Issue → branch → small PR → CI green → review → merge → deploy → verify. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## Quick start
```bash
pre-commit install          # run checks before every commit
cd services/intake && uv sync && uv run pytest
```
