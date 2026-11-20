# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/cadcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/cadcraft
Коммит исходника (последний, в котором менялся README.md): 2c8b8f438cd5f59f11a9e41da740ab4ec8daaa52
Дата коммита: 20 ноября 2026, 07:18 (America/Los_Angeles, PT); в исходнике 2026-11-20T15:18:35Z
SHA256 исходника: a2e868c053bf36fd55365c903d7743aafa961818f4f251fe834e5df01c193d11
Git blob SHA: 7947339c0b6fdb3b75005a314fea81cfa827c2db
Размер исходника: 34782 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/cadcraft/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.cadcraft.png" width="128" height="128" alt="Значок CADCraft: чертёжный угольник и дуга циркуля на синей клетчатой плитке">
</p>

<h1 align="center">CADCraft</h1>

<p align="center">
  <b>Автоматизированное проектирование и черчение; современная двумерная и трёхмерная САПР с открытым исходным кодом, построенная на чистом Rust.</b>
</p>

<p align="center">
  Быстрый рабочий процесс САПР с открытым исходным кодом: командная строка, объектные привязки, слои,
  размеры, штриховки, блоки и чертежи DXF, которые вы уже знаете. Работает нативно в macOS,
  Windows, Linux и FreeBSD и в браузере через WebAssembly.<br>
  <i>Команда ArtCraft.</i>
</p>

<p align="center">
  <img alt="Written in Rust" src="https://img.shields.io/badge/written%20in-Rust-0b6f88?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows, Linux, FreeBSD and the web" src="https://img.shields.io/badge/runs%20on-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20BSD%20%C2%B7%20Web-14a3c7?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-0b6f88?style=flat-square">
  <img alt="Agent-drivable over MCP" src="https://img.shields.io/badge/agents-MCP-14a3c7?style=flat-square">
  <img alt="Status: early development" src="https://img.shields.io/badge/status-early%20development-f07a3a?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_cadcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/cadcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/cadcraft"><b>CADCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/ui-apartment.png" alt="CADCraft с открытым планом квартиры: заштрихованные серые стены, синие окна, зелёные дуги дверей, контуры мебели, жёлтые имена комнат с площадями, жёлтая таблица ведомости помещений, выноска с несколькими лидерами и голубые размеры с архитектурными засечками; слева наборы инструментов, справа слои и свойства, внизу командная строка" width="100%">
  <br><sub><b>План квартиры</b> (<a href="examples/apartment.dxf">examples/apartment.dxf</a>): стены со штриховкой по точке выбора, подписи комнат TrueType MTEXT, TABLE, выноска и архитектурные размеры — собрано целиком командами CADCraft.</sub>
</p>

