# Instagram User Lookup – Unofficial API

---

## Description

This script uses a **private undocumented Instagram API endpoint** (`/users/lookup/`) to retrieve information related to an account based on:

- Username  
- Email address  
- Phone number  

The script is written in **pure Python** without any external dependencies. It uses only the standard library (`urllib`), making it runnable as-is on any standard Python ≥ 3.x installation.

---

## Features

- Identify an Instagram account from different inputs (`username`, email, phone)  
- Works also on **private accounts**  
- Returns **partially obfuscated information** (examples: `*@gmail.com`, `@y****.fr`, `+** * ** ** ** 06`)  
- Provides available **account recovery options** for the account:  
  - Email reset: `"can_email_reset": true`  
  - SMS reset: `"can_sms_reset": true`  
  - WhatsApp reset: `"can_wa_reset": false`  

---

## Known Limitations

- **Verified accounts (blue badge)** return a **404 error**, even if they exist.  
- Searches by **phone** or **email** generally return limited information.  
- Search by **username** returns the most detailed and useful information.  

---

## Usage Example

```bash
python instaosl.py <query>
```

# Instagram User Lookup – API non officielle

---

## Description

Ce script utilise un **endpoint privé non documenté de l’API Instagram** (`/users/lookup/`) pour récupérer des informations liées à un compte à partir de :

- Nom d’utilisateur (username)  
- Adresse e-mail  
- Numéro de téléphone
  
---

## Fonctionnalités

- Identification d’un compte Instagram à partir de différentes entrées (`username`, email, téléphone)  
- Fonctionne également sur les **comptes privés**  
- Retourne des **informations partielles masquées** (exemples : `*@gmail.com`, `@y****.fr`, `+** * ** ** ** 06`)  
- Fournit les **modes de récupération disponibles** pour le compte :  
  - Réinitialisation par e-mail : `"can_email_reset": true`  
  - Réinitialisation par SMS : `"can_sms_reset": true`  
  - Réinitialisation WhatsApp : `"can_wa_reset": false`  

---

## Limitations connues

- **Les comptes certifiés (badge bleu)** renvoient une **erreur 404**, même s’ils existent.  
- Les recherches par **téléphone** ou **email** retournent généralement des informations peu détaillées.  
- La recherche par **nom d’utilisateur (username)** est celle qui fournit le plus d’informations exploitables.  

---

## Exemple d’utilisation

```bash
python instaosl.py <query>
```
