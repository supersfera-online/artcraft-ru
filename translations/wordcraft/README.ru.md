# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/wordcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/wordcraft
Коммит исходника (последний, в котором менялся README.md): 739cdcad0b4abc7502906a57ac1019613669437b
Дата коммита: 16 ноября 2026, 20:15 (America/Los_Angeles, PT); в исходнике 2026-11-17T04:15:46Z
SHA256 исходника: 8f56af322cd661c6da244c7c885a276ba9f20e8f80762e0033f374b3c2329923
Git blob SHA: ee41a08d2deaf659392db23033317c5ed6b903cb
Размер исходника: 35815 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/wordcraft/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.wordcraft.png" width="128" height="128" alt="Значок WordCraft: страница документа и перо на синей плитке">
</p>

<h1 align="center">WordCraft</h1>

<p align="center">
  <b>Письмо и оформление документов; современный текстовый процессор с открытым исходным кодом, построенный на чистом Rust.</b>
</p>

<p align="center">
  Быстрый текстовый процессор с открытым исходным кодом и знакомым рабочим процессом: лента, стили,
  таблицы, исправления, ссылки и слияние почты. Читает и пишет .docx, работает нативно в
  macOS, Windows, Linux и BSD и в браузере через WebAssembly.<br>
  <i>Команда ArtCraft.</i>
</p>

<p align="center">
  <img alt="Written in Rust" src="https://img.shields.io/badge/written%20in-Rust-2b47b5?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows, Linux, BSD and the web" src="https://img.shields.io/badge/runs%20on-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20BSD%20%C2%B7%20Web-3b5bdb?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-2b47b5?style=flat-square">
  <img alt="Agent-drivable over MCP" src="https://img.shields.io/badge/agents-MCP%20%C2%B7%20CLI-3b5bdb?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_wordcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/wordcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/wordcraft"><b>WordCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/hero.png" alt="WordCraft с открытой вкладкой «Главная» ленты над двухстраничным документом The Open Studio Handbook. Панель навигации слева перечисляет заголовки документа, галерея стилей показывает живые образцы Normal, Heading 1, Title и Subtitle, в первом абзаце выбрано слово." width="100%">
  <br><sub><b>The Open Studio Handbook</b>, встроенный образец WordCraft: лента, живая галерея стилей, линейки и панель навигации.</sub>
</p>

