# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# PROGRESS — SolidCraft ru (автообновляется work/progress.py)

Обновлено: 2026-11-20 11:46 PST. Коммит клона: `0301073f3e45d19618ccd9bb986418184282245a`. [проверено]

- Было недостающих: 2285; переведено: **2285**; осталось: **0** (список: work/remaining-keys.txt). [проверено: скрипт]
- Готовые группы полностью: (ключ = английский текст), ai.*, boundary_fill.*, browser.*, cmd.*, component.*, config.*, constrain.*, contact.*, delete.*, design_view.*, diagnostic.*, dialog.*, document.*, drawing_export.*, dxf.*, error.*, explode.*, export.*, file.*, file_load.*, graphics.*, help.*, hole.*, hole_folder.*, home.*, import_report.*, insert_airfoil.*, joint.*, kernel.*, library.*, links.*, measure.*, motion.*, nav.*, navbar.*, operations.*, parameters.*, parts.*, pattern.*, perf.*, plugin_data.*, plugin_error.*, plugin_install.*, policy.*, prefs.*, recovery.*, refused.*, render.*, report.*, section.*, settings.*, sheet.*, shell.*, sketch.*, starting.*, tab_strip.*, thread.*, timeline.*, ui.*, view_gizmo.*

| Префикс | Было | Переведено | Осталось |
|---|---|---|---|
| `ui.*` | 574 | 574 | 0 |
| `(ключ = английский текст)` | 388 | 388 | 0 |
| `prefs.*` | 276 | 276 | 0 |
| `render.*` | 244 | 244 | 0 |
| `cmd.*` | 235 | 235 | 0 |
| `library.*` | 59 | 59 | 0 |
| `report.*` | 50 | 50 | 0 |
| `import_report.*` | 40 | 40 | 0 |
| `help.*` | 38 | 38 | 0 |
| `sketch.*` | 32 | 32 | 0 |
| `sheet.*` | 28 | 28 | 0 |
| `constrain.*` | 25 | 25 | 0 |
| `plugin_install.*` | 22 | 22 | 0 |
| `browser.*` | 19 | 19 | 0 |
| `joint.*` | 14 | 14 | 0 |
| `links.*` | 14 | 14 | 0 |
| `operations.*` | 14 | 14 | 0 |
| `file_load.*` | 13 | 13 | 0 |
| `ai.*` | 12 | 12 | 0 |
| `nav.*` | 12 | 12 | 0 |
| `plugin_error.*` | 12 | 12 | 0 |
| `thread.*` | 12 | 12 | 0 |
| `document.*` | 11 | 11 | 0 |
| `refused.*` | 11 | 11 | 0 |
| `dialog.*` | 9 | 9 | 0 |
| `navbar.*` | 9 | 9 | 0 |
| `design_view.*` | 8 | 8 | 0 |
| `view_gizmo.*` | 8 | 8 | 0 |
| `tab_strip.*` | 7 | 7 | 0 |
| `diagnostic.*` | 6 | 6 | 0 |
| `policy.*` | 6 | 6 | 0 |
| `recovery.*` | 6 | 6 | 0 |
| `config.*` | 5 | 5 | 0 |
| `dxf.*` | 4 | 4 | 0 |
| `graphics.*` | 4 | 4 | 0 |
| `insert_airfoil.*` | 4 | 4 | 0 |
| `measure.*` | 4 | 4 | 0 |
| `plugin_data.*` | 4 | 4 | 0 |
| `settings.*` | 4 | 4 | 0 |
| `starting.*` | 4 | 4 | 0 |
| `boundary_fill.*` | 3 | 3 | 0 |
| `drawing_export.*` | 3 | 3 | 0 |
| `file.*` | 3 | 3 | 0 |
| `home.*` | 3 | 3 | 0 |
| `parameters.*` | 3 | 3 | 0 |
| `pattern.*` | 3 | 3 | 0 |
| `error.*` | 2 | 2 | 0 |
| `export.*` | 2 | 2 | 0 |
| `hole.*` | 2 | 2 | 0 |
| `section.*` | 2 | 2 | 0 |
| `timeline.*` | 2 | 2 | 0 |
| `component.*` | 1 | 1 | 0 |
| `contact.*` | 1 | 1 | 0 |
| `delete.*` | 1 | 1 | 0 |
| `explode.*` | 1 | 1 | 0 |
| `hole_folder.*` | 1 | 1 | 0 |
| `kernel.*` | 1 | 1 | 0 |
| `motion.*` | 1 | 1 | 0 |
| `parts.*` | 1 | 1 | 0 |
| `perf.*` | 1 | 1 | 0 |
| `shell.*` | 1 | 1 | 0 |