> [!NOTE]
> **ArtCraft — это сообщество художников из самых разных сфер.** Живописцы, фотографы,
> кинематографисты, иллюстраторы, дизайнеры, аниматоры, любители и те, кто взял карандаш
> на прошлой неделе. Если вы что-то создаёте, вы один из нас. **[Заходите поздороваться в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#screenshots">Снимки экрана</a> ·
  <a href="#why-cadcraft">Зачем CADCraft</a> ·
  <a href="#what-works-today">Что уже работает</a> ·
  <a href="#quick-start">Быстрый старт</a> ·
  <a href="#drive-it-from-agents-mcp-and-the-cli">Агенты, MCP и CLI</a> ·
  <a href="#architecture">Архитектура</a> ·
  <a href="#roadmap">План</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">Лицензия и благодарности</a>
</p>

<a id="screenshots"></a>
## Снимки экрана

<table>
  <tr>
    <td width="50%"><img src="docs/images/ui-layout.png" alt="Лист пространства листа в CADCraft: белый лист с пунктирной печатаемой областью и видовым экраном, показывающим план квартиры в масштабе; в строке состояния вкладка листа A1 Plan и переключатель PAPER"></td>
    <td width="50%"><img src="docs/images/ui-bracket.png" alt="CADCraft с чертежом кронштейна: вид спереди с отверстиями под болты, осевыми линиями и размерами, заштрихованный разрез, примечания и основная надпись"></td>
  </tr>
  <tr>
    <td><sub><b>Листы</b>: пространство листа с видовыми экранами, наборами параметров страницы и PLOT в PDF. Дважды щёлкните видовой экран, чтобы работать в пространстве модели через него.</sub></td>
    <td><sub><b>Кронштейн</b>: чертёж детали в двух видах с осевыми линиями, скрытыми линиями, штриховкой разреза ANSI31 и основной надписью.</sub></td>
  </tr>
</table>

<a id="why-cadcraft"></a>
## Зачем CADCraft

- **Знакомый рабочий процесс.** Введите `L`, щёлкните две точки, введите `@5<45`, нажмите Enter. Командная
  строка, подсказки со щелкабельными `[Keywords]`, AutoComplete, объектные привязки, полярное отслеживание, ортогональность,
  прямой ввод расстояния, рамка и секущая рамка выбора, ручки и повтор правой кнопкой ведут себя
  так, как десятилетия чертёжной привычки того ожидают.
- **Открытые файлы.** DXF читается и пишется нативно (ASCII и двоичный, R12–2018), а файлы DWG
  (R13–2018) открываются и сохраняются через библиотеку acadrust с открытым исходным кодом. Выгрузка в SVG
  и PNG уже есть.
- **Быстро и нативно.** Чистый Rust и egui, без Electron и без веб-представления. Один двоичный файл в macOS
  (универсальный), Windows, Linux и FreeBSD плюс сборка WebAssembly для браузера.
- **Для агентов.** Каждый пункт меню, инструмент и подсказка — это команда. Агенты могут вводить в
  командную строку точно как человек, вызывать любую команду с JSON, проверять чертёж, чтобы удостовериться
  в работе, и визуализировать его — через MCP, канал управления JSON или CLI.
- **Бесплатно.** MIT OR Apache-2.0, без учётной записи и без подписки.

<a id="what-works-today"></a>
## Что уже работает

CADCraft находится в ранней, быстрой разработке. Честное состояние (числа сопоставимости — в [ROADMAP.md](ROADMAP.md)):

| Область | Состояние |
|---|---|
| Область черчения | Пространство модели с адаптивной сеткой, осями, панорамой/масштабом (колесо, среднее перетаскивание, щипок), курсор-перекрестье с прицелом, значок ПСК, ViewCube, подпись видового экрана |
| Командная строка | Подсказки с ключевыми словами, история, AutoComplete, псевдонимы, `@dx,dy`, `@d<a`, `#x,y`, прямой ввод расстояния, Enter/пробел/правый щелчок для повтора, прозрачные команды, сценарии в стиле `.scr` |
| Черчение | LINE, PLINE (дуги, ширины), CIRCLE (центр/радиус/диаметр, 2P, 3P), ARC, RECTANG (сопряжение/фаска), POLYGON, ELLIPSE (+дуги), SPLINE, POINT, XLINE, RAY, DONUT, TEXT, MTEXT |
| Изменение | ERASE, MOVE, COPY, ROTATE, SCALE, MIRROR, STRETCH, OFFSET, TRIM, EXTEND, FILLET, CHAMFER, BREAK, JOIN, EXPLODE, прямоугольный/круговой ARRAY, порядок прорисовки, OVERKILL |
| Точность | Объектные привязки (конечная, середина, центр, геометрический центр, узел, квадрант, пересечение, точка вставки, перпендикуляр, касательная, ближайшая; отложенные касательная/перпендикуляр для первой точки линии, например линии ремня, касательные к двум окружностям), полярное отслеживание, ортогональность, привязка к сетке |
| Слои и свойства | Палитра слоёв и диспетчер свойств слоёв (вкл/выкл, заморозка, блокировка, печать, цвет, тип линии), инструменты слоёв (изолировать, заморозить, выключить, заблокировать, сопоставить, предыдущий), палитра свойств с правкой по объекту, типы линий, веса линий, цветовой индекс и истинный цвет |
| Оформление | Все команды DIM* с полными переменными DIMSTYLE, переопределениями и каждым наконечником, ассоциативные размеры, которые следуют за геометрией, MLEADER, TABLE, шрифты TrueType (коллекции `.ttf`, `.otf`, `.ttc`), коды форматирования MTEXT (шрифты, высоты, цвета, многоэтажные дроби), собственный одноштриховой чертёжный шрифт |
| Штриховка и блоки | Границы штриховки по точке выбора с островами, заливки по образцу, сплошные и градиентные из собственной библиотеки образцов, BLOCK/INSERT, атрибуты и вложенные блоки |
| Файлы | Чтение DXF (R12–2018, ASCII и двоичный) и запись (R2000), включая размерные стили, ассоциативность, таблицы и ограничения; чтение DWG (через библиотеку acadrust) и запись (R2000); печать в PDF, выгрузка SVG и PNG. Объекты, которые CADCraft ещё не моделирует, при сохранении не сохраняются: см. [сопоставимость форматов файлов](docs/file-format-parity.md) |
| Листы и печать | Листы пространства листа, видовые экраны (масштаб, блокировка, заморозка слоёв на видовом экране), MSPACE/PSPACE через видовые экраны, наборы параметров страницы, PLOT и EXPORTPDF |
| Параметрика | Геометрические и размерные ограничения, AUTOCONSTRAIN, PARAMETERS с выражениями, обнаружение конфликтов; ограничения пересчитываются после каждой правки |
| Ручки | Горячие ручки, Space перебирает Stretch, Move, Rotate, Scale и Mirror |
| Языки интерфейса | английский, украинский (Українська), бразильский португальский (Português (Brasil)), немецкий (Deutsch), испанский (Español), чешский (Čeština), русский (Русский), французский (Français), упрощённый китайский (简体中文, при установленном шрифте CJK), итальянский (Italiano), корейский (한국어, при установленном шрифте хангыль), шведский (Svenska), арабский (العربية, при установленном арабском шрифте), венгерский (Magyar), турецкий (Türkçe), греческий (Ελληνικά), боснийский (Bosanski) и грузинский (ქართული), переключение сразу и запоминаемый выбор «Авто»/язык системы; [подробности](docs/localization.md) |
| Автоматизация | Сервер MCP, канал управления JSON, `cadcraft-cli` (info, convert, run, commands, mcp) |

<a id="quick-start"></a>
## Быстрый старт

CADCraft требует Rust 1.95 или новее.

```sh
git clone https://github.com/storytold/cadcraft
cd cadcraft
cargo run --release -p cadcraft -- --sample       # opens the sample drawing
```

Затем попробуйте ввести в командную строку:

```text
line 0,0 @10,0 @0,5 c          a closed triangle
circle 5,2 1                    a circle
offset 0.25                     then pick the circle and a side
zoom e                          zoom to extents
```

Веб-сборка: `cd apps/cadcraft-web && trunk serve` (нужен [trunk](https://github.com/trunk-rs/trunk)).

<a id="fonts"></a>
### Шрифты

В репозитории CADCraft шрифтов нет; он использует шрифты TrueType/OpenType, установленные в вашей
системе. Сборки с необязательным вводом [craft-fonts](https://github.com/storytold/craft-fonts)
(`CRAFT_FONTS_DIR=<absolute path to a checkout> cargo build --release`) также встраивают его
шрифты: BIZ UDPGothic, BIZ UDMincho и Shippori Mincho (японские) и Noto Sans Arabic (веб-сборка,
у которой нет системных шрифтов, только BIZ UDPGothic Regular и Noto Sans Arabic). Стиль текста
может использовать их по имени семейства, и они рисуют знаки, которых нет в шрифте текста, когда ни один установленный
широкоохватный шрифт CJK их не содержит. Без `CRAFT_FONTS_DIR` ничего не встраивается. Шрифты SHX
(включая большие шрифты вроде `chineset.shx`) ещё не читаются: текст в стиле SHX рисуется
нашим штриховым шрифтом, а любой знак, которого нет в шрифте текста (например CJK), берётся из
установленного шрифта, который его содержит, с предпочтением широкоохватным вроде Noto Sans CJK, Source Han
Sans, WenQuanYi, PingFang или Microsoft JhengHei. Два параметра, задаваемые `SETVAR` или (для каждого
запуска) переменной окружения, этим управляют:

| Переменная | Окружение | Значение |
|---|---|---|
| `FONTALT` | `CADCRAFT_FONTALT` | Шрифт вместо шрифта стиля текста, который не найден (файл SHX, отсутствующий TTF), по имени файла или семейства, например `Noto Sans CJK TC`. Пусто (по умолчанию) = наш штриховой шрифт. |
| `FONTFALLBACK` | `CADCRAFT_FONTFALLBACK` | Шрифты, которые пробуются первыми для знаков, которых нет в шрифте текста, через запятую, например `Noto Sans CJK TC, msjh.ttc`. |

`.` очищает любой из них.

**Свои шрифты.** Подойдёт любой шрифт `.ttf`, `.otf` или `.ttc`: установите его в системную папку шрифтов
(Windows `C:\Windows\Fonts` или шрифты пользователя, macOS `/Library/Fonts` или `~/Library/Fonts`,
Linux и BSD `/usr/share/fonts`, `/usr/local/share/fonts`, `~/.local/share/fonts` или
`~/.fonts`) и укажите его в стиле текста (`STYLE` или `style {"name":"FA","font":"Vazirmatn"}`)
по имени файла (`Vazirmatn-Regular.ttf`) или семейства (`Vazirmatn`) либо встройте в MTEXT
`\fVazirmatn;`. Перезапустите CADCraft после установки шрифта: папки шрифтов сканируются один раз.

**Текст справа налево (персидский, арабский, урду, иврит).** Строки TEXT и MTEXT раскладываются
алгоритмом двунаправленности Юникода (направление абзаца берётся из первой буквы, поэтому числа
и латинские слова внутри персидского текста сохраняют свой порядок), а текст на арабской письменности формируется
OpenType (контекстные формы букв, лам-алиф и другие лигатуры, ZWNJ / ZWJ, позиционирование знаков).
Выключка (влево, по центру, вправо, привязка и перенос MTEXT) по-прежнему относится к рамке текста.
В нашем штриховом шрифте нет арабских букв, поэтому персидский в стиле штрихового шрифта рисуется
установленным шрифтом, который их содержит: сначала ищутся Vazirmatn, Noto Naskh Arabic, Noto Sans Arabic, Segoe UI, Tahoma,
Arial и DejaVu Sans. Чтобы выбрать шрифт, установите бесплатный персидский шрифт, например
[Vazirmatn](https://github.com/rastikerdar/vazirmatn) (SIL Open Font License), и либо используйте его
в стиле текста, либо задайте `FONTFALLBACK` (`CADCRAFT_FONTFALLBACK="Vazirmatn"`). Смена оформления
внутри слова (смена цвета MTEXT в середине персидского слова) разрывает соединение в этой
точке.

<a id="portable-windows-zip"></a>
### Переносной ZIP для Windows

Переносной ZIP для Windows включает `portable.txt` рядом с `cadcraft.exe`. При наличии этого
маркера настройки настольной программы, журналы, автосохранения, данные рабочей среды,
файлы устройств печати и настройки/состояние окна eframe хранятся в `CADCraftData` рядом с
исполняемым файлом. eframe сохраняет свои настройки и состояние окна в `CADCraftData/app.ron`.
Сохраняйте этот каталог при замене двоичных файлов. В MSI маркера нет,
и он по-прежнему использует обычный профиль пользователя.

`CADCRAFT_CONFIG_DIR` имеет приоритет над маркером, включая пустое или
пробельное значение, которое отключает папку настроек. Если `CADCraftData` нельзя
создать или в него нельзя писать, CADCraft предупреждает и использует обычный профиль. Существующие настройки
профиля в переносной каталог автоматически не копируются.

Прежде чем переводить существующую установку Windows в переносной режим, закройте CADCraft,
сделайте резервную копию `%APPDATA%\CADCraft` и скопируйте настройки, которые хотите сохранить, в
`CADCraftData`. Включите папку `autosave`, если нужно восстанавливать несохранённые чертежи.
Настройки и состояние окна хранятся отдельно, в `%APPDATA%\ai.storyteller.cadcraft\data\app.ron`:
скопируйте этот файл в `CADCraftData\app.ron`, чтобы их сохранить.
Обновление переносного ZIP, в том числе через средство обновления, может восстановить `portable.txt`;
задайте `CADCRAFT_CONFIG_DIR` на существующую папку профиля, чтобы продолжать ею пользоваться при обновлениях.

`cadcraft-cli.exe` маркер не обнаруживает. Чтобы совместно использовать переносные настройки
настольной программы, передайте `--config-dir` с полным путём к `CADCraftData` или задайте
`CADCRAFT_CONFIG_DIR` на этот путь. Маркер также распознаётся на других настольных
платформах, но рассчитан на автономную установку с записью, а не внутрь
подписанного пакета приложения macOS.

<a id="logs"></a>
### Журнал

Настольная программа пишет записи `log` в стандартный поток ошибок и в `logs/cadcraft.log` в каталоге
настроек (Linux и BSD `~/.config/cadcraft/logs/` или
`$XDG_CONFIG_HOME/cadcraft/logs/`; macOS `~/Library/Application Support/CADCraft/logs/`; Windows
`%APPDATA%\CADCraft\logs\`; либо под `CADCRAFT_CONFIG_DIR`). Запуск из меню рабочего стола или
Dock не даёт терминала, поэтому к сообщению об ошибке прикладывайте этот файл. Каждый запуск переносит
предыдущий журнал в `cadcraft.1.log` (а тот — в `cadcraft.2.log`), так что журнал аварийного запуска
переживает следующий старт. Файл перестаёт расти на 16 MiB. `--version` файл не пишет.

| Переменная | Действие |
|---|---|
| `CADCRAFT_CONFIG_DIR` | Использовать этот каталог вместо системного каталога настроек (журнал пишется в его `logs/`); пустое значение значит, что папки настроек нет (нет файла журнала, автосохранения, рабочей среды и устройств печати) |
| `RUST_LOG` | Уровни журнала для стандартного потока ошибок и файла журнала. По умолчанию: `info` для собственных крейтов CADCraft, `warn` для всего остального. Директивы в стиле env_logger подменяют это, например `RUST_LOG=debug`, `RUST_LOG=warn,cadcraft_io=trace` или `RUST_LOG=info,wgpu_core=warn`; директива, оканчивающаяся на `*`, покрывает все цели, которые с неё начинаются (`cadcraft*=debug`). `cadcraft_engine=debug` также записывает каждое сообщение командной строки. |

Журнал — в `apps/cadcraft/src/logging.rs`; веб-сборка пишет в консоль браузера.

<a id="drive-it-from-agents-mcp-and-the-cli"></a>
## Управление агентами, MCP и CLI

```sh
# MCP server on stdio, headless:
cadcraft-cli mcp
# …or bridged to the running app (start it with --control 7979):
cadcraft-cli mcp --connect 127.0.0.1:7979
# …or headless, with the agent confined to a work folder:
cadcraft-cli mcp --automation-read-root ~/work --automation-write-root ~/work/out

# One-shot headless runs:
cadcraft-cli run --sample --script 'CIRCLE 22,3 1\n' --save out.dxf --export out.png
cadcraft-cli info drawing.dxf
cadcraft-cli convert drawing.dxf drawing.svg

# Frame part of the drawing (model space, drawing units, lower-left corner first):
cadcraft-cli convert drawing.dwg detail.png --window 0,0,20000,15000
cadcraft-cli run drawing.dwg --cmd 'zoom {"mode":"window","p1":[0,0],"p2":[20000,15000]}' --export detail.png
cadcraft-cli run drawing.dwg --cmd 'select {"window":[[0,0],[20000,15000]]}' --cmd 'zoom {"mode":"object"}' --export sel.png

# Act on what an earlier --cmd made: {last} is the last handle it returned.
cadcraft-cli run --metric --cmd 'layout.set {"name":"Layout1"}' \
  --cmd 'mview {"p1":[20,20],"p2":[200,150]}' --cmd 'viewport.set {"handle":"{last}","scale":1}'
```

Как кадрируются выгрузки изображений (PNG 2400×1600, SVG, PDF): `convert` вписывает границы пространства модели.
`run --export` показывает текущий вид, если сценарий или команды его изменили (`zoom`, `pan`,
`view.set`, …), и иначе тоже вписывает границы. `--window x0,y0,x1,y1` показывает именно этот
прямоугольник, центрированный и масштабированный без искажений; `--view extents` или `--view current` принудительно выбирает
тот или иной охват. Чтобы вписать набор выбора, после выделения выполните `zoom {"mode":"object"}`.

Когда при чтении файла что-то оказывается пропущенным (записи, которые читатель DXF не может разместить, записи объектов повреждённого
DWG), `info` об этом сообщает (`skipped`, `readNotes`), `convert` предупреждает в stderr, а `run`
печатает замечания DWG вместе с журналом; код выхода остаётся 0. MCP `open` отвечает замечаниями как
`warnings`.

Инструменты MCP включают `command_line` (ввод в приглашение), `execute` (любая команда с JSON),
`inspect_drawing`, `query_entities`, `render` (возвращает PNG) и, при подключении к программе,
`screenshot` и `ui_click`. Канал управления JSON настольной программы описан в
[docs/control-protocol.md](docs/control-protocol.md).

Чтобы выполнять процедуры LISP, сценарии и файлы псевдонимов или управлять CADCraft из своих программ, см.
[docs/customization.md](docs/customization.md).

`cadcraft-cli --help` документирует каждую подкоманду и флаг; коды выхода, потоки, переменные
окружения и его соглашения RFC-0012 — в [docs/cli.md](docs/cli.md).

<a id="architecture"></a>
## Архитектура

```text
geom ─┐                       f64 geometry: arcs, bulges, splines, intersections, offsets
dxf   │  (standalone)         DXF tag reader/writer
color ┤                       colour index, true colour
doc   ┤                       drawing database, copy-on-write entity store (cheap undo)
fonts ┤ render               stroke font + TEXT/MTEXT layout │ display lists, linetypes, hatches, dims, CPU raster
io    ┤                       DXF mapping, SVG/PNG export
engine┤                       sessions, commands, command line + prompts, snaps, selection, undo
ui-egui · mcp                 the swappable egui front end · MCP server
apps: cadcraft · cadcraft-cli · cadcraft-web
```

Ниже `ui-egui` никто не знает об egui, поэтому оболочку можно заменить. `cargo xtask ci`
проверяет форматирование, clippy, тесты, указание ресурсов, слоистость крейтов и сборку wasm.

Кнопки значков черчения и палитры слоёв используют закреплённый компонент кнопки `craft-ui` для взаимодействия,
доступных подписей и клавиатурного фокуса. CADCraft сохраняет свой многоцветный рисовальщик значков, тёмную палитру,
оттенок отключённого состояния и команды инструментов. Нативный хост атомарно сохраняет видимость рабочей среды и выбор наборов инструментов;
`CADCRAFT_CONFIG_DIR` выбирает изолированный профиль. Компактные группы панели инструментов уходят в
меню «Ещё», а индикаторы состояния обрезаются со всплывающей подсказкой полного значения, прежде чем дойти до вкладок листов.
Нарисованные элементы панели инструментов и вкладок
имеют доступные подписи и видимый клавиатурный фокус. Элементы свойств остаются специфичными для программы.

<a id="accessibility"></a>
## Специальные возможности

<a id="system-cursor"></a>
### Системный курсор

Над областью черчения CADCraft скрывает системный курсор и рисует своё перекрестье. Инструменты, которые следят за системным курсором (экранная лупа Windows, настроенная следовать за указателем или держать его в центре, другие экранные лупы, средства записи экрана, удалённые рабочие столы), теряют его там. Включите **Вид ▸ Специальные возможности ▸ Показать системный курсор**, чтобы оставить маленькое системное перекрестье видимым в центре нарисованного, или запустите CADCraft с переменной окружения `CADCRAFT_SYSTEM_CURSOR=1` (в Windows задайте её один раз командой `setx CADCRAFT_SYSTEM_CURSOR 1` и запустите CADCraft снова). Агенты могут переключать это каналом управления: `ui.set {"systemCursor": true}`.

<a id="animation-effects"></a>
### Эффекты анимации

CADCraft следует системной настройке анимации. Когда в системе анимации отключены, диалоги, меню и подсказки появляются сразу, без проявления, сворачиваемые разделы и полосы прокрутки меняются сразу, а колесо мыши прокручивает списки на целый шаг, без скольжения. Масштабирование чертежа колесом всегда идёт на целый шаг; с удерживаемым Ctrl (щипок тачпада в Windows) оно скользит к новому масштабу только пока эффекты анимации показаны.

| Система | Где находится настройка |
|---|---|
| Windows | Параметры ▸ Специальные возможности ▸ Визуальные эффекты ▸ Эффекты анимации |
| macOS | Системные настройки ▸ Универсальный доступ ▸ Уменьшение движения |
| Linux, BSD | настройка уменьшения движения (или анимации) рабочего стола, читаемая через портал XDG Desktop |
| Веб | `prefers-reduced-motion` браузера |

Изменение системной настройки подхватывается, пока CADCraft работает, за несколько секунд. Чтобы выбрать только для CADCraft, используйте **Вид ▸ Специальные возможности ▸ Эффекты анимации**: **Как в системе** (по умолчанию), **Вкл** или **Выкл**. То же самое есть в «Параметры ▸ Экран». Агенты могут задать это каналом управления: `ui.set {"animations": "off"}` (`"system"`, `"on"` или `"off"`), а `ui.inspect` сообщает, показаны ли анимации (`animations`).

Чертёжная обратная связь не является эффектом анимации и остаётся как есть: резиновые линии и предварительный просмотр, маркеры привязки, пауза захвата точки отслеживания объектной привязки, мигание текстового курсора, индикатор ожидания при открытии чертежа, а также панорама и масштаб, которые напрямую следуют за указателем и колесом.

<a id="roadmap"></a>
## План

См. [ROADMAP.md](ROADMAP.md) про этап, измеренную сопоставимость и оценку оставшейся работы и [docs/gaps.md](docs/gaps.md) про всё, чего ещё не хватает.

<a id="downloads"></a>
## Загрузки

**Скачайте CADCraft** с GitHub: в [последнем выпуске](https://github.com/storytold/cadcraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/cadcraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

> [!WARNING]
> Скачивайте официальные сборки CADCraft из [выпусков storytold/cadcraft](https://github.com/storytold/cadcraft/releases). Убедитесь, что владелец репозитория — `storytold`. Прежде чем запускать загрузку, проверьте, что её контрольная сумма совпадает со строкой этого файла в `SHA256SUMS.txt` выпуска:
>
> ```sh
> shasum -a 256 cadcraft-<ver>-macos-universal.dmg     # macOS (on Linux: sha256sum FILE)
> Get-FileHash .\cadcraft-<ver>-windows-x64.msi        # Windows PowerShell
> ```

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `cadcraft-<ver>-windows-x64.msi` | `cadcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `cadcraft-<ver>-windows-arm64.msi` | `cadcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `cadcraft-<ver>-windows-x86.msi` | `cadcraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы подписаны.

Установщик добавляет CADCraft в меню «Пуск» и спрашивает, добавить ли также ярлык на рабочий стол (по умолчанию не отмечено). Для тихой установки с ярлыком на рабочем столе: `msiexec /i cadcraft-<ver>-windows-x64.msi /qn DESKTOPSHORTCUT=1`.
Тихая установка по умолчанию — для текущего пользователя; добавьте `ALLUSERS=1` из терминала или средства развёртывания с повышенными правами для установки для всех пользователей.

**Если программа не открывается в Windows:** настольная программа по умолчанию инициализирует только DirectX 12.
Если позволить wgpu ещё и создать экземпляр OpenGL, некоторые графические драйверы (например,
`atio6axx.dll` AMD) могут аварийно завершиться до появления окна, и программа мелькнёт в «Диспетчере задач» и выйдет.
`WGPU_BACKEND` подменяет значение по умолчанию для диагностики (например `dx12` или `vulkan`). В
PowerShell, из папки с исполняемым файлом:

```powershell
$env:WGPU_BACKEND = "vulkan"
& .\cadcraft.exe
Remove-Item Env:WGPU_BACKEND                     # restore the default for later launches
```

Явная подмена `gl` может вернуть сбой драйвера на затронутых системах. Значения подсистемы по умолчанию для macOS, Linux
и веба не менялись.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `cadcraft-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `cadcraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `cadcraft-<ver>-linux-x86_64.AppImage` | `cadcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `cadcraft-<ver>-linux-x86_64.flatpak` | `cadcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `cadcraft-<ver>-linux-x86_64.deb` | `cadcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `cadcraft-<ver>-linux-x86_64.rpm` | `cadcraft-<ver>-linux-aarch64.rpm` | |
| Архив | `cadcraft-<ver>-linux-x86_64.tar.gz` | `cadcraft-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

RISC-V (riscv64): `cadcraft-<ver>-linux-riscv64.tar.gz`, кросс-компиляция; нужен glibc 2.39 или новее (Ubuntu 24.04+, Debian 13+).

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `cadcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `cadcraft-web-<ver>.zip` | Работает в современном браузере; разместите на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

CADCraft — одно из приложений **Crafting Apps**: бесплатные творческие инструменты с открытым исходным кодом от команды
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
  <a href="https://getartcraft.com/apps/cadcraft">CADCraft</a>
</p>

<a id="license-and-credits"></a>
## Лицензия и благодарности

CADCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the CADCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Значки CADCraft, его одноштриховой чертёжный шрифт, образцы штриховки и типы линий — всё
оригинальная работа, нарисованная или заданная в коде. Образцовые чертежи тоже порождены кодом.

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и CADCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>

Наборы инструментов, «Слои» и «Свойства» можно перегруппировывать, разделять, откреплять внутри окна программы, закрывать и открывать снова. Холст чертежа остаётся видимым и его нельзя закрыть или превратить во вкладку. Перетащите заголовок панели к целевому краю или к другому заголовку. Его контекстное меню предлагает «Открепить панель», «Переместить в группу» и «Закрыть панель». Существующие переключатели панелей снова открывают панели в сохранённом месте; «Сбросить раскладку панелей» восстанавливает раскладку программы. Плавающие панели остаются внутри текущего окна программы.
