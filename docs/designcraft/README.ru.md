# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/designcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/designcraft
Коммит исходника (последний, в котором менялся README.md): 4a1ff582e945acff00fae66431af2ec2450cb712
Дата коммита: 3 ноября 2026, 13:44 (America/Los_Angeles, PT); в исходнике 2026-11-03T21:44:59Z
SHA256 исходника: 02a45e06061ed08a5551d0d6ee75e88f3b769eebd044e4ac7ef1fabe65f47292
Git blob SHA: 92dcae7bfbddb6b2cac02f08c14bf4dcb8a64178
Размер исходника: 29189 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/designcraft/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.designcraft.png" width="128" height="128" alt="Значок DesignCraft: гравированная кошка в шарфе в горошек на зелёной плитке">
</p>

<h1 align="center">DesignCraft</h1>

<p align="center">
  <b>Вёрстка и публикация: современная студия настольной издательской системы и вёрстки страниц с открытым исходным кодом, написанная на чистом Rust.</b>
</p>

<p align="center">
  Быстрый рабочий процесс настольной издательской системы и вёрстки страниц с открытым исходным кодом. Работает нативно в macOS,
  Windows и Linux и в браузере через WebAssembly.<br>
  <i>Команда ArtCraft.</i>
</p>

<p align="center">
  <img alt="Written in Rust" src="https://img.shields.io/badge/written%20in-Rust-4d7a0a?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows, Linux and the web" src="https://img.shields.io/badge/runs%20on-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20Web-7bb51c?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-4d7a0a?style=flat-square">
  <img alt="Agent-drivable over MCP" src="https://img.shields.io/badge/agents-MCP-7bb51c?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_designcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/designcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/designcraft"><b>DesignCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/ui-spread.png" alt="DesignCraft показывает журнальный разворот: выделен связанный трёхколоночный текст с входным и выходным портами и линией связи, панель управления показывает положение в пиках, панель «Свойства» — параметры текстовой рамки" width="100%">
  <br><sub><b>Quarterly, весенний выпуск</b>: связанный трёхколоночный основной текст, обтекаемая выноска и колонцифры с родительских страниц — всё набрано собственным абзацным композитором DesignCraft.</sub>
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Цифра, генеративное искусство, музыка,
> игры &mdash; если вы что-то создаёте, вы один из нас. **[Загляните в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#the-sample-magazine">Образцовый журнал</a> ·
  <a href="#why-designcraft">Почему DesignCraft</a> ·
  <a href="#quick-start">Быстрый старт</a> ·
  <a href="#web">Веб</a> ·
  <a href="#architecture">Архитектура</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">Лицензия и благодарности</a>
</p>

<a id="the-sample-magazine"></a>
## Образцовый журнал

Каждая страница ниже свёрстана DesignCraft из кода (`crates/engine/src/sample.rs`) и выведена
его собственным визуализатором. Попробуйте сами командой `Help → Sample Document` или запустите программу с
`--sample`.

<table>
<tr>
<td width="50%" valign="top"><img src="docs/images/page-cover.png" alt="Обложка журнала The Spring Issue, No. 01: сумеречный пейзаж слоистых фиолетовых холмов под большим бледным солнцем, белый антиквенный заголовок The Quiet Art of Layout и курсивный лид под ним" width="100%"><p align="center"><sub><b>Обложка.</b> Графическая рамка на вылет, акцидентный текст и курсивный лид.</sub></p></td>
<td width="50%" valign="top"><img src="docs/images/page-2.png" alt="Открытие материала Notes on the Grid: оранжевый кикер FEATURE · DESIGN над линейкой, курсивный лид, широкий пейзажный снимок с небольшой подписью и две колонки выключенного основного текста над колонцифрой QUARTERLY" width="100%"><p align="center"><sub><b>Стили.</b> Линейка кикера, заголовок, лид, подпись и выключенный двухколоночный основной текст.</sub></p></td>
</tr>
<tr>
<td width="50%" valign="top"><img src="docs/images/page-3.png" alt="Трёхколоночная страница выключенного, с переносами основного текста, который обтекает затенённую выноску The best layouts disappear. What remains is the story., с градиентной линейкой и колонцифрой SPRING ISSUE внизу" width="100%"><p align="center"><sub><b>Связывание, колонки и обтекание текстом.</b> Один материал течёт через три колонки и вокруг выноски.</sub></p></td>
<td width="50%" valign="top"><img src="docs/images/page-4.png" alt="Страница Coming Next с заголовком Color, Ink and Paper на сливовом фоне, четыре кружка образцов Ink Plum, Sunset, C=100 M=0 Y=0 K=0 и Paper Warm над коротким абзацем основного текста" width="100%"><p align="center"><sub><b>Образцы.</b> Именованные цвета и триадный образец CMYK, разложенные как палитра.</sub></p></td>
</tr>
</table>

<a id="why-designcraft"></a>
## Почему DesignCraft

- **Привычно.** Привычные раскладка, инструменты, меню, панели и сочетания клавиш: развороты и родительские страницы,
  шаблонные страницы, текстовые рамки, связанный текст, стили абзацев и символов, таблицы, обтекание текстом и
  многое другое. Всё стоит там, где вы ожидаете.
- **Красивый набор.** Абзацный композитор Кнута–Пласса (и однострочный), словарные переносы
  (общедоступный список слов Moby плюс наши собственные обученные шаблоны), выключка по словам, буквам и масштабу знаков,
  удержания, оптическое выравнивание полей, колонки, сетка базовых линий, табуляции, линейки и заливка.
  Разрывы строк на экране и в PDF совпадают.
- **Быстро.** Многопоточный SIMD-рендеринг (vello_cpu), документы с копированием при записи и снимками отмены за O(1)
  и кэшированная вёрстка.
- **Открыто.** Документированный собственный формат, импорт и экспорт IDML, импорт INDD (через
  [indd-utils](https://github.com/storytold/indd-utils)), редактируемый экспорт .pptx и экспорт PNG, PDF
  (PDF/X-4, PDF/A-2b) и EPUB.

  Никакой подписки, никакого сервера лицензий, никакой телеметрии.
- **Для агентов.** Каждым пунктом меню, жестом инструмента, элементом панели и диалогом можно управлять по
  JSON-каналу управления и через **MCP-сервер**, так что Claude и другие агенты могут вёрстать и править
  документы как дизайнер. См. [`docs/control-protocol.md`](docs/control-protocol.md) и
  [`docs/mcp.md`](docs/mcp.md).
- **Везде.** Одна кодовая база на Rust для настольной программы и веба.

<a id="quick-start"></a>
## Быстрый старт

Оболочка на egui требует Rust 1.95 или новее (включая общие компоненты `craft-ui`).

```sh
cargo run --release -p designcraft                         # desktop app (start screen)
cargo run --release -p designcraft -- --sample             # open the sample magazine
cargo run --release -p designcraft -- --sample --control 7979   # + JSON control channel
cargo run --release -p designcraft-cli -- run --sample --all-pages out/       # headless: render every page to PNG
cargo run --release -p designcraft-cli -- commands         # list every command
cargo run --release -p designcraft-cli -- script --help    # command script syntax (docs/agents.md)
cargo xtask ci                                             # fmt, clippy, tests, assets, layering, wasm
```

Японский текст (интерфейс и документы) набирается шрифтами из
[storytold/craft-fonts](https://github.com/storytold/craft-fonts), необязательный вход сборки (файлы
шрифтов сюда никогда не коммитятся; см. открытое
[руководство по подключению craft-fonts](https://github.com/storytold/craft-fonts/blob/main/docs/integration.md)
с инструкциями по сборке):

```sh
git clone https://github.com/storytold/craft-fonts ../craft-fonts
CRAFT_FONTS_DIR="$PWD/../craft-fonts" cargo run --release -p designcraft   # absolute path
```

Без него японский падает на системные шрифты (в вебе их нет). Сборки выпуска всегда
его включают.

Чтобы управлять запущенной программой, отправляйте строки JSON на `127.0.0.1:7979`. Протокол описан в
[`docs/control-protocol.md`](docs/control-protocol.md).

<a id="logs"></a>
### Журнал

Настольная программа пишет записи `log` в стандартный поток ошибок и в `logs/designcraft.log` в каталоге
настроек, рядом с `ui.json` и `prefs.json` (Linux `~/.config/designcraft/logs/` или
`$XDG_CONFIG_HOME/designcraft/logs/`; macOS `~/Library/Application Support/DesignCraft/logs/`;
Windows `%APPDATA%\DesignCraft\logs\`). Запуск из меню рабочего стола или Dock не даёт
терминала, поэтому к сообщению об ошибке прикладывайте этот файл: найденные графические адаптеры и тот,
который рисует, почему программа остановилась (в том числе когда окно так и не открылось), отчёт паники охранника сбоев
и неудачное сохранение при восстановлении после сбоя попадают туда. Каждый запуск переносит предыдущий журнал в `designcraft.1.log`
(а тот — в `designcraft.2.log`), так что журнал аварийного запуска переживает следующий старт.
Файл перестаёт расти на 16 MiB. `--version` файл не пишет.

| Переменная | Действие |
|---|---|
| `RUST_LOG` | Уровни журнала для стандартного потока ошибок и файла журнала. По умолчанию: `info` для собственных крейтов DesignCraft, `warn` для всего остального. Директивы в стиле env_logger подменяют это, например `RUST_LOG=debug`, `RUST_LOG=warn,designcraft_render=trace` или `RUST_LOG=info,wgpu_core=warn`; директива, оканчивающаяся на `*`, покрывает все цели, которые с неё начинаются (`designcraft*=debug`). |
| `WGPU_BACKEND` | Графическая подсистема, которая компонует окно: `dx12`, `vulkan`, `gl` или `metal` (список через запятую позволяет wgpu выбрать из них). По умолчанию: DirectX 12 в Windows, Vulkan в Linux, Metal в macOS, с OpenGL как запасным вариантом. Если задать, также отключается запасной путь при запуске, описанный ниже. |
| `WGPU_POWER_PREF` | Тип GPU, который рисует окно: `low` (встроенный), `high` (дискретный) или `none` (порядок системы). По умолчанию: GPU, который ведёт основной дисплей, затем `low` в Windows и macOS и `none` в остальных случаях. |
| `WGPU_ADAPTER_NAME` | Графический адаптер по (части) имени, без учёта регистра (`nvidia`, `radv`, `intel`); имена перечислены в журнале. |
| `WGPU_VALIDATION_INDIRECT_CALL` | `1` снова включает проверку wgpu косвенных аргументов отрисовки. DesignCraft ничего не рисует косвенно и отключает её: нужный ей вычислительный шейдер не скомпилировался на Intel Mac и потерял графическое устройство (#334). |

Журналирование — в `apps/designcraft/src/logging.rs`; веб-сборка пишет в консоль браузера.

<a id="portable-mode"></a>
### Переносной режим

Файл с именем `portable.txt` рядом с исполняемым файлом (в macOS — рядом с `DesignCraft.app`) делает установку переносной: настройки, журналы и
восстановление после сбоя хранятся в папке `DesignCraftData` рядом с ним, а не в указанных выше папках пользователя.
Переносной zip для Windows поставляется с таким файлом; удалите его, чтобы вернуться к `%APPDATA%\DesignCraft`.
Если в `DesignCraftData` нельзя писать (копия распакована в Program Files), используются папки пользователя,
и журнал и строка состояния об этом говорят.
`DESIGNCRAFT_CONFIG_DIR` по-прежнему имеет приоритет. Код — в `apps/designcraft/src/profile.rs`.

<a id="graphics-backend-and-processor"></a>
### Графическая подсистема и процессор

Холст рисуется на ЦП; GPU только компонует интерфейс через wgpu, поэтому подойдёт любой
адаптер, который может показать окно. Код — в `apps/designcraft/src/gpu.rs` (адаптер)
и `apps/designcraft/src/gpu/backend.rs` (подсистема).

- **Подсистема.** Драйвер, который аварийно завершается, валит процесс до того, как какой-либо код Rust сможет
  это перехватить, поэтому каждый запуск создаёт экземпляр wgpu с одной подсистемой, выбранной до появления окна:
  в Windows DirectX 12, затем OpenGL, затем Vulkan, каждый по отдельности (создание экземпляра OpenGL
  падало внутри `atio6axx.dll` AMD, #167, а создание экземпляра Vulkan загружает каждый
  установленный драйвер Vulkan, и неисправный из них может уронить программу); в Linux Vulkan с OpenGL
  рядом, затем один OpenGL; в macOS Metal. Встречалось на практике: на ноутбуке AMD с гибридной графикой
  (Radeon RX 6800M рядом со встроенным Radeon) драйвер AMD Vulkan падал на первом
  показе кадра, поэтому в Windows по умолчанию стоит DirectX 12.
- **Запуск, который так и не показал кадр, запоминается:** `gpu.json` в каталоге настроек
  записывает подсистему, которую пробуют, пока не будет показан первый кадр. Оставшаяся запись
  значит, что эта подсистема упала (или программу убили) при старте, поэтому следующий запуск пробует следующую
  подсистему и говорит об этом в строке состояния. Список начинается сначала, когда не сработала ни одна подсистема, или
  с новой версией DesignCraft; удалите файл или задайте `WGPU_BACKEND`, чтобы начать заново.
- **Адаптер.** Среди адаптеров этих подсистем программа берёт тот, который рисует окно
  (`native_adapter_selector` eframe): адаптеры, которые сообщают, что не могут показывать в окно, никогда
  не пробуются; затем тот, который назван в `WGPU_ADAPTER_NAME`; аппаратные раньше программных (llvmpipe, WARP);
  родные подсистемы раньше OpenGL; GPU, который ведёт дисплей, и среди них тот, который
  ведёт основной дисплей; затем предпочтение по питанию; затем адаптер DirectX 12 данного GPU раньше его
  адаптера Vulkan. GPU без монитора — неверный выбор, даже если он может показывать: Windows приходится
  копировать каждый кадр на GPU, который его показывает, и драйвер встроенного GPU из-за этого сбрасывался,
  теряя графическое устройство или гася все мониторы на минуты. Windows сообщает, какой GPU ведёт
  какой дисплей (`EnumDisplayDevices`), Linux — через `/sys/class/drm` (встроенная панель `eDP`, `LVDS` или
  `DSI` считается основным дисплеем); в macOS или когда ничего не совпадает, решает предпочтение
  по питанию: энергосбережение в Windows и macOS, порядок системы в остальных случаях (Mesa ставит
  первым GPU, на котором работает рабочий стол, а композитор Wayland может отказаться от кадров с другого GPU).
  `WGPU_POWER_PREF` подменяет это выбором типа со стороны пользователя.
- **Если окно не запускается на своём адаптере при старте** (ошибка wgpu, например потерянное
  устройство, или паника внутри wgpu, egui-wgpu или naga в первых кадрах), программа стартует
  снова без этого адаптера и пробует следующий, сообщая какой в строке состояния; неудачный запуск
  сохраняет свой журнал как `designcraft.1.log`. Когда адаптеров у подсистем этого старта не осталось, она
  стартует снова со следующей подсистемой. Программные визуализаторы (WARP, llvmpipe) идут последними: их
  пропускают, пока есть другая подсистема, которую можно попробовать, и допускают, когда ни один графический процессор не смог
  показать окно. В Unix новая программа подменяет процесс (AppImage остаётся смонтированным); в
  Windows она стартует рядом. Адаптеры различают по подсистеме и PCI-идентификаторам или по имени, если
  подсистема идентификаторов не сообщает (Metal перечисляет каждый GPU двухпроцессорного Mac как `0000:0000`). То, что отбросили,
  передаётся в аргументе `--gpu-skip=` перезапущенной программы (`Vulkan:1002:164e`, `Metal:Intel
  Iris Pro Graphics` или целая подсистема, например `Dx12`), на каждом перезапуске на один больше, поэтому
  перезапуски заканчиваются. Когда ничего не осталось, программа записывает в журнал, почему, и выходит с ошибкой. Документы,
  восстановленные после сбоя, остаются в папке восстановления, пока их не сохранят или не закроют, поэтому перезапуск
  их не теряет.
- **Если первый кадр окна запаздывает** (20 секунд после создания программы и открытия файлов,
  названных при старте), журнал и строка состояния об этом говорят. Адаптер считается зависшим,
  и программа стартует снова без него, только если поток интерфейса застрял в графическом
  стеке, вне собственного кода DesignCraft, на 60 секунд, а окно не было известно как
  свёрнутое, перекрытое или в фоне. Большой документ, который верстается на медленной машине, никогда
  не считается.
- **Журнал** перечисляет GPU, которые ведут дисплей (`display GPUs (PCI vendor:device): 10de:2204
  (primary)`), каждый адаптер и ведёт ли он дисплей, тот, на котором рисуют, и почему (`drawing
  on NVIDIA GeForce RTX 3090 (Dx12, DiscreteGpu): it drives the primary display`), и версию
  драйвера. Это первое, что искать в сообщении об окне, которое остаётся чёрным или не
  открывается.
- В Linux с Mesa `MESA_VK_DEVICE_SELECT=10de:2f04!` (vendor:device так, как показывают `vulkaninfo --summary`
  или `lspci -nn`) оставляет Vulkan только этот GPU, а `DRI_PRIME=1` выбирает другой GPU.

<a id="web"></a>
### Веб

```sh
cd apps/designcraft-web && trunk build --release          # → dist/web (serve it with any static server)
cd apps/designcraft-web && trunk serve --release          # http://127.0.0.1:8767
```

Нужны [trunk](https://trunkrs.dev) и цель `wasm32-unknown-unknown`. Та же программа работает
через веб-запускатель eframe на WebGPU с запасным путём WebGL2 (`?webgl` принуждает его; `?sample` открывает
образцовый журнал). «Открыть» и «Поместить» вызывают выбор файла браузера, перетаскивание тоже работает.
«Сохранить» и «Экспорт» скачивают файл. У веб-сборки нет канала управления.

<a id="architecture"></a>
## Архитектура

DesignCraft — это Cargo workspace с движком в основе и принудительной слоистостью (`cargo xtask layers`).
Оболочка на egui — отдельный крейт, поэтому интерфейс можно заменить, не трогая движок.

| Слой | Крейты |
|---|---|
| L0 | `geom` (контуры, единицы и разбор измерений, параметры углов) · `color` (CMYK/RGB/Lab, образцы, тинты, градиенты) |
| L1 | `doc` (развороты, страницы, родители, слои, рамки, материалы, стили) · `fonts` (база шрифтов, форма набора, контуры) |
| L2 | `compose` (текстовый движок) · `images` |
| L3 | `render` (vello_cpu) · `pdf` · `idml` · `epub` · `pptx` · `textimport` · `format` |
| L4 | `tools` (события указателя → команды + наложения) |
| L5 | `engine` (сеанс, история, реестр команд) |
| L6 | `ui-egui` (издательский интерфейс, канал управления) · `mcp` |
| L7 | `apps/designcraft`, `apps/designcraft-cli`, `apps/designcraft-web` |

- **Состояние и вехи:** [ROADMAP.md](ROADMAP.md) (этап: пре-альфа); оценка возможностей: [`docs/target-app-parity.md`](docs/target-app-parity.md); известные пробелы: [`docs/gaps.md`](docs/gaps.md)
- **Правила для участников и агентов** (чистая комната, политика ресурсов, качественные проверки): [`AGENTS.md`](AGENTS.md)
- **Встроенные ресурсы:** каждый указан с лицензией в [`ASSETS.md`](ASSETS.md)
- **Значок и цвет программы:** трёхцветная кошка в шарфе в горошек на зелёном DesignCraft `#7bb51c`; см. [`assets/app-icon/`](assets/app-icon/README.md)

<a id="downloads"></a>
## Загрузки

**Впервые в DesignCraft?** Скачайте программу со [страницы DesignCraft на getartcraft.com](https://getartcraft.com/apps/designcraft). Так установить проще всего.

**Нужна конкретная сборка или формат?** На GitHub в [последнем выпуске](https://github.com/storytold/designcraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/designcraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `designcraft-<ver>-windows-x64.msi` | `designcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `designcraft-<ver>-windows-arm64.msi` | `designcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `designcraft-<ver>-windows-x86.msi` | `designcraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы подписаны.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа и встроенный CLI, универсальные (Apple silicon + Intel) | `designcraft-<ver>-macos-universal.dmg` | Подписаны и нотариально заверены |
| Инструмент командной строки, универсальный | `designcraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `designcraft-<ver>-linux-x86_64.AppImage` | `designcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `designcraft-<ver>-linux-x86_64.flatpak` | `designcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `designcraft-<ver>-linux-x86_64.deb` | `designcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `designcraft-<ver>-linux-x86_64.rpm` | `designcraft-<ver>-linux-aarch64.rpm` | |
| Arch Linux/Manjaro | `designcraft-<ver>-linux-x86_64.pkg.tar.zst` | `designcraft-<ver>-linux-aarch64.pkg.tar.zst` | `sudo pacman -U <file>`; ставится как `ai.storyteller.designcraft`, заменяя пакет из AUR |
| Архив | `designcraft-<ver>-linux-x86_64.tar.gz` | `designcraft-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

RISC-V (riscv64): только `designcraft-<ver>-linux-riscv64.tar.gz`, кросс-компиляция; нужен glibc 2.39+ (Ubuntu 24.04 или новее).

<a id="community-packages"></a>
#### Пакеты сообщества

Эти пакеты сопровождают участники сообщества, а не команда DesignCraft.

В Gentoo оверлей [::snakebyte overlay](https://github.com/switch87/snakebyte-overlay) упаковывает
выпуск для Linux как `media-gfx/designcraft-bin` (готовая сборка) и `media-gfx/designcraft` (сборка из исходников):

```sh
eselect repository add snakebyte git https://github.com/switch87/snakebyte-overlay.git
emaint sync -r snakebyte
echo 'media-gfx/designcraft-bin ~amd64' >> /etc/portage/package.accept_keywords/designcraft
emerge --ask media-gfx/designcraft-bin
```

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `designcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `designcraft-web-<ver>.zip` | Работает в современном браузере; разместите на любом статическом сервере |
<a id="the-crafting-apps"></a>
## The Crafting Apps

DesignCraft — одно из приложений **Crafting Apps**: бесплатных творческих инструментов с открытым исходным кодом от команды
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
  <a href="https://getartcraft.com/apps/designcraft">DesignCraft</a>
</p>

<a id="license-and-credits"></a>
## Лицензия и благодарности

DesignCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the DesignCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ASSETS.md](ASSETS.md).

Встроенные шрифты и шрифты craft-fonts, которые встраивают сборки выпуска, распространяются на условиях SIL Open
Font License; все значки интерфейса нарисованы в коде и оригинальны.

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и DesignCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<br>

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
