# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/gridcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/gridcraft
Коммит исходника (последний, в котором менялся README.md): ef99f1e51f5f971a7c83da5acbc4dc7bcc62f2c5
Дата коммита: 15 ноября 2026, 23:59 (America/Los_Angeles, PT); в исходнике 2026-11-16T07:59:28Z
SHA256 исходника: 83644aaa6c12aa1b753b5ef79ebf65cc5181bd4af646ae21ac27e6fbcfa8bb1f
Git blob SHA: a58f4fb1951dd480662eb6356ee87e3d9d72b93b
Размер исходника: 25914 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/gridcraft/main/README.md
Перевод выполнен локально; авторам не отправлялся. Строки-переключателя языков нет: в репозитории нет других README.<код>.md.
-->
<!-- Перевод не проверен авторами -->
<p align="center">
  <a href="https://getartcraft.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/artcraft-logo-white.svg">
      <img alt="ArtCraft" src="docs/brand/artcraft-logo.svg" width="200">
    </picture>
  </a>
</p>

<p align="center">
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.gridcraft.png" width="128" height="128" alt="Значок GridCraft: страница электронной таблицы на зелёной плитке">
</p>

<h1 align="center">GridCraft</h1>

<p align="center">
  <b>Электронные таблицы и данные; высокопроизводительная современная программа для таблиц с открытым исходным кодом, написанная на чистом Rust.</b>
</p>

<p align="center">
  Быстрый взгляд с открытым исходным кодом и с чистого листа на современные рабочие процессы электронных таблиц. Работает нативно в macOS,
  Windows, Linux и BSD и в браузере через WebAssembly.<br>
  <i>Команда ArtCraft.</i>
</p>

