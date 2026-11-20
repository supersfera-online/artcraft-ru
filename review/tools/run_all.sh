#!/usr/bin/env bash
# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# Все проверки перевода по папкам отдела l10n. Только локально; ничего не публикует.
#   run_all.sh                    все ru-каталоги в craft-i18n/, apps/, solidcraft/, packaging/ (+cli/, docs/)
#   run_all.sh --only-changed     только клоны, изменившиеся с прошлого снимка (review/state/last.txt)
#   run_all.sh --native           плюс штатные проверки с auto=yes из native_checks.tsv (cargo)
#   run_all.sh --native=photocraft,figcraft   выбранные штатные проверки (долгая сборка)
#   run_all.sh --locale de        то же для другого языка (проба формата)
# Отчёты: review/reports/<ГГГГММДД-ЧЧММСС>-<цель>.md/.tsv и …-run_all.md. Код: 0 ок, 1 есть ошибки, 2 сбой.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$here/run_all.py" "$@"