> [!NOTE]
> **ArtCraft — это сообщество художников из самых разных сфер.** Живописцы, фотографы,
> кинематографисты, иллюстраторы, дизайнеры, аниматоры, любители и те, кто взял карандаш
> на прошлой неделе. Если вы что-то создаёте, вы один из нас. **[Заходите поздороваться в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#a-tour">Обзор</a> ·
  <a href="#why-wordcraft">Зачем WordCraft</a> ·
  <a href="#what-works-today">Что уже работает</a> ·
  <a href="#quick-start">Быстрый старт</a> ·
  <a href="#for-agents-cli-and-mcp">Для агентов</a> ·
  <a href="#architecture">Архитектура</a> ·
  <a href="#roadmap">План</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">Лицензия и благодарности</a>
</p>

<a id="a-tour"></a>
## Обзор

Каждый снимок ниже — сам WordCraft, отрисованный вне экрана его собственным стендом тестов интерфейса
(`cargo run -p wordcraft-ui-egui --example ui_shot`).

<table>
<tr>
<td width="50%" valign="top"><img src="docs/images/review.png" alt="Вкладка «Рецензирование» с включёнными исправлениями: слово forty вставлено пурпурным, thirty зачёркнуто; три прокомментированные фразы затенены и соединены пунктирными выносками с пузырями комментариев в серой области разметки справа от страницы" width="100%"><p align="center"><sub><b>Рецензирование.</b> Исправления, пузыри комментариев на поле, принять и отклонить, орфография и грамматика по мере ввода.</sub></p></td>
<td width="50%" valign="top"><img src="docs/images/references.png" alt="Вкладка «Ссылки» с двумя страницами рядом: оглавление с точечными отточиями и номерами страниц на первой и оформленная таблица, нумерованный список и гиперссылка на второй" width="100%"><p align="center"><sub><b>Ссылки.</b> Оглавления, сноски, цитаты в APA, MLA, Chicago или IEEE, указатель и подписи.</sub></p></td>
</tr>
<tr>
<td width="50%" valign="top"><img src="docs/images/design.png" alt="Вкладка «Дизайн» с образцами наборов стилей; документ набран в антиквенной теме со сливовыми заголовками, подчёркнутыми тонкими линейками, и бледным диагональным водяным знаком DRAFT за текстом" width="100%"><p align="center"><sub><b>Дизайн.</b> Темы, наборы стилей, интервалы абзацев, водяные знаки, цвет и границы страницы.</sub></p></td>
<td width="50%" valign="top"><img src="docs/images/dark.png" alt="WordCraft в тёмном режиме с открытой вкладкой «Вставка» и показанными знаками форматирования: символы абзаца в концах абзацев и точки вместо пробелов" width="100%"><p align="center"><sub><b>Тёмный режим</b> со знаками форматирования и вкладка «Вставка»: таблицы, рисунки, фигуры, ссылки, колонтитулы, поля и символы.</sub></p></td>
</tr>
<tr>
<td colspan="2"><img src="docs/images/layout.png" alt="Вкладка «Макет» при масштабе 80 %: первый абзац открывается буквицей E в три строки, тёмно-синий круг стоит рядом со вторым разделом, абзац обтекает его и переносит art-ist в конце строки, каждая строка пронумерована на левом поле, тонкая синяя рамка окружает страницу" width="100%"><p align="center"><sub><b>Макет.</b> Буквицы, обтекание текстом рисунков и фигур, автоматическая расстановка переносов, номера строк и границы страницы.</sub></p></td>
</tr>
<tr>
<td colspan="2"><img src="docs/images/backstage.png" alt="Стартовая страница вкладки «Файл» с приветствием Good morning, миниатюрами шаблонов Blank document, Studio handbook, Letter, Résumé и Report и списком недавних документов" width="100%"><p align="center"><sub><b>Файл.</b> Начните с шаблона, откройте недавние документы, правьте свойства, выгружайте в PDF и другие форматы.</sub></p></td>
</tr>
</table>

<a id="why-wordcraft"></a>
## Зачем WordCraft

- **Привычно.** Вкладки ленты, группы, сочетания и поведение: Enter продолжает список,
  Tab понижает его уровень, Ctrl/⌘+B делает полужирным слово под кареткой, галерея стилей показывает стили вживую,
  F4 повторяет, F7 проверяет орфографию, F8 расширяет выделение.
- **Ваши файлы.** Открывает и сохраняет .docx (OOXML), а также .odt, .rtf, .html, .md, .tex (LaTeX), .txt; открывает устаревшие .doc 97-2003; выгружает PDF
  с настоящим выделяемым текстом, ссылками и закладками.
- **Быстро.** Раскладка абзацев кэшируется, поэтому ввод в 188-страничном документе перераскладывает его примерно за
  1,4 мс; страницы рисуются по требованию.
- **Везде.** Одна кодовая база на Rust для macOS, Windows, Linux, BSD и веба. Без Electron и без
  Tauri: нативный [egui](https://github.com/emilk/egui) на GPU.
- **Для агентов.** Каждое действие — команда с идентификатором. Те же 422 команды управляют
  лентой, сочетаниями клавиш, поиском команд, инструментом командной строки, каналом управления JSON и
  сервером MCP.
- **Приватно.** Орфография, грамматика и всё остальное работают без сети.
- **Открыто.** MIT OR Apache-2.0. Чистая комната: построено по открытым спецификациям и наблюдению, каждый
  ресурс оригинален или открыто лицензирован.

<a id="what-works-today"></a>
## Что уже работает

| Область | Главное |
|---|---|
| **Письмо** | Быстрый ввод с IME, умные кавычки, автозамена, автоформат списков (`* `, `1. `), тире; выделение слова, предложения, абзаца; выделение протяжкой; буфер обмена с оформлением; отмена/повтор; поиск и замена с регулярными выражениями |
| **Оформление** | Шрифты, размеры, стили полужирный/курсив/подчёркивание, зачёркивание, верхний/нижний индекс, все прописные, выделение цветом, цвета, межбуквенный интервал, формат по образцу, смена регистра, очистка форматирования |
| **Абзацы** | Выравнивание, отступы (перетаскиваются на линейке), интервалы, межстрочный интервал, табуляции с отточиями, границы, заливка, не отрывать от следующего, контроль висячих строк |
| **Стили** | Встроенный набор стилей, живая галерея, панель стилей, создание/изменение/обновление стилей, наборы стилей, темы |
| **Списки** | Маркеры, нумерация, многоуровневые, начать заново, задать значение, пользовательские форматы |
| **Таблицы** | Вставка по сетке, объединение/разделение, стили с чередованием строк, границы, заливка, строки заголовка, повторяющиеся на страницах, строки, которые разделяются по страницам, сортировка, формулы, текст ↔ таблица |
| **Страницы** | Поля, ориентация, размер, колонки, разрывы страницы/колонки/раздела, колонтитулы (первая страница, нечётные/чётные), номера страниц, водяной знак, границы страницы, номера строк, вертикальное выравнивание, буквицы, автоматическая расстановка переносов |
| **Объекты** | Рисунки (размер, кадрирование, перекраска, яркость/контраст, прозрачность, удаление фона, стили рисунка, поворот), фигуры, надписи, плавающее положение с обтеканием текстом (вокруг, сверху и снизу, за текстом или перед текстом) |
| **Ссылки** | Оглавление, сноски и концевые сноски, цитаты и библиография (APA, MLA, Chicago, IEEE), подписи, список иллюстраций, перекрёстные ссылки, указатель, список источников права |
| **Рецензирование** | Орфография и грамматика с подсказками (английский и польский, по языку каждого запуска), тезаурус, число слов, комментарии в пузырях на поле или на панели, исправления, принять/отклонить, сравнение документов, ограничение правки, проверка доступности, инспектор документа |
| **Рассылки** | Слияние почты из CSV, поля слияния, блок адреса, строка приветствия, правила, предварительный просмотр, завершение в документ; конверты и наклейки |
| **Вид** | Разметка страницы, веб-разметка, черновик, режим чтения, фокус, масштаб, одна/несколько страниц, по ширине страницы, панель навигации, линейки, линии сетки, тёмный режим; интерфейс на английском, 简体中文, 繁體中文, 日本語, Português (Brasil), Español, Українська, Српски / Srpski, Eesti, Türkçe, Русский, Italiano, Deutsch, Polski, Čeština, Magyar, Français, Български, Tiếng Việt, 한국어, Svenska, Hrvatski, Nederlands, Dansk, Română, العربية (зеркально) Slovenščina или Bosanski (по умолчанию следует языку системы) |
| **Файлы** | Чтение/запись .docx, импорт устаревших .doc 97-2003, выгрузка PDF, импорт/экспорт .odt, .rtf, .html, .md, .tex, .txt, изображения страниц |

Честная картина по областям — в [ROADMAP.md](ROADMAP.md),
[оценке сопоставимости](docs/target-app-parity.md) и порождённом
[контрольном списке возможностей](docs/parity-checklist.md).

<a id="quick-start"></a>
## Быстрый старт

```sh
git clone https://github.com/storytold/wordcraft
cd wordcraft
cargo run --release -p wordcraft -- --sample        # the desktop app with the sample document
cargo run --release -p wordcraft -- report.docx     # open a document
```

Переводы интерфейса и данные орфографии и переносов берутся из
[craft-i18n](https://github.com/storytold/craft-i18n), необязательного входа сборки. Чтобы собрать с ними,
получите его на коммите из `craft-i18n.rev` и укажите на него `CRAFT_I18N_DIR` (абсолютный
путь); без него WordCraft собирается с английским интерфейсом, английская орфография отступает к
установленному английскому Hunspell или встроенному списку слов craft-proof, а переносятся только болгарский, турецкий и
русский (по правилам):

```sh
git clone https://github.com/storytold/craft-i18n ../craft-i18n
git -C ../craft-i18n checkout "$(cat craft-i18n.rev)"
CRAFT_I18N_DIR="$PWD/../craft-i18n" cargo run --release -p wordcraft -- --sample
```

Командная строка:

```sh
wordcraft-cli convert report.docx report.pdf        # docx, pdf, odt, rtf, html, md, tex, txt, png
wordcraft-cli convert report.docx report.pdf --strict   # exit 3, no file, if a character or picture would be left out
wordcraft-cli text report.docx                      # plain text
wordcraft-cli inspect report.docx                   # structure as JSON
wordcraft-cli run --template sample \
  --cmd 'select.text={"text":"Membership"}' --cmd format.bold --save out.docx
wordcraft-cli run --script job.json                 # the same from a file: commands, then save to docx and pdf
```

`convert --strict` (только вывод `.pdf` или `.png`) и `render --strict` (PNG одной страницы) отказываются от молча неполного вывода: они завершаются с кодом 3
и ничего не пишут, если вывод нарисовал бы знак, которого нет ни в одном шрифте (пустой квадрат), или пропустил бы
рисунок. Коды выхода: 0 (записано), 1 (нечитаемый ввод, ошибка использования или `--strict` с другим
типом вывода, проверка до чтения ввода) и 3 (отказ в строгом режиме). При коде 3 в stderr есть одна
строка `wordcraft-cli: strict: …` на каждый вид, затем одна строка JSON:

```sh
wordcraft-cli convert in.docx out.pdf --strict
# wordcraft-cli: strict: 1 character cannot be drawn: U+2D30 (×3)
# wordcraft-cli: strict: 1 picture(s) left out: word/media/image2.bin (header2.xml): unsupported format
# {"schema":1,"strict":"failed","missing_glyphs":[{"cp":"U+2D30","count":3}],"missing_pictures":[{"part":"word/media/image2.bin","source_part":"word/header2.xml","reason":"unsupported_format"}],"truncated":false,"total_missing_glyphs":1,"total_missing_pictures":1,"glyphs_truncated":false,"pictures_truncated":false}
```

Строка JSON (схема 1, также то, что возвращает `file.strictReport`) содержит `schema`, `strict`
(`"passed"` или `"failed"`), `missing_glyphs` (записи `{"cp", "count"}`, по кодовой точке),
`missing_pictures` (записи `{"part", "source_part", "reason"}`: часть или цель рисунка, часть
истории, в которой он лежит, например `word/header2.xml`, и код причины; `source_part` также бывает
`background` (рисунок страницы), `body`, `header`, `footer`, `footnote`, `endnote`, `comment` или
`text box`, когда имя части неизвестно (документ, открытый не из DOCX), либо путь фрагмента вроде
`word/afchunk1.docx > word/header1.xml` для рисунка внутри встроенного фрагмента DOCX), `truncated`, два итога
`total_missing_glyphs` и `total_missing_pictures`, а также `glyphs_truncated` и
`pictures_truncated` для каждого списка. Коды причин: `missing_part`, `external_target`,
`link_only`, `undecodable` и `unsupported_format`; строки stderr называют их обычными словами. Когда список обрезан, строка stderr даёт итог
(`300 characters cannot be drawn (first 256 listed)`).
Каждый список обрывается отдельно на 256 записях; `truncated` истинно, если обрезан любой, а итоги
считают каждый найденный различимый знак и рисунок, включая те, что за пределом. Считаются только знаки, которые рисует вывод (не скрытый текст и не удалённый текст
без `--markup`), а знак, который рисует запасной шрифт, годится. Текст внутри рисунка WMF или EMF тоже считается, набирается шрифтом, который называет рисунок, без запасного пути. Знак из области частного использования
не проходит только если ни один установленный шрифт его не отображает. Результат зависит от шрифтов, установленных на узле
(см. #5624 про фиксированный набор шрифтов). Внешняя цель рисунка никогда не запрашивается: о ней сообщают, её не
загружают. Рисунки, отброшенные при открытии DOCX (отсутствующая часть, внешняя цель или рисунок `link only` без встроенной копии), сообщаются только для ввода DOCX. У них нет страницы, поэтому PNG любой страницы тоже отвергается при отсутствующем или внешнем рисунке где угодно в документе, включая неиспользуемые колонтитулы. `render --strict` проверяет только ту страницу, которую
пишет (`--page`; `--scale` не важен), при отказе ничего не печатает в stdout и сообщает
так же. Движок принимает `strict: true` в `file.save`, `file.saveAs`, `file.exportPdf` и
`file.exportPng`, а `file.strictReport {markup?, page?}` возвращает отчёт без записи.

Веб: `cd apps/wordcraft-web && trunk serve`, затем откройте <http://127.0.0.1:8771/?sample>.

<a id="for-agents-cli-and-mcp"></a>
## Для агентов: CLI и MCP

WordCraft задуман так, чтобы им управляли люди *и* ИИ-агенты.

```sh
claude mcp add wordcraft -- wordcraft-cli mcp                  # headless documents
# confine the agent to folders: wordcraft-cli mcp --automation-read-root DIR --automation-write-root DIR
wordcraft --control 7981 &                                     # or drive the running app…
claude mcp add wordcraft-app -- wordcraft-cli mcp --connect 127.0.0.1:7981
```

Инструменты включают `list_commands`, `execute`, `batch`, `type_text`, `select_text`, `inspect_document`,
`render_page`, `save_document` и, при запущенной программе, `screenshot`, `click` и `key`. Агенты
могут проверять свою работу через `inspect_document` без снимков экрана. См. [docs/mcp.md](docs/mcp.md)
и [протокол управления](docs/control-protocol.md). Макросы записывают любую последовательность команд и
воспроизводят её (`tools.recordMacro`, `tools.macros`).

<a id="logs"></a>
## Журнал

Настольная программа пишет записи журнала в стандартный поток ошибок и в `logs/wordcraft.log` рядом со своими
настройками: в Linux `$XDG_CONFIG_HOME/wordcraft/logs/` (по умолчанию `~/.config/wordcraft/logs/`),
в macOS `~/Library/Application Support/WordCraft/logs/`, в Windows `%APPDATA%\WordCraft\logs\`.
Запуск из меню рабочего стола или Dock не даёт терминала, поэтому к сообщению об ошибке прикладывайте этот файл:
нечитаемые части .docx, рисунки или шрифты, которые выгрузка PDF была вынуждена пропустить, и паники, от которых
оправился охранник команд, попадают туда. Каждый запуск переносит предыдущий журнал в `wordcraft.1.log`
(а тот — в `wordcraft.2.log`), так что журнал аварийного запуска переживает следующий старт; файл
перестаёт расти на 16 MiB. `--version` файл не пишет, а запуски с `WORDCRAFT_NO_PREFS` (тестовые запуски
агентов) пишут только в стандартный поток ошибок. Текст документа никогда не журналируется; сообщение паники опускает
текст, который цитирует.

По умолчанию собственные крейты WordCraft пишут на уровне `info`, всё остальное — `warn`. `RUST_LOG` подменяет
это директивами в стиле env_logger, например `RUST_LOG=debug`,
`RUST_LOG=warn,wordcraft_docx=trace` или `RUST_LOG=info,wgpu_core=warn`; директива, оканчивающаяся на `*`,
покрывает все цели, которые с неё начинаются (`wordcraft*=debug`). Журнал —
`apps/wordcraft/src/logging.rs`.

<a id="architecture"></a>
## Архитектура

| Слой | Крейт | Назначение |
|---|---|---|
| L0 | `wordcraft-geom` | единицы и измерения |
| L1 | `wordcraft-doc`, `wordcraft-fonts`, `wordcraft-proof` ([`craft-proof`](https://github.com/storytold/craft-libs/tree/main/crates/proof) из craft-libs) | модель документа и правка; шрифты и формирование; орфография, грамматика, переносы (данные: `language-data/` в craft-i18n, `CRAFT_I18N_DIR`) |
| L2 | `wordcraft-layout`, `wordcraft-docx`, `wordcraft-formats` | разрыв строк, разбиение на страницы, таблицы, примечания, проверка попаданий; OOXML; ODT/RTF/HTML/Markdown/TXT |
| L3 | `wordcraft-render`, `wordcraft-pdf` | растеризатор (vello_cpu); PDF ([craft-pdf](docs/shared-pdf.md), Krilla) |
| L4 | `wordcraft-engine` | сеанс, отмена, 422 команды, каталог возможностей документа |
| L5 | `wordcraft-mcp` | сервер MCP |
| L6 | `wordcraft-ui-egui` | оболочка текстового процессора (сменная) |
| apps | `wordcraft`, `wordcraft-cli`, `wordcraft-web` | настольная программа, командная строка, браузер |

`cargo xtask ci` запускает форматирование, clippy, около 800 тестов, проверку указания ресурсов, проверку
слоёв и сборку wasm. Инструкции для участников и агентов: [AGENTS.md](AGENTS.md).

<a id="roadmap"></a>
## План

WordCraft находится в **альфе**. Сегодня у него есть команды для 97 % возможностей ленты и меню в каталоге возможностей
([`docs/parity-checklist.md`](docs/parity-checklist.md)); считая
глубину, верность файлов, устойчивость и прочее, мы оцениваем его примерно на 60 % готовым к настоящей работе,
примерно на 55 % — к типичной еженедельной работе профессионала и примерно на 63 % — к повседневным основам. Для беты
нужны испытания на настоящих файлах .docx, сохранение диаграмм и SmartArt при круговом обходе,
большая верность разбиения на страницы, проход по устойчивости и нативная печать. Подробности и оценки:
[ROADMAP.md](ROADMAP.md) и [где мы ещё не дотягиваем](docs/gaps.md).

<a id="downloads"></a>
## Загрузки

**Скачайте WordCraft** с GitHub: в [последнем выпуске](https://github.com/storytold/wordcraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/wordcraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `wordcraft-<ver>-windows-x64.msi` | `wordcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `wordcraft-<ver>-windows-arm64.msi` | `wordcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `wordcraft-<ver>-windows-x86.msi` | `wordcraft-<ver>-windows-x86-portable.zip` |

Установщик — один пакет с двумя областями действия. По умолчанию он ставит только для вашей учётной записи,
в `%LOCALAPPDATA%\Programs\ArtCraft\WordCraft`, и права администратора не нужны; выбор
«Все на этом компьютере» на первой странице ставит в `C:\Program Files\ArtCraft\WordCraft` (`Program Files (x86)` для 32-разрядной сборки)
и запрашивает администратора. Ставьте только одну копию: копия для другой области действия отклоняется, поэтому
сначала удалите программу, чтобы сменить, для кого установлен WordCraft. Установщики и исполняемые файлы подписаны.

**Если программа не открывается в Windows:** настольная программа по умолчанию инициализирует только DirectX 12.
Если позволить wgpu ещё и создать экземпляр OpenGL, некоторые графические драйверы (например,
`atio6axx.dll` AMD) могут аварийно завершиться до появления окна, и программа мелькнёт в «Диспетчере задач» и выйдет.
`WGPU_BACKEND` подменяет значение по умолчанию для диагностики (например `dx12` или `vulkan`). В
PowerShell, из папки с исполняемым файлом:

```powershell
$env:WGPU_BACKEND = "vulkan"
& .\wordcraft.exe
Remove-Item Env:WGPU_BACKEND                     # restore the default for later launches
```

Явная подмена `gl` может вернуть сбой драйвера на затронутых системах. Значения подсистемы по умолчанию для macOS, Linux
и веба не менялись.

**32-разрядная** сборка использует OpenGL, даже когда есть видеокарта DirectX 12.
В 32-разрядной Windows создание конвейера DirectX 12 сразу завершается ошибкой, и программа выходит до
появления окна. `WGPU_BACKEND=vulkan` (или `dx12`) по-прежнему это подменяет.

**Если программа выходит сразу после появления окна, а в журнале «Parent device is lost»:**
WordCraft компилирует шейдеры DirectX 12 с FXC, компилятором, встроенным в Windows, поэтому ему не нужны
`dxcompiler.dll`/`dxil.dll`, и он игнорирует любую копию, которую другая программа положила в `PATH` (#603).
`WGPU_DX12_COMPILER` (`fxc`, `dxc`, `auto`) это подменяет; с `dxc` рядом с исполняемым файлом должны лежать
подходящие `dxcompiler.dll` *и* `dxil.dll` — рядом с `wordcraft.exe`. `WGPU_BACKEND = "vulkan"`
также полностью обходит DirectX 12.

**Если программа медленная на старом ПК с Windows:** когда DirectX 12 не находит видеокарту с
драйвером для него (например графика Intel 4-го поколения в Windows 11), он предлагает только встроенный
программный визуализатор, который рисует каждый кадр на процессоре. WordCraft обычно вместо этого использует OpenGL,
ничего не задавая. Если у OpenGL нет пригодного адаптера, можно взять программный адаптер WARP DirectX 12.
Файл журнала записывает выбор (строки, начинающиеся с
`graphics:`). `WGPU_BACKEND` по-прежнему это подменяет, например `$env:WGPU_BACKEND = "gl"` или `"dx12"`.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `wordcraft-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `wordcraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `wordcraft-<ver>-linux-x86_64.AppImage` | `wordcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `wordcraft-<ver>-linux-x86_64.flatpak` | `wordcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `wordcraft-<ver>-linux-x86_64.deb` | `wordcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `wordcraft-<ver>-linux-x86_64.rpm` | `wordcraft-<ver>-linux-aarch64.rpm` | |
| Архив | `wordcraft-<ver>-linux-x86_64.tar.gz` | `wordcraft-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

RISC-V (riscv64): `wordcraft-<ver>-linux-riscv64.tar.gz`, архив, кросс-компиляция для glibc 2.39+
(Ubuntu 24.04, Debian 13 и новее).

**Чтение вслух** (Рецензирование › Читать вслух) говорит через речевую программу, установленную в системе: сначала
пробует `espeak-ng`, затем `espeak`, а если ни одна не установлена, обращается к Speech Dispatcher.
Пакет `.rpm` рекомендует `espeak-ng`; пакет `.deb` рекомендует `espeak-ng` или
`speech-dispatcher`, поэтому менеджер пакетов по умолчанию ставит один из двух. С
AppImage или архивом установите один сами, если нет ни одного (`sudo apt install espeak-ng`,
`sudo dnf install espeak-ng`, `sudo pacman -S espeak-ng`). Flatpak пока не говорит: у него нет
доступа к звуку и в него не входят `espeak-ng`, `espeak` или Speech Dispatcher.

**Wayland:** на рабочем столе Wayland программа идёт через XWayland, когда он доступен, потому что
winit (библиотека окон) поддерживает перетаскивание файлов в окно только в X11. Чтобы использовать
нативную подсистему Wayland (например для более чёткого текста с дробным масштабом, ценой
перетаскивания файлов), выберите **Файл › Параметры › Дополнительно › Сервер отображения Linux › Wayland**; это
применяется при следующем запуске WordCraft, а **X11 (XWayland)** или **Автоматически** возвращает обратно.
Переменная окружения `WORDCRAFT_WAYLAND` подменяет настройку: `1` для нативного Wayland, `0` для
XWayland:

```sh
WORDCRAFT_WAYLAND=1 wordcraft
```

XWayland нужны библиотеки X11, которые пакеты только рекомендуют, а архив не
ставит: libX11, libX11-xcb, libXcursor, libXi и libxkbcommon-x11 (в Debian и Ubuntu
`libx11-6`, `libx11-xcb1`, `libxcursor1`, `libxi6` и `libxkbcommon-x11-0`). Без них программа
открывается в нативном Wayland, что бы ни говорила настройка, и записывает в журнал, каких не хватает.

**Arch Linux (AUR).** Участники сообщества сопровождают три пакета AUR; сам проект в AUR
не публикует. Установите один из них:
| Пакет | Что ставит | Когда выбирать |
|---|---|---|
| [`wordcraft-bin`](https://aur.archlinux.org/packages/wordcraft-bin) | Архив выпуска выше, готовая сборка (x86_64, aarch64) | Нужен последний выпуск без компиляции (быстрее всего) |
| [`wordcraft`](https://aur.archlinux.org/packages/wordcraft) | Последний выпуск, сборка из исходников с `cargo` | Предпочитаете собирать выпуски сами |
| [`wordcraft-git`](https://aur.archlinux.org/packages/wordcraft-git) | Текущая ветка `main`, сборка из исходников | Нужны ещё не выпущенные изменения, и допустима изредка сломанная сборка |
Например `yay -S wordcraft-bin` или `paru -S wordcraft-bin`.

<a id="community-packages"></a>
#### Пакеты сообщества

Эти пакеты сопровождают участники сообщества, а не команда WordCraft.

В Gentoo оверлей [::snakebyte overlay](https://github.com/switch87/snakebyte-overlay) упаковывает
выпуск для Linux как `app-office/wordcraft-bin` (готовая сборка) и `app-office/wordcraft` (сборка из исходников):

```sh
eselect repository add snakebyte git https://github.com/switch87/snakebyte-overlay.git
emaint sync -r snakebyte
echo 'app-office/wordcraft-bin ~amd64' >> /etc/portage/package.accept_keywords/wordcraft
emerge --ask app-office/wordcraft-bin
```

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `wordcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `wordcraft-web-<ver>.zip` | Работает в современном браузере; разместите на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

WordCraft — одно из приложений **Crafting Apps**: бесплатные творческие инструменты с открытым исходным кодом от команды
[ArtCraft](https://getartcraft.com/), каждый написан с нуля на Rust и каждый может
работать сам по себе.

| | Программа | Для чего | Код | Подробнее |
|:-:|---|---|---|---|
| <img src="https://raw.githubusercontent.com/storytold/photocraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.photocraft.png" alt="" width="32" height="32"> | **PhotoCraft** | Редактирование изображений: слои, маски, текст и настоящие файлы PSD| [GitHub](https://github.com/storytold/photocraft) | [Сайт](https://getartcraft.com/apps/photocraft) |
| <img src="https://raw.githubusercontent.com/storytold/vectorcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.vectorcraft.png" alt="" width="32" height="32"> | **VectorCraft** | Векторная иллюстрация| [GitHub](https://github.com/storytold/vectorcraft) | [Сайт](https://getartcraft.com/apps/vectorcraft) |
| <img src="https://raw.githubusercontent.com/storytold/filmcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.filmcraft.png" alt="" width="32" height="32"> | **FilmCraft** | Монтаж видео, цвет и звук      | [GitHub](https://github.com/storytold/filmcraft) | [Сайт](https://getartcraft.com/apps/filmcraft) |
| <img src="https://raw.githubusercontent.com/storytold/lightcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.lightcraft.png" alt="" width="32" height="32"> | **LightCraft** | Библиотека фотографий и проявление raw| [GitHub](https://github.com/storytold/lightcraft) | [Сайт](https://getartcraft.com/apps/lightcraft) |
| <img src="https://raw.githubusercontent.com/storytold/pdfcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.pdfcraft.png" alt="" width="32" height="32"> | **PdfCraft** | Чтение, организация и защита PDF        | [GitHub](https://github.com/storytold/pdfcraft) | [Сайт](https://getartcraft.com/apps/pdfcraft) |
| <img src="https://raw.githubusercontent.com/storytold/effectcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.effectcraft.png" alt="" width="32" height="32"> | **EffectCraft** | Моушн-графика и визуальные эффекты | [GitHub](https://github.com/storytold/effectcraft) | [Сайт](https://getartcraft.com/apps/effectcraft) |
| <img src="https://raw.githubusercontent.com/storytold/designcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.designcraft.png" alt="" width="32" height="32"> | **DesignCraft** | Вёрстка и публикация       | [GitHub](https://github.com/storytold/designcraft) | [Сайт](https://getartcraft.com/apps/designcraft) |
| <img src="https://raw.githubusercontent.com/storytold/figcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.figcraft.png" alt="" width="32" height="32"> | **FigCraft** | Дизайн интерфейсов и прототипирование| [GitHub](https://github.com/storytold/figcraft) | [Сайт](https://getartcraft.com/apps/figcraft) |
| <img src="https://raw.githubusercontent.com/storytold/wordcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.wordcraft.png" alt="" width="32" height="32"> | **WordCraft** | Текстовый процессор и документы| [GitHub](https://github.com/storytold/wordcraft) | [Сайт](https://getartcraft.com/apps/wordcraft) |
| <img src="https://raw.githubusercontent.com/storytold/soundcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.soundcraft.png" alt="" width="32" height="32"> | **SoundCraft** | Запись и редактирование звука| [GitHub](https://github.com/storytold/soundcraft) | [Сайт](https://getartcraft.com/apps/soundcraft) |
| <img src="https://raw.githubusercontent.com/storytold/deckcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.deckcraft.png" alt="" width="32" height="32"> | **DeckCraft** | Презентации и слайд-колоды    | [GitHub](https://github.com/storytold/deckcraft) | [Сайт](https://getartcraft.com/apps/deckcraft) |
| <img src="https://raw.githubusercontent.com/storytold/cadcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.cadcraft.png" alt="" width="32" height="32"> | **CADCraft** | Автоматизированное проектирование| [GitHub](https://github.com/storytold/cadcraft) | [Сайт](https://getartcraft.com/apps/cadcraft) |
| <img src="https://raw.githubusercontent.com/storytold/gridcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.gridcraft.png" alt="" width="32" height="32"> | **GridCraft** | Электронные таблицы и данные| [GitHub](https://github.com/storytold/gridcraft) | [Сайт](https://getartcraft.com/apps/gridcraft) |
| <img src="https://raw.githubusercontent.com/storytold/texturecraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.texturecraft.png" alt="" width="32" height="32"> | **TextureCraft** | Рисование 3D-текстур| [GitHub](https://github.com/storytold/texturecraft) | [Сайт](https://getartcraft.com/apps/texturecraft) |
| <img src="https://raw.githubusercontent.com/storytold/craft-anything/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.craft-anything.png" alt="" width="32" height="32"> | **Craft Anything** | Смотрите, как устроена любая программа, и собирайте свою| [GitHub](https://github.com/storytold/craft-anything) | [Сайт](https://getartcraft.com/apps/craft-anything) |
| <img src="https://raw.githubusercontent.com/tangency-labs/solidcraft/main/assets/icons/app/linux/exports/hicolor/64x64/apps/io.tangencylabs.solidcraft.png" alt="" width="32" height="32"> | **SolidCraft** | Параметрический 3D CAD от Tangency Labs (приложение сообщества)| [GitHub](https://github.com/tangency-labs/solidcraft) | |


И сама [**ArtCraft**](https://getartcraft.com/) — наша студия изображений и видео на основе ИИ для художников, которым нужен настоящий контроль.

<br>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<h3 align="center">Приходите творить с нами</h3>

<p align="center">
  Наш Discord — место, где собираются художники любого рода: те, кто пишет, снимает, рисует, монтирует фильм,
  набирает текст, и те, кто ещё выясняет, что им нравится создавать. Покажите, над чем работаете,
  попросите помощи, расскажите, что сломано, или расскажите, что вы хотите, чтобы эти инструменты умели.
  Каким бы ни был ваш материал и как давно вы этим занимаетесь, вам здесь рады.
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><b>discord.gg/artcraft</b></a> ·
  <a href="https://getartcraft.com/">getartcraft.com</a> ·
  <a href="https://getartcraft.com/apps">The Crafting Apps</a> ·
  <a href="https://getartcraft.com/apps/wordcraft">WordCraft</a>
</p>

<a id="license-and-credits"></a>
## Лицензия и благодарности

WordCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the WordCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Английская орфография сначала пробует подходящий словарь Hunspell из папки Dictionaries.
Иначе она использует словари SCOWL 2026 для конкретных диалектов, когда собрана с языковыми данными;
без них орфография отступает к системным словарям Hunspell или к списку слов Moby Hyphenator II Грейди Уорда, находящемуся в общественном достоянии. Английские переносы используют список Moby и шаблоны, обученные на нём. Польская орфография читает словарь Hunspell `pl_PL`, установленный в системе (не встроенный), как
и орфография русского, португальского, чешского, итальянского, хорватского и турецкого (как их установить:
[docs/spelling-dictionaries.md](docs/spelling-dictionaries.md)), а
польские переносы — шаблоны TeX Ханны Колодзейской, Богуслава Яцковского и Марека Рыцько (вариант
MIT). Образцовые документы и шаблоны — оригинальный текст, написанный для WordCraft.

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и WordCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