<p align="center">
  <img alt="Written in Rust" src="https://img.shields.io/badge/written%20in-Rust-147a40?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows, Linux, BSD and the web" src="https://img.shields.io/badge/runs%20on-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20BSD%20%C2%B7%20Web-1f9d55?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-147a40?style=flat-square">
  <img alt="Agent-drivable over MCP" src="https://img.shields.io/badge/agents-MCP-1f9d55?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_gridcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/gridcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/gridcraft"><b>GridCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/hero-sales.png" alt="GridCraft показывает квартальную панель продаж: оформленная таблица с чередованием строк, кнопками фильтра, строкой итогов, гистограммами, значками стрелок и спарклайнами рядом с кластерной столбчатой диаграммой и круговой диаграммой" width="100%">
  <br><sub><b>Квартальная панель продаж</b>: таблица со строкой итогов, условным форматированием, спарклайнами и двумя живыми диаграммами — целиком собрана командами GridCraft (<code>File → New → Sample</code>).</sub>
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Живописцы, фотографы,
> кинематографисты, иллюстраторы, дизайнеры, аниматоры, любители и те, кто взял карандаш
> в руки только на прошлой неделе. Если вы что-то создаёте, вы один из нас. **[Загляните в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#a-look-around">Взгляд вокруг</a> ·
  <a href="#why-gridcraft">Почему GridCraft</a> ·
  <a href="#quick-start">Быстрый старт</a> ·
  <a href="#for-agents-mcp-cli-and-the-control-channel">Для агентов</a> ·
  <a href="#architecture">Архитектура</a> ·
  <a href="#roadmap">План работ</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">Лицензия и благодарности</a>
</p>

<a id="a-look-around"></a>
## Взгляд вокруг

<table>
<tr>
<td width="50%" valign="top"><img src="docs/images/budget.png" alt="Семейный бюджет с бухгалтерскими числовыми форматами, красной подсветкой перерасходованных категорий, зелёно-жёлто-красной цветовой шкалой в столбце процента использования, строкой итогов с двойной границей и горизонтальной линейчатой диаграммой, сравнивающей бюджет с фактом" width="100%"><p align="center"><sub><b>Форматирование.</b> Бухгалтерские форматы, стили ячеек, условные правила и цветовые шкалы, закреплённые заголовки и линейчатая диаграмма.</sub></p></td>
<td width="50%" valign="top"><img src="docs/images/grades-formulas.png" alt="Журнал оценок со средними и буквенными оценками, посчитанными через IFS, зелёной подсветкой пятёрок и гистограммами; открыта вкладка ленты «Формулы» с библиотекой функций" width="100%"><p align="center"><sub><b>Формулы.</b> Более 500 функций, динамические массивы, LET и LAMBDA, структурированные ссылки таблиц.</sub></p></td>
</tr>
<tr>
<td width="50%" valign="top"><img src="docs/images/dark-insert.png" alt="Панель продаж в тёмном режиме с открытой вкладкой ленты «Вставка»: кнопки «Сводная таблица», «Таблица», «Рисунки», «Фигуры», диаграмма, спарклайн, ссылка, примечание, надпись и символ" width="100%"><p align="center"><sub><b>Тёмный режим</b> и вкладка «Вставка»: таблицы, диаграммы, спарклайны, рисунки, фигуры, ссылки и примечания.</sub></p></td>
<td width="50%" valign="top"><img src="docs/images/pivot.png" alt="Сводная таблица с итогами выручки по регионам и продуктам, фильтром отчёта Channel, общими итогами и денежным форматом; справа открыта панель полей сводной таблицы с отмеченными полями и областями «Фильтры», «Столбцы», «Строки» и «Значения»" width="100%"><p align="center"><sub><b>Сводные таблицы.</b> Список полей, фильтры, макеты, группировка дат и «показать значения как», запись в XLSX и чтение из него.</sub></p></td>
</tr>
<tr>
<td width="50%" valign="top"><img src="docs/images/format-chart.png" alt="Панель продаж с выделенной столбчатой диаграммой: манипуляторы размера на диаграмме, исходные данные обведены в таблице, открыта вкладка «Конструктор диаграмм» и справа панель «Формат области диаграммы»" width="100%"><p align="center"><sub><b>Диаграммы.</b> Семнадцать типов диаграмм, вкладка «Конструктор диаграмм» и панель «Формат»; при выделении диаграммы обводятся её исходные данные.</sub></p></td>
<td width="50%" valign="top"><img src="docs/images/page-break.png" alt="Семейный бюджет в страничном режиме: область печати обведена синим с пунктирным разрывом страницы, водяные знаки «Страница 1» и «Страница 2», область вне диапазона печати затемнена" width="100%"><p align="center"><sub><b>Страничный режим</b>, параметры печати, экспорт в PDF и печать.</sub></p></td>
</tr>
</table>

<a id="why-gridcraft"></a>
## Почему GridCraft

- **Привычно.** Лента, строка формул, поле имени, ярлыки листов, сочетания клавиш, маркер заполнения,
  ввод формул в режиме указания с цветными ссылками, «Формат ячеек», «Специальная вставка»,
  условное форматирование, таблицы, диаграммы и многое другое. Всё стоит там, где вы ожидаете.
- **Совместимо.** XLSX — собственный формат: стили, темы, формулы (включая динамические массивы),
  таблицы, условные форматы, проверка, примечания, гиперссылки, диаграммы, рисунки, спарклайны,
  сводные таблицы и параметры печати проходят туда и обратно. Также CSV и TSV.
  Устаревшие книги 97-2003 `.xls` открываются со значениями, формулами и числовыми форматами (оформление и объекты пока нет).
  [Данные листов XLSB можно импортировать](docs/xlsb-import.md), используя сохранённые значения вместо формул.
  [Данные листов ODS можно импортировать](docs/ods-import.md), используя сохранённые значения вместо формул.
  [Статичные рисунки могут жить внутри ячеек](docs/cell-pictures.md), подстраиваясь под размер и двигаясь вместе с данными.
- **Умело.** Движок расчёта на графе зависимостей с динамическими массивами и растеканием,
  более 500 функций листа плюс LET, LAMBDA, MAP, REDUCE, SCAN, BYROW, BYCOL и MAKEARRAY,
  структурированные ссылки таблиц, богатый язык числовых форматов, сортировка и автофильтр,
  мгновенное заполнение, проверка данных, структура и промежуточные итоги.
- **Быстро.** Книги с копированием при записи (снимки для отмены почти ничего не стоят), инкрементный пересчёт
  и виртуализированная сетка, которая размечает только то, что на экране.
- **Для агентов.** Каждая кнопка ленты, пункт меню, диалог, нажатие клавиши и жест мыши — это
  команда, которую агенты могут выполнить по JSON-каналу управления, через **MCP-сервер** или из CLI.
- **Везде.** Одна кодовая база на Rust для настольной программы и веба. Никакой подписки, никакого сервера лицензий,
  никакой телеметрии.

<a id="quick-start"></a>
## Быстрый старт

```sh
cargo run --release -p gridcraft                              # desktop app
cargo run --release -p gridcraft -- --sample sales            # open a sample (sales, budget, grades)
cargo run --release -p gridcraft -- book.xlsx                 # open a workbook
cargo run --release -p gridcraft -- --sample sales --control 7979   # + JSON control channel
cargo xtask ci                                                 # fmt, clippy, tests, assets, layering, wasm
```

Выберите Español в Вид → Язык интерфейса, чтобы получить [испанские имена функций, десятичные запятые и аргументы через точку с запятой](docs/formula-input.md).
В книгах, обмене через буфер обмена и программных API сохраняется канонический английский синтаксис.

<a id="web"></a>
### Веб

```sh
cd apps/gridcraft-web && trunk build --release     # → dist/web (serve it with any static server)
cd apps/gridcraft-web && trunk serve --release     # http://127.0.0.1:8771  (?sample=sales opens a sample)
```

Нужны [trunk](https://trunk-rs.github.io/trunk/) и цель `wasm32-unknown-unknown`. «Открыть» вызывает
системный выбор файла браузера (перетаскивание тоже работает), а «Сохранить» скачивает книгу.

<a id="ribbon-access-keys"></a>
### Клавиши доступа ленты

Нажмите и отпустите **левый Alt** в Windows/Linux/BSD или нажмите **F10** на любой платформе,
затем введите одну из последовательностей ниже по одной клавише. Подсказки клавиш появляются на поддерживаемых элементах вкладки
«Главная» и пунктах меню. В macOS используйте F10 (Fn+F10, если так устроена клавиатура); Option
по-прежнему служит для ввода символов с диакритикой.

| Последовательность после Alt/F10 | Действие |
|---|---|
| `H A L` / `H A C` / `H A R` | Выровнять по левому краю / по центру / по правому краю |
| `H V S` или прежнее `E S` | Открыть «Специальную вставку» |
| `H O I` или прежнее `O C A` | Автоподбор ширины выделенных столбцов |

В «Специальной вставке» **T/V/F/C** выбирают форматы/значения/формулы/примечания, а **E** включает и выключает
транспонирование. **Enter** применяет выбранные параметры; **Escape** закрывает диалог.
Эти буквы также работают с удержанным Alt в Windows/Linux/BSD.

Escape возвращает на один уровень подсказок назад; повторное Alt/F10 выходит из режима подсказок. Щелчок, прокрутка
или переключение окон отменяют навигацию. Клавиши доступа не запускаются, пока вы правите текст
или открыт другой диалог. Это начальная поддержка этих путей вкладки «Главная» и прежних сочетаний;
остальные команды ленты и навигация полностью без мыши ещё впереди.
Браузеры или среды рабочего стола могут оставлять Alt/F10 за своими меню.

<a id="logs"></a>
### Журнал

Настольная программа пишет журнал в стандартный поток ошибок и в `gridcraft.log` в папке `logs`
рядом с настройками: `~/.config/gridcraft/logs` в Linux и BSD (`$XDG_CONFIG_HOME/gridcraft/logs`,
если задано), `~/Library/Application Support/GridCraft/logs` в macOS и
`%APPDATA%\GridCraft\logs` в Windows. Каждый запуск переносит предыдущий журнал в `gridcraft.1.log`, а
тот — в `gridcraft.2.log`, так что журнал аварийного запуска переживает следующий старт; приложите
их к сообщению об ошибке. Файл журнала перестаёт расти на 16 MiB. По умолчанию собственные крейты GridCraft пишут
на уровне `info`, а всё остальное — на `warn`; `RUST_LOG` подменяет это директивами в стиле env_logger,
например `RUST_LOG=debug` или `RUST_LOG=warn,gridcraft_engine=debug` (завершающая `*`
совпадает с префиксом: `gridcraft*=debug`). Запуски с установленным `GRIDCRAFT_NO_PREFS` (без сохранённых настроек)
пишут только в стандартный поток ошибок.

<a id="for-agents-mcp-cli-and-the-control-channel"></a>
## Для агентов: MCP, CLI и канал управления

```sh
claude mcp add gridcraft -- gridcraft-cli mcp                 # headless MCP server
gridcraft-cli mcp --connect 7979                               # MCP bridged to a running window
gridcraft-cli eval '=XLOOKUP("b",{"a","b"},{1,2})'             # → 2
gridcraft-cli run --sample budget --cmd 'home.bold={"range":"B4:F4"}' --out budget.xlsx
gridcraft-cli cat budget.xlsx --range B4:F15                   # aligned text table
gridcraft-cli commands --search chart                          # every command and its params
```

MCP-сервер предлагает такие инструменты, как `read_range`, `write_range`, `set_cell`, `evaluate_formula`,
`format_range`, `insert_chart`, `create_table`, `sort_range`, `filter` и `execute_command`
(последний достаёт до каждой команды GridCraft). Канал управления настольной программы добавляет настоящий
ввод указателя и клавиатуры, диалоги и снимки экрана. См. [`docs/mcp.md`](docs/mcp.md),
[`docs/cli.md`](docs/cli.md) и [`docs/control-protocol.md`](docs/control-protocol.md).

<a id="architecture"></a>
## Архитектура

GridCraft — это Cargo workspace с движком в основе и принудительной слоистостью (`cargo xtask layers`).
Оболочка на egui — отдельный крейт, поэтому интерфейс можно заменить, не трогая движок.

| Слой | Крейты |
|---|---|
| L0 | `core` (адреса, значения, ошибки, даты, разбор ввода) · `numfmt` (коды числовых форматов) |
| L1 | `formula` (лексер, анализатор, печать, правка ссылок) · `functions` (библиотека функций листа) |
| L2 | `model` (книга, листы, ячейки с копированием при записи, стили, таблицы, диаграммы…) · `calc` (граф зависимостей, вычислитель, динамические массивы) · `xlsx` (XLSX, CSV, плюс импорт данных XLSB и ODS) |
| L3 | `chart` (вёрстка и отрисовка диаграмм без внешнего набора инструментов) |
| L5 | `engine` (сеанс, команды, история, буфер обмена, заполнение, сортировка, фильтр, файловый ввод-вывод) |
| L6 | `ui-egui` (интерфейс таблицы, канал управления) · `mcp` (MCP-сервер) |
| L7 | `apps/gridcraft`, `apps/gridcraft-cli`, `apps/gridcraft-web` |

- **Правила для участников и агентов** (чистая комната, политика ресурсов, никаких падений, качественные проверки): [`AGENTS.md`](AGENTS.md)
- **Встроенные ресурсы:** каждый указан с лицензией в [`ATTRIBUTION.md`](ATTRIBUTION.md)
- **Выпуски:** подписанные сборки для macOS, Windows, Linux, BSD и веба; см. [`docs/releasing.md`](docs/releasing.md)

<a id="roadmap"></a>
## План работ

GridCraft в **альфе**: базовый рабочий процесс проходит от начала до конца, но глубина, точность и совместимость
файлов ещё черновые. Покрыто 89% стандартных команд ленты в нашем каталоге
([`docs/parity-checklist.md`](docs/parity-checklist.md)) и 514 стандартных функций листа
([`docs/function-parity.md`](docs/function-parity.md)); это опись паритета, а не подсчёт работающих реализаций. С весами по тому, на что опираются пользователи таблиц, мы
оцениваем готовность к настоящей работе примерно в 50%. Дальше: точность XLSX на реальных файлах, очень большие
книги и многопоточный пересчёт, глубина диаграмм, текст во всех письменностях и импорт `.xls`. Этап,
цифры и оценки — в [ROADMAP.md](ROADMAP.md); упорядоченный список работ — в [`docs/gaps.md`](docs/gaps.md).

<a id="downloads"></a>
## Загрузки

**Скачайте GridCraft** с GitHub: в [последнем выпуске](https://github.com/storytold/gridcraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/gridcraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `gridcraft-<ver>-windows-x64.msi` | `gridcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `gridcraft-<ver>-windows-arm64.msi` | `gridcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `gridcraft-<ver>-windows-x86.msi` | `gridcraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы подписаны. Установщик MSI предлагает необязательный ярлык на рабочем столе
(при новой установке снят).

**Если программа не открывается в Windows:** настольная программа по умолчанию инициализирует только DirectX 12.
Если позволить wgpu также создать экземпляр OpenGL, некоторые графические драйверы (AMD
`atio6axx.dll`) могут аварийно завершиться до появления окна, и программа мигнёт в «Диспетчере задач» и выйдет.
`WGPU_BACKEND` подменяет значение по умолчанию для диагностики (например, `dx12` или `vulkan`). В
PowerShell, из папки с исполняемым файлом:

```powershell
$env:WGPU_BACKEND = "vulkan"
& .\gridcraft.exe
Remove-Item Env:WGPU_BACKEND                     # restore the default for later launches
```

Явный ключ `gl` может вернуть падение драйвера на затронутых системах, а `vulkan` может
вернуть падение в некоторых драйверах Intel UHD Graphics (`igvk64.dll`, #120). Значения по умолчанию для macOS, Linux и
веба не менялись.

**Если программа медленно работает на старом ПК с Windows или DirectX 12 не запускается:** когда DirectX 12 не находит
видеокарту с подходящим драйвером, он предлагает только программный визуализатор от Windows, который рисует каждый
кадр на процессоре. В этом случае GridCraft сам переходит на OpenGL, без дополнительных настроек; если
первый визуализатор не запускается, другой пробуется один раз. Выбор записывается в файл журнала
(строки, начинающиеся с `graphics:`). `WGPU_BACKEND` по-прежнему его подменяет (и тогда больше ничего не
пробуется), например `$env:WGPU_BACKEND = "gl"` или `"dx12"`.

Шейдеры DirectX 12 компилируются через FXC, который входит в Windows, поэтому `dxcompiler.dll` и
`dxil.dll` не нужны, и копия, которую другая программа положила в `PATH`, больше не может остановить программу при запуске
(«Parent device is lost», #339). `$env:WGPU_DX12_COMPILER = "dxc"` (или `"auto"`) снова включает обработку DXC в wgpu
для диагностики.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `gridcraft-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `gridcraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `gridcraft-<ver>-linux-x86_64.AppImage` | `gridcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `gridcraft-<ver>-linux-x86_64.flatpak` | `gridcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `gridcraft-<ver>-linux-x86_64.deb` | `gridcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `gridcraft-<ver>-linux-x86_64.rpm` | `gridcraft-<ver>-linux-aarch64.rpm` | |
| Архив | `gridcraft-<ver>-linux-x86_64.tar.gz` | `gridcraft-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `gridcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `gridcraft-web-<ver>.zip` | Работает в современном браузере; разместите на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

GridCraft — одно из приложений **Crafting Apps**: бесплатных творческих инструментов с открытым исходным кодом от команды
[ArtCraft](https://getartcraft.com/), каждое написано с нуля на Rust и каждое может работать само по себе.

| | Приложение | Для чего | Код | Подробнее |
|:-:|---|---|---|---|
| <img src="https://raw.githubusercontent.com/storytold/photocraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.photocraft.png" alt="" width="32" height="32"> | **PhotoCraft** | Редактирование изображений: слои, маски, текст и настоящие файлы PSD | [GitHub](https://github.com/storytold/photocraft) | [Сайт](https://getartcraft.com/apps/photocraft) |
| <img src="https://raw.githubusercontent.com/storytold/vectorcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.vectorcraft.png" alt="" width="32" height="32"> | **VectorCraft** | Векторная иллюстрация | [GitHub](https://github.com/storytold/vectorcraft) | [Сайт](https://getartcraft.com/apps/vectorcraft) |
| <img src="https://raw.githubusercontent.com/storytold/filmcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.filmcraft.png" alt="" width="32" height="32"> | **FilmCraft** | Монтаж видео, цвет и звук | [GitHub](https://github.com/storytold/filmcraft) | [Сайт](https://getartcraft.com/apps/filmcraft) |
| <img src="https://raw.githubusercontent.com/storytold/lightcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.lightcraft.png" alt="" width="32" height="32"> | **LightCraft** | Библиотека фотографий и проявление raw | [GitHub](https://github.com/storytold/lightcraft) | [Сайт](https://getartcraft.com/apps/lightcraft) |
| <img src="https://raw.githubusercontent.com/storytold/pdfcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.pdfcraft.png" alt="" width="32" height="32"> | **PdfCraft** | Чтение, организация и защита PDF | [GitHub](https://github.com/storytold/pdfcraft) | [Сайт](https://getartcraft.com/apps/pdfcraft) |
| <img src="https://raw.githubusercontent.com/storytold/effectcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.effectcraft.png" alt="" width="32" height="32"> | **EffectCraft** | Моушн-графика и визуальные эффекты | [GitHub](https://github.com/storytold/effectcraft) | [Сайт](https://getartcraft.com/apps/effectcraft) |
| <img src="https://raw.githubusercontent.com/storytold/designcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.designcraft.png" alt="" width="32" height="32"> | **DesignCraft** | Вёрстка и публикация | [GitHub](https://github.com/storytold/designcraft) | [Сайт](https://getartcraft.com/apps/designcraft) |
| <img src="https://raw.githubusercontent.com/storytold/figcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.figcraft.png" alt="" width="32" height="32"> | **FigCraft** | Дизайн интерфейсов и прототипирование | [GitHub](https://github.com/storytold/figcraft) | [Сайт](https://getartcraft.com/apps/figcraft) |
| <img src="https://raw.githubusercontent.com/storytold/wordcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.wordcraft.png" alt="" width="32" height="32"> | **WordCraft** | Текстовый процессор и документы | [GitHub](https://github.com/storytold/wordcraft) | [Сайт](https://getartcraft.com/apps/wordcraft) |
| <img src="https://raw.githubusercontent.com/storytold/soundcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.soundcraft.png" alt="" width="32" height="32"> | **SoundCraft** | Запись и редактирование звука | [GitHub](https://github.com/storytold/soundcraft) | [Сайт](https://getartcraft.com/apps/soundcraft) |
| <img src="https://raw.githubusercontent.com/storytold/deckcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.deckcraft.png" alt="" width="32" height="32"> | **DeckCraft** | Презентации и слайд-колоды | [GitHub](https://github.com/storytold/deckcraft) | [Сайт](https://getartcraft.com/apps/deckcraft) |
| <img src="https://raw.githubusercontent.com/storytold/cadcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.cadcraft.png" alt="" width="32" height="32"> | **CADCraft** | Автоматизированное проектирование | [GitHub](https://github.com/storytold/cadcraft) | [Сайт](https://getartcraft.com/apps/cadcraft) |
| <img src="https://raw.githubusercontent.com/storytold/gridcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.gridcraft.png" alt="" width="32" height="32"> | **GridCraft** | Электронные таблицы и данные | [GitHub](https://github.com/storytold/gridcraft) | [Сайт](https://getartcraft.com/apps/gridcraft) |
| <img src="https://raw.githubusercontent.com/storytold/texturecraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.texturecraft.png" alt="" width="32" height="32"> | **TextureCraft** | Рисование 3D-текстур | [GitHub](https://github.com/storytold/texturecraft) | [Сайт](https://getartcraft.com/apps/texturecraft) |
| <img src="https://raw.githubusercontent.com/storytold/craft-anything/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.craft-anything.png" alt="" width="32" height="32"> | **Craft Anything** | Смотрите, как устроена любая программа, и собирайте свою | [GitHub](https://github.com/storytold/craft-anything) | [Сайт](https://getartcraft.com/apps/craft-anything) |
| <img src="https://raw.githubusercontent.com/tangency-labs/solidcraft/main/assets/icons/app/linux/exports/hicolor/64x64/apps/io.tangencylabs.solidcraft.png" alt="" width="32" height="32"> | **SolidCraft** | Параметрический 3D CAD от Tangency Labs (приложение сообщества) | [GitHub](https://github.com/tangency-labs/solidcraft) | |

И сам [**ArtCraft**](https://getartcraft.com/) — наша ИИ-студия изображений и видео для художников, которым нужен настоящий контроль.

<br>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<h3 align="center">Приходите творить с нами</h3>

<p align="center">
  Наш Discord — место, где собираются художники всех направлений: те, кто пишет красками, снимает, рисует, монтирует
  кино, набирает текст, и те, кто ещё ищет, что им нравится делать. Покажите, над чем работаете,
  попросите помощи, расскажите, что сломалось, или чего вы ждёте от этих инструментов.
  В каком бы материале вы ни работали и сколько бы вы этим ни занимались, вам здесь рады.
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><b>discord.gg/artcraft</b></a> ·
  <a href="https://getartcraft.com/">getartcraft.com</a> ·
  <a href="https://getartcraft.com/apps">The Crafting Apps</a> ·
  <a href="https://getartcraft.com/apps/gridcraft">GridCraft</a>
</p>

<a id="license-and-credits"></a>
## Лицензия и благодарности

GridCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the GridCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Все значки интерфейса нарисованы в коде и оригинальны; образцовые книги и каждый снимок экрана в
этом README сделаны самим GridCraft. GridCraft не встраивает шрифты: он использует шрифты,
установленные в системе.

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и GridCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<br>

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
