# ADR-0001: Repository standards

- **Status:** accepted
- **Date:** 2026-10-15

## Context
This project is practice for production engineering, so the repo should work the way a
production team's does from the first commit.

## Decision
- Private GitHub repo; `main` is always deployable; work happens on short-lived branches.
- Every change: issue → branch → small PR (template) → CI green → review → squash merge.
- CI runs pre-commit (ruff lint + format, gitleaks secret scan, file hygiene) and tests, with a
  least-privilege workflow token.
- Dependabot keeps CI actions and Python dependencies current.
- CODEOWNERS requires owner review; Conventional Commits for history.
- Monorepo layout: `services/`, `deploy/`, `infra/`, `docs/`.

## Alternatives considered
| Option | Why not |
|---|---|
| One repo per service | More overhead than a single small team needs; harder to change things together |
| No pre-commit, CI only | Slower feedback; secrets could reach history before CI catches them |

## Consequences
Slightly slower for tiny changes, but every habit matches what production teams expect.
Follow-ups: branch protection / rulesets (depends on GitHub plan), pin actions to commit SHAs.