Как продолжить: смотри раздел «Процесс» ниже.

## Проверки задания 1 (20.11.2026, PST)
- work/merge_check.py: 2285 добавлено, ru.json 7417 ключей, недостающих в основном каталоге 0; ошибок 0; 103 предупреждения (бренды/форматы/CLI латиницей, строки-плейсхолдеры, Letter/Legal/Tabloid, клавиши Up/Down) [проверено: скрипт]
- старые переводы авторов в ru.json не изменены: сравнение с `git show HEAD:assets/locales/ru.json` [проверено]
- формат: `cargo xtask lists` OK [проверено]
- `cargo xtask i18n --no-registry` без sudo, после задания 1: ru missing 2463 → 178 (43 pending + 135 ui-text), work/xtask-i18n-after.log [проверено]
- UI-тесты не гонялись во второй задаче; в первой rustc был убит OOM [проверено]

## Задание 2 (20.11.2026, 11:21 PST)

### 178 оставшихся строк
- 43 en-ключа из `assets/locales/pending/*.json` (ещё нет в en.json) — ru добавлен в те же шесть pending-файлов, где уже стоит en (app-bar-overflow, drawing-template-scdwg, multi-window, multi-window-drag, view-placement, view-pop-out). Отдельный pending-файл с теми же id `xtask lists` отверг бы. В ru.json их не клали. [проверено: pending/README.md, NOTES-rules.md, xtask lists]
- 135 ключей — в `crates/ui-text/locales/ru.json` (стало 254/254). [проверено]
- Комментарий об авторстве в pending JSON не ставился: файл общий для нескольких языков, в JSON комментариев нет; xtask lists с чужеродным текстом не прошёл бы. Отметку в описании PR и коммите ставит координатор (см. ниже). [из файла: RULES-AUTHORSHIP.md]

### Проверки задания 2
- merge_check.py: 2285, ru.json 7417, авторские строки не изменены, ошибок 0 [проверено]
- плейсхолдеры (алгоритм теста Rust) на основном ru, ui-text и pending ru: 0 расхождений [проверено]
- `cargo xtask i18n --no-registry`: «catalog coverage ok», строки «ru is missing» нет (= 0), код 0; work/xtask-i18n-task2.log [проверено]
- `cargo xtask lists`: OK, pending fold cleanly, код 0; work/xtask-lists-task2.log [проверено]
- fold-pending не запускался; git commit в клоне не делался; sudo не использовался; наружу ничего не отправлялось [проверено: git log — один коммит авторов]

### Ё
- Правило «ё всегда» применено к нашим 2285+178. Слепой замены е→ё не было: сверка со словарём eyo-safe и ручной разбор неоднозначных (все/всё, ребра/рёбра, чем/чём, перед/перёд, стекло/стёкла и др.).
- Замены в наших строках: 3 (шелкографию→шёлкографию; «ДВА РЕБРА»→«ДВА РЁБРА» в двух заголовках). Остальные неоднозначные совпадения — ложные (род. п. «ребра», «прежде чем», «все вкладки» и т.п.), не менялись. [проверено: словарь + контекст]
- В 5132 авторских строках ничего не менялось. Кандидаты: work/yo-candidates-old.tsv, 3 строки («два ребра»→«два рёбра»). В старом ru.json букву ё уже содержат 611 строк; однозначных пропусков по eyo-safe нет (0); «е» на месте «ё» по эвристике — эти 3 строки. [проверено]

