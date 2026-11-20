# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# Инвентарь CLI и сообщений об ошибках комплекта ArtCraft

Составлен 20 ноября 2026 (зона America/Los_Angeles) отделом локализации (CLI и ошибки) по разделу 4.7 плана `plan-ru-localization.md`. Это инвентарь и классификация, не перевод и не публикация наружу.

Пометки: **проверено (источник: файл:строка или URL)** — факт из исходника или публичного документа; **из файла** — из уже лежащих материалов отдела; **догадка**; **не проверено**. Цифры строк — результат разбора исходников, клонированных только для чтения; это не полный каталог ошибок движка.

## 1. Метод и границы

- Охват: все 19 программ из раздела 3 плана (версии на установленной системе — из файла `findings-20261120-ru.md`, исходники — свежий `main` на GitHub 20.11.2026). Плюс все найденные `*-cli`, точки входа десктопа (`--help` / `--version` / `--control` и т.п.), `anicraft`/`serve`, шлюз `craft-ai-mcp` (его отдаёт лаунчер).
- Исходники: разреженные shallow-клоны в `cli/src/` (только чтение, без форков, issue, PR, звёзд). Компьютер установленная система не использовался, бинари не запускались.
- Классификация каждой извлечённой строки: `translate` (перевод разрешён и идёт через механизм i18n CLI), `contract` (нарочно английский / стабильный машинный или тестовый контракт), `unclear` (нет явного разрешения и нет явного запрета/пина).
- Правило плана 4.7: где авторы запрещают перевод — не навязывать; ломать контракт CLI/MCP (идентификаторы команд) нельзя; переводятся только подписи для человека — и то если авторы это принимают.
- Извлечение: литералы `--help`/USAGE, doc-комментарии и атрибуты clap, `#[error]`, `writeln!`/`eprintln!`/`format!` с сообщениями, строки, которые тесты сверяют буквально. Не извлечены: полный текст ошибок движка во внутренних крейтеах, строки общего `craft-libs` (репозиторий не клонировался), help clap, который появляется только в сгенерированном выводе без отдельного литерала.

Глоссарий отдела `glossary/` пуст. Черновики `draft-ru-*.tsv` не делались: ни у одной программы нет явного механизма перевода CLI, категория `translate` пуста (см. `terms-needed.md`).

## 2. Сквозные выводы

### 2.1. Механизма локализации CLI нет ни у одной программы

**проверено:** во всех крейтах `*-cli` / `crates/cli` и в разобранных `args.rs` нет вызовов `tr!` / `trn!` / `tl!`, gettext, Fluent или `craft_i18n` для вывода командной строки. Каталоги craft-i18n и локальные UI-каталоги описывают интерфейс приложения, не `--help`.

У SoundCraft `localization::error_text` переводит часть ошибок движка в UI (pt-BR). **проверено (источник: soundcraft/docs/localization-parity.md:10-12).** Что тот же путь используется в `soundcraft-cli` — не проверено (в коде CLI-крейта вызовов не видно).

### 2.2. Нарочно английский вывод (главные доказательства контракта)

