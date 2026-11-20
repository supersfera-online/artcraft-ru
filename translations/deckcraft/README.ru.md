# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/deckcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/deckcraft
Коммит исходника (последний, в котором менялся README.md): 8bdc96db64e22ff64e17c616e1a94043a9d3f1a0
Дата коммита: 19 ноября 2026, 20:13 (America/Los_Angeles, PT); в исходнике 2026-11-20T04:13:45Z
SHA256 исходника: 685354ea3b5b125c996aabcdefebfb5cebf305f9329d16708711afdf7fd3cbcb
Git blob SHA: 32d9b0e56e3f9893c304efcd7f435346ff774d99
Размер исходника: 22960 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/deckcraft/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.deckcraft.png" width="128" height="128" alt="Значок DeckCraft: экран презентации со столбчатой диаграммой на оранжевой плитке">
</p>

<h1 align="center">DeckCraft</h1>

<p align="center">
  <b>Презентации и слайд-шоу: открытый современный конструктор презентаций и слайдов, написанный на чистом Rust.</b>
</p>

<p align="center">
  Собирайте колоды с темами, макетами, фигурами, рисунками, таблицами, диаграммами, переходами и анимацией,
  открывайте и сохраняйте файлы презентаций .pptx, открывайте файлы PowerPoint 97–2003 .ppt/.pot/.pps (только импорт) и показывайте их на полный
  экран. Нативно на macOS, Windows, Linux
  и FreeBSD и в браузере. Каждая кнопка — это также команда, которой могут управлять CLI и ИИ-агенты
  (через MCP).
</p>

<p align="center">
  <img alt="Status: early development" src="https://img.shields.io/badge/status-early%20development-f26b1d?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue?style=flat-square">
  <img alt="Written in Rust" src="https://img.shields.io/badge/written%20in-Rust-b7410e?style=flat-square">
  <img alt="Platforms" src="https://img.shields.io/badge/platforms-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20BSD%20%C2%B7%20Web-555?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_deckcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/deckcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/deckcraft"><b>DeckCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Живописцы, фотографы,