### Термины
- Решение координатора для SolidCraft оставлено как есть: Pattern → «Массив», Workspace → «Рабочая область», Preset → «Пресет». [из файла: задание 2]

### Длинные строки (UI-тесты не гонялись)
- work/long-strings.tsv: 1280 строк, где len(ru) > 1,5 × len(en) (плейсхолдеры `{name}` исключены из длины), по всему ru.json и ui-text (включая pending). [проверено: скрипт]
- Из них кнопок 378, меню 9 (вместе 387); остальных 893. Наших 361 (из них кнопок+меню 125), авторских 919. [проверено]
- В столбце «предложение» — 28 вариантов укорочения наших строк; в каталоги не применялись. [догадка: укорочения]

### Авторство (для координатора)
При сборке PR нужна отметка об авторстве перевода в описании PR и в коммите: «Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0». В JSON комментариев нет, её туда не ставить. Имена исполнителей в репозиторий и в коммиты не попадают. Лицензионные файлы авторов не трогать. Перепись авторства и отправку делает координатор; сейчас ждать команды правообладателя. [из файла: RULES-AUTHORSHIP.md]

## Задание 3 (20.11.2026, 11:45 PST)

### Правки терминолога (glossary/fixes/solidcraft.md, 6 пунктов) — все применены
- `import_report.ok`: «OK» → «ОК» (наша строка, не из 5132) [из файла]
- `prefs.workspace`: «Рабочее пространство» → «Рабочая область» (**авторская**) [из файла]
- `ui.3d_mouse_circles_help`: «Круги показывают…» → «Окружности показывают…» (**авторская**) [из файла]
- `ui.heading_ok`: «OK» → «ОК» (**авторская**) [из файла]
- `ui.workspace_footer`: «Все рабочие среды…» → «Все рабочие области…» (**авторская**) [из файла]
- `terms-solidcraft-ru.tsv`, ключ workspace: «рабочая область (в ru.json также «рабочее пространство»)» → «Рабочая область» (файл вне клона, в коммит не входил). Колонки «источник»/счётчики не трогал. [из файла]
- Координатор уже вернул «ДВА РЕБРА» в двух заголовках; «шёлкографию» оставлена; укорочения не применялись. [проверено]

### Проверки
- merge_check.py: сначала пересборка из эталона+добавлений (чтобы не затереть авторские правки), затем 4 авторские правки вручную. После этого: ru 7417, недостающих 0, авторские ключи отличаются от HEAD только этими 4, формат канонический, плейсхолдеры 0 расхождений (ru, ui-text, pending) [проверено]
- `cargo xtask i18n --no-registry`: «catalog coverage ok», «ru is missing» нет (= 0), код 0; work/xtask-i18n-task3.log [проверено]
- `cargo xtask lists`: OK, код 0; work/xtask-lists-task3.log [проверено]

### Локальный коммит (без push)
- ветка `l10n-ru` от `0301073f`
- коммит `df88f6fbae12c8663216b23e0a70290fe00ba923` (20.11.2026, 11:45 PST)
- автор и коммиттер: supersfera <223132313+supersfera-online@users.noreply.github.com>
- сообщение: `i18n(ru): complete Russian catalog` + пустая строка + `Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0`
- 8 файлов: assets/locales/ru.json; 6 pending (app-bar-overflow, drawing-template-scdwg, multi-window, multi-window-drag, view-placement, view-pop-out); crates/ui-text/locales/ru.json
- имён исполнителей, Co-authored-by и подписи нет; global git config не менялся; remote не трогался, push не делался [проверено: git log -1 --format=fuller, git show --stat]

## Что осталось
- Вычитка носителем; 3 кандидата «ё» в авторских («два ребра») координатор уже решил оставить без ё в наших заголовках — авторские 3 в yo-candidates-old.tsv по-прежнему только список
- fold-pending не запускать; наружу ничего не отправлять, пока не скажет правообладатель; при сборке PR координатор переписывает авторство при необходимости