1. **AniCraft — прямой запрет.** «Not translated, on purpose: … `anicraft-cli`, `serve` and MCP (scripts and agents see the same English everywhere), log output, and the `--help` text.» Движковые сообщения «not yet», остаются по-английски. **проверено (источник: anicraft/docs/localisation.md:12-17).**
2. **PhotoCraft — ошибки движка и часть статусов.** «Engine error and status messages, user document, layer and preset names, and automation command IDs stay in English, as in every language.» И в parity: «Not covered anywhere: engine error and status messages and filter parameter help, which are English in every language.» **проверено (источник: photocraft/docs/localization-ru.md:57-60; docs/localization-parity.md:15-16).** Это про сообщения движка/автоматизации, не отдельный абзац про `--help` CLI; справка CLI при этом зафиксирована тестами и эталоном RFC-0012.
3. **PdfCraft — детали ошибок движка и ОС.** «Not counted: error details from the engine and the operating system, which are shown in English inside a translated frame; there is no translated user documentation or help yet.» «every catalog leaves engine error details in English, and none has translated help» (здесь «help» — справка UI, не обязательно CLI). **проверено (источник: pdfcraft/docs/localization-parity.md:30-32, 67).**
4. **LightCraft — ошибки нижних слоёв пока английские `format!`.** Планируется провести их через переводимые id, «must not change what the app does» (решения по виду ошибки, не по тексту). **проверено (источник: lightcraft/docs/localization-parity.md:87-90).** Это план на будущее, не действующий механизм CLI.
5. **SolidCraft — идентификаторы.** «Command IDs, shortcuts, file formats, units and user-provided names are not translated.» Каталоги «not every engine error». CLI отдельно не назван. **проверено (источник: solidcraft/docs/localization.md:99, 112, 226).**
6. **Общий план отдела.** «Ломать контракт CLI/MCP (стабильные английские идентификаторы команд) нельзя.» **из файла: plan-ru-localization.md:119.**

### 2.3. RFC-0012: справка и usage как стабильный интерфейс