> кинематографисты, иллюстраторы, дизайнеры, аниматоры, любители и те, кто взял карандаш в руки
> только на прошлой неделе. Если вы что-то создаёте, вы один из нас. **[Заходите поздороваться в Discord](https://discord.gg/artcraft).**

<p align="center">
  <img alt="Правка слайда в DeckCraft: лента, миниатюры слайдов с разделами, схема процесса на холсте, заметки и строка состояния" src="docs/images/editor.png" width="900">
</p>

<p align="center">
  <a href="#what-works-today">Что уже работает</a> ·
  <a href="#getting-started">С чего начать</a> ·
  <a href="#agents-cli-and-mcp">Агенты, CLI и MCP</a> ·
  <a href="#roadmap">План работ</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">Лицензия</a>
</p>

<a id="what-works-today"></a>
## Что уже работает

DeckCraft в альфе, курс на бету (см. [план работ](ROADMAP.md)).
Сегодня программа умеет:

- **Собирать колоды**: образцы слайдов и одиннадцать макетов с заполнителями, которые наследуют положение и
  оформление, восемь оригинальных тем со схемами цвета и шрифтов, разделы, заметки, комментарии,
  колонтитулы, пользовательские размеры слайдов.
- **Чертить**: более 150 фигур из наборов с маркерами настройки, соединители, которые остаются приклеенными к фигурам, инструменты свободной формы,
  кривой и каракулей, объединение фигур (объединение, совмещение, фрагмент, пересечение, вычесть), градиентные,
  растровые и узорные заливки, обводки с пунктиром и наконечниками стрелок, тени, свечение, мягкие края и
  отражения.
- **Писать**: правку текста на месте с полным оформлением шрифта и абзаца, маркеры и нумерацию,
  столбцы, автоподгонку, вертикальный текст, поля и гиперссылки.
- **Добавлять содержимое**: рисунки с обрезкой и коррекциями, таблицы со стилями, диаграммы, основы SmartArt,
  звук и видео (MP3, AAC, FLAC, ALAC, Ogg, Opus, WAV, AIFF; H.264, HEVC, VP9, AV1).
- **Показывать**: переходы (включая Morph), анимацию появления, выделения, исчезновения и по траектории движения,
  построение по абзацам, полноэкранный показ слайдов, вид докладчика, перо, репетицию времени, воспроизведение медиа.
- **Обмениваться файлами**: открывать и сохранять презентации .pptx, открывать файлы PowerPoint 97–2003 .ppt/.pot/.pps (только импорт: «Сохранить» просит новое имя), экспортировать PDF (слайды, страницы заметок, раздаточные материалы
  с выделяемым текстом), PNG/JPEG, анимированный GIF колоды и структуры. Несохранённая работа сохраняется через AutoRecover.
- **Автоматизировать**: более 200 команд с отменой, все доступны из CLI, по каналу управления JSON и через
  MCP-сервер для ИИ-агентов.

<table>
  <tr>
    <td width="50%"><img alt="Выделенная фигура со вкладкой «Формат фигуры»" src="docs/images/shape-format.png"><br><sub>Контекстная вкладка «Формат фигуры» и маркеры выделения</sub></td>
    <td width="50%"><img alt="Панель «Формат фигуры» правит градиентную заливку" src="docs/images/format-pane.png"><br><sub>Панель «Формат фигуры»: тип градиента, направление и стопы</sub></td>
  </tr>
  <tr>
    <td width="50%"><img alt="Вид сортировщика слайдов с переходами под каждым слайдом" src="docs/images/slide-sorter.png"><br><sub>Сортировщик слайдов с переходом каждого слайда</sub></td>
    <td width="50%"><img alt="DeckCraft в тёмном режиме со слайдом с диаграммой" src="docs/images/dark-mode.png"><br><sub>Тёмный режим, со встроенной диаграммой</sub></td>
  </tr>
</table>

<p align="center">
  <img alt="Все восемь слайдов образца колоды «Северное сияние»" src="docs/images/sample-deck.png" width="900"><br>
  <sub>Встроенная образцовая колода, отрисованная командой <code>deckcraft-cli render --sample --all</code></sub>
</p>

<a id="getting-started"></a>
## С чего начать

Экспорт PDF использует общий писатель `craft-pdf` с отключёнными возможностями импорта. См.
[`crates/pdf/README.md`](crates/pdf/README.md) — зависимости и требования к проверке.

```sh
git clone https://github.com/storytold/deckcraft
cd deckcraft
cargo run --release -p deckcraft-cli -- render --sample --all --scale 1 out/
```

В Linux для сборки также нужны заголовки ALSA, чтобы в показе слайдов был звук: `alsa-lib-devel` в Fedora,
`libasound2-dev` в Debian и Ubuntu, `alsa-lib` в Arch. Без них сборка останавливается на `alsa-sys`.

Шрифты берутся из [craft-fonts](https://github.com/storytold/craft-fonts): клонируйте его рядом с этим репозиторием
(`../craft-fonts`), и локальные сборки подхватят его сами; без него DeckCraft использует системные
шрифты.

В каждом [релизе на GitHub](https://github.com/storytold/deckcraft/releases) есть готовые сборки, в Linux — как
AppImage, `.deb`, `.rpm` и tarball. В Gentoo сообщество в [оверлее ::snakebyte](https://github.com/switch87/snakebyte-overlay)
упаковывает Linux-релиз как
`app-office/deckcraft-bin` (не сопровождается командой DeckCraft):

```sh
eselect repository add snakebyte git https://github.com/switch87/snakebyte-overlay.git
emaint sync -r snakebyte
echo 'app-office/deckcraft-bin ~amd64' >> /etc/portage/package.accept_keywords/deckcraft
emerge --ask app-office/deckcraft-bin
```

<a id="logs"></a>
### Журналы

Настольная программа пишет записи `log` в стандартный поток ошибок и в `logs/deckcraft.log` в каталоге
настроек, рядом с `ui.json` и `prefs.json` (Linux `~/.config/deckcraft/logs/` или
`$XDG_CONFIG_HOME/deckcraft/logs/`; macOS `~/Library/Application Support/DeckCraft/logs/`; Windows
`%APPDATA%\DeckCraft\logs\`). Запуск из меню рабочего стола или из Dock не даёт терминала, поэтому к отчёту об ошибке стоит приложить именно этот файл: туда попадают отчёт о панике от защиты при сбое, неудачное сохранение после восстановления,
пропущенные при импорте части и проблемы вывода звука. Каждый запуск переносит
предыдущий журнал в `deckcraft.1.log` (а тот — в `deckcraft.2.log`), так что журнал упавшего запуска
переживает следующий старт. Файл перестаёт расти при 16 МиБ. `--version` файл не пишет.

| Переменная | Действие |
|---|---|
| `RUST_LOG` | Уровни журнала для стандартного потока ошибок и файла журнала. По умолчанию: `info` для собственных crate DeckCraft, `warn` для всего остального. Директивы в стиле env_logger заменяют это, например `RUST_LOG=debug`, `RUST_LOG=warn,deckcraft_pptx=trace` или `RUST_LOG=info,wgpu_core=warn`; директива, оканчивающаяся на `*`, покрывает все цели, которые с неё начинаются (`deckcraft*=debug`). |

Средство журналирования — `apps/deckcraft/src/logging.rs`; обратный вызов звука в реальном времени в журнал не пишет. Веб-программа
вместо этого пишет в консоль браузера.

<a id="agents-cli-and-mcp"></a>
## Агенты, CLI и MCP

Каждое действие в DeckCraft — команда со стабильным идентификатором, поэтому люди, сценарии и ИИ-агенты используют одни и
те же глаголы:

```sh
deckcraft-cli commands format.          # list commands
deckcraft-cli run --sample --cmd 'slide.new={"layout":"titleOnly","title":"Hello"}' --save hello.deckcraft
deckcraft-cli mcp                       # MCP server over stdio (headless)
deckcraft-cli mcp --connect 7990        # drive the running app (deckcraft --control 7990)
deckcraft-cli mcp --automation-read-root DIR --automation-write-root DIR   # confine the headless agent to folders
```

<a id="roadmap"></a>
## План работ

DeckCraft находится в **альфе**. Он покрывает **84% возможностей, отслеживаемых в [`docs/target-app-parity.md`](docs/target-app-parity.md), по широте** (92% основных,
измерено) и готов примерно на **55% к настоящей работе по всем отслеживаемым возможностям** (оценка).
См. [ROADMAP.md](ROADMAP.md) про этап, числа по каждому измерению и что дальше,
[docs/target-app-parity.md](docs/target-app-parity.md) — полная оценка,
[docs/gaps.md](docs/gaps.md) — каждый известный пробел и
[docs/parity-checklist.md](docs/parity-checklist.md) — перечень возможностей пункт за пунктом.

<a id="downloads"></a>
## Загрузки

**Скачайте DeckCraft** с GitHub: в [последнем релизе](https://github.com/storytold/deckcraft/releases/latest) перечислены все сборки ниже, а в [списке всех релизов](https://github.com/storytold/deckcraft/releases) — предыдущие версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму для каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная версия |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `deckcraft-<ver>-windows-x64.msi` | `deckcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `deckcraft-<ver>-windows-arm64.msi` | `deckcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `deckcraft-<ver>-windows-x86.msi` | `deckcraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы имеют цифровую подпись.

**Если программа не открывается в Windows:** настольная программа по умолчанию инициализирует только DirectX 12.
Если позволить wgpu также создать экземпляр OpenGL, на некоторых графических драйверах (AMD
`atio6axx.dll`) это может привести к сбою ещё до появления окна, так что программа мелькнёт в «Диспетчере задач» и завершится.
`WGPU_BACKEND` подменяет значение по умолчанию для поиска неисправностей (например `dx12` или `vulkan`). В
PowerShell, из папки с исполняемым файлом:

```powershell
$env:WGPU_BACKEND = "vulkan"
& .\deckcraft.exe
Remove-Item Env:WGPU_BACKEND                     # restore the default for later launches
```

Явная подмена `gl` может снова вызвать сбой драйвера на затронутых системах. Значения по умолчанию для программной части macOS, Linux
и веба не менялись.

Шейдеры DirectX 12 компилируются FXC, который входит в Windows, поэтому `dxcompiler.dll` и
`dxil.dll` не нужны («Parent device is lost» при старте, #153). `$env:WGPU_DX12_COMPILER = "dxc"`
(или `"auto"`) снова включает обработку DXC в wgpu для поиска неисправностей.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `deckcraft-<ver>-macos-universal.dmg` | Подписана и нотаризована |
| Инструмент командной строки, универсальный | `deckcraft-cli-<ver>-macos-universal.zip` | Подписан и нотаризован |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `deckcraft-<ver>-linux-x86_64.AppImage` | `deckcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `deckcraft-<ver>-linux-x86_64.flatpak` | `deckcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `deckcraft-<ver>-linux-x86_64.deb` | `deckcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `deckcraft-<ver>-linux-x86_64.rpm` | `deckcraft-<ver>-linux-aarch64.rpm` | |
| Tarball | `deckcraft-<ver>-linux-x86_64.tar.gz` | `deckcraft-<ver>-linux-aarch64.tar.gz` | Распаковать куда угодно |

RISC-V 64 (riscv64): только tarball `deckcraft-<ver>-linux-riscv64.tar.gz` (кросс-сборка; нужен glibc 2.39+, например Ubuntu 24.04+).

**Библиотеки времени выполнения.** Библиотеки оконной системы, GPU и диалогов файлов, которые нужны DeckCraft, открываются
при запуске программы (`dlopen` через `x11-dl`, `xkbcommon-dl`, `ash`, `glutin` и `rfd`), а не
связываются при сборке, поэтому `ldd` их не показывает: установка, которая удовлетворяет связанным зависимостям,
всё равно может не запуститься с ошибкой загрузчика и без подсказки, что ставить. Только
`libasound.so.2` (звук показа слайдов) — жёсткая зависимость времени связывания, и только у графической программы `deckcraft`
— `deckcraft-cli` не использует ни звук, ни дисплей. `.deb` и `.rpm` объявляют набор в
`packaging/linux/nfpm.yaml`; установка из tarball или система musl должны предоставить его сами:

```sh
apk add libx11 libxcursor libxrandr libxi libxkbcommon xkeyboard-config \
        wayland-libs-client alsa-lib \
        vulkan-loader mesa-vulkan-swrast \
        mesa-gl mesa-egl mesa-dri-gallium \
        xdg-desktop-portal
```

Выше — имена Alpine Linux `v3.22`; musl-вариант Void использует тот же загрузчик `/lib/ld-musl-x86_64.so.1`
и те же библиотеки, что `libX11 libXcursor libXrandr libXi libxkbcommon xkeyboard-config
wayland alsa-lib vulkan-loader mesa xdg-desktop-portal`. Среди артефактов релиза musl-сборки пока нет — это то, что нужно во время выполнения сборке из исходников на musl, и то, что понадобится будущему musl-артефакту (#954).

- `mesa-vulkan-swrast` — программный драйвер Vulkan: работает где угодно, включая виртуальные машины и контейнеры. На настоящей GPU ставьте драйвер производителя (`mesa-vulkan-intel`,
  `mesa-vulkan-ati`, `mesa-vulkan-nouveau`, …).
- Без Vulkan программа отступает к отрисовке на CPU через GL-драйверы Mesa. Это работает, но
  медленно — ограничение драйвера, а не ошибка DeckCraft.
- `xdg-desktop-portal` (с `xdg-desktop-portal-gtk` или `-kde`; у `-wlr` нет выбора файлов, поэтому
  на композиторах wlroots поставьте `zenity`) — то, с чем говорят диалоги «Открыть» и «Сохранить»; в `xkeyboard-config` лежат данные клавиатуры XKB, которые читает `libxkbcommon`.
- fontconfig и freetype не нужны: DeckCraft сам читает `/usr/share/fonts` и встраивает свои
  шрифты презентаций.

Для сборки из исходников на musl также нужны `build-base pkgconf alsa-lib-dev` (`alsa-lib-dev` — это
заголовки ALSA).

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `deckcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `deckcraft-web-<ver>.zip` | Работает в современном браузере; размещается на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

DeckCraft — одно из приложений **Crafting Apps**: бесплатных творческих инструментов с открытым исходным кодом от команды
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
  <a href="https://getartcraft.com/apps/deckcraft">DeckCraft</a>
</p>

<a id="license-and-credits"></a>
## Лицензия и благодарности

DeckCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the DeckCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Темы, макеты, геометрия фигур, значки и образцовые колоды DeckCraft — оригинальная работа, нарисованная или
порождённая в коде; сторонние закрытые рисунки, шрифты, темы и шаблоны не используются.

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и DeckCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
