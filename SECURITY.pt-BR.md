# 🔐 Segurança & Privacidade

[🇺🇸 English](./SECURITY.md) · 🇧🇷 **Português**

Este é um repositório de estudos **público**. Estas regras mantêm segredos e dados pessoais fora dele.

## Nunca commitar

- Chaves de API, tokens e senhas (OpenAI/Anthropic/Hugging Face/Kaggle, credenciais de cloud, arquivos `.env`)
- `credentials.json`, `*.pem`, `*.key`, arquivos de conta de serviço
- Dados pessoais: telefone, endereço, CPF/RG, data de nascimento, e-mail pessoal
- Prints que mostrem abas do navegador, notificações, caminhos de pasta com seu usuário ou dados de outras pessoas
- Datasets com informações pessoais de pessoas reais

Chaves ficam num arquivo `.env` (já ignorado pelo `.gitignore`) ou em **GitHub → Settings → Secrets** para workflows.

## Configuração única

1. **GitHub → Settings → Emails:** ativar *Keep my email addresses private* e *Block command line pushes that expose my email*.
2. **Git local:** `git config --global user.email "<id>+<usuario>@users.noreply.github.com"` (o endereço exato aparece nessa mesma página de Emails).
3. **2FA:** ativar a verificação em duas etapas na conta do GitHub.
4. **Repositório → Settings → Code security:** ativar *Secret scanning* e *Push protection* (gratuitos em repositório público — bloqueiam pushes com formatos de chave conhecidos).

## Antes de cada commit

- `git diff --staged` — leia o que está prestes a ficar público.
- **Notebooks do Colab/Jupyter:** limpe saídas que imprimam chaves ou dados pessoais (*Editar → Limpar todas as saídas*); nunca cole uma chave numa célula — use os *Secrets* do Colab (ícone 🔑).
- **Prints:** recorte só o que importa.

## Se um segredo vazar

1. **Revogue/troque a chave imediatamente** no provedor. Apagar o commit **não** basta: o histórico e os forks guardam.
2. Substitua por uma chave nova guardada no `.env` / GitHub Secrets.
3. Opcional: reescrever o histórico (`git filter-repo`) — só depois de revogar a chave.

## Reportar

Achou algo sensível neste repositório? Abra uma issue **sem** colar o conteúdo sensível, ou fale comigo pelo LinkedIn (veja o README).
