#!/bin/bash
# Run from your project root: flask_structure/
# This aggressively restructures your app to the clean blueprint layout.

set -e

echo "==> Creating new directory structure..."
mkdir -p app/web/auth
mkdir -p app/api/auth
mkdir -p app/services
mkdir -p app/templates/{auth,tenants}
mkdir -p app/static/{css,js}

echo "==> Removing old auth folder (backed up first)..."
cp -r app/auth app/auth_backup
rm -rf app/auth

echo "==> Removing duplicate tasks.py (keeping tasks/ folder)..."
[ -f app/tasks.py ] && rm app/tasks.py

echo "==> Removing old views/ folder..."
[ -d app/views ] && rm -rf app/views

echo "==> Creating __init__.py files..."
touch app/web/__init__.py
touch app/web/auth/__init__.py
touch app/api/__init__.py
touch app/api/auth/__init__.py
touch app/services/__init__.py

echo ""
echo "Done. Now copy in the new file contents from the refactor."
echo "Backup of old auth/ is at app/auth_backup/ - delete when confirmed working."
