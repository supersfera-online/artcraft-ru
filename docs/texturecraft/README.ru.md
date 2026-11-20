# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/texturecraft/blob/main/README.md
Репозиторий: https://github.com/storytold/texturecraft
Коммит исходника (последний, в котором менялся README.md): 9feb78523a644a490197f45523102f8b839b167f
Дата коммита: 18 ноября 2026, 09:12 (America/Los_Angeles, PT); в исходнике 2026-11-18T17:12:29Z
SHA256 исходника: 0bbd6974ba36f9c1572318707ee98bd22fa22050d4208fe0d57f9565e8b570ff
Git blob SHA: 345c32c1f9abb2867a2d7a43a415c6c33cf22712
Размер исходника: 23772 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/texturecraft/main/README.md
Перевод выполнен локально; авторам не отправлялся. Строки-переключателя языков нет: в репозитории нет других README.<код>.md.
-->
<!-- Перевод не проверен авторами -->
<p align="center">
  <a href="https://getartcraft.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/artcraft-logo-white.png">
      <img alt="ArtCraft" src="docs/brand/artcraft-logo.png" width="200">
    </picture>
  </a>
</p>


<p align="center">
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.texturecraft.png" width="128" height="128" alt="Значок TextureCraft: гравированная зебра на медной плитке">
</p>

<h1 align="center">TextureCraft</h1>

<p align="center">
  <b>Рисование 3D-текстур: современная программа с открытым исходным кодом, написанная на чистом Rust.</b>
</p>

<p align="center">
  Быстрый рабочий процесс рисования 3D-текстур с открытым исходным кодом: рисуйте PBR-материалы прямо на моделях
  слоями с масками, запекайте карты сетки, стройте по ним умные материалы и экспортируйте текстуры
  для любого движка. Работает нативно в macOS, Windows, Linux и FreeBSD и в браузере через WebAssembly.
  Сделано командой ArtCraft.
</p>

