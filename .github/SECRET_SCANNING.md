# GitHub Secret Scanning Configuration

This repository uses GitHub's native Secret Scanning feature for detecting and preventing secrets in code.

## Features Enabled:

### 🔐 Secret Scanning
- **Push Protection**: Prevents commits containing secrets
- **Secret Alerts**: Automatic detection of exposed secrets
- **Partner Program**: 200+ service providers (GitHub, AWS, Google, etc.)
- **Historical Scanning**: Scans all repository history

### 🚨 Alert Notifications
- Repository admins get alerts for detected secrets
- Email notifications for new secret detections
- Security tab integration for secret management

## Supported Secret Types:

- **GitHub Tokens** (Personal Access Tokens, App tokens)
- **AWS Credentials** (Access Keys, Secret Keys)
- **Google API Keys** (GCP, Firebase, etc.)
- **Azure Tokens** (Service Principal, etc.)
- **Database URLs** (MongoDB, PostgreSQL, etc.)
- **API Keys** (Stripe, SendGrid, Slack, etc.)
- **Private Keys** (SSH, PGP, JWT signing keys)
- **OAuth Tokens** (Various providers)
- **And 200+ more...**

## Repository Settings:

1. Go to **Repository Settings** → **Code security and analysis**
2. Enable **Secret scanning**
3. Enable **Push protection** (recommended)
4. Configure **Secret scanning alerts**

## Local Development:

GitHub Secret Scanning works automatically on push. No local setup required!
For additional local validation, bandit security scanner is still active in pre-commit hooks.

## Resources:

- [GitHub Secret Scanning Documentation](https://docs.github.com/en/code-security/secret-scanning)
- [Supported Secret Types](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-patterns)
