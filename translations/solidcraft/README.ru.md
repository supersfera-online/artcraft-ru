# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!--
Источник: https://github.com/tangency-labs/solidcraft/blob/main/README.md
Репозиторий: https://github.com/tangency-labs/solidcraft
Коммит исходника (последний, в котором менялся README.md): cf51e29516f4f65b37e59d15858c2ade1b7f5f27
Дата коммита: 17 ноября 2026, 17:16 (America/Los_Angeles, PT); в исходнике 2026-11-18T01:16:22Z
SHA256 исходника: 93cc1caa5c244f35f274a044a181215d6e69f1b0fb5f5f01c2dab6ad051851f2
Git blob SHA: 477b48aa87c61f536697f7767f12a79a83b8df3a
Размер исходника: 20322 байт
Снято чтением raw: https://raw.githubusercontent.com/tangency-labs/solidcraft/main/README.md
Перевод выполнен локально; авторам не отправлялся. Строки-переключателя языков нет: в репозитории нет других README.<код>.md.
-->
<!-- Перевод не проверен авторами -->
<p align="center">
  <img src="assets/icons/app/linux/exports/hicolor/256x256/apps/io.tangencylabs.solidcraft.png" width="96" height="96" alt="SolidCraft" />
</p>

<h1 align="center">SolidCraft</h1>

<p align="center">
  <strong>Открытая параметрическая 3D CAD-программа, написанная на чистом Rust.</strong><br />
  Стройте эскизы, накладывайте ограничения и собирайте тела по параметрической шкале операций. Измените размер
  и смотрите, как модель перестраивается. Запускайте на настольной программе, в браузере или поручите ИИ-агентам
  моделировать через встроенный MCP-сервер.
</p>

<div align="center">

[![Download for Windows][badge-windows]][windows-msi]
[![Download for macOS][badge-macos]][macos-dmg]
[![Download for Linux][badge-linux]][linux-appimage]
[![Get it from the Snap Store][badge-snap]][snap-store]
[![Try it in your browser][badge-web]][web-app]

</div>

<p align="center">
  <a href="https://solidcraft.io">Сайт</a> ·
  <a href="https://solidcraft.io/download">Скачать</a> ·
  <a href="https://solidcraft.io/app">Попробовать в браузере</a> ·
  <a href="https://docs.solidcraft.io/">Документация</a> ·
  <a href="https://www.blacksmith.sh"><img src="https://img.shields.io/badge/CI-Blacksmith-000000?logo=githubactions&logoColor=white" alt="CI powered by Blacksmith" /></a>
  <a href="https://discord.gg/FtU4NQNVDH">Discord</a> ·
  <a href="https://github.com/tangency-labs/solidcore">SolidCore</a>
</p>

<p align="center">
  <a href="https://github.com/tangency-labs/solidcraft/actions/workflows/ci.yml?query=branch%3Amain"><img src="https://github.com/tangency-labs/solidcraft/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI" /></a>
  <a href="https://github.com/tangency-labs/solidcraft/releases/latest"><img src="https://img.shields.io/github/v/release/tangency-labs/solidcraft?label=release" alt="Latest release" /></a>
  <a href="https://github.com/tangency-labs/solidcraft/releases"><img src="https://img.shields.io/github/downloads/tangency-labs/solidcraft/total?label=downloads" alt="Downloads" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/tangency-labs/solidcraft" alt="Licence" /></a>
  <a href="https://discord.gg/FtU4NQNVDH"><img src="https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://remade.wiki/projects/solidcraft/"><img src="https://remade.wiki/badges/listed-on-remade-classic.svg" alt="Listed on Remade" /></a>
  <a href="https://github.com/tangency-labs/solidcraft/stargazers"><img src="https://img.shields.io/github/stars/tangency-labs/solidcraft?style=flat" alt="Stars" /></a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/296178?utm_source=trendshift-badge&utm_medium=badge&utm_campaign=badge-trendshift-296178" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/296178/daily" alt="tangency-labs%2Fsolidcraft | Trendshift" width="250" height="55"/></a>
  <a href="https://trendshift.io/repositories/296178?utm_source=trendshift-badge&utm_medium=badge&utm_campaign=badge-trendshift-296178" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/296178/daily?language=Rust" alt="tangency-labs%2Fsolidcraft | Trendshift (Rust)" width="250" height="55"/></a>
