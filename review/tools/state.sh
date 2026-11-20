#!/usr/bin/env bash
# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# Снимок состояния папок l10n и режим --changed (см. state.py).
#   state.sh                 записать снимок в review/state/last.txt
#   state.sh --changed       что изменилось с прошлого снимка (код 0 — ничего, 3 — есть изменения)
#   state.sh --changed --update   то же и обновить снимок
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ "${1:-}" == "--changed" ]]; then
  shift
  exec python3 "$here/state.py" changed "$@"
fi
exec python3 "$here/state.py" snapshot "$@"
