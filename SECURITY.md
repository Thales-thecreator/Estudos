# 🔐 Security & Privacy

🇺🇸 **English** · [🇧🇷 Português](./SECURITY.pt-BR.md)

This is a **public** study repository. These rules keep secrets and personal data out of it.

## Never commit

- API keys, tokens and passwords (OpenAI/Anthropic/Hugging Face/Kaggle keys, cloud credentials, `.env` files)
- `credentials.json`, `*.pem`, `*.key`, service-account files
- Personal data: phone, home address, ID numbers (CPF/RG), date of birth, personal email
- Screenshots showing browser tabs, notifications, file paths with your username, or other people's data
- Datasets with personal information about real people

Keys go in a `.env` file (already ignored by `.gitignore`) or in **GitHub → Settings → Secrets** for workflows.

## One-time setup

1. **GitHub → Settings → Emails:** enable *Keep my email addresses private* and *Block command line pushes that expose my email*.
2. **Local Git:** `git config --global user.email "<id>+<username>@users.noreply.github.com"` (the exact address is shown on that same Emails page).
3. **2FA:** enable two-factor authentication on the GitHub account.
4. **Repository → Settings → Code security:** enable *Secret scanning* and *Push protection* (free on public repos — blocks pushes that contain known key formats).

## Before every commit

- `git diff --staged` — read what is about to go public.
- **Colab/Jupyter notebooks:** clear outputs that print keys or personal data (*Edit → Clear all outputs*); never paste a key into a cell — use Colab *Secrets* (🔑 icon) instead.
- **Screenshots:** crop to what matters.

## If a secret leaks

1. **Revoke/rotate the key immediately** at the provider. Deleting the commit is **not** enough: the history and forks keep it.
2. Replace it with a new key stored in `.env` / GitHub Secrets.
3. Optionally rewrite history (`git filter-repo`) — but only after the key is revoked.

## Reporting

Found something sensitive in this repo? Please open an issue **without** pasting the sensitive content, or contact me via LinkedIn (see the README).
