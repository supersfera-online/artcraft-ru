# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/materialcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/materialcraft
Коммит исходника (последний, в котором менялся README.md): 827ba9259a89a9d62401f32f255c6b8d86ef0d94
Дата коммита: 18 ноября 2026, 15:54 (America/Los_Angeles, PT); в исходнике 2026-11-18T23:54:45Z
SHA256 исходника: 6837e654bfc4ef0825e01685f53161d6bcf65d26353291009e6e93213b31d376
Git blob SHA: fd9a7629967a215967e27949696b0130ecb048a4
Размер исходника: 20479 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/materialcraft/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.materialcraft.png" width="128" height="128" alt="Значок MaterialCraft: гравированный носорог на бирюзовой плитке">
</p>

<h1 align="center">MaterialCraft</h1>

<p align="center">
  <b>Процедурные материалы: открытый конструктор материалов на графе узлов, написанный на чистом Rust.</b>
</p>

<p align="center">
  Собирайте процедурные материалы из примитивов и функций в графе узлов, смотрите, как они
  обновляются вживую в 2D и на 3D-модели, и экспортируйте карты для любого движка. Программа работает нативно на
  macOS, Windows, Linux и FreeBSD и в браузере через WebAssembly. Сделана командой ArtCraft.
</p>

<p align="center">
  <img alt="Status: in active development" src="https://img.shields.io/badge/status-in%20active%20development-178a9c?style=flat-square">
  <img alt="Written in pure Rust" src="https://img.shields.io/badge/pure-Rust-b83a24?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows, Linux, FreeBSD and the web" src="https://img.shields.io/badge/runs%20on-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-555555?style=flat-square">
  <img alt="MCP server for agents" src="https://img.shields.io/badge/agents-MCP%20server-555555?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-555555?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_materialcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/materialcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/materialcraft"><b>MaterialCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/materialcraft-workspace.png" alt="Рабочая среда MaterialCraft: обозреватель и библиотека узлов слева; материал кирпичной стены как граф узлов с живыми миниатюрами в середине, поверх 3D-вида скруглённого куба из красного кирпича и 2D-вида базового цвета; справа параметры генератора кирпича" width="100%">
  <br><sub><b>Рабочая среда</b>: обозреватель, библиотека, граф узлов, 3D-вид, 2D-вид и свойства</sub>
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Живописцы, скульпторы, художники
> игр, художники материалов и текстур, фотографы, кинематографисты, иллюстраторы, дизайнеры,
> любители и те, кто взял перо в руки только на прошлой неделе. Если вы что-то создаёте, вам здесь место.
> **[Заходите поздороваться в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#a-look-around">Взгляд вокруг</a> ·
  <a href="#made-in-materialcraft">Сделано в MaterialCraft</a> ·
  <a href="#why-materialcraft">Почему MaterialCraft</a> ·
  <a href="#quick-start">Быстрый старт</a> ·
  <a href="#status">Состояние</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">Лицензия</a>
</p>

<a id="a-look-around"></a>
## Взгляд вокруг

Эти снимки показывают прежнюю процедурную библиотеку. Текущая сборка использует каталог примитивов,
описанный в [рабочем процессе с примитивами](docs/atomic-workflow.md).

<table>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/materialcraft-wood.png" alt="Граф деревянных досок: анизотропный шум, искажённый шумом Перлина и умноженный на узор досок, на скруглённом кубе и в 2D-виде" width="100%">
  <p align="center"><sub><b>Деревянные доски</b>: анизотропная текстура, искажённая и уложенная досками</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/materialcraft-lava.png" alt="Граф лавовой породы: пластины Вороного с трещинами и светящимися швами, тёмная порода с оранжевыми излучающими трещинами на скруглённом кубе" width="100%">
  <p align="center"><sub><b>Лавовая порода</b>: потрескавшиеся пластины над светящимися излучающими швами</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/materialcraft-new-graph.png" alt="Диалог «Создать граф»: шары шаблонов для пустого, PBR, кирпичной стены, каменной плитки, деревянных досок, крашеных металлических пластин, ржавого металла, лавовой породы, полированного мрамора, плетёного лозового, тканого полотна и замшелой земли, с именем и размером графа" width="100%">
  <p align="center"><sub><b>Создать граф</b>: начните с шаблона PBR или образца материала</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/materialcraft-ground.png" alt="Граф замшелой земли: камни, смешанные по высоте с землёй, и мох в щелях, на скруглённом кубе и в 2D-виде" width="100%">
  <p align="center"><sub><b>Замшелая земля</b>: камни и земля, смешанные по высоте, мох в промежутках</sub></p>
</td>
</tr>
</table>

<a id="made-in-materialcraft"></a>
## Сделано в MaterialCraft

Эти исторические отрисовки использовали прежнюю библиотеку на Rust и больше не входят в комплект как шаблоны.
Они собраны из
её собственных процедурных узлов (без фотографий, сканов и текстур откуда-либо ещё) и отрисованы командой
`materialcraft-cli render --scene sphere --full --hq` (выход высоты смещает сетку, с
трассированным Ambient Occlusion и ключевым светом с тенями).

<p align="center">
  <img src="docs/images/materialcraft-materials.png" alt="Восемь сфер материалов: красный кирпич, лавовая порода со светящимися трещинами, синие крашеные металлические пластины с заклёпками, деревянные доски, плетёный лозовый, замшелая земля, потрескавшаяся каменная плитка и полированный белый мрамор" width="100%">
</p>
<p align="center"><sub>Кирпичная стена · Лавовая порода · Крашеные металлические пластины · Деревянные доски<br>Плетёный лозовый · Замшелая земля · Каменная плитка · Полированный мрамор</sub></p>

<a id="why-materialcraft"></a>
## Почему MaterialCraft

- **Привычно.** Компоновка, панели, меню и жесты, которые художники материалов уже знают: обозреватель
  пакетов, библиотека узлов с просмотром, граф узлов с живыми миниатюрами, 3D-вид, 2D-вид
  и панель свойств с базовыми и особыми параметрами («Уровни» правятся поверх
  гистограммы своего входа, см. [docs/levels-editor.md](docs/levels-editor.md)). Пробел открывает
  поиск узлов.
- **Быстро.** Каждый узел готовится на всех ядрах процессора, а кэш по адресу содержимого значит, что правка
  пересчитывает только то, что лежит ниже по потоку.
  Подготовка идёт на рабочем потоке, поэтому интерфейс никогда не ждёт.
- **Бесшовно по замыслу.** Шумы и узоры живут на целочисленных решётках, поэтому всё стыкуется
  без швов при любом разрешении, от 16 пикселей до 8K.
- **Надёжно.** В выпускном коде нет паник, каждая команда проверена враждебным вводом, каждый узел приготовлен
  в тестах на странных входах, отмена из снимков состояния и собственные файлы проектов SBS. Сохраняйте `.sbs` с
  соседней папкой `resources/` или самодостаточный ZIP `.mcraft` с `package.sbs` и `resources/`.
- **Открыто.** Экспортируйте базовый цвет, нормаль, шероховатость, металличность, высоту и Ambient Occlusion как PNG,
  JPEG, TGA, BMP, WEBP, EXR или HDR с 8, 16 или 32 битами, по своему шаблону имени файла.
- **Работает с TextureCraft.** **Файл ▸ Отправить в TextureCraft** помещает материал на полку TextureCraft
  как переносимый `.mcmat`; нанесённый там на сетку, входы его графа остаются живыми ползунками и
  цветами, их заново готовит MaterialCraft в разрешении набора текстур, а запечённые карты сетки
  питают входные узлы графа.
- **Для агентов изначально.** Каждый пункт меню и каждая правка — команда, которой можно управлять из CLI, по каналу
  управления JSON (включая синтетический ввод мыши и клавиатуры) или через **MCP-сервер**, так что Claude
  и другие агенты могут собирать материалы так же, как человек.
- **Везде.** Одна кодовая база для настольных программ и тот же интерфейс в браузере.

<a id="quick-start"></a>
## Быстрый старт

```sh
git clone https://github.com/storytold/materialcraft
cd materialcraft

cargo run --release -p materialcraft                          # desktop app
cargo run --release -p materialcraft -- package.sbs           # open an SBS package
cargo run --release -p materialcraft -- --control 7878        # + JSON control channel
cargo run --release -p materialcraft-cli -- mcp               # MCP server (stdio)
cargo run --release -p materialcraft-cli -- new pbr surface.sbs --name Surface
cargo run --release -p materialcraft-cli -- render surface.sbs surface.png --scene sphere --full --hq
cargo run --release -p materialcraft-cli -- export surface.sbs textures --format png --depth 16
cargo run --release -p materialcraft-cli -- export my.sbs out --set wear=0.7    # with a graph input "wear" set first
cargo run --release -p materialcraft-cli -- publish surface.sbs surface.mcmat --graph Surface
cargo run --release -p materialcraft-cli -- export surface.mcmat build/surface --profile materialx --size 512
cd apps/materialcraft-web && trunk serve                      # web build
cargo xtask ci                                                # fmt, clippy, tests, layering, wasm
```

Нужен Rust 1.95 или новее. Программа открывается с пустым графом в новом пакете; **Файл ▸ Создать ▸ Граф...**
начинает с шаблона PBR или одного из образцов материалов.

<a id="use-it-from-claude-code-and-other-agents"></a>
### Использовать из Claude Code и других агентов

Зарегистрируйте MCP-сервер в Claude Code, указав папки, которые ему можно читать и писать:

```sh
claude mcp add materialcraft -- /path/to/materialcraft-cli mcp --read-root /work/materials --write-root /work/materials
```

Чтобы вести уже запущенную программу, стартуйте её с `--control 7878` и соедините мостом:

```sh
claude mcp add materialcraft-app -- /path/to/materialcraft-cli mcp --bridge 7878
```

Подробности — в [`docs/control-protocol.md`](docs/control-protocol.md).

<a id="status"></a>
## Состояние

MaterialCraft активно разрабатывается. В [**ROADMAP.md**](ROADMAP.md) — оценка паритета по
областям, оставшаяся работа и что дальше.

**Сейчас в фокусе (2026-11-16):** поведение узлов, покрытие регрессий и сохранение/загрузка SBS. Старая процедурная
библиотека на Rust удалена. На замену — 29 записей основного графа, 85 функциональных
операций и четыре вида узлов узора. Начните с **Файл → Создать → Atomic sample**.

См. [рабочий процесс с примитивами](docs/atomic-workflow.md) — использование, область проверки и ограничения.
[Состояние каталога](docs/node-catalog-parity.md) фиксирует реализованное поведение и оставшуюся работу.
Полная численная совместимость и произвольная взаимозаменяемость SBS пока не установлены.

**Состав репозитория:** `crates/{core, geom, nodes, eval, formats, engine, render, automation, ui-egui}`
и `apps/{materialcraft, materialcraft-cli, materialcraft-web}`. Интерфейс на egui — отдельный
crate, так что интерфейс можно заменить, не трогая движок; в [`docs/architecture.md`](docs/architecture.md)
объяснено, как это складывается.

Правила для агентов и участников (чистая комната, политика ресурсов, никаких паник в выпускном коде, ворота качества)
— в [`AGENTS.md`](AGENTS.md). Каждый входящий в комплект ресурс указан со своей лицензией в
[`ATTRIBUTION.md`](ATTRIBUTION.md).

<a id="downloads"></a>
## Загрузки

**Впервые в MaterialCraft?** Скачайте программу со [страницы MaterialCraft на getartcraft.com](https://getartcraft.com/apps/materialcraft). Так её проще всего установить.

**Нужна конкретная сборка или формат?** На GitHub в [последнем релизе](https://github.com/storytold/materialcraft/releases/latest) перечислены все сборки ниже, а в [списке всех релизов](https://github.com/storytold/materialcraft/releases) — предыдущие версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму для каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная версия |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `materialcraft-<ver>-windows-x64.msi` | `materialcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `materialcraft-<ver>-windows-arm64.msi` | `materialcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `materialcraft-<ver>-windows-x86.msi` | `materialcraft-<ver>-windows-x86-portable.zip` |

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `materialcraft-<ver>-macos-universal.dmg` | Подписана и нотаризована |
| Инструмент командной строки, универсальный | `materialcraft-cli-<ver>-macos-universal.zip` | Подписан и нотаризован |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `materialcraft-<ver>-linux-x86_64.AppImage` | `materialcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `materialcraft-<ver>-linux-x86_64.flatpak` | `materialcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `materialcraft-<ver>-linux-x86_64.deb` | `materialcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `materialcraft-<ver>-linux-x86_64.rpm` | `materialcraft-<ver>-linux-aarch64.rpm` | |
| Tarball | `materialcraft-<ver>-linux-x86_64.tar.gz` | `materialcraft-<ver>-linux-aarch64.tar.gz` | Распаковать куда угодно |

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `materialcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `materialcraft-web-<ver>.zip` | Работает в современном браузере; размещается на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

MaterialCraft — одно из приложений **Crafting Apps**: бесплатных творческих инструментов с открытым исходным кодом от команды
[ArtCraft](https://getartcraft.com/), каждое написано с нуля на Rust и каждое может работать само по себе.

| | Приложение | Для чего | Код | Подробнее |
|:-:|---|---|---|---|
| <img src="https://raw.githubusercontent.com/storytold/photocraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.photocraft.png" alt="" width="32" height="32"> | **PhotoCraft** | Редактирование изображений: слои, маски, текст и настоящие файлы PSD | [GitHub](https://github.com/storytold/photocraft) | [Сайт](https://getartcraft.com/apps/photocraft) |
| <img src="https://raw.githubusercontent.com/storytold/vectorcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.vectorcraft.png" alt="" width="32" height="32"> | **VectorCraft** | Векторная иллюстрация | [GitHub](https://github.com/storytold/vectorcraft) | [Сайт](https://getartcraft.com/apps/vectorcraft) |
| <img src="https://raw.githubusercontent.com/storytold/texturecraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.texturecraft.png" alt="" width="32" height="32"> | **TextureCraft** | Рисование 3D-текстур | [GitHub](https://github.com/storytold/texturecraft) | [Сайт](https://getartcraft.com/apps/texturecraft) |
| <img src="https://raw.githubusercontent.com/storytold/materialcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.materialcraft.png" alt="" width="32" height="32"> | **MaterialCraft** | **Процедурные материалы на графах узлов · вы здесь** | [GitHub](https://github.com/storytold/materialcraft) | [Сайт](https://getartcraft.com/apps/materialcraft) |
| <img src="https://raw.githubusercontent.com/storytold/filmcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.filmcraft.png" alt="" width="32" height="32"> | **FilmCraft** | Монтаж видео, цвет и звук | [GitHub](https://github.com/storytold/filmcraft) | [Сайт](https://getartcraft.com/apps/filmcraft) |
| <img src="https://raw.githubusercontent.com/storytold/lightcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.lightcraft.png" alt="" width="32" height="32"> | **LightCraft** | Библиотека фотографий и проявление raw | [GitHub](https://github.com/storytold/lightcraft) | [Сайт](https://getartcraft.com/apps/lightcraft) |
| <img src="https://raw.githubusercontent.com/storytold/pdfcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.pdfcraft.png" alt="" width="32" height="32"> | **PdfCraft** | Чтение, организация и защита PDF | [GitHub](https://github.com/storytold/pdfcraft) | [Сайт](https://getartcraft.com/apps/pdfcraft) |
| <img src="https://raw.githubusercontent.com/storytold/effectcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.effectcraft.png" alt="" width="32" height="32"> | **EffectCraft** | Моушн-графика и визуальные эффекты | [GitHub](https://github.com/storytold/effectcraft) | [Сайт](https://getartcraft.com/apps/effectcraft) |
| <img src="https://raw.githubusercontent.com/storytold/designcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.designcraft.png" alt="" width="32" height="32"> | **DesignCraft** | Вёрстка и публикация | [GitHub](https://github.com/storytold/designcraft) | [Сайт](https://getartcraft.com/apps/designcraft) |
| <img src="https://raw.githubusercontent.com/storytold/gridcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.gridcraft.png" alt="" width="32" height="32"> | **GridCraft** | Электронные таблицы и данные | [GitHub](https://github.com/storytold/gridcraft) | [Сайт](https://getartcraft.com/apps/gridcraft) |

И сам [**ArtCraft**](https://getartcraft.com/) — наша ИИ-студия изображений и видео для художников, которым нужен настоящий контроль.

<br>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<h3 align="center">Приходите творить с нами</h3>

<p align="center">
  Наш Discord — место, где собираются художники всех направлений: те, кто пишет красками, лепит, моделирует, собирает
  материалы, снимает, рисует, монтирует кино, набирает текст, и те, кто ещё ищет, что им нравится делать.
  Покажите, над чем работаете, попросите помощи, расскажите, что сломалось, или чего вы ждёте от этих
  инструментов. В каком бы материале вы ни работали и сколько бы вы этим ни занимались, вам здесь рады.
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><b>discord.gg/artcraft</b></a> ·
  <a href="https://getartcraft.com/">getartcraft.com</a> ·
  <a href="https://getartcraft.com/apps">The Crafting Apps</a> ·
  <a href="https://getartcraft.com/apps/materialcraft">MaterialCraft</a>
</p>

<a id="star-history"></a>
## История звёзд

[![Star History Chart](https://api.star-history.com/svg?repos=storytold/materialcraft&type=Date&legend=top-left)](https://www.star-history.com/?repos=storytold%2Fmaterialcraft&type=date&legend=top-left)

<a id="license-and-credits"></a>
## Лицензия и благодарности

MaterialCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the MaterialCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан с
автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Каждый показанный материал, шум, узор, окружение, образец библиотеки и сетка порождены
процедурно самим MaterialCraft; в снимках нет сторонних текстур, сканов или моделей. MaterialCraft — независимая реализация рабочего процесса процедурных материалов на графе узлов по принципу чистой комнаты
и не связан ни с одним другим поставщиком программ.

Значок программы (гравированный носорог на бирюзовом цвете MaterialCraft `#178a9c`) — оригинальная работа, сделанная для этого
проекта его владельцем; файлы и заметки — в [`assets/app-icon/`](assets/app-icon/).

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и MaterialCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