<p align="center">
  <img alt="Status: in active development" src="https://img.shields.io/badge/status-in%20active%20development-c2672b?style=flat-square">
  <img alt="Written in pure Rust" src="https://img.shields.io/badge/pure-Rust-b83a24?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows, Linux, FreeBSD and the web" src="https://img.shields.io/badge/runs%20on-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-555555?style=flat-square">
  <img alt="MCP server for agents" src="https://img.shields.io/badge/agents-MCP%20server-555555?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-555555?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_texturecraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/texturecraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/texturecraft"><b>TextureCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/texturecraft-workspace.png" alt="Рабочая среда TextureCraft: библиотека материалов слева; 3D-вид и 2D-вид развёртки UV переносного телевизора 1970-х в состаренном кремовом пластике с нарисованным от руки цветком мелком; справа список наборов текстур, стопка слоёв с папками Crayon doodle и Wear and dirt и свойства слоя заливки" width="100%">
  <br><sub><b>Рабочая среда</b>: полка ресурсов, 3D-вид, 2D-вид UV, наборы текстур, стопка слоёв и свойства</sub>
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Живописцы, скульпторы, игровые
> художники, фотографы, кинематографисты, иллюстраторы, дизайнеры, любители и те, кто взял
> перо в руки только на прошлой неделе. Если вы что-то создаёте, вам сюда. **[Загляните в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#a-look-around">Взгляд вокруг</a> ·
  <a href="#made-in-texturecraft">Сделано в TextureCraft</a> ·
  <a href="#why-texturecraft">Почему TextureCraft</a> ·
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
  <img src="docs/images/texturecraft-bake.png" alt="Режим запекания на переносном телевизоре: семь наборов текстур и печи карт сетки слева, общие параметры запекания под ними и кнопка Bake selected textures под видом" width="100%">
  <p align="center"><sub><b>Запекание карт сетки</b>: затенение окружения, кривизна, толщина и другое, с трассировкой лучей на GPU</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/texturecraft-export.png" alt="Диалог «Экспорт текстур»: наборы текстур для экспорта, каталог вывода, шаблон имени, тип файла, размер, отступ и формат карты нормалей" width="100%">
  <p align="center"><sub><b>Экспорт текстур</b>: наборы для распространённых движков или свои шаблоны вывода с упаковкой каналов</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/texturecraft-rendering.png" alt="Режим визуализации: переносной телевизор с трассировкой путей на GPU при 256 выборках и шумоподавлением, изогнутый экран ловит студийный свет, настройки визуализации в карточке поверх вида" width="100%">
  <p align="center"><sub><b>Режим визуализации</b> (F10): ваши текстуры с трассировкой путей на GPU и шумоподавлением</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/texturecraft-light.png" alt="TextureCraft в светлом уровне яркости с синим акцентом: те же панели плитками на светлом фоне вокруг тёмного 3D-вида" width="100%">
  <p align="center"><sub><b>Светлая тема</b>: четыре уровня яркости и семь акцентных цветов</sub></p>
</td>
</tr>
</table>

<a id="made-in-texturecraft"></a>
## Сделано в TextureCraft

Два оригинальных реквизита, смоделированных процедурно участниками проекта, текстурированных слой за слоем
собственными материалами, масками и генераторами карт сетки TextureCraft (никаких текстур и моделей
извне) и визуализированных трассировкой путей на GPU командой `texturecraft-cli render`.

<table>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/texturecraft-lantern.png" alt="Штормовой фонарь с трассировкой путей на тёмной сцене: красная эмаль обколота до голой стали по рёбрам, ржавчина и копоть в швах, кремовая каёмка, потускневшая латунная горелка и регулятор, ржавые проволочные дужки и горящее пламя за стеклянной колбой" width="100%">
  <p align="center"><sub><b>Штормовой фонарь</b>: сколотая эмаль, ржавчина, копоть и горящее пламя на восьми наборах текстур</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/texturecraft-camera.png" alt="Винтажная дальномерная камера с трассировкой путей: чёрная эмаль стёрта до латуни по рёбрам и углам верхней панели, коньячный кожзам, накатанные хромированные диски, чёрный тубус объектива с гравированной шкалой дистанций и просветлённой передней линзой" width="100%">
  <p align="center"><sub><b>Дальномерная камера</b>: чёрная краска стёрта до латуни, кожзам, хром и просветлённое стекло</sub></p>
</td>
</tr>
</table>

<a id="why-texturecraft"></a>
## Почему TextureCraft

- **Привычно.** Раскладка, инструменты, меню, панели и сочетания клавиш, которые художники по текстурам уже знают: наборы
  текстур, стопка слоёв со смешиванием по каналам, маски и генераторы, умные материалы, полка
  инструментов, 3D- и 2D-виды. Вы уже умеете этим пользоваться.
- **Быстро.** Тайловый движок текселов с копированием при записи на всех ядрах ЦП и вид wgpu (Vulkan,
  Metal, DX12, WebGPU). Карты сетки запекаются на GPU примерно в 12× быстрее, чем на ЦП, режим визуализации
  трассирует пути примерно в 25× быстрее, а наборы текстур 8K остаются отзывчивыми, пока вы рисуете.
- **Без швов.** Отпечатки кисти живут на 3D-поверхности, поэтому штрихи перетекают через швы UV, а
  видимость камеры не даёт краске попасть на обратную сторону модели.
- **Надёжно.** Никаких паник в поставляемом коде, каждая команда проверена на враждебных входных данных, неограниченная отмена
  по снимкам с копированием при записи и проекты `.tcraft` без потерь.
- **Открыто.** На вход — glTF/GLB, FBX, COLLADA, USD, Alembic, OBJ, PLY и STL; на выход — текстуры PNG, JPEG, TGA, TIFF, BMP,
  WEBP, EXR и HDR с глубиной 8, 16 или 32 бита, с тайлами UDIM; экспорт текстурированных сеток OBJ, GLB и USD.
  Каждый материал, окружение, альфа кисти и встроенная сетка — процедурные.
- **Работает с MaterialCraft.** Материалы на графах узлов из
  [MaterialCraft](https://github.com/storytold/materialcraft) (`.mcmat`, сразу попадают на
  полку) рисуются и заливают как любой материал, а входы графа остаются здесь ползунками, цветами и
  наборами: каждое изменение пересчитывает материал в разрешении набора текстур, а запечённые карты
  этой сетки питают граф.
- **Для агентов.** Каждый пункт меню и каждый инструмент — команда, которой можно управлять из CLI, по JSON-каналу
  управления или через **MCP-сервер**, так что Claude и другие агенты могут рисовать, запекать и экспортировать так же,
  как человек.
- **Везде.** Одна кодовая база для настольных программ и тот же интерфейс в браузере.

Полный список возможностей — в [`docs/features.md`](docs/features.md).

<a id="quick-start"></a>
## Быстрый старт

```sh
git clone https://github.com/storytold/texturecraft
cd texturecraft

cargo run --release -p texturecraft                          # desktop app (starts with no project)
cargo run --release -p texturecraft -- model.glb             # a new project from a mesh
cargo run --release -p texturecraft -- --control 7878        # + JSON control channel
cargo run --release -p texturecraft-cli -- mcp               # MCP server (stdio)
cargo run --release -p texturecraft-cli -- new builtin:crate crate.tcraft --sample
cargo run --release -p texturecraft-cli -- render crate.tcraft crate.png --samples 256   # path traced
cargo run --release -p texturecraft-cli -- export crate.tcraft textures                 # headless export
cd apps/texturecraft-web && trunk serve                      # web build
cargo xtask ci                                               # fmt, clippy, tests, layering, wasm
```

Нужен Rust 1.95 или новее. Программа открывается без проекта (**Файл ▸ Открыть образцовый проект** загружает уже запечённый, а **Файл ▸ Закрыть** возвращает к пустому состоянию).
**Файл ▸ Новый проект** начинается с вашего файла сетки и шаблона проекта. TextureCraft строит UV, если у сетки их нет.

Текст интерфейса на японском, китайском, корейском и арабском набирается шрифтами
[storytold/craft-fonts](https://github.com/storytold/craft-fonts), когда они есть: это необязательный
вход сборки (в выпусках он всегда используется): `CRAFT_FONTS_DIR="$PWD/../craft-fonts" cargo run --release -p texturecraft`
(абсолютный путь). Без него настольная программа берёт установленные системные шрифты.

Если программа не может запуститься (например, нет подходящего GPU) или ей приходится закрыться, она сообщает причину в окне сообщения и
дописывает подробности в `errors.log` рядом со своими настройками (`%APPDATA%\TextureCraft\data` в Windows,
`~/Library/Application Support/TextureCraft` в macOS, `~/.local/share/texturecraft` в Linux).
На машине с несколькими GPU выбрать адаптер можно ключами `--gpu <part of the name>` или `--power-pref high`.

<a id="use-it-from-claude-code-and-other-agents"></a>
### Использовать из Claude Code и других агентов

Зарегистрируйте MCP-сервер в Claude Code, указав папки, которые ему можно читать и писать:

```sh
claude mcp add texturecraft -- /path/to/texturecraft-cli mcp --read-root /work/project --write-root /work/project
```

Чтобы управлять уже запущенной программой, стартуйте её с `--control 7878` и перебросьте канал:

```sh
claude mcp add texturecraft-app -- /path/to/texturecraft-cli mcp --bridge 7878
```

Подробности — в [`docs/control-protocol.md`](docs/control-protocol.md).

<a id="status"></a>
## Состояние

TextureCraft активно развивается. В [**ROADMAP.md**](ROADMAP.md) — оценка паритета по
областям, оставшаяся работа и ближайшие шаги.

**Где мы сейчас (2026-11-01):** по нашей оценке, примерно 93% повседневной работы художника по текстурам проходит от начала
до конца, с весами по тому, сколько дня занимает каждая область: импорт сеток, наборы текстур и тайлы
UDIM, стопка слоёв с масками, эффектами и умными материалами, все инструменты рисования, запекание, PBR-вид
и режим визуализации, наборы и шаблоны экспорта и полный набор меню. Интерфейс
говорит по-английски, по-французски, по-немецки, по-испански, по-португальски, по-итальянски, по-японски, по-китайски, по-корейски и по-арабски;
подробности — в [localization-parity.md](docs/localization-parity.md). Оценки мы выставили сами
по коду, сверяясь с открытой документацией.

**Чего ещё нет:**
- аппаратной трассировки лучей в режиме визуализации;
- наклона пера и нажима пера в Linux, macOS и настольных браузерах (слой окон пока
  их не сообщает);
- файлов Alembic в старом контейнере HDF5 и анимации Alembic (первый семпл уже читается);
- проверки переводов носителями языка;
- первого подписанного выпуска на каждой платформе.

**Куда идём:** первый выпуск, v0.1.0, на каждой платформе; затем оставшиеся пробелы в визуализации
и форматах файлов. Упорядоченный список — в [`ROADMAP.md`](ROADMAP.md).

**Состав репозитория:** `crates/{core, texel, geom, compose, bake, paint, formats, engine, render, automation, ui-egui}`
и `apps/{texturecraft, texturecraft-cli, texturecraft-web}`. Оболочка на egui — отдельный крейт, поэтому
интерфейс можно заменить, не трогая движок; как это устроено, объясняет [`docs/architecture.md`](docs/architecture.md).

Правила для агентов и участников (чистая комната, политика ресурсов, никаких паник в поставляемом коде, качественные проверки)
— в [`AGENTS.md`](AGENTS.md), а [`docs/releasing.md`](docs/releasing.md) описывает, как собираются, подписываются и публикуются выпуски. Каждый встроенный ресурс указан с лицензией в
[`ATTRIBUTION.md`](ATTRIBUTION.md).

<a id="downloads"></a>
## Загрузки

**Впервые в TextureCraft?** Скачайте программу со [страницы TextureCraft на getartcraft.com](https://getartcraft.com/apps/texturecraft). Так установить проще всего.

**Нужна конкретная сборка или формат?** На GitHub в [последнем выпуске](https://github.com/storytold/texturecraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/texturecraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `texturecraft-<ver>-windows-x64.msi` | `texturecraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `texturecraft-<ver>-windows-arm64.msi` | `texturecraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `texturecraft-<ver>-windows-x86.msi` | `texturecraft-<ver>-windows-x86-portable.zip` |

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `texturecraft-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `texturecraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `texturecraft-<ver>-linux-x86_64.AppImage` | `texturecraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `texturecraft-<ver>-linux-x86_64.flatpak` | `texturecraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `texturecraft-<ver>-linux-x86_64.deb` | `texturecraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `texturecraft-<ver>-linux-x86_64.rpm` | `texturecraft-<ver>-linux-aarch64.rpm` | |
| Архив | `texturecraft-<ver>-linux-x86_64.tar.gz` | `texturecraft-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `texturecraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `texturecraft-web-<ver>.zip` | Работает в современном браузере; разместите на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

TextureCraft — одно из приложений **Crafting Apps**: бесплатных творческих инструментов с открытым исходным кодом от команды
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
  <a href="https://getartcraft.com/apps/texturecraft">TextureCraft</a>
</p>

<a id="star-history"></a>
## История звёзд

[![Star History Chart](https://api.star-history.com/svg?repos=storytold/texturecraft&type=Date&legend=top-left)](https://www.star-history.com/?repos=storytold%2Ftexturecraft&type=date&legend=top-left)

<a id="license-and-credits"></a>
## Лицензия и благодарности

TextureCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the TextureCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md). Сборки выпуска также встраивают
шрифты [craft-fonts](https://github.com/storytold/craft-fonts/blob/main/ATTRIBUTION.md)
(начертания для японского и упрощённого китайского; SIL Open Font License 1.1).

Каждый показанный материал, окружение, альфа кисти и сетка порождены процедурно самим TextureCraft;
в снимках экрана нет сторонних текстур и моделей.

Значок программы (гравированная зебра на меди TextureCraft, `#c2672b`) — оригинальная работа владельца;
файлы — в [`assets/app-icon/`](assets/app-icon/).

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и TextureCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.png" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
