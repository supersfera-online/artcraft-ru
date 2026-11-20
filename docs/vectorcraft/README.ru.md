# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/vectorcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/vectorcraft
Коммит исходника (последний, в котором менялся README.md): f363f0a3e0de2e5adc7105d664c7c10746057bfe
Дата коммита: 20 ноября 2026, 06:30 (America/Los_Angeles, PT); в исходнике 2026-11-20T14:30:25Z
SHA256 исходника: 346b6d34bb0dea534a62197616d8a7b036034bddaea8d4160864633ca56f85ca
Git blob SHA: 158a4ca2c8dda65b534311ac393e1740e435c5ea
Размер исходника: 28542 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/vectorcraft/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.vectorcraft.png" width="128" height="128" alt="Значок VectorCraft: гравированный дракон на красной плитке">
</p>

<h1 align="center">VectorCraft</h1>

<p align="center">
  <b>Векторная иллюстрация: современная программа векторного рисунка с открытым исходным кодом, написанная на чистом Rust.</b>
</p>

<p align="center">
  Быстрый рабочий процесс векторной иллюстрации с открытым исходным кодом. Работает нативно в
  macOS, Windows, Linux и FreeBSD и в браузере через WebAssembly. Сделано командой ArtCraft.
</p>

<p align="center">
  <img alt="Status: in active development" src="https://img.shields.io/badge/status-in%20active%20development-e8573f?style=flat-square">
  <img alt="Written in pure Rust" src="https://img.shields.io/badge/pure-Rust-b83a24?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows, Linux, FreeBSD and the web" src="https://img.shields.io/badge/runs%20on-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-555555?style=flat-square">
  <img alt="MCP server for agents" src="https://img.shields.io/badge/agents-MCP%20server-555555?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-555555?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_vectorcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/vectorcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/vectorcraft"><b>VectorCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/shot-1-neon.png" alt="VectorCraft правит плакат Neon Drive: заголовок выделен, панель «Внешний вид» показывает параметры его живого внешнего свечения, панель «Свойства» — параметры символов" width="100%">
  <br><sub><b>Neon Drive</b>: солнце, вырезанное обработкой контуров, живое внешнее свечение на тексте и сетке, обтравочные маски · <code>examples/neon-drive.vectorcraft</code></sub>
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Цифра, генеративное искусство, музыка,
> игры &mdash; если вы что-то создаёте, вы один из нас. **[Загляните в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#a-look-around">Взгляд вокруг</a> ·
  <a href="#made-in-vectorcraft">Сделано в VectorCraft</a> ·
  <a href="#why-vectorcraft">Почему VectorCraft</a> ·
  <a href="#quick-start">Быстрый старт</a> ·
  <a href="#status">Состояние</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">Лицензия</a>
</p>

<a id="a-look-around"></a>
## Взгляд вокруг

<table>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/shot-2-ribbons.png" alt="Три живых перехода-ленты, обрезанные по монтажной области; одна выделена, видны её опорные контуры; панель «Слои» перечисляет группу обрезки, переходы и два опорных контура выделенного перехода" width="100%">
  <p align="center"><sub><b>Живые переходы и слои</b>: редактируемые опорные контуры, плавный цвет, каждый объект — строка</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-4-bezier.png" alt="Инструмент «Прямое выделение» показывает опорные точки и манипуляторы Безье на полумесяце, построенном обработкой контуров, под ним контекстная панель задач" width="100%">
  <p align="center"><sub><b>Перо и прямое выделение</b>: настоящие опорные точки и манипуляторы Безье и контекстная панель задач</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/shot-6-revolve.png" alt="Натюрморт: ваза, чаша, шар и бутылка, сделанные инструментом «3D-вращение»; ваза выделена, в диалоге вращения — поворот, крышка и вид рядом с манипулятором вращения" width="100%">
  <p align="center"><sub><b>3D-вращение</b>: плавная векторная светотень, крышки и манипулятор вращения · <code>examples/still-life.vectorcraft</code></sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-7-dimensions.png" alt="Чертёж кронштейна в светлой теме с линейными, угловыми, диаметральными и радиусными размерами; активен инструмент размеров, в панели «Свойства» — единицы, точность и стиль выбранного размера" width="100%">
  <p align="center"><sub><b>Инструмент размеров</b>: длины, углы и радиусы, которые следуют за измеряемым рисунком · <code>examples/bracket-drawing.vectorcraft</code></sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/shot-5-perspective.png" alt="Два освещённых фасада зданий на левой и правой плоскостях двухточечной сетки перспективы на закате, инструмент «Выделение в перспективе» и виджет переключения плоскостей" width="100%">
  <p align="center"><sub><b>Сетка перспективы</b>: рисунок, привязанный к плоскостям, остаётся редактируемым в перспективе · <code>examples/perspective-city.vectorcraft</code></sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-3-sheet.png" alt="Четыре монтажные области в светлой теме интерфейса: обработка контуров, сетчатый градиент, радиальное повторение и искажение оболочки" width="100%">
  <p align="center"><sub><b>Несколько монтажных областей, светлая тема</b>: обработка контуров · сетчатый градиент · живое радиальное повторение · искажение оболочки · <code>examples/feature-sheet.vectorcraft</code></sub></p>
</td>
</tr>
</table>

<a id="made-in-vectorcraft"></a>
## Сделано в VectorCraft

Каждая работа ниже собрана целиком через командный API VectorCraft — тот же, который MCP-сервер
отдаёт агентам, — и выведена собственным визуализатором VectorCraft. Исходные файлы — в
[`examples/`](examples).

<table>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/art-neon-drive.png" alt="Синтвейв-плакат Neon Drive: полосатое оранжевое солнце садится между фиолетовыми горами над светящейся розовой сеткой" width="100%">
  <p align="center"><sub><b>Neon Drive</b>: синтвейв-плакат со светящимся текстом и сеткой</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/dusk-poster.png" alt="Плакат Dusk: градиентное небо со звёздами и птицами, светящееся солнце за слоистыми фиолетовыми горами и соснами" width="100%">
  <p align="center"><sub><b>Dusk</b>: градиентное небо, светящееся солнце, слоистые горы</sub></p>
</td>
</tr>
<tr>
<td colspan="2" valign="top">
  <img src="docs/images/art-ribbons.png" alt="Живые переходы: три широкие ленты, переходящие от жёлтого к розовому и от бирюзового к фиолетовому, пересекаются на тёмном фоне" width="100%">
  <p align="center"><sub><b>Живые переходы</b>: 70 шагов, плавный цвет, редактируемые хребты</sub></p>
</td>
</tr>
<tr>
<td colspan="2" valign="top">
  <img src="docs/images/art-still-life.png" alt="Натюрморт: бирюзовая ваза, коралловая чаша, белый шар и горчичная бутылка на тёплом столе, всё сделано 3D-вращением" width="100%">
  <p align="center"><sub><b>Натюрморт</b>: четыре профиля вращения с плавной векторной светотенью</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/art-repeat.png" alt="Мандала радиального повторения: бирюзовые лепестки вокруг кораллового центра, кольцо жёлтых точек" width="100%">
  <p align="center"><sub><b>Радиальное повторение</b>: живая мандала</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/art-envelope.png" alt="Искажение оболочки: радужные полосы и слово WARP изогнуты в развевающийся флаг" width="100%">
  <p align="center"><sub><b>Искажение оболочки</b>: полосатый текст, изогнутый в флаг</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/art-mesh.png" alt="Сетчатый градиент: три мягко затенённых фиолетовых, розовых и голубых шара на тёмном фоне" width="100%">
  <p align="center"><sub><b>Сетчатый градиент</b>: затенённые шары</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/art-pathfinder.png" alt="Обработка контуров: фиолетовый градиентный полумесяц и три оранжевые звезды на персиковом фоне" width="100%">
  <p align="center"><sub><b>Обработка контуров</b>: полумесяц и звёзды из точных булевых операций</sub></p>
</td>
</tr>
</table>

<a id="why-vectorcraft"></a>
## Почему VectorCraft

- **Привычно.** Привычные раскладка, инструменты, меню, панели и сочетания клавиш: Перо, прямое выделение,
  обработка контуров, умные направляющие, «Внешний вид», «Образцы», «Слои» и другое. Вы уже умеете этим пользоваться.
- **Быстро.** Многопоточный SIMD-рендеринг вне потока интерфейса. 20 000 фигур рисуются примерно за 27 мс в
  полном разрешении Retina, а интерфейс держит 120 кадров в секунду.
- **Надёжно.** Точные булевы операции по кривым (никакого «невозможно выполнить операцию»), неограниченная отмена через структурное
  разделение и проверённые на свойствах круговые поездки файлов.
- **Открыто.** Документированный собственный формат (`.vectorcraft`, JSON), полноценные импорт и экспорт SVG, PDF (и
  совместимого с PDF `.ai`), экспорт PNG/JPEG/WebP, «Экспорт для экранов», а также SVGZ,
  шаблоны, GIF, TIFF и BMP при открытии.
- **Для агентов.** Каждым пунктом меню, жестом инструмента, панелью и диалогом можно управлять по JSON-каналу
  управления и через **MCP-сервер**, так что Claude и другие агенты могут рисовать, править и экспортировать так же,
  как человек.
- **Везде.** Одна кодовая база для настольных программ и тот же интерфейс в браузере.

<a id="quick-start"></a>
## Быстрый старт

Про плакаты и выкройки см. [Печать большого плаката на нескольких страницах](docs/print-tiling.md).

```sh
git clone https://github.com/storytold/vectorcraft
cd vectorcraft

cargo run --release -p vectorcraft                          # desktop app
cargo run --release -p vectorcraft -- examples/dusk-poster.vectorcraft
cargo run --release -p vectorcraft -- --control 7979        # + JSON control channel
cargo run --release -p vectorcraft-cli -- mcp               # MCP server (stdio)
cargo run --release -p vectorcraft-cli -- run --in examples/ribbons.vectorcraft --export out.pdf   # headless batch
cargo run --release -p vectorcraft-cli -- bench examples/neon-drive.vectorcraft                   # render timing
cargo xtask bundle                                        # dist/VectorCraft.app (macOS)
cd apps/vectorcraft-web && trunk build --release            # web build → dist/web
cargo xtask ci                                            # fmt, clippy, tests, layering, wasm, vendor names
```

Про текст и собственные буквенные формы см. [Типографика и наборный рисунок букв](docs/typography-lettering.md).

Японские шрифты берутся из [storytold/craft-fonts](https://github.com/storytold/craft-fonts), необязательный
вход сборки (в выпусках он всегда используется): `CRAFT_FONTS_DIR="$PWD/../craft-fonts" cargo run --release -p vectorcraft` (абсолютный путь).
Без него японский текст идёт установленными системными шрифтами. См. [`docs/development.md`](docs/development.md#fonts-craft-fonts-optional-build-input).

На машинах с двумя графическими процессорами VectorCraft по умолчанию рисует на энергосберегающем (встроенном) в
Windows и macOS и на том, на котором работает рабочий стол, в Linux. Чтобы выбрать, откройте **Настройки › Производительность ›
Графический процессор** и перезапустите. Если графический процессор не может показать окно, VectorCraft стартует снова на
следующем. Чтобы выбрать адаптер при запуске, задайте `WGPU_POWER_PREF=high` (или `low`) или `WGPU_ADAPTER_NAME` как часть
его имени, например `WGPU_ADAPTER_NAME=nvidia` (см. [`docs/development.md`](docs/development.md#desktop-graphics-processor)).

В нативном Wayland winit 0.30 не доставляет брошенные файлы. Чтобы открыть SVG, используйте Файл › Открыть;
чтобы поместить рисунок в текущий документ, скопируйте и вставьте файл в файловом менеджере. Для перетаскивания
файлов задайте **Настройки › Производительность › Сервер отображения Linux** значение **X11 (XWayland)** и перезапустите или запустите
программу как `WAYLAND_DISPLAY= vectorcraft`: окно тогда открывается через XWayland, где бросание работает
(см. [`docs/development.md`](docs/development.md#linux-wayland-and-x11)).

В Linux с Wayland под KDE Plasma 6.3 или новее и под GNOME VectorCraft пока не может получить ввод пера графического планшета
в нативном Wayland (#491, #2028). Если перо подключено к моменту запуска VectorCraft, окно открывается через
XWayland, где перо работает как мышь, а программа читает его нажим (#4967; `VECTORCRAFT_NATIVE_WAYLAND=1` оставляет
Wayland). Для пера, подключённого позже, задайте ту же настройку **X11 (XWayland)** и перезапустите или запустите программу как
`WAYLAND_DISPLAY= vectorcraft` (см. [`docs/development.md`](docs/development.md#linux-wayland-and-x11)).

<a id="use-it-from-claude-code-and-other-agents"></a>
### Использовать из Claude Code и других агентов

Зарегистрируйте MCP-сервер в Claude Code:

```sh
claude mcp add vectorcraft -- /path/to/vectorcraft-cli mcp
```

Чтобы ограничить агента файлами одного проекта, дайте ему папки для чтения и записи (те же флаги, что у PhotoCraft):

```sh
claude mcp add vectorcraft -- /path/to/vectorcraft-cli mcp --automation-read-root /work/project --automation-write-root /work/project
```

Подробности — в [`docs/mcp.md`](docs/mcp.md) и [`docs/control-protocol.md`](docs/control-protocol.md).

<a id="status"></a>
## Состояние

VectorCraft активно развивается. В [**ROADMAP.md**](ROADMAP.md) — этап, цифры по измерениям
и ближайшие шаги; в [`docs/target-app-parity.md`](docs/target-app-parity.md) — полная оценка паритета, а в
[`docs/gaps.md`](docs/gaps.md) — упорядоченный список того, чего ещё нет.

**Где мы сейчас (2026-10-10): альфа.** Около 88% основных пунктов меню, инструментов, эффектов и форматов уже есть
(92,5% пунктов меню что-то делают), глубина возможностей ~75%, и мы оцениваем готовность к настоящей работе обычного иллюстратора примерно в ~65% (~62% по всем учитываемым возможностям): повседневная
векторная иллюстрация близка к пригодной: инструменты рисования и контуров,
обработка контуров и конструктор форм, краска, градиенты, внешний вид и прозрачность, текст со стилями, связанные текстовые рамки и двунаправленная вёрстка иврита и арабского, и
файлы (SVG, PDF и совместимый с PDF `.ai` с PDF/X, устаревший `.ai` версии 7 с сохранением слоёв, групп и текста, EPS, DXF, EMF/WMF, растровые форматы, PSD на выход, PSD/PSB открываются со своими слоями и помещаются как сведённое изображение, JPEG XL на вход, «Печать», «Упаковать»).
Документы Affinity (`.af` из Affinity 3, `.afdesign`, `.afpub` и, по содержимому, `.afphoto` из Affinity 1 и 2) открываются
и помещаются нативно: слои, группы, монтажные области и страницы, кривые и фигуры, заливки, градиенты и обводки, обтравка
и маски, текст с отступами, интервалами и интерлиньяжем каждого абзаца, таблицы (как текстовые рамки и линии), шаблонные
страницы, тени, свечения, контуры и наложения, встроенные документы Affinity и изображения; то, что не вошло
(корректировки, размытия, скосы, кисти…), перечисляется в предупреждении импорта; файл, чьи собственные данные прочитать нельзя, открывается как встроенный просмотр с объяснением, почему. VectorCraft
не записывает файлы Affinity. Текущая проверка `.af` включает 33 закреплённых файла, нативное сохранение и повторное открытие
и экспорт каждой монтажной области в SVG/PDF/PSD, с правками для монтажных областей Affinity 3, JPEG с исходником и текстовых прогонов.
[Объём и ограничения](crates/affinity/README.md); [разбор источников и оставшиеся пробелы](docs/affinity-validation.md).
Интерфейс
говорит по-английски, по-немецки, по-японски, по-корейски, по-вьетнамски, на традиционном и упрощённом китайском, по-испански, по-французски, по-венгерски, по-итальянски, по-польски, на бразильском португальском, по-русски, по-шведски, по-украински, по-фински, по-болгарски, по-гречески, по-чешски, по-грузински и по-каталански;
подробности — в [localization-parity.md](docs/localization-parity.md).
Оценки мы выставили сами по коду, сверяясь с открытой документацией;
[target-app-parity.md](docs/target-app-parity.md#how-this-was-measured-2026-10-10) объясняет, насколько им можно доверять.

Все 57 приближённых растровых фильтров в стиле Photoshop доступны. В галерее эффектов есть миниатюры фильтров и просмотр внутри диалога.

**Чего ещё нет:**
- надёжного обмена файлами .ai (структура слоёв в настоящих файлах; редакторская копия, которую пишет сохранение, держит живые эффекты только на контурах, составных контурах и группах, которые подходят (не больше одной заливки и одной обводки, ненулевое правило заливки, если есть заливка, без большого холста) и чьи внешний вид и эффекты умеет записывать писатель стилей рисунка (см. [docs/file-format-parity.md](docs/file-format-parity.md)), опускает эффекты других объектов, кроме геометрических, и записывает живые объекты как их рисунок);
- прохода по точности взаимодействия, покрывающего модификаторы и мелкое поведение каждого инструмента;
- 3D и материалов сверх начального живого вращения (выдавливание и скос, раздувание, поворот, материалы);
- CJK-вёрстки для вертикального текста (сам вертикальный текст уже имеет начальную поддержку, с японским интерфейсом);
- сценариев и остальной части переменных (виды изображений и графиков, импорт наборов данных);
- генеративных возможностей ИИ.

**Куда идём:** дальше — проход по точности взаимодействия, файлы `.ai` от настоящих пользователей и стабильность запуска,
параллельно с пакетом растровых эффектов; затем текст, недавние добавления и 3D. Упорядоченный список — в
[`docs/gaps.md`](docs/gaps.md).

**Состав репозитория:** `crates/{geom, color, doc, pathops, text, effects, three-d, trace, brush, render, svg, pdf, eps, cad, metafile, format, tools, engine, ui-egui, mcp, testkit}`
и `apps/{vectorcraft, vectorcraft-cli, vectorcraft-web}`. Оболочка на egui — отдельный крейт, поэтому
интерфейс можно заменить, не трогая движок.

Правила для агентов и участников — общие правила в
[`AGENTS.md`](AGENTS.md), там же перечислены проверки для изменённых вами крейтов; [`docs/development.md`](docs/development.md#robustness-vectorcraft-never-crashes)
объясняет, как VectorCraft избегает падений, а [`docs/releasing.md`](docs/releasing.md) — как собираются,
подписываются и публикуются выпуски. Каждый встроенный ресурс указан с лицензией в [`ASSETS.md`](ASSETS.md).

<a id="downloads"></a>
## Загрузки

**Впервые в VectorCraft?** Скачайте программу со [страницы VectorCraft на getartcraft.com](https://getartcraft.com/apps/vectorcraft). Так установить проще всего.

**Нужна конкретная сборка или формат?** На GitHub в [последнем выпуске](https://github.com/storytold/vectorcraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/vectorcraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `vectorcraft-<ver>-windows-x64.msi` | `vectorcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `vectorcraft-<ver>-windows-arm64.msi` | `vectorcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `vectorcraft-<ver>-windows-x86.msi` | `vectorcraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы подписаны.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `vectorcraft-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `vectorcraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `vectorcraft-<ver>-linux-x86_64.AppImage` | `vectorcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `vectorcraft-<ver>-linux-x86_64.flatpak` | `vectorcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `vectorcraft-<ver>-linux-x86_64.deb` | `vectorcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `vectorcraft-<ver>-linux-x86_64.rpm` | `vectorcraft-<ver>-linux-aarch64.rpm` | |
| Архив | `vectorcraft-<ver>-linux-x86_64.tar.gz` | `vectorcraft-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `vectorcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `vectorcraft-web-<ver>.zip` | Работает в браузере с WebAssembly SIMD (Chrome/Edge 91, Firefox 89, Safari 16.4 или новее), см. `packaging/web/README.md`; разместите на любом статическом сервере |
<a id="the-crafting-apps"></a>
## The Crafting Apps

VectorCraft — одно из приложений **Crafting Apps**: бесплатных творческих инструментов с открытым исходным кодом от команды
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
  <a href="https://getartcraft.com/apps/vectorcraft">VectorCraft</a>
</p>

<a id="star-history"></a>
## История звёзд

[![Star History Chart](https://api.star-history.com/svg?repos=storytold/vectorcraft&type=Date&legend=top-left)](https://www.star-history.com/?repos=storytold%2Fvectorcraft&type=date&legend=top-left)

<a id="license-and-credits"></a>
## Лицензия и благодарности

VectorCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the VectorCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ASSETS.md](ASSETS.md). Сборки выпуска также встраивают
шрифты [craft-fonts](https://github.com/storytold/craft-fonts/blob/main/ATTRIBUTION.md) (начертания для японского,
упрощённого китайского и арабского; SIL Open Font License 1.1).

Значок программы (гравированный дракон на красном VectorCraft, `#e8573f`) — оригинальная работа владельца; палитра и
файлы — в [`assets/app-icon/`](assets/app-icon/README.md).

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и VectorCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