Документ [RFC-0012: Command-line conventions](https://github.com/storytold/craft-contrib/pull/18) (файл `rfcs/0012-cli-conventions.md`). Состояние на 20.11.2026: **PR открыт, не слит** (`state=open`, `merged=false`). **проверено (источник: GitHub API, https://github.com/storytold/craft-contrib/pull/18).** Заголовок PR в API — «RFC-0018: Command-line conventions» (номер PR 18); в теле и файле фигурирует RFC-0012. Эталон — `photocraft-cli`.

Правила, важные для перевода: коды выхода 0/1/2; результаты на stdout (JSON для программ); ошибки на stderr в виде `error: <message>`; «Help is the documentation» (doc-комментарии clap); «Tests pin the interface» — тесты сверяют `--help`/`--version` и каждое usage-сообщение. **проверено (источник: текст RFC, строки 45-50, 75-77, 110-112).**

Уже ссылаются на RFC-0012 в своих репозиториях (при том, что RFC ещё не в `main` craft-contrib):

| Программа | Доказательство |
|---|---|
| photocraft | Эталон в тексте RFC; clap + тесты, пинающие help/usage. **проверено (источник: RFC; apps/photocraft-cli/tests/)** |
| cadcraft | «follows RFC-0012»; «`--help` … are the reference». **проверено (источник: cadcraft/docs/cli.md:5, 7-8)** |
| soundcraft | «follows RFC-0012»; «tests that pin help and every usage error». **проверено (источник: soundcraft/docs/cli.md:136-138)** |
| figcraft | «The CLI follows RFC-0012»; «`--help` is the source of truth»; перечислены ещё не закрытые пункты RFC. **проверено (источник: figcraft/docs/cli.md:7-33)** |
| craft-anything | clap в CLI есть; отдельной фразы «Follows RFC-0012» в просмотренных docs не найдено. Тесты help есть. |

Остальные `*-cli` в основном с ручным разбором аргументов и константой `USAGE` (как в черновике RFC: «none of them uses clap» — эта фраза RFC уже частично устарела). **проверено** наличие/отсутствие clap по исходникам.

Идентификаторы подкоманд, флагов, переменных `<APP>_*`, ключи JSON, имена MCP-инструментов и command id — **контракт** во всех программах, даже без RFC.

### 2.4. Сводка чисел

Извлечено **3578** строк в `strings-<program>.tsv`: **3212 contract**, **366 unclear**, **0 translate**.

Число — нижняя оценка человекочитаемых и контрактных литералов в CLI-крейтеах и точках входа, плюс часть строк из тестов, которые фиксируют вывод. Ошибки движка в `crates/engine` почти не входили в разбор; по документам авторов они часто нарочно английские и в инвентаре учтены политикой, а не построчным списком.

## 3. Программы (все 19, ни одна не пропущена)

Версии в скобках — установленные на установленной системе 20.11.2026 **из файла: findings-20261120-ru.md**. SHA — `HEAD` клона `main` на 20.11.2026.

### photocraft 0.23.1 — `photocraft-cli`

- Репозиторий: https://github.com/storytold/photocraft (`877d58844029`)
- Локально: `cli/src/photocraft/apps/photocraft-cli/` (+ `crates/automation/src/args.rs`, десктоп `apps/photocraft/src/main.rs`)
- i18n CLI: нет. UI — craft-i18n.
- Механизм CLI: clap (эталон RFC-0012), thiserror, тесты help/usage, пример `man-and-completions`.
- Строки: 535 (contract 480, unclear 55, translate 0).
- Контракт: справка clap и usage, пинаемые тестами; JSON/MCP/command id; ошибки движка и статусы по `docs/localization-ru.md` и `localization-parity.md`.
- Неясно: часть прогресса/предупреждений десктопа при старте (`photocraft: control server…`) без пина точного текста.
- Файл: `strings-photocraft.tsv`.

### pdfcraft 0.21.1 — `pdfcraft-cli`

- https://github.com/storytold/pdfcraft (`df18640982f6`)
- `cli/src/pdfcraft/apps/pdfcraft-cli/` (ручной разбор, константа USAGE; clap нет)
- 288 строк (contract 273, unclear 15, translate 0)
- Контракт: USAGE/`--help`, тесты; детали ошибок движка/ОС по `docs/localization-parity.md:30-32, 67`.
- Есть также `apps/pdfcraft-ocr-worker` в дереве репозитория — отдельный разбор CLI-строк **не делался** (не проверено содержимое воркера).
- `strings-pdfcraft.tsv`

### wordcraft 0.18.1 — `wordcraft-cli`

- https://github.com/storytold/wordcraft (`f2e6234c5240`)
- Ручной CLI, тесты help есть (`apps/wordcraft-cli/tests/it/help.rs`). clap нет.
- 179 (contract 145, unclear 34, translate 0)
- i18n CLI нет. Политики «не переводить --help» в просмотренных localization-документах нет (есть языковые parity-заметки про UI).
- `strings-wordcraft.tsv`

### vectorcraft 0.24.1 — `vectorcraft-cli`

- https://github.com/storytold/vectorcraft (`063f55080244`)
- Ручной CLI, тесты `tests/it/cli.rs`. clap нет.
- 101 (contract 82, unclear 19, translate 0)
- `strings-vectorcraft.tsv`

### filmcraft 0.20.1 — `filmcraft-cli`

- https://github.com/storytold/filmcraft (`960a66100176`)
- Ручной CLI, тесты help. clap нет.
- 91 (все contract по пинам/справке в этой выборке; перевод CLI не разрешён механизмом)
- `strings-filmcraft.tsv`

### cadcraft 0.20.1 — `cadcraft-cli` (+ `cadcraft --help` у десктопа)

- https://github.com/storytold/cadcraft (`1d92bb275c75`)
- clap, RFC-0012, тесты `tests/it/help.rs` и `usage.rs`, ast-grep (`clap-error-message`, `string-error`), man/completions.
- 356 (contract 352, unclear 4, translate 0)
- `docs/cli.md:35-37`: десктоп перечисляет флаги через `cadcraft --help`; неверное значение `CADCRAFT_CONTROL_PORT` — usage error.
- `strings-cadcraft.tsv`

### artcraft-launcher 0.19.2 — своего `*-cli` нет; есть `artcraft-launcher` и `craft-ai-mcp`

- https://github.com/storytold/craft-launcher (`bbb3844954d9`)
- Отдельного `artcraft-launcher-cli` в дереве нет. **проверено (источник: дерево репозитория).**
- Десктоп читает `--version`/`-V` и `--hidden` (остальное игнорирует, включая не-UTF-8); на Windows ещё `--install-msis`. **проверено (источник: apps/artcraft-launcher/src/main.rs:63-73; crates/native/src/login.rs:16; tests/arguments.rs:3-10, 19-31).** Отдельного `--help` у лаунчера не найдено.
- `--version` пинается тестом упаковки: точная строка `artcraft-launcher <версия>\n`. Это контракт.
- `craft-ai-mcp`: тонкая обёртка `craft_ai_mcp::cli::main` из https://github.com/storytold/craft-ai-integrations (`a822ad5b4db2`). USAGE: `usage: craft-ai-mcp --stdio`. Имена инструментов `craft_list_apps`, `craft_find_tools`, `craft_describe_tool`, `craft_call_tool` — контракт. **проверено (источник: craft-ai-integrations/crates/app/ai-mcp/src/cli.rs; docs/CRAFT-AI-MCP.md).**
- 10 строк в `strings-artcraft-launcher.tsv` (contract 6, unclear 4, translate 0). Выборка узкая: у лаунчера мало CLI-прозы.

### lightcraft 0.21.1 — `lightcraft-cli`

- https://github.com/storytold/lightcraft (`968b0428fc15`)
- Ручной CLI, clap нет; отдельного help-теста в выборке не видно.
- 168 (contract 126, unclear 42, translate 0)
- Ошибки catalog/raw/codecs/engine пока английские; перевод запланирован через id, без смены поведения. **проверено (источник: docs/localization-parity.md:87-90).**
- `strings-lightcraft.tsv`

### figcraft 0.18.1 — `figcraft-cli`

- https://github.com/storytold/figcraft (`8320b6699e3f`)
- clap, следует RFC-0012 с оговорками («Not yet…» в docs/cli.md:25-33). `--help` — источник правды; usage: `error: …`, выход 2.
- 212 (contract 186, unclear 26, translate 0)
- В дереве есть `apps/figcraft-server` — разбор его CLI **не делался** полностью (не проверено, кроме факта наличия пакета).
- `strings-figcraft.tsv`

### craft-anything 0.6.1 — `craft-anything-cli`

- https://github.com/storytold/craft-anything (`827be601e781`)
- clap есть, тесты help есть; явной отсылки к RFC-0012 в просмотренных docs нет.
- 224 (contract 183, unclear 41, translate 0)
- `strings-craft-anything.tsv`

### designcraft 0.20.1 — `designcraft-cli`

- https://github.com/storytold/designcraft (`4000591c6681`)
- Ручной CLI, тесты `tests/it/cli.rs`. clap нет.
- 197 (contract 180, unclear 17, translate 0)
- `strings-designcraft.tsv`

### gridcraft 0.19.1 — `gridcraft-cli`

- https://github.com/storytold/gridcraft (`442a40ecb14e`)
- Ручной CLI, есть `docs/cli.md`, тесты help. clap нет.
- 103 (contract 91, unclear 12, translate 0)
- `strings-gridcraft.tsv`

### texturecraft 0.6.1 — `texturecraft-cli`

- https://github.com/storytold/texturecraft (`9be964a00eb4`)
- Ручной CLI, константа USAGE, тесты `tests/cli.rs`. clap нет.
- 39 (contract 12, unclear 27, translate 0). Малый CLI; часть usage без пина оставлена как unclear.
- UI через `tr()` / craft-i18n; в parity CLI не выведен из перевода отдельной фразой (в отличие от AniCraft). **проверено (источник: docs/localization-parity.md, начало файла — про UI).**
- `strings-texturecraft.tsv`

### anicraft 0.2.1 — `anicraft-cli`, плюс `serve` и флаги десктопа `anicraft`

- https://github.com/storytold/anicraft (`3ccb59e02b1a`)
- CLI: `crates/cli/` (пакет `anicraft-cli`). Весь вывод CLI, `--help`, MCP, логи — нарочно английские.
- 42 (все contract, translate 0). Выборка неполная относительно всех сообщений control/MCP (часть форматов собирается динамически).
- В `src/main.rs` десктопа есть `tr!` (UI). Это не механизм перевода CLI. **проверено.**
- `strings-anicraft.tsv`

### deckcraft 0.18.1 — `deckcraft-cli`

- https://github.com/storytold/deckcraft (`b16257a8b20e`)
- Ручной CLI (`src/help.rs`), тесты. clap нет. В самой программе UI-каталога ещё нет (из файла: план, строка про deckcraft).
- 98 (contract 76, unclear 22, translate 0)
- `strings-deckcraft.tsv`

### soundcraft 0.20.1 — `soundcraft-cli`

- https://github.com/storytold/soundcraft (`85623f28f99a`)
- clap, RFC-0012, «tests that pin help and every usage error», man/completions, общие флаги в `crates/automation/src/args.rs`.
- 320 (все contract в этой выборке, translate 0)
- Перевод части ошибок в UI (`error_text`, pt-BR) не равен разрешению переводить CLI.
- `strings-soundcraft.tsv`

### materialcraft 0.4.1 — `materialcraft-cli`

- https://github.com/storytold/materialcraft (`4ff5af9af737`)
- Ручной CLI, USAGE в `main.rs`. Отдельного help-теста в выборке почти нет (`tests/published.rs`).
- 20 (contract 3, unclear 17, translate 0). USAGE и «unknown command» без пина — unclear.
- `strings-materialcraft.tsv`

### effectcraft 0.24.1 — `effectcraft-cli`

- https://github.com/storytold/effectcraft (`c561e7352f60`)
- Ручной CLI, тесты `tests/it/cli.rs`. clap нет.
- 198 (contract 191, unclear 7, translate 0)
- `strings-effectcraft.tsv`

### solidcraft 0.45.0 — `solidcraft-cli` (Tangency Labs)

- https://github.com/tangency-labs/solidcraft (`0301073f3e45`)
- Отдельная i18n: JSON `assets/locales/*.json`, `app.tr("…")` — для UI, не для CLI (в `apps/solidcraft-cli` вызовов `tr` для help не видно). **проверено поиском в CLI-крейте.**
- Ручной/свой CLI (не clap RFC-0012). Тесты есть, в т.ч. результаты `run`.
- 397 (contract 373, unclear 24, translate 0)
- Command ID / форматы / единицы — не переводятся (`docs/localization.md:99`).
- `strings-solidcraft.tsv`

## 4. Список бинарников CLI (для сверки, ничего не пропущено из найденного)

| Бинарь | Программа | Где в исходнике |
|---|---|---|
| photocraft-cli | photocraft | apps/photocraft-cli |
| photocraft (флаги десктопа) | photocraft | apps/photocraft/src/main.rs |
| pdfcraft-cli | pdfcraft | apps/pdfcraft-cli |
| wordcraft-cli | wordcraft | apps/wordcraft-cli |
| vectorcraft-cli | vectorcraft | apps/vectorcraft-cli |
| filmcraft-cli | filmcraft | apps/filmcraft-cli |
| cadcraft-cli | cadcraft | apps/cadcraft-cli |
| cadcraft (флаги десктопа) | cadcraft | apps/cadcraft + docs/cli.md |
| artcraft-launcher | artcraft-launcher | apps/artcraft-launcher (нет *-cli) |
| craft-ai-mcp | artcraft-launcher (шлюз) | craft-launcher/apps/craft-ai-mcp → craft-ai-integrations/crates/app/ai-mcp |
| lightcraft-cli | lightcraft | apps/lightcraft-cli |
| figcraft-cli | figcraft | apps/figcraft-cli |
| craft-anything-cli | craft-anything | apps/craft-anything-cli |
| designcraft-cli | designcraft | apps/designcraft-cli |
| gridcraft-cli | gridcraft | apps/gridcraft-cli |
| texturecraft-cli | texturecraft | apps/texturecraft-cli |
| anicraft-cli | anicraft | crates/cli |
| anicraft / serve | anicraft | src/main.rs, CLI serve/MCP |
| deckcraft-cli | deckcraft | apps/deckcraft-cli |
| soundcraft-cli | soundcraft | apps/soundcraft-cli |
| materialcraft-cli | materialcraft | apps/materialcraft-cli |
| effectcraft-cli | effectcraft | apps/effectcraft-cli |
| solidcraft-cli | solidcraft | apps/solidcraft-cli |

Не разбирались построчно (факт наличия в дереве **проверен**, содержимое CLI **не проверено**): `pdfcraft-ocr-worker`, `figcraft-server`, xtask’и, возможно другие служебные бинари.

## 5. Открытые вопросы и что блокирует

1. **Глоссарий отдела пуст** (`dept/l10n/glossary/`). Даже если авторы позже разрешат перевод `--help`, спорные термины нужно запросить у Терминолога (см. `terms-needed.md`).
2. **Нет механизма i18n для CLI.** Перевод «просто файлом TSV» в текущую инфраструктуру craft-i18n без согласия авторов и без проводки в clap/USAGE ломал бы тесты и RFC-0012. Это блокирует черновики.
3. **RFC-0012 не слит.** Ссылаться как на принятый стандарт craft-contrib нельзя; как на черновик, которому уже следуют несколько репозиториев — можно, с пометкой.
4. **Полнота ошибок движка.** По документам они часто остаются английскими; полный перечень в engine-крейтеах не инвентаризирован (нужны были бы полные клоны, не только CLI).
5. **Не клонирован storytold/craft-libs** — общая автоматизация/MCP могла бы содержать разделяемые английские сообщения. **не проверено.**
6. **Ставит ли выпускной конвейер перевод UI** — к CLI не относится напрямую; открытый вопрос ROADMAP craft-i18n (из файла: план).
7. **Совпадает ли установленная на установленной системе версия с сегодняшним `main`.** Инвентарь по `main` 20.11.2026; пакеты на машине могут отставать. **не проверено построчно против пакетов** (на установленной системе не заходили).
8. **Animation/serve JSON-RPC и MCP-описания инструментов** (кроме имён) — частично в других крейтеах; не всё попало в TSV.

## 6. Источники

- План: `plan-ru-localization.md` (особенно §4.7 и таблица 19 программ)
- Замер: `findings-20261120-ru.md`
- Клоны: `cli/src/<repo>` (URL и SHA в §3)
- RFC-0012: https://github.com/storytold/craft-contrib/pull/18 и raw `rfcs/0012-cli-conventions.md` с SHA `540825a56883` в этом PR
- Документы авторов: `docs/localisation.md` / `localization.md` / `localization-parity.md` / `localization-ru.md` / `docs/cli.md` в соответствующих репозиториях
- Таблицы строк: `strings-<program>.tsv` в этом каталоге

## 7. Вторая разборка строк unclear (20.11.2026, после 10:38 PT)

По указанию координатора: CLI и ошибки движков, которые авторы нарочно держат английскими, не переводим. Все **366** строк категории `unclear` из первого инвентаря разобраны заново. Если доказательств нет — строка осталась `unclear`, с уточнённым основанием.

Правила этой проходки **проверено** по исходникам и тестам клонов (не догадка, кроме явно помеченного):

- в **contract** переведены только строки с доказательством: тест сверяет точный текст или устойчивый префикс; директива протокола Cargo (`cargo:` / `cargo::` в `build.rs`); машинный JSON; печать той же справки `{USAGE}`, которую тесты уже считают источником правды;
- ошибки движка, которые документы авторов оставляют английскими, в этой выборке unclear почти не встречались (они либо уже были `contract`, либо живут в engine-крейтеах, которые здесь не разбирались);
- в **translate** ничего не переведено: нет ни механизма i18n CLI, ни явного разрешения авторов на перевод этих строк. «Не оговорено» само по себе не считается разрешением. **не выдумано.**

### Счётчики после проходки

Всего строк в TSV по-прежнему **3578** (ничего не удалялось).

| | Было (первый инвентарь) | Стало |
|---|---:|---:|
| contract | 3212 | **3252** |
| unclear | 366 | **326** |
| translate | 0 | **0** |

Из 366 unclear: **40** переведены в contract, **326** остались unclear (основания обновлены), **0** в translate.

По программам после проходки (n / contract / unclear / translate):

| Программа | n | contract | unclear | translate |
|---|---:|---:|---:|---:|
| anicraft | 42 | 42 | 0 | 0 |
| artcraft-launcher | 10 | 6 | 4 | 0 |
| cadcraft | 356 | 352 | 4 | 0 |
| craft-anything | 224 | 186 | 38 | 0 |
| deckcraft | 98 | 79 | 19 | 0 |
| designcraft | 197 | 181 | 16 | 0 |
| effectcraft | 198 | 191 | 7 | 0 |
| figcraft | 212 | 187 | 25 | 0 |
| filmcraft | 91 | 91 | 0 | 0 |
| gridcraft | 103 | 91 | 12 | 0 |
| lightcraft | 168 | 127 | 41 | 0 |
| materialcraft | 20 | 4 | 16 | 0 |
| pdfcraft | 288 | 280 | 8 | 0 |
| photocraft | 535 | 492 | 43 | 0 |
| solidcraft | 397 | 374 | 23 | 0 |
| soundcraft | 320 | 320 | 0 | 0 |
| texturecraft | 39 | 14 | 25 | 0 |
| vectorcraft | 101 | 82 | 19 | 0 |
| wordcraft | 179 | 153 | 26 | 0 |

### Что ушло в contract (40 строк) — типы доказательств

- **Тесты сверяют текст.** Примеры: `photocraft-cli serving on`, `photocraft-cli control token:`, `PHOTOCRAFT_CONTROL_PORT=… serving on TCP instead of stdio`, «N succeeded, M failed»; `rendered page 1 at 18 dpi`; `pdfcraft-cli: {e}` (много `assert_eq` stderr); `unknown command \`frobnicate\`` и формат usage у WordCraft; «character cannot be drawn»; `usage: deckcraft-cli {sub}`; префикс `lightcraft-cli:` при ошибке транспорта. **проверено (источник: указанные tests/it/… в основании каждой строки TSV).**
- **Протокол Cargo** в `build.rs` (`cargo:rerun-if-…`, `cargo::error=`, `cargo:warning=`, `cargo:rustc-link-arg-bins=`) у photocraft, pdfcraft, figcraft, craft-anything, solidcraft: это инструкции сборки, их парсит Cargo. **проверено (источник: соответствующие build.rs).**
- **Печать `{USAGE}`** там, где справка уже закреплена тестами (wordcraft, texturecraft, designcraft, deckcraft desktop). **проверено.**
- **JSON** `{"error": "…"}` у materialcraft-cli. **проверено (источник: apps/materialcraft-cli/src/main.rs:160).**

### Почему 326 остались unclear

Типичные основания (в колонке «основание» каждой строки):

- человекочитаемый прогресс, предупреждения, приглашения (`Allow?`, calibrate/snapshot, «wrote …», старт окна десктопа) — нет пина и нет запрета/разрешения авторов;
- usage-проза вроде «unknown option» у программ, где тесты проверяют только код выхода 2, но не точный текст;
- вывод примеров/бенчмарков (`gpu_bench.rs`, `bench_cull.rs`);
- имя временного файла в тесте WordCraft, не вывод CLI;
- `--version` WordCraft (`wordcraft-cli {версия}`): отдельного assert на этот формат не найдено (help-тест сверяет другой префикс «wordcraft-cli — »).

Категория **translate** пуста, черновики `draft-ru-*.tsv` по-прежнему не создавались: точки перевода CLI нет.

Глоссарий отдела на момент первой проходки (≈10:24 PT) в `glossary/` был пуст; к этой проходке файл уже есть — сверка в `terms-needed.md`.
