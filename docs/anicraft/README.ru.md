# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!--
Источник: https://github.com/storytold/anicraft/blob/main/README.md
Репозиторий: https://github.com/storytold/anicraft
Коммит исходника (последний, в котором менялся README.md): 12148ff77fb9d5c1f1ba41de4450b323873312ba
Дата коммита: 15 ноября 2026, 05:57 (America/Los_Angeles, PT); в исходнике 2026-11-15T13:57:11Z
SHA256 исходника: 8b69538cec14a1447cf7afb64a595896e28c0d7c10bda3ac0411618affcf423f
Git blob SHA: 6e63fcf4852c341ec42e26c68fdd7a36cb7e5b04
Размер исходника: 25290 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/anicraft/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.anicraft.png" width="128" height="128" alt="Значок AniCraft: гравированный кролик на жёлтой плитке">
</p>

<h1 align="center">AniCraft</h1>

<p align="center">
  <b>Студия 2D-векторной анимации; открытая реализация Adobe Animate, написанная с чистого листа на чистом Rust.</b>
</p>

<p align="center">
  Нативный редактор 2D-векторной анимации со шкалой времени, слоями, ключевыми кадрами, классическими твинами и твинами формы,
  калькой и столом на egui. Работает нативно в macOS, Windows, Linux и FreeBSD
  и в браузере через WebAssembly. Сделано командой ArtCraft.
</p>

