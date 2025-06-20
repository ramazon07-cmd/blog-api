#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

# Vercel uchun handler qo'shish (bu aslida serverless uchun emas, lekin ish beradi)
try:
    from core.asgi import app
    handler = app
except ImportError:
    pass
