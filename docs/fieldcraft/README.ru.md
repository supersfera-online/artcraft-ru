# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/tangency-labs/fieldcraft/blob/main/README.md
Репозиторий: https://github.com/tangency-labs/fieldcraft
Коммит исходника (последний, в котором менялся README.md): 8307d782a75e76a4a3bb5615d9ef59aa61657287
Дата коммита: 18 ноября 2026, 08:33 (America/Los_Angeles, PT); в исходнике 2026-11-18T16:33:52Z
SHA256 исходника: 8e8432b3494b6ae25cc2c9452f6c37b6e4c006662181371d6153976645f8723c
Git blob SHA: 090353736e75912f66b8fe46ef5da370b832aee4
Размер исходника: 13954 байт
Снято чтением raw: https://raw.githubusercontent.com/tangency-labs/fieldcraft/main/README.md
Перевод выполнен локально; авторам не отправлялся. Строки-переключателя языков нет: в репозитории нет других README.<код>.md.
-->
<!-- Перевод не проверен авторами -->
# FieldCraft

[![Download for macOS](https://img.shields.io/badge/macOS%20%28Apple%20silicon%29-Download-000000?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/tangency-labs/fieldcraft/releases/latest)
[![Download for Windows](https://img.shields.io/badge/Windows-Download-0078D6?style=for-the-badge)](https://github.com/tangency-labs/fieldcraft/releases/latest)
[![Download for Linux](https://img.shields.io/badge/Linux-Download-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/tangency-labs/fieldcraft/releases/latest)
[![Try it in your browser](https://img.shields.io/badge/Browser-Try%20it-2ea44f?style=for-the-badge&logo=webassembly&logoColor=white)](https://tangency-labs.github.io/fieldcraft/app/)
[![Documentation](https://img.shields.io/badge/Docs-Read-4b5563?style=for-the-badge&logo=mdbook&logoColor=white)](https://tangency-labs.github.io/fieldcraft/)
[![Support on Ko-fi](https://img.shields.io/badge/Ko--fi-Support-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/jyviko)

Открытая CAE-программа по принципу чистой комнаты на чистом Rust: от параметрической детали SolidCraft до
проверенного конечно-элементного расчёта, с тетраэдрической и гексаэдрической сеткой, собственными неявными,
явными, тепловыми решателями и решателем решёточных уравнений Больцмана, а также расчётными колодами для Abaqus, Nastran и LS-DYNA.
Настольная программа, командная строка и ИИ-агенты (через MCP) вызывают одни и те же команды.

**Состояние:** рано, но уже работает от начала до конца — откройте деталь, постройте сетку, задайте расчёт, решите,
посмотрите результаты — с нелинейным неявным решателем (большие деформации, пластичность, резина), который уже
на месте. Центр тяжести — гексаэдрическая сетка. Дальше: устойчивость и метод длины дуги, контакт, затем
более широкая библиотека материалов и многофизики. См. [ROADMAP.md](ROADMAP.md).
**Хотите помочь?** Возьмите обращение с меткой
[good first issue](https://github.com/tangency-labs/fieldcraft/labels/good%20first%20issue) или
[help wanted](https://github.com/tangency-labs/fieldcraft/labels/help%20wanted) и прочитайте
[CONTRIBUTING.md](CONTRIBUTING.md).

![Claude в FieldCraft по MCP анализирует консоль из двутавра: открывает деталь, строит гексаэдрическую сетку, задаёт сталь, защемление и нагрузку 1 кН на конце, решает, показывает напряжения по Мизесу и деформированную форму и сверяет прогиб конца с теорией балки](docs/media/claude-mcp.gif)

*Claude управляет FieldCraft через его [MCP-сервер](docs/mcp.md): один запрос — и он открывает деталь, строит сетку, задаёт и решает расчёт, затем сверяет прогиб конца с теорией балки. Настоящий сеанс, ожидания сокращены. [Полное видео](docs/media/claude-mcp.mp4).*

![ИИ-агент в FieldCraft по MCP анализирует консоль из двутавра: открыть, гексаэдрическая сетка, сталь, защемление и нагрузка на конце, решение, контуры Мизеса, деформированная форма и облёт вокруг неё](docs/media/ibeam-analysis.gif)

ИИ-агент ведёт FieldCraft через [MCP](docs/mcp.md), каждый этап подписан инструментом, который он
вызывает: открывает двутавр, строит гексаэдрическую сетку, задаёт материал, защемление и нагрузку 1000 Н на конце,
решает и показывает напряжения по Мизесу и деформированную форму (прогиб конца 0,176 мм; теория балки
со сдвигом 0,177 мм).
[MP4](docs/media/ibeam-analysis.mp4) · переснято с помощью [tools/demo-video](tools/demo-video/README.md).

<a id="download"></a>
## Скачать

- **macOS:** откройте `.dmg` и перетащите FieldCraft в Applications (Apple silicon).
- **Windows:** распакуйте и запустите `fieldcraft.exe`.
- **Linux:** `.AppImage` (разрешите запускать как программу) или `.tar.gz`.
- **Браузер:** [попробуйте на tangency-labs.github.io/fieldcraft/app](https://tangency-labs.github.io/fieldcraft/app/), установка не нужна.
- **Ночные сборки:** [ночные предрелизы](https://github.com/tangency-labs/fieldcraft/releases?q=nightly&expanded=true) собирают `develop` каждую ночь, когда ветка сдвинулась и прошла CI ([docs/updates.md](docs/updates.md#nightly-builds)).
- **Командная строка:** `fieldcraft-cli` входит в каждый пакет; ИИ-агенты подключаются к нему через MCP
  ([docs/mcp.md](docs/mcp.md)).

В каждом релизе контрольные суммы перечислены в `SHA256SUMS.txt`. Сборка из исходников описана в
[CONTRIBUTING.md](CONTRIBUTING.md#get-it-running-about-10-minutes-on-a-fast-machine).

<a id="hex-meshing-a-part-that-does-not-sweep"></a>
## Гексаэдрическая сетка детали, которую нельзя «протянуть» одним куском

Галтелевый L-кронштейн с отверстием в каждой полке нельзя получить одним сдвигом (sweep) целиком. Разбитый на 30
ячеек в SolidCraft, в FieldCraft он получает полностью гексаэдрическую согласованную сетку — O-сетки вокруг отверстий,
сгущение через галтель — и прогиб конца на hex20 совпадает с мелким решением tet10 до 0,1 %.
Та же деталь также автоматически получает полностью гексаэдрическую сетку октовым сеточником (`mesh.hex.octree`).

| Ячейки | Согласованная гексаэдрическая сетка | Мизес (защемление и нагрузка нарисованы) |
|---|---|---|
| ![Кронштейн, разбитый на 30 цветных ячеек](docs/media/bracket-partition.png) | ![Полностью гексаэдрическая сетка с O-сетками вокруг отверстий](docs/media/bracket-hex.png) | ![Напряжения по Мизесу с пиком у отверстия, конусы защемления и стрелки нагрузки](docs/media/bracket-stress.png) |

<a id="what-it-does-today"></a>
## Что умеет сейчас

- **Геометрия на входе:** проекты SolidCraft (`.solidcraft`) с устойчивыми именами граней, рёбер и тел,
  а также сетки 3MF с тегами граней; проверки поверхности (сшивка, многообразие, ориентация, самопересечения).
- **Сетки:** связанные тетраэдры Делоне (tet4, tet10) с точными предикатами и
  сертифицированным контролем корректности; уточнение Делоне, сглаживание и удаление «сливков»; структурированные гексаэдры
  протягиванием, вращением и отображением (hex8, hex20) и согласованная многоблочная гексаэдрическая сетка по детали,
  разбитой на ячейки (`mesh.hex.blocks`); неструктурированная октовая полностью гексаэдрическая сетка для любой детали
  (`mesh.hex.octree`); двумерные сетки четырёхугольников и треугольников; показатели качества по элементу и по набору.
- **Элементы:** объёмные (tet4, tet10, wedge6, hex8 с несовместными модами, hex20 полный и
  сокращённый, гибридный u–p для почти несжимаемых материалов), плоское напряжённое и плоское деформированное состояние и
  осесимметрия, фермы, балки Тимошенко, оболочки MITC3/MITC4, пружины, демпферы и точечные массы.
- **Модель:** наборы, привязанные к именам геометрии, поэтому они переживают перестроение сетки; изотропная и ортотропная
  упругость, пластичность J2 (изотропное и кинематическое упрочнение, Johnson–Cook), повреждение Johnson–Cook,
  гиперупругость neo-Hookean, Mooney–Rivlin и Yeoh, тепловые свойства; условия закрепления, перемещения,
  симметрии и температуры; силы, моменты, давление, тяжесть, центробежные и тепловые
  нагрузки; опорные точки с кинематическими и распределяющими связями; отмена, повтор и
  файл `.fieldcraft`, удобный для текстового сравнения.
- **Решатели:** линейный статический и частотный (наддиагональный Холецкий, блочный Ланцош); нелинейный статический
  методом Ньютона–Рафсона с автоматическими приращениями — большие деформации (полная лагранжева постановка) на каждом
  объёмном элементе, следящее давление, пластичность конечных и малых деформаций с одной и той же картой возврата,
  что и у явного решателя, резина и температурная деформация, с измеренной квадратичной сходимостью; стационарная и
  нестационарная теплопередача и связанное термонапряжённое состояние; явная динамика с пластичностью, повреждением,
  эрозией и жёсткими стенками; течение D3Q19 по решёточным уравнениям Больцмана с силами на гранях детали. Результаты
  никогда не зависят от числа потоков.
- **Колоды:** писатели Abaqus, Nastran и LS-DYNA, каждый по имени отказывается от того, чего не может выразить.
- **Результаты:** контуры напряжений, деформаций и перемещений с легендой, деформированные формы, формы
  мод, кадры явного и нелинейного расчёта, зонды и суммы реакций; опоры, нагрузки, опорные
  точки и связи рисуются в окне вида.
- **Проверка:** каждая возможность сверяется с замкнутыми формами и опубликованными эталонами
  (NAFEMS, MacNeal–Harder, Scordelis–Lo, эластика, пластический цилиндр Хилла, труба Ривлина) в [`tests/oracle`](tests/oracle), результаты заморожены,
  чтобы не «уплывали»: 170 из 176 величин проходят в 50 случаях, остальные 6 задокументированы как известные
  расхождения ([docs/oracle.md](docs/oracle.md)).
- **Управление:** настольная программа в компоновке семейства Craft, CLI, канал управления JSON и
  MCP-сервер; каждая возможность — это команда ([docs/features.md](docs/features.md)).

![Окно FieldCraft: защемлённая консоль с опорами, давлением, тяжестью и связанной опорной точкой, нарисованными в окне вида](docs/media/setup-symbols.png)

<a id="examples"></a>
## Примеры

Готовые к решению образцы: откройте один из **Файл ▸ Образцы** (или со стартового экрана) либо запустите программу
командой `fieldcraft --sample NAME` и нажмите **Решить**. Каждый открывается и решается меньше чем за полминуты и сверен
с замкнутой формой или эталонным решением ([docs/examples.md](docs/examples.md)).

<table>
<tr>
<td width="33%" valign="top"><img src="docs/media/examples/drop-test.png" alt="Испытание на падение" width="100%"><br><b>Испытание на падение</b> (<code>drop-test</code>): алюминиевый кронштейн, сброшенный с 2 м на наклонную плоскость; явная динамика, волны напряжений от удара</td>
<td width="33%" valign="top"><img src="docs/media/examples/rubber-seal.png" alt="Резиновое уплотнение" width="100%"><br><b>Резиновое уплотнение</b> (<code>rubber-seal</code>): кольцевая прокладка Mooney–Rivlin, сжатая на 25 %; нелинейный статический расчёт, большая деформация</td>
<td width="33%" valign="top"><img src="docs/media/examples/heated-bracket.png" alt="Нагретый кронштейн" width="100%"><br><b>Нагретый кронштейн</b> (<code>heated-bracket</code>): защемлённый стальной кронштейн, нагреваемый с одного конца; стационарное тепло и термонапряжения</td>
</tr>
<tr>
<td width="33%" valign="top"><img src="docs/media/examples/bracket-hex.png" alt="Кронштейн с гексаэдрической сеткой" width="100%"><br><b>Кронштейн с гексаэдрической сеткой</b> (<code>bracket-hex</code>): кронштейн, разбитый на 30 ячеек, сетка полностью гексаэдрическая (hex20), Мизес</td>
<td width="33%" valign="top"><img src="docs/media/examples/crank-arm.png" alt="Шатун велосипеда" width="100%"><br><b>Шатун велосипеда</b> (<code>crank-arm</code>): алюминиевый шатун со структурированной полностью гексаэдрической сеткой (hex20) по разделённой половине и её зеркальному отражению, вес ездока на педали; изгиб у корня в пределах 0,3 % от M/Z</td>
<td width="33%" valign="top"><i>Снимка пока нет: окно вида не рисует результаты течения (M12).</i><br><b>Обтекание кронштейна</b> (<code>flow-past</code>): воздух мимо L-кронштейна на полу; течение по решёточным уравнениям Больцмана, сопротивление и сила на каждой грани</td>
</tr>
</table>

<a id="build"></a>
## Сборка

```sh
cargo xtask ci                                  # fmt, assets, layers, clippy, tests, wasm
cargo xtask test --heavy                        # the heavy (ignored) tests and the doc tests
cargo run -p fieldcraft-cli -- commands         # every command and its parameters
cargo run -p fieldcraft-cli -- run script.json  # run a command script
cargo run -p fieldcraft-cli -- snapshot script.json --out shot.png  # draw it to a PNG, no window
cargo run -p fieldcraft-cli -- mcp              # MCP server on stdio for AI agents (docs/mcp.md)
```

Rust 1.99.1 через rustup (`rust-toolchain.toml`, с целью `wasm32-unknown-unknown`, которая нужна `cargo xtask ci`); 1.95 и новее тоже собирается.

С Nix (`flake.nix`, Linux и macOS):

```sh
nix run github:tangency-labs/fieldcraft                         # the desktop app (package fieldcraft)
nix run github:tangency-labs/fieldcraft#fieldcraft-cli -- mcp   # the CLI (package fieldcraft-cli)
nix develop          # runtime libraries for `cargo run` (window, GPU, file dialogs); your own toolchain
nix develop .#rust   # the same with nixpkgs' Rust, building into target/nix
```

В Linux драйверы GPU берутся из системы: `hardware.graphics.enable` на NixOS, nixGL в остальных случаях.

<a id="documentation"></a>
## Документация

Сайт документации:
[tangency-labs.github.io/fieldcraft](https://tangency-labs.github.io/fieldcraft/), собирается из
`docs/` с каждым релизом (`cargo xtask book`). Главные страницы:

- [Примеры](docs/examples.md): готовые к решению образцы и их проверки
- [Архитектура](docs/architecture.md): crate, слои и конвейер сеток
- [Библиотека элементов](docs/manual/structural/elements.md), [материалы](docs/manual/structural/materials.md), [цитируемая библиотека материалов](docs/manual/structural/material-library.md) и [верификация и валидация](docs/verification.md)
- [Список возможностей](docs/parity.md) и [план работ](ROADMAP.md)
- [Библиотеки и лицензии](docs/adr/0001-libraries.md)
- [ИИ-агенты (MCP)](docs/mcp.md): `claude mcp add fieldcraft -- /path/to/fieldcraft-cli mcp`
- [Протокол управления](docs/control-protocol.md): управление настольной программой
- [Выпуск релизов](docs/releasing.md): как релиз собирается, проверяется и публикуется
- [Участие](CONTRIBUTING.md) и [инструкции для агентов](AGENTS.md)

<a id="privacy"></a>
## Конфиденциальность

FieldCraft ничего не отправляет, пока вы не согласитесь. При первом запуске программа один раз спрашивает, делиться ли анонимной
статистикой использования (какие инструменты вы используете, ничего из ваших моделей); это меняется в «Справка › Настройки…», а
`FIELDCRAFT_TELEMETRY=0` отключает её. Имена файлов, пути, геометрия, содержимое моделей, значения параметров
и сообщения никогда не отправляются: в [docs/privacy.md](docs/privacy.md) перечислено каждое событие и
каждое свойство. Отчёты о сбоях и журнал остаются на вашем компьютере; «Справка › Сообщить об ошибке» открывает обращение GitHub,
которое вы сами просматриваете и отправляете, с приложением сеанса или модели только если вы это отметите
([docs/crash-reports.md](docs/crash-reports.md)).

<a id="sponsors"></a>
## Спонсоры

[![CI powered by Blacksmith](docs/sponsors/blacksmith-ci-powered.png)](https://www.blacksmith.sh)

Непрерывная интеграция FieldCraft работает на [Blacksmith](https://www.blacksmith.sh), который оплачивает её минуты CI.

Поддержать разработку FieldCraft можно на [Ko-fi](https://ko-fi.com/jyviko).

<a id="disclaimer"></a>
## Отказ от ответственности

Файлы в этом репозитории предоставляются как есть, без гарантий, ответственности и возмещения убытков, и
Tangency Labs и участники не несут ответственности за любое вредное или противоправное их
использование: читайте [DISCLAIMER.md](DISCLAIMER.md).

<a id="license"></a>
## Лицензия

Двойная лицензия [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор. Уведомления
— в [NOTICE](NOTICE); лицензии третьих сторон — в
THIRD-PARTY-LICENSES.txt, который входит в каждый пакет релиза (`cargo xtask licences` его записывает).

FieldCraft — независимый проект, не связанный с Dassault
Systèmes, MSC Software, Siemens или Ansys, не спонсируемый и не одобряемый ими. Abaqus, Nastran, MSC Nastran, Simcenter Nastran и
LS-DYNA являются товарными знаками своих владельцев и названы только для описания совместимости файлов.