</p>

![SolidCraft: корпус Raspberry Pi 4 из пустого проекта: эскиз с размерами по параметрам, выдавливание, скругления и оболочка, кромка скруглена одним указанием, стойки, размноженные массивом по крепёжным отверстиям платы, вырезы портов, вентиляционные пазы, «Pi 4», выгравированный шрифтом, материал PETG с массой в «Свойствах» и изменение высоты в «Параметрах»](docs/screenshots/demo.gif)

*Корпус Raspberry Pi 4 из пустого проекта: эскиз с размерами по параметрам платы, выдавливание, скругление, оболочка, кромка скруглена одним указанием, стойка M2.5, размноженная массивом по прямоугольнику отверстий 58 × 49 мм, вырезы портов, вентиляционные пазы, «Pi 4», выгравированный шрифтом DejaVu Sans Bold, и материал PETG, заданный в проекте, с массой в «Свойствах», затем высота 24 → 32 мм в «Параметрах» — и всё перестраивается. Воспроизведение 6×, паузы простоя вырезаны. [Полное видео](https://github.com/tangency-labs/solidcraft/raw/refs/heads/main/docs/screenshots/demo.mp4), записано [сценарием демонстрации](examples/demo/record_ui.sh).*

<a id="download"></a>
## Скачать

- **Windows:** [установщик][windows-msi].
- **macOS:** [образ диска][macos-dmg] (Apple silicon и Intel).
- **Linux:** [AppImage][linux-appimage] или `sudo snap install solidcraft` ([Snap Store][snap-store]).
- **Веб:** [попробуйте в браузере][web-app], установка не нужна.

Сборки ARM64 и 32-разрядные, переносной zip, .deb, .rpm, Flatpak и прочие пакеты — на
[странице загрузок](docs/downloads.md). Программа для macOS подписана Developer ID и нотаризована
Apple. Подпись Windows: бесплатная подпись кода от SignPath.io, сертификат — от SignPath
Foundation ([политика подписи кода](https://docs.solidcraft.io/code-signing-policy.html)). Пока
производственный сертификат не установлен, SmartScreen может предупредить: выберите **Подробнее**, затем **Всё равно запустить**. В SolidCraft 0.11–0.14 скачайте один раз вручную; см.
[обновление](https://docs.solidcraft.io/guide/updates.html#updating-from-011-to-014).

<a id="what-works"></a>
## Что уже работает

Рано, но уже можно для простых деталей: 75 из 76 открытых эталонных деталей совпадают по аналитическому или
вычисленному в FreeCAD объёму, площади, центру масс и габаритному ящику ([оракул](docs/oracle.md));
остальная — отслеживаемая ошибка.

- **Эскизы и ограничения:** линии, дуги, сплайны, текст и другое, решаемые собственным решателем ограничений, с размерами, задаваемыми параметрами.
- **Операции:** выдавливание, вращение, протягивание, лофтинг, скругление, фаска, оболочка, уклон, отверстия, резьбы, массивы, зеркало, разделение и объединение на редактируемой параметрической шкале.
- **Параметры и конфигурации** с выражениями, учитывающими единицы измерения.
- **Сборки** с сопряжениями, исследованием движения, наборами контакта, пересечениями и массовыми свойствами.
- **Листовой металл** с отбортовками, подгибами, сгибом и разгибом и развёртками, а также операции пластиковых корпусов.
- **Файлы:** STEP, IGES, 3MF, STL, OBJ и glTF на вход и выход там, где это поддерживается, экспорт URDF, проекты `.sc` (файлы `.solidcraft` более ранних выпусков по-прежнему открываются).
- **Настольная программа, браузерная программа, CLI без окна и MCP-сервер**, все выполняют одни и те же команды.

Полный список — в [docs/capabilities.md](docs/capabilities.md) и [docs/features.md](docs/features.md);
состояние и планы — в [ROADMAP.md](ROADMAP.md). См. также [что люди уже собрали](docs/showcase.md),
[поддержку 3D-мыши](docs/3d-mouse.md) и [архитектуру](docs/architecture.md).

<a id="build-from-source"></a>
## Сборка из исходников

```sh
cargo run --release -p solidcraft -- --sample      # desktop app with a sample part
cargo run --release -p solidcraft-cli -- commands  # the command registry
cargo run --release -p solidcraft-cli -- run examples/bracket.json --out bracket.step
cargo xtask ci                                     # fmt, clippy, tests, icons, assets, layers, wasm
```

Другие команды, кросс-сборка под Windows и сборка для браузера — в [docs/building.md](docs/building.md).

<a id="ai-agents-mcp"></a>
## ИИ-агенты (MCP)

`solidcraft-cli mcp` — сервер [Model Context Protocol](https://modelcontextprotocol.io). Без графического интерфейса он
ведёт собственный сеанс проектирования, а с `--connect` управляет уже запущенной программой, так что можно смотреть.
Claude Code: `claude mcp add solidcraft -- solidcraft-cli mcp`. Если терминал не находит
`solidcraft-cli` (старые установщики Windows не кладут его в `PATH`), укажите полный путь (по умолчанию
`"C:\\Program Files\\SolidCraft\\solidcraft-cli.exe"`). Инструменты, правила доступа и пример сеанса:
[docs/mcp.md](docs/mcp.md).

<a id="scripts"></a>
## Сценарии

Сценарий — это JSON-список тех же команд, что выполняет интерфейс, запускаемый командой `solidcraft-cli run`.
Формат и пример: [docs/scripts.md](docs/scripts.md). Страницы также можно вести через
[API команд браузера](docs/browser-api.md).

<a id="plugins-experimental-desktop-runtime"></a>
## Плагины (экспериментальная среда настольной программы)

Плагины добавляют отдельно распространяемое поведение, не вшивая его в SolidCraft.
Первая среда загружает **компоненты WebAssembly**, явно запрошенные пользователем. Одна лишь
установка папки, включение в «Настройки» или открытие проекта никогда не выполняет код плагина.
Интерфейс экспериментальный: пакет WIT `craft:plugin@0.2.0`, возможность `commands@0.2` (плагины, собранные для 0.1, по-прежнему запускаются). Пока
версия 0.x, младший выпуск может сломать предыдущий; хост отказывает плагину, которому нужна
возможность, которой у хоста нет, и говорит об этом простыми словами. После обновления просмотрите плагин снова. Настольная программа и CLI без окна используют одни и те же команды. Выполнение в
браузере, автоматические загрузки и обновления, собственные панели и типы параметрических операций,
задаваемые плагином, — дело будущего.

<a id="install-and-inspect"></a>
### Установить и просмотреть

Пакет — это папка, названная по его идентификатору, с файлами `plugin.json` и компонентом `.wasm`.
«Настройки > Плагины» перечисляет пакеты в папке данных пользователя: `%LOCALAPPDATA%/SolidCraft/plugins`
в Windows, `~/Library/Application Support/SolidCraft/plugins` в macOS и
`${XDG_DATA_HOME:-~/.local/share}/solidcraft/plugins` в Linux. **Показать в папке** открывает это место.
Можно также просмотреть и явно запустить пакет из другой папки. Хост ничего не загружает сам.

Минимальный манифест выглядит так. Пакеты плагинов и примеры ведутся вне этого
репозитория, как задано в [RFC о плагинах](docs/rfcs/0002-plugins.md).

```json
{
  "id": "example-box",
  "name": "Example box",
  "version": "0.1.0",
  "description": "Create an ordinary editable box from dimensions.",
  "capabilities": ["commands@0.1"],
  "runtime": {
    "module": "plugin.wasm",
    "entries": ["make"],
    "commands": ["solid.box"],
    "limits": {"fuel": 10000000, "memory_mib": 64, "deadline_ms": 5000}
  }
}
```

Выполните `plugin.inspect` с `{"path":"/path/to/example-box"}` через JSON-сценарии CLI, MCP
`execute` или `engine.execute` канала управления настольной программы. Команда читает манифест и компонент,
не выполняя их, и возвращает объявленные команды, пределы и хэш одобрения SHA-256 `approval`.
Прежде чем пользоваться этим хэшем, просмотрите автора, код и объявленные права. Просмотр сам по себе пакет не одобряет.
Уже существующие пакеты только с метаданными по-прежнему можно перечислять, но запускать их нельзя, пока они не объявят среду выполнения.

<a id="run-explicitly"></a>
### Запустить явно

После просмотра осмотренного пакета выполните:

```json
{
  "command": "plugin.run",
  "params": {
    "path": "/path/to/example-box",
    "approval": "<exact approval hash returned by plugin.inspect>",
    "entry": "make",
    "params": {"length": 20, "width": 10, "height": 3}
  }
}
```

Например, сохраните эту команду в JSON-массиве и используйте `solidcraft-cli run commands.json`.
Для запущенной настольной программы отправьте её как `command` и `params` отдельного
запроса `engine.execute` (см. [протокол управления](docs/control-protocol.md)). Нативный хост выполняет
это на рабочем потоке и оставляет окно отзывчивым. «Остановить» или изменение проекта отбрасывает ожидаемый
результат; хост не перезапускает внешний код автоматически. Настольные пакеты команд и сценарии должны отправлять
`plugin.run` отдельно. Сценарии CLI без окна могут включать его как обычную команду.

Хэш связывает **и точные байты манифеста, и байты компонента**, поэтому обновлённый пакет
требует нового просмотра и повторного разрешения. Это удостоверение содержимого, а не подпись и не
репутация автора. Чат с агентом спрашивает, прежде чем выполнять внешний код плагина. MCP и канал
управления сохраняют прежние области доступа к файлам: при необходимости явно разрешите папку пакета. Указание
имени пакета никогда не даёт доступ к другой папке.

<a id="user-resource-ceilings"></a>
### Потолки ресурсов пользователя

Значения вызова по умолчанию остаются **10 000 000 единиц топлива, 64 МиБ гостевой памяти и 5000 мс**.
Потолки хоста по умолчанию остаются **100 000 000 000 единиц топлива и 128 МиБ**. Пакет может объявить
большие бюджеты топлива или памяти, но выполнение отклоняется, пока вы явно не поднимете потолки
хоста и не одобрите именно это содержимое пакета. `plugin.inspect` бездействует и сообщает
запрошенные пределы, текущие `host_limits`, `within_host_limits` и любой `limits_error`, даже когда
запрос слишком велик.

В нативном графическом интерфейсе откройте **Настройки > Плагины**, введите **Макс. топливо плагина** и
**Макс. память плагина (МиБ)**, затем выберите **Применить** или **ОК**. Клавиша Enter также принимает оба значения;
**Отмена** откатывает изменения с последнего «Применить», а **Восстановить значения по умолчанию** сбрасывает эту страницу.
Настройки сохраняются в пользовательских настройках и не едут вместе с сохранёнными проектами.

Для отдельных сеансов CLI или MCP без окна создайте файл JSON в UTF-8, например
`plugin-limits.json` с содержимым:

```json
{"max_fuel": 200000000000, "max_memory_mib": 512}
```

Передайте его явно при запуске процесса:

```text
solidcraft-cli --plugin-limits plugin-limits.json run inspect-plugin.json --results
solidcraft-cli --plugin-limits plugin-limits.json mcp --headless --allow-path /path/to/plugins
```

Отсутствующие поля используют исходные потолки хоста. Подключённые настольные сеансы используют
настройки графического интерфейса; настройки CLI не могут их переопределить. Принимаются положительные целые значения топлива до `u64::MAX`
без округления. Гостевая память ограничена 4096 МиБ текущим ABI Wasm32;
чтобы изменить эту техническую границу, нужен другой ABI среды выполнения. Ни одна из настроек не меняет
объявленный бюджет пакета, не выполняет его, не добавляет разрешений и не повторяет неудачный вызов.
Просмотрите его манифест и компонент, получите хэш одобрения содержимого и вызовите его явно.
Изменённый бюджет в манифесте требует нового хэша одобрения. Держите выбранные потолки в пределах
доступных ресурсов машины; это пределы гостевого выполнения, а не всей памяти SolidCraft
или нативной CAD-работы. Независимый максимальный срок выполнения остаётся 30 секунд.

Отдельные запуски CLI и MCP без окна используют плагины, установленные для настольной программы; данные там
одобрения действуют на время запуска. Добавьте `--keep-plugin-approvals`, чтобы сохранить их между запусками, совместно
с настольной программой, так что плагин устанавливается и одобряется один раз, и `--plugins-dir DIR`, чтобы использовать
отдельный набор плагинов и одобрений, например в CI. Список сохранённых одобрений:
`solidcraft-cli --keep-plugin-approvals exec plugin.grants`, отозвать одно:
`solidcraft-cli --keep-plugin-approvals exec plugin.revoke '{"id":"PLUGIN_ID"}'`
([Использование без окна](docs/plugins.md#headless-use)).

<a id="permissions-results-and-saved-designs"></a>
### Разрешения, результаты и сохранённые проекты

Плагин может вызывать любую команду каталога MCP, точный идентификатор которой перечислен в его манифесте. Команды, которые
выходят за пределы открытого проекта, сгруппированы: `file` (сохранение, экспорт, импорт, вставка из файлов,
библиотек), `doc` (открытие или переключение проектов), `app` (настройки, окно, диагностика) и `plugin`
(просмотр или запуск плагинов). Каждая группа отклоняется, пока манифест не запросит её в
`runtime.permissions.command_groups` и пользователь её не выдаст; в этой версии интерфейса выдачи ещё нет.
Вызовы файловой системы требуют совпадающих разрешений манифеста и одобренных прав на папки. Часы
требуют своего разрешения в манифесте; иначе возвращают фиксированную эпоху. API WASI, сокетов и процессов
не подключаются. Контейнер проекта резервирует `plugins/<plugin-id>/` для собственных данных плагина, они сохраняются
и записываются обратно нетронутыми, если плагина нет; плагины не могут читать или писать туда, пока не появится
возможность `storage`.
Команды просмотра могут раскрывать данные модели, поэтому их тоже рассматривайте как разрешения. В частности, необязательное
разрешение `model.mesh` отдаёт вычисленные вершины и треугольники запрошенного тела в координатах его
компонента (миллиметры), с явными пределами передачи. Никакого преобразования оно не выполняет.

Правки идут по изолированной копии проекта. Принимается только успешный вызов, как **один шаг
«Отменить»**. Ловушка, исчерпание топлива, предел памяти, неверный результат или отклонённый вызов хоста отбрасывают
транзакцию, сохраняя предыдущий проект и историю отмены и повтора. Хост проверяет полученные
нативные операции, прежде чем принять их. Плагин, который перехватил отклонённый вызов хоста, не может зафиксировать
более раннюю частичную правку. Тяжёлые для процессора гостевые циклы ограничены топливом и сроком; руководство объясняет
отдельную стоимость компиляции компонента и выполнения разрешённой нативной команды.

Результат — обычные нативные операции: они сохраняются, отменяются, повторяются и перестраиваются без плагина.
Удаление пакета отключает будущие вызовы; уже созданные операции оно не удаляет.
Изменение собственных параметров плагина в этой первой версии означает ещё один вызов; крюка
оценки шкалы, принадлежащего плагину, пока нет. Выключите установленный плагин в «Настройки > Плагины»,
чтобы отклонять последующие вызовы настольной программы. Его отключение или смена потолков ресурсов во время ожидающего
вызова препятствует принятию результата. Процессы
CLI имеют свою политику сеанса и не читают настройки настольной программы.

Полный манифест, граница поддерживаемых команд, пределы, параметры сборки, тесты и текущие ограничения — в [руководстве по среде и для авторов](docs/plugin-runtime.md).
Пошаговые проверки пакета и ожидаемые результаты — в [английском руководстве по тестам](docs/plugin-test-guide.md). Существующий
[проект параметрических плагинов](docs/plugins.md) остаётся отдельной будущей фазой.

<a id="contributing"></a>
## Участие

Помощь приветствуется. [CONTRIBUTING.md](CONTRIBUTING.md) описывает, как собирать и тестировать, карту кода,
правила чистой комнаты и лицензии и где помощь нужнее всего. Открытая работа — в
[обращениях GitHub](https://github.com/tangency-labs/solidcraft/issues); общение — в
[Discord](https://discord.gg/FtU4NQNVDH).

<a id="sponsors"></a>
## Спонсоры

[![CI powered by Blacksmith](docs/sponsors/blacksmith-ci-powered.png)](https://www.blacksmith.sh)

Непрерывная интеграция SolidCraft работает на [Blacksmith](https://www.blacksmith.sh), который
оплачивает её минуты CI.

<a id="disclaimer"></a>
## Отказ от ответственности

Файлы в этом репозитории предоставляются как есть, без гарантий, ответственности и возмещения убытков, и
Tangency Labs и участники не несут ответственности за любое вредное или противоправное их
использование: читайте [DISCLAIMER.md](DISCLAIMER.md).

<a id="licence"></a>
## Лицензия

MIT OR Apache-2.0, на ваш выбор. Разработка ведётся по
[правилам вклада по принципу чистой комнаты](AGENTS.md); сторонний код и ресурсы сохраняют свои
задокументированные лицензии и указание авторства.

Бренд и интерфейс SolidCraft лицензируются отдельно, на условиях
[LICENSE-BRAND](LICENSE-BRAND): набор элементов интерфейса, внешний вид (значки интерфейса, глифы, встроенные темы),
токены оформления и палитры темы, а также имя, логотип и значок программы SolidCraft. Их можно свободно использовать
как часть SolidCraft. Использование в другой программе или продукте сначала требует письменного разрешения
сопровождающих.

SolidCraft независим. Поведение проектируется по открытой документации, общим соглашениям CAD
и отзывам пользователей. Эталонные тесты используют аналитические значения и инструменты с открытым исходным кодом.
SolidCraft не связан с Autodesk, Dassault Systèmes, PTC,
Siemens или любым другим поставщиком CAD, не спонсируется и не одобряется ими. Fusion, AutoCAD, Inventor, SolidWorks, Onshape, Creo, Blender и
Tinkercad являются товарными знаками соответствующих владельцев и названы только для описания совместимости
(см. [NOTICE](NOTICE)).

[badge-windows]: https://img.shields.io/badge/Windows-Download-0078D6?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yIDJoOS41djkuNUgyek0xMi41IDJIMjJ2OS41aC05LjV6TTIgMTIuNWg5LjVWMjJIMnpNMTIuNSAxMi41SDIyVjIyaC05LjV6Ii8%2BPC9zdmc%2B
[badge-macos]: https://img.shields.io/badge/macOS-Download-333333?style=for-the-badge&logo=apple&logoColor=white
[badge-linux]: https://img.shields.io/badge/Linux-AppImage-E95420?style=for-the-badge&logo=linux&logoColor=white
[badge-snap]: https://img.shields.io/badge/Snap-Snap_Store-82BEA0?style=for-the-badge&logo=snapcraft&logoColor=white
[badge-web]: https://img.shields.io/badge/Web-Try_in_browser-2EA44F?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIvPjxwYXRoIGQ9Ik0yIDEyaDIwTTEyIDJhMTUgMTUgMCAwIDEgMCAyME0xMiAyYTE1IDE1IDAgMCAwIDAgMjAiLz48L3N2Zz4%3D
[windows-msi]: https://github.com/tangency-labs/solidcraft/releases/latest/download/solidcraft-windows-x64.msi
[macos-dmg]: https://github.com/tangency-labs/solidcraft/releases/latest/download/solidcraft-macos-universal.dmg
[linux-appimage]: https://github.com/tangency-labs/solidcraft/releases/latest/download/solidcraft-linux-x86_64.AppImage
[snap-store]: https://snapcraft.io/solidcraft
[web-app]: https://solidcraft.io/app

