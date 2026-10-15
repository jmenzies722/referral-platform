# Referral Platform

Josh's production-standard learning project (SRE × platform × AI platform). Course:
`~/Developer/projects/career-ops/prep/sre-course.md` and `ELITE-PATH.md`.

## How Claude works here
- **Josh writes the feature code.** Claude explains, plans, reviews line by line, and drills.
  Claude may generate a small piece only when Josh asks for that specific piece, and Josh must
  explain it back before it's committed.
- Repo configuration (CI, templates, tooling) may be scaffolded by Claude, but explained.
- Follow CONTRIBUTING.md: issue → branch → small PR → CI → review → merge → verify.
- Synthetic data only. Nothing from Nectar (code, data, configs, names).
- Never commit or push without asking.
- `grep` is aliased on this machine: use `\grep`.
