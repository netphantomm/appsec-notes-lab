# AppSec Notes Lab

## Purpose

A learning project demonstrating authentication, sessions,
and ownership-based access control for notes.

## Installation and running

Run these commands from the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 5000
```

## Demo accounts

These are public demo credentials for local practice.

| Username | Password |
|---|---|
| elliot | training-password |
| alex | alex-password |

## Access checks

- Requesting a protected note without logging in → 401 Unauthorized.
- Requesting your own note → 200 OK.
- Requesting another user's note → 403 Forbidden.
- Requesting a nonexistent note after login → 404 Not Found.
- Requesting a protected note after logout → 401 Unauthorized.

## Limitations

- Local learning lab.
- Users and notes are defined in code; there is no database.
- Restarting the server changes the signing key and invalidates existing sessions.
- Logout deletes the current client's session cookie; copied cookies are not revoked.
- Explicit CSRF protection and login rate limiting are not implemented.