<p align="center">
  <img alt="Status: early alpha" src="https://img.shields.io/badge/status-early%20alpha-dac604?style=flat-square">
  <img alt="Written in pure Rust" src="https://img.shields.io/badge/pure-Rust-b7410e?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows, Linux, FreeBSD and the web" src="https://img.shields.io/badge/runs%20on-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-555555?style=flat-square">
  <img alt="MCP server for agents" src="https://img.shields.io/badge/agents-MCP%20server-555555?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-555555?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_anicraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/anicraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/anicraft"><b>AniCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/shot-1-stage.png" alt="AniCraft с открытой образцовой анимацией: на столе мяч, звезда и солнце над холмами в сумерках; на шкале времени внизу пять слоёв с фиолетовыми диапазонами классических твинов, а в панели «Свойства» — кривая сглаживания движения выбранного твина" width="100%">
  <br><sub><b>Образцовая анимация</b>: стол, инструменты, шкала времени с классическими твинами и «Свойства» с кривой сглаживания движения · <code>cargo run</code></sub>
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Живописцы, аниматоры, кинематографисты,
> иллюстраторы, создатели игр &mdash; если вы что-то создаёте, вы один из нас. **[Загляните в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#a-look-around">Взгляд вокруг</a> ·
  <a href="#made-in-anicraft">Сделано в AniCraft</a> ·
  <a href="#why-anicraft">Почему AniCraft</a> ·
  <a href="#features">Возможности</a> ·
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
  <img src="docs/images/shot-2-subselection.png" alt="Инструмент «Частичное выделение» показывает опорные точки и манипуляторы Безье на синей фигуре рядом с волнистой линией, нарисованной «Карандашом»; в панели «Свойства» — положение, масштаб, заливка и обводка фигуры" width="100%">
  <p align="center"><sub><b>Частичное выделение, Перо и Карандаш</b>: настоящие опорные точки и манипуляторы Безье, свободно проведённые линии с подгонкой кривых</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-3-frames.png" alt="На шкале времени выделен блок кадров на трёх слоях, мяч сплюснут в середине твина на столе" width="100%">
  <p align="center"><sub><b>Шкала времени</b>: диапазоны кадров по слоям, ключевые кадры, которые можно перетаскивать, классические твины и твины формы</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/shot-4-transform.png" alt="«Свободное трансформирование» на мяче с угловыми и серединными манипуляторами; в панели «Свойства» — положение, масштаб, поворот, альфа и зацикливание экземпляра символа" width="100%">
  <p align="center"><sub><b>Свободное трансформирование и символы</b>: масштабируйте, поворачивайте и перемещайте экземпляры со вложенными шкалами времени</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-5-palette.png" alt="Палитра команд открыта над столом, в поиске набрано key, показаны команды ключевых кадров и их сочетания клавиш" width="100%">
  <p align="center"><sub><b>Палитра команд</b>: любая команда движка — один поиск (<code>Ctrl+K</code>)</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/shot-6-shortcuts.png" alt="Редактор сочетаний клавиш: список основных команд и инструментов с клавишами, поле фильтра и кнопки сброса" width="100%">
  <p align="center"><sub><b>Редактор сочетаний</b>: переназначьте, добавьте или очистите клавишу любой команды или инструмента (<code>F1</code>)</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-7-preferences.png" alt="Окно «Настройки»: шрифты интерфейса и данных, масштаб интерфейса, режим визуализации стола, шкала времени, диалог файлов и параметры безопасности" width="100%">
  <p align="center"><sub><b>Настройки</b>: шрифты, масштаб интерфейса, визуализация стола и подтверждения</sub></p>
</td>
</tr>
</table>

<a id="made-in-anicraft"></a>
## Сделано в AniCraft

Образцовая анимация, выведенная как анимированный GIF собственным визуализатором AniCraft из командной строки
(`anicraft-cli gif --sample --out sample.gif --scale 0.5`).

<p align="center">
  <img src="docs/images/sample-animation.gif" alt="Образцовая анимация: мяч прыгает и сплющивается по холмам в сумерках, звезда крутится, солнце пульсирует" width="640">
  <br><sub><b>Образцовая анимация</b>: классические твины со сглаживанием движения, символы со своими шкалами времени, 48 кадров при 24 кадрах в секунду</sub>
</p>

<a id="why-anicraft"></a>
## Почему AniCraft

- **Привычно.** Стол, инструменты, шкала времени, слои, ключевые кадры, «Свойства» и «Библиотека» стоят там, где их ждут
  руки. Если вы знаете Adobe Animate или Flash, вы уже знаете AniCraft.
- **Быстро.** Движок на чистом Rust с детерминированным аналитическим сглаживанием на ЦП, параллельной отрисовкой
  полосами, тайловым столом и фоновым рабочим потоком визуализации. Никакого Electron, никакого webview, никакого ожидания.
- **Надёжно.** Никакого кода `unsafe` (`unsafe_code = "forbid"`), никаких паник на входных данных, каждая команда пропущена через фаззинг, а
  отмена со структурным разделением (`Arc`) держит историю мгновенной и пропорциональной памяти.
- **Время — функция.** Документ — обычные данные, а картинка на кадре — чистая функция,
  `evaluate(doc, frame)`. Классические твины с наборами сглаживания движения и твины формы с морфингом контуров.
- **Открыто.** Документированный собственный формат (`.anicraft`, JSON). Открывает документы Adobe Animate (`.fla`,
  `.xfl`, папки XFL), импортирует SVG на стол и экспортирует кадры и последовательности PNG, анимированный GIF,
  кадры SVG, спрайт-листы, Lottie и WebM/MP4 через ваш собственный ffmpeg.
- **Для агентов.** Каждое действие — команда движка. Тем же движком можно управлять из интерфейса, из CLI, по каналу
  JSON-lines или через **MCP-сервер**, так что Claude и другие агенты могут рисовать, анимировать и экспортировать.

<a id="features"></a>
## Возможности

<a id="stage-and-drawing-tools"></a>
### Стол и инструменты рисования
* **Выделение и частичное выделение**: выделяйте, перемещайте, сдвигайте стрелками, правьте опорные точки и манипуляторы Безье на контурах (`Subselection (A)`), добавляйте и удаляйте точки.
* **Векторное рисование**: Перо (`P`) с гладкими манипуляторами и преобразованием углов, Карандаш (`Shift+Y`) с подгонкой кривых по Шнейдеру и сглаживанием, Прямоугольник (со скруглением углов), Овал, Многоугольник/звезда, Линия и Текст (`T`).
* **Слияние при рисовании**: фигуры на слое разрезают и соединяют друг друга, как в Animate (заливки заменяют или сливаются, линии разбиваются в пересечениях); сегмент выбирается щелчком, связанные части — двойным щелчком, а «Рисование объектов» (`J`) оставляет фигуры раздельными.
* **Свободное трансформирование (`Q`)**: интерактивное масштабирование, угловые и серединные манипуляторы с пропорциональным Shift и модификатором центра Alt, поворот с привязкой 15°.
* **Заливки и обводки**: Ведро заливки (`K`) с закрытием разрывов, Чернильница (`S`), сплошные цвета, линейные и радиальные градиенты, растровые заливки и оформление обводки.
* **Порядок и выравнивание**: выровнять по левому краю / по центру / по правому краю / поверху / посередине / понизу (в том числе относительно стола), распределение, поворот на 90° по и против часовой стрелки, отражение по горизонтали и по вертикали.

<a id="timeline-and-animation"></a>
### Шкала времени и анимация
* **Слои и организация**: обычные слои, направляющие, направляющие движения и слои-маски, а также вложенные папки слоёв.
* **Работа с кадрами**: ключевые кадры (`F6`), пустые ключевые кадры (`F7`), вставка кадров (`F5`), перетаскивание диапазонов, выделение нескольких кадров сразу на нескольких слоях, вырезание, копирование и вставка кадров.
* **Классические твины и твины формы**: классические твины с 8 наборами сглаживания движения и своими кривыми сглаживания; твины формы морфируют между произвольными векторными контурами.
* **Калька**: видимый диапазон до и после головки воспроизведения для прорисовки промежуточных кадров.
* **Символы и экземпляры**: графические символы со вложенными шкалами времени и режимами цикла (Цикл, Проиграть один раз, Один кадр), клипы, фильтры и режимы смешивания, а также сцены.

<a id="workflow-and-customization"></a>
### Рабочий процесс и настройка
* **Редактор сочетаний (`F1`)**: интерактивный редактор карты клавиш, чтобы настроить, переназначить или очистить сочетание любого инструмента или команды.
* **Палитра команд (`Ctrl+K`)**: быстрый нечёткий поиск и выполнение всех команд движка.
* **Безопасность и восстановление**: многоуровневое подтверждение разрушительных действий, защита от несохранённых изменений, автосохранение при сбое и импорт без заголовка, который не перезаписывает файлы.

<a id="quick-start"></a>
## Быстрый старт

```sh
git clone https://github.com/storytold/anicraft
cd anicraft

cargo run --release                                     # desktop app with the sample animation
cargo run --release -- --screenshot shots/now.png       # draw ~120 frames, save the window, exit
cargo run --release -p anicraft-cli -- info --sample
cargo run --release -p anicraft-cli -- render --sample --frame 12 --out frame12.png
cargo run --release -p anicraft-cli -- render-seq --sample --out-dir frames --scale 0.5
cargo run --release -p anicraft-cli -- gif --sample --out animation.gif
cargo run --release -p anicraft-cli -- commands         # the command registry as JSON
cargo run --release -p anicraft-cli -- guide --out guide  # the user guide as HTML pages
cargo run --release -p anicraft-cli -- exec --sample draw.rect '{"x":10,"y":10,"w":80,"h":40}' --save out.anicraft
cargo run --release -p anicraft-cli -- serve --sample   # JSON-lines on stdin/stdout
cargo test                                              # all crates
```

Гарнитуры интерфейса (Inter и JetBrains Mono) берутся из [storytold/craft-fonts](https://github.com/storytold/craft-fonts),
необязательный вход сборки: `CRAFT_FONTS_DIR="$PWD/../craft-fonts" cargo run --release` (абсолютный путь). Без него AniCraft
использует встроенные шрифты egui. См. [`docs/development.md`](docs/development.md).

Протокол `serve` принимает по одному JSON-запросу на строку, `{"id": 1, "cmd": "timeline.insert_keyframe", "params": {"frame": 10}}`,
и отвечает своим состоянием, `{"id": 1, "ok": true, "result": {}, "revision": 7, "frame": 0}`. Чтобы выйти, отправьте `{"cmd": "quit"}`.

<a id="use-it-from-claude-code-and-other-agents"></a>
### Использовать из Claude Code и других агентов

Зарегистрируйте MCP-сервер в Claude Code:

```sh
claude mcp add anicraft -- /path/to/anicraft-cli mcp
```

Подробности, включая запись сервера для других MCP-клиентов, — в [`docs/mcp.md`](docs/mcp.md).

<a id="status"></a>
## Состояние

> [!IMPORTANT]
> **Ранняя альфа: ещё не для производственной анимации.** Базовая модель документа, векторный визуализатор,
> оболочка на egui, классические твины и твины формы и первые импорты XFL и SVG уже работают; многое ещё впереди.

В [**docs/roadmap.md**](docs/roadmap.md) — честное состояние по измерениям, вехи M0–M8 и ближайшие шаги.

**Чего ещё нет:** ActionScript за пределами подмножества шкалы времени (скрипты кадров сохраняются, и те,
что управляют шкалой времени, выполняются; ADR 0013), и твины движения из XFL.

**Состав репозитория:** строго нисходящая слоистость, её проверяет `cargo test`:

```text
crates/geom     L0  Vec2, Affine (decompose/compose), Rect, Path, flattening, hit testing
crates/xml      L0  Bounded XML element reader shared by the importers (XFL, SVG)
crates/doc      L1  Document model, easing, timeline evaluation, sample scene
crates/text     L1  Fonts on this computer, shaping and line layout into outlines (ADR 0012)
crates/render   L2  CPU oracle renderer (coverage accumulation, paints, strokes, PNG)
crates/xfl      L2  XFL/FLA import: own XML + zip readers, edges → paths (ADR 0009)
crates/svg      L2  SVG import: shapes, groups, use, styles, transforms, gradients → shapes
crates/engine   L3  Session, undo (with gesture coalescing), command registry, .anicraft format
crates/cli      L4  anicraft-cli: info/render/render-seq/commands/exec/run/new/serve/mcp
src/            L5  egui shell (app, menus, stage, timeline, panels, theme)
```

Никакой код ниже `src/` не зависит от egui, eframe или библиотек окон.

**Впервые в AniCraft?** [**Руководство пользователя**](docs/guide/index.md) написано для художников: с чего начать, каждый
рабочий процесс, глава для тех, кто [пришёл из Animate](docs/guide/coming-from-animate.md), и сгенерированные справочники
[команд](docs/guide/reference/commands.md) и [сочетаний клавиш](docs/guide/reference/shortcuts.md). Его также можно
открыть без сети из **Справка › Руководство пользователя**.

Правила для агентов и участников (чистая комната, политика ресурсов, никаких паник в поставляемом коде) — в [`AGENTS.md`](AGENTS.md).
В [`docs/requirements.md`](docs/requirements.md) — объём, в [`docs/architecture.md`](docs/architecture.md) — устройство,
в [`docs/product-principles.md`](docs/product-principles.md) — принципы устройства и взаимодействия,
в [`docs/accessibility.md`](docs/accessibility.md) — поддержка клавиатуры, программ чтения с экрана, высокой контрастности и масштабирования, а
в [`docs/development.md`](docs/development.md) — подготовка, испытания и гигиена сборки. Каждый встроенный ресурс указан
с лицензией в [`ATTRIBUTION.md`](ATTRIBUTION.md).

<a id="downloads"></a>
## Загрузки

**Впервые в AniCraft?** Скачайте программу со [страницы AniCraft на getartcraft.com](https://getartcraft.com/apps/anicraft). Так установить проще всего.

**Нужна конкретная сборка или формат?** На GitHub в [последнем выпуске](https://github.com/storytold/anicraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/anicraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `anicraft-<ver>-windows-x64.msi` | `anicraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `anicraft-<ver>-windows-arm64.msi` | `anicraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `anicraft-<ver>-windows-x86.msi` | `anicraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы подписаны.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `anicraft-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `anicraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `anicraft-<ver>-linux-x86_64.AppImage` | `anicraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `anicraft-<ver>-linux-x86_64.flatpak` | `anicraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `anicraft-<ver>-linux-x86_64.deb` | `anicraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `anicraft-<ver>-linux-x86_64.rpm` | `anicraft-<ver>-linux-aarch64.rpm` | |
| Архив | `anicraft-<ver>-linux-x86_64.tar.gz` | `anicraft-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

RISC-V (riscv64): `anicraft-<ver>-linux-riscv64.tar.gz`, только архив.

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `anicraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `anicraft-web-<ver>.zip` | Пока нет в выпусках: соберите сами с `packaging/web/package.sh` ([docs/web.md](docs/web.md)), затем разместите на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

AniCraft — одно из приложений **Crafting Apps**: бесплатных творческих инструментов с открытым исходным кодом от команды
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
| <img src="assets/app-icon/hicolor/64x64/apps/ai.storyteller.anicraft.png" alt="" width="32" height="32"> | **AniCraft** | **2D-векторная анимация · вы здесь** | [GitHub](https://github.com/storytold/anicraft) | [Сайт](https://getartcraft.com/apps/anicraft) |
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
  <a href="https://getartcraft.com/apps/anicraft">AniCraft</a>
</p>

<a id="star-history"></a>
## История звёзд

[![Star History Chart](https://api.star-history.com/svg?repos=storytold/anicraft&type=Date&legend=top-left)](https://www.star-history.com/?repos=storytold%2Fanicraft&type=date&legend=top-left)

<a id="license-and-credits"></a>
## Лицензия и благодарности

AniCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the AniCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Значок программы (гравированный кролик на жёлтом AniCraft, `#dac604`) — оригинальная работа владельца; палитра и
файлы — в [`assets/app-icon/`](assets/app-icon/README.md).

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и AniCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<sub>Adobe, Animate и Flash являются товарными знаками или зарегистрированными товарными знаками Adobe Inc. в Соединённых Штатах и/или других странах. AniCraft — независимый проект с открытым исходным кодом и не связан с Adobe Inc., не спонсируется ею и не одобрен ею; эти имена используются только чтобы описать рабочие процессы и форматы файлов, с которыми программа совместима.</sub>

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
