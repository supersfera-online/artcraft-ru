# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# SolidCraft: правила для русского каталога (конспект)

Клон: `solidcraft/` (git clone --depth 1), коммит `0301073f3e45d19618ccd9bb986418184282245a`
(2026-11-20 09:49 PST, «Consume plugin preview view actions for sketch and empty results (#20038)»). [проверено: git log]

Источники: `docs/localization.md`, `CONTRIBUTING.md` (стр. ~356–380), `AGENTS.md`,
`.agents/skills/solidcraft-ui-text/SKILL.md`, `assets/locales/pending/README.md`,
`xtask/src/i18n.rs`, `xtask/src/pending.rs`, `xtask/src/lists.rs`,
`docs/book/src/reference/glossary.md` (в задаче путь `book/src/...` — фактически `docs/book/src/...`). [проверено]

## Формат каталога
- `assets/locales/<locale>.json` — плоский JSON-объект «id → строка», все значения строки. [проверено: lists.rs `canonical`]
- Одна запись на строку, отсортировано по id (порядок байт UTF-8 = serde_json BTreeMap), без дублей,
  вид `serde_json::to_string_pretty` (2 пробела, не-ASCII как есть) + `\n` в конце. Проверяет `cargo xtask lists`,
  чинит `cargo xtask lists --fix`. [проверено: lists.rs; текущие en.json и ru.json совпадают байт-в-байт с
  `json.dumps(ensure_ascii=False, indent=2, sort_keys=True)` + `\n`]
- Часть ключей — это сам английский текст (адаптер `app.tr_label`, ~388 недостающих), часть — стабильные id (`ui.*`, `cmd.*`…). Ключи не переводятся. [проверено]
- Плейсхолдеры именованные `{name}`; подстановка буквальная. Переводить всё предложение целиком с пунктуацией. [проверено: localization.md]
- Плюрализации нет: «named substitution, not locale-specific plural selection». Поэтому счётчики пишем
  как «Тела: {count}» / «замечаний: {count}» (так уже сделано в ru.json; аналогичное правило явно записано для pl и ka). [проверено: localization.md; стиль ru — из файла]
- Есть ещё общий каталог `crates/ui-text/locales/ru.json` (сливается с основным, id не должен повторяться в двух источниках). [проверено: i18n.rs `read`]. В нём у ru не хватает 135 ключей из 254 — вне этой задачи. [проверено]

## Частичные каталоги
- ru — частичный: пробелы падают в английский, `cargo xtask i18n` их показывает, `--check` не валит. Полные (COMPLETE): ar, he, ja, vi, zh
  (в localization.md ещё без vi, в xtask и CONTRIBUTING — с vi). [проверено]
- Новая метка обязана быть в en, ar, he, ja, vi, zh, de, ko; ru «may follow later». [проверено]

## Pending-файлы
- Новые строки (id, которых ещё нет в en.json) идут в новый `assets/locales/pending/<slug>.json` {"en":{…},"de":{…}}, каталоги не правятся.
- id не должен уже быть в каталоге этой локали и в другом pending-файле. Чтобы изменить/добавить перевод к существующему id — правится сам каталог.
  Поэтому для ru (добавление переводов к уже существующим английским ключам) правим `ru.json` напрямую. [проверено: pending/README.md; uk-sync-20-nov.json — пример «синхронизации» локали через pending, тоже допустимый путь — догадка о предпочтении мейнтейнеров]
- `cargo xtask fold-pending` запускает только workflow на main после merge. В PR НЕ запускать. [проверено]
- Сейчас в pending 43 новых en-ключа (multi-window и др.) без ru — их в ru.json не добавляем (они ещё не в en.json; их место — pending). [проверено: подсчёт; решение — моё]

## Стиль и термины
- Команды `cmd.*` в английском Title Case, прочее — sentence case. В русском: обычный регистр предложения, команды — инфинитив
  («Переименовать», «Создать развёртку») — так в текущем ru.json. [из файла]
- Обращение: «вы» строчное, повелительное «Откройте/Щёлкните» в подсказках (53 случая «вы», 4 «Вы» — вероятно, начало предложения). [из файла]
- ё используется (609 строк). Кавычки «ёлочки» (138), прямых " нет. Многоточие — символ … (82; «...» в 7 строках там, где так в en). Тире — «—». [из файла]
- Глоссарий книги: «одна идея — один термин»; многозначные слова (Construction, Flat, Round, Normal, Gap, Clearance, Instance, History, Part, Profile, Fit, Quantity, Reference) — разные переводы по смыслу. Browser ≠ веб-браузер. [проверено]
- Командные id, сочетания клавиш, форматы файлов, единицы, имена пользователя не переводятся; символы единиц (`mm`) не переводятся. [проверено: localization.md, разделы it/bs/pl]
- Перед отправкой у них: `cargo xtask lists --fix`, затем `cargo xtask i18n` (у нас — только локальный прогон, ничего не отправляем).
