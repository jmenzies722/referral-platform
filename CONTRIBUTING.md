# How we work

## The flow (every change, no exceptions)
1. **Issue first.** Problem, acceptance criteria, risks. Non-trivial design → an ADR in
   `docs/adr/`.
2. **Branch** from `main`: `feat/<issue#>-short-name`, `fix/…`, `chore/…`.
3. **Small commits** using Conventional Commits: `feat: …`, `fix: …`, `chore: …`, `docs: …`,
   `test: …`, `ci: …`.
4. **Pull request** using the template. Keep it small (aim for < 400 changed lines).
5. **CI must be green:** pre-commit (ruff lint + format, secret scan, hygiene) and tests.
6. **Review:** every line must be explainable by the author.
7. **Merge** (squash), deploy, **verify**, update runbooks and docs.

## Definition of done
- [ ] Acceptance criteria met and tested
- [ ] CI green
- [ ] Docs, runbook, or ADR updated if behaviour changed
- [ ] Verified in the running system, not just "it compiled"

## Rules
- Synthetic data only. Never real PHI, never anything from an employer.
- Never commit secrets. The pre-commit secret scan blocks them; if one slips, **rotate it
  first**, then clean up history.
- Never log request bodies.
