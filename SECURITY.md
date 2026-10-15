# Security

- **Data:** synthetic only. No real patient data (PHI) and no employer data, ever.
- **Secrets:** never in code, config, or Git history. Local secrets go in `.env` (gitignored);
  deployed secrets come from a secrets manager (Vault / AWS Secrets Manager from Stage 4).
- **Leaked secret?** Rotate it immediately, then remove it from history and write a
  postmortem.
- **Dependencies:** kept current by Dependabot; scanned in CI.
- **Logging:** never log request bodies or personal data.
