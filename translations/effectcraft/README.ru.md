# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/effectcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/effectcraft
Коммит исходника (последний, в котором менялся README.md): 5a0dde4e62f62c872cb4d0c0c5e5f455a754ed65
Дата коммита: 20 ноября 2026, 03:09 (America/Los_Angeles, PT); в исходнике 2026-11-20T11:09:23Z
SHA256 исходника: 5828a7cc0951d9e3237a96ea792de16e28f4cc1272972183974606b84c30c76c
Git blob SHA: ec18dde2129efd073b241f8aac00f5bf8b3faba2
Размер исходника: 27584 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/effectcraft/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.effectcraft.png" width="128" height="128" alt="Значок EffectCraft: гравированный единорог на розовой плитке">
</p>

<h1 align="center">EffectCraft</h1>

<p align="center">
  <b>Моушн-графика и визуальные эффекты; профессиональная студия моушн-графики и визуальных эффектов с открытым исходным кодом, написанная на чистом Rust.</b>
</p>

<p align="center">
  Бесплатный композитор с открытым исходным кодом: композиции, слои,
  ключевые кадры, 308 эффектов, стили слоя, выражения, 3D-камеры и источники света и очередь визуализации; нативно в macOS,
  Windows и Linux и в браузере. Молодой, быстро развивается и уже пригоден к работе.
</p>

<p align="center">
  <img alt="Status: young and moving fast" src="https://img.shields.io/badge/status-young%20and%20moving%20fast-e0368f?style=flat-square">
  <img alt="Written in Rust" src="https://img.shields.io/badge/rust-1.95%2B-b0206c?style=flat-square&logo=rust&logoColor=white">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-555?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_effectcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/effectcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/effectcraft"><b>EffectCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/effectcraft-hero.png" alt="Главное окно EffectCraft: анимированная демонстрационная композиция в панели «Композиция», панель «Проект», шкала времени со слоями текста, фигур и солидов и панель «Свойства» с трансформированием, шрифтом и параметрами абзаца выделенного текстового слоя" width="100%">
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Цифра, генеративное искусство, музыка,
> игры &mdash; если вы что-то создаёте, вы один из нас. **[Загляните в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#what-effectcraft-is">Что это</a> ·
  <a href="#animate">Анимация</a> ·
  <a href="#effects">Эффекты</a> ·
  <a href="#3d">3D</a> ·
  <a href="#export">Экспорт</a> ·
  <a href="#built-for-agents">Агенты</a> ·
  <a href="#get-started">С чего начать</a> ·
  <a href="#where-it-stands">Состояние</a> ·
  <a href="#how-its-made">Как это устроено</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">Лицензия</a>
</p>

<a id="what-effectcraft-is"></a>
## Что такое EffectCraft

EffectCraft — для анимированных титров, моушн-графики и композитинга: того, что нужно
моушн-дизайнерам и художникам по визуальным эффектам. Вы собираете композицию из слоёв (солиды, фигуры,
текст, футаж, другие композиции), анимируете их свойства ключевыми кадрами, накладываете эффекты
и визуализируете результат.

Интерфейс ощущается естественно и отзывчиво: отдельные панели («Проект», «Композиция», «Шкала времени»,
«Слой», «Футаж», «Элементы управления эффектом», «Инструменты», «Просмотр», «Эффекты и наборы», «Звук», «Сведения», «Абзац»,
«Символ», «Выравнивание», «Ход работы», «Очередь визуализации») и обычные сочетания клавиш моушн-графики, а в нескольких местах мы идём дальше,
потому что это важно для нас:

- **Импорт и экспорт Lottie встроены**, так что анимацию можно сразу отдать в веб и приложения
  без подключаемого модуля.
- **Файл проекта, который можно прочитать.** Проекты — версионированный JSON (`.ecproj`), поэтому они чисто расходятся
  в системе контроля версий.
- **Всё можно сценарировать.** Действия меню, правки шкалы времени и изменения свойств выведены как
  команды. Команды движка доступны через CLI, JSON-канал управления и MCP;
  команды только интерфейса идут через диспетчер оболочки и вызываются по каналу управления
  или через подключённый мост MCP.
- **Без FFmpeg.** Декодирование и кодирование видео и звука — на чистом Rust: кодеки FilmCraft и
  собственные кодировщики EffectCraft для VP9, AV1, HEVC и Opus.

<a id="animate"></a>
## Анимация

Панели, меню и сочетания клавиш следуют обычным соглашениям моушн-дизайна:
«Проект», «Композиция», «Шкала времени», «Элементы управления эффектом», «Свойства», «Эффекты и наборы», «Символ»,
«Абзац», «Выравнивание», «Сведения», «Просмотр», «Звук» и «Очередь визуализации» стыкуются так, как вы ожидаете. Перетаскивайте
футаж, композиции и эффекты между ними: на просмотр композиции, где они встают под указателем,
или на шкалу времени — между слоями и в тот момент времени, на который вы указываете.

- **Слои всех видов:** солиды, фигуры, текст, футаж, вложенные композиции, нуль-объекты,
  корректирующие слои, камеры и источники света; родительские связи, трек-матты, все 38 режимов смешивания, размытие в движении.
- **Ключевые кадры ведут себя так же:** линейные, Безье, удержание, автоматическое и непрерывное Безье, плавающие
  ключи, Easy Ease (F9), диалоги «Скорость ключевого кадра» и «Интерполяция», копирование и вставка в текущий
  момент, и **редактор графиков** с графиками значения и скорости и перетаскиваемыми манипуляторами.
- **Время:** переназначение времени, растяжение времени, обращение времени, стоп-кадр, рабочая область, маркеры, точный
  покадровый тайминг на любой частоте кадров, включая 29,97 с выпадающими кадрами.
- **Фигуры и маски:** слои фигур с обрезкой контуров, повторителями, скруглением углов, смещением, зигзагом,
  скручиванием, покачиванием, слиянием контуров и градиентными обводками; маски, нарисованные инструментом «Перо», с режимами,
  растушёвкой, расширением и правкой вершин в окне просмотра.
- **Текст:** точечный и абзацный текст с настоящей формой набора любым шрифтом, установленным на машине, панели
  «Символ» и «Абзац» и текстовые аниматоры с селекторами диапазона.
- **Выражения:** JavaScript по стандартной модели выражений моушн-графики (`wiggle`, `loopOut`,
  `thisComp.layer("…")`, векторная математика на массивах), встроенный редактор и указатель привязки (pick-whip).
- **Шкала времени, какую вы знаете:** раскрывайте слои к «Трансформированию», маскам, эффектам и остальному; перетаскивайте
  строки, чтобы менять порядок слоёв; переименовывайте клавишей Enter или двойным щелчком; сочетания свойств (A, P, S,
  R, T, M, F, E, L, U и их двойные нажатия AA, PP, SS, RR, TT, MM, FF, EE, LL, UU), Shift, чтобы
  добавить свойства, Alt+Shift+A/P/S/R/T, чтобы поставить ключ в текущий момент, Ctrl+` чтобы свернуть выделенные слои.
- **Инструменты марионетки:** булавки «Положение», «Расширенный», «Изгиб», «Крахмал» и «Перекрытие» на сетке, построенной из
  слоя, запись булавок в реальном времени, манипуляторы поворота и масштаба, булавки, которыми управляют (или которые несут) нуль-объекты для
  оснастки, и инерция для волос и ткани.

<p align="center">
  <img src="docs/images/effectcraft-graph-editor.png" alt="Редактор графиков показывает сглаженную кривую значения для «Начала диапазона» текстового аниматора и панель кнопок редактора для удержания, линейной интерполяции, автоматического Безье и Easy Ease" width="100%">
</p>

<a id="effects"></a>
## Эффекты

308 встроенных эффектов по категориям, у каждого свои имена параметров, порядок и
значения по умолчанию: размытие и резкость, канал, цветокоррекция («Кривые», «Уровни», «Цветовой тон/Насыщенность», полная
панель цветокоррекции…), искажение («Искривление», «Выпуклость», «Турбулентное смещение», «Привязка перспективы»…), генерация («Фрактальный шум»,
«Градиентный переход», «Обводка», «Рисование», «Аудиоспектр»…), кеинг, мат, шум и зерно, перспектива,
**симуляция** («Трёхмерный излучатель частиц», «Дождь», «Разрушение», «Танец карточек», «Каустика», «Мир волн»…),
стилизация («Свечение», «Стеклянный рельеф»…), **время** («Эхо», «Постеризация времени», «Искажение времени», «Смещение во времени»…),
**звук** («Реверберация», «Параметрический эквалайзер», «Задержка», «Стереомикшер»…), текст, переходы, служебные и элементы управления
выражениями. Все девять **стилей слоя** («Внешняя тень», внутреннее и внешнее свечение, «Скос и рельеф», «Атлас»,
наложения, «Обводка») с общим светом. Просмотр играет звук синхронно, с индикаторами и осциллограммами.

<a id="3d"></a>
## 3D

Классический 3D-композитинг: 3D-слои с ориентацией и параметрами материала,
одно- и двухточечные **камеры** с глубиной резкости, **источники света** (параллельный, прожектор, точечный, рассеянный)
с мягкими тенями по трассировке лучей, слои, которые корректно пересекаются, инструменты камеры «орбита», «панорама» и «тележка»,
и виды «Спереди», «Сверху», «Слева» и «Пользовательский».

<p align="center">
  <img src="docs/images/effectcraft-3d.png" alt="Демонстрация 3D Showcase в пользовательском виде 1: пересекающиеся карточки, освещённые прожектором с мягкими тенями на сетчатом полу; усечённая пирамида камеры и источник света нарисованы каркасом" width="100%">
</p>

<a id="export"></a>
## Экспорт

Отдельная очередь визуализации с параметрами визуализации и модулями вывода: **H.264** MP4 и
**ProRes** MOV (от Proxy до 4444 XQ с альфой) со звуком, **HEVC** (Main / Main 10) и **AV1**
MP4, **WebM** (VP9 с промежуточными кадрами и альфой или AV1; звук Opus), последовательности PNG, JPEG, TIFF, Targa и 32-битного EXR, анимированный GIF и WAV/AIFF. Черезстрочная
визуализация с pulldown 3:2, переопределения эффектов, соло, направляющих и глубины, кадрирование, область интереса и
изменение размера, шаблоны параметров визуализации и модуля вывода со значениями по умолчанию, действия после визуализации, переполнение
хранилища и журналы визуализации. Та же очередь работает из командной строки. Каждый кодировщик — на чистом
Rust (H.264, ProRes, HEVC, VP9, AV1 и AAC из craft-libs; собственный Opus EffectCraft); внутри нет
FFmpeg.

**Lottie** работает в обе стороны: Файл ▸ Экспорт ▸ Lottie JSON… записывает композицию (прекомпозиции, слои фигур,
солидов, изображений, текста и нуль-объектов, сглаженные и пространственные ключевые кадры, маски, трек-матты, режимы
смешивания, переназначение времени, по желанию выражения) как `.json` или `.lottie` и перечисляет всё, что Lottie
не умеет выразить; Файл ▸ Импорт ▸ Lottie… открывает файл как новую композицию.

<p align="center">
  <img src="docs/images/effectcraft-render-queue.png" alt="Панель «Очередь визуализации» с двумя постановленными в очередь композициями" width="100%">
</p>

<a id="built-for-agents"></a>
## Создано для агентов

Команды движка доступны через CLI, JSON-канал управления и MCP. Командам только интерфейса
нужен диспетчер оболочки запущенной программы: полный доступ к меню требует канала управления
программы или подключённого моста MCP. Сеансы MCP без окна открывают поддерживаемые команды движка,
но не команды только интерфейса и не инструменты `ui_*`, доступные лишь через мост.

- **MCP-сервер:** `effectcraft-cli mcp` говорит по протоколу Model Context Protocol через stdio, без окна
  или с мостом к запущенной программе (`--bridge 9877`). Инструменты покрывают команды, дерево проекта и свойств,
  ключевые кадры и визуализированные кадры. В этом репозитории уже есть готовый [`.mcp.json`](.mcp.json).
- **Командная строка:** одноразовые вызовы с выводом JSON, например
  `effectcraft-cli set Main '#1' transform/position '[100,360]' --time 0 main.ecproj --save`
  или `effectcraft-cli render --comp Main --out main.mp4`, или
  `effectcraft-cli exec file.exportLottie '{"comp":"Main","path":"main.json"}' main.ecproj`.
- **Канал управления:** `effectcraft --control 9877` принимает строки JSON, чтобы выполнять команды, осматривать
  и нажимать любой виджет по его идентификатору автоматизации и делать снимки экрана.

См. [docs/agents.md](docs/agents.md) и [docs/control-protocol.md](docs/control-protocol.md).

<a id="get-started"></a>
## С чего начать

Установщики каждой версии лежат на странице [выпусков](https://github.com/storytold/effectcraft/releases):
универсальная программа для macOS; MSI и переносные zip для Windows x64, x86 и ARM64; Linux
AppImage, Flatpak, deb, rpm и tar.gz для x86_64 и aarch64, плюс tar.gz для riscv64; архив FreeBSD x86_64; и
веб-сборка. В [Загрузках](#downloads) перечислен каждый файл. Сборка Windows ARM64 работает нативно в
Windows on ARM, без эмуляции x64. CI устанавливает этот MSI на оборудовании Windows 11 ARM64, проверяет,
что обе программы — ARM64, и запускает там инструмент командной строки, но пока не открывает окно программы
и не гоняет набор испытаний нативно на ARM64, поэтому сообщайте, если что-то ведёт себя иначе.

В Gentoo сообщество в оверлее [::snakebyte overlay](https://github.com/switch87/snakebyte-overlay) упаковывает
выпуск для Linux как `media-video/effectcraft-bin` (команда EffectCraft его не сопровождает):

```sh
eselect repository add snakebyte git https://github.com/switch87/snakebyte-overlay.git
emaint sync -r snakebyte
echo 'media-video/effectcraft-bin ~amd64' >> /etc/portage/package.accept_keywords/effectcraft
emerge --ask media-video/effectcraft-bin
```

Чтобы собрать самостоятельно, нужен [Rust](https://rustup.rs/) 1.95 или новее.

```sh
git clone https://github.com/storytold/effectcraft
cd effectcraft
cargo run --release -p effectcraft          # the app (add `-- --demo` to open the demo project)
cargo run --release -p effectcraft-cli -- render --out intro.mp4    # render the demo headless
cargo xtask web --serve 8765                # the browser build on http://127.0.0.1:8765/ (docs/web.md)
```

Впервые здесь? [docs/footage.md](docs/footage.md) рассказывает, как импортировать футаж и последовательности изображений и про
«Интерпретацию футажа».

Чтобы работать над программой: `cargo test --workspace`, и проверки для изменённых вами крейтов (`cargo xtask ci --affected`; полный `cargo xtask ci` покрывает формат, линтеры,
испытания, слоистость, указание авторства ресурсов и сборку WebAssembly). См. [CONTRIBUTING.md](CONTRIBUTING.md),
[docs/architecture.md](docs/architecture.md) и [docs/testing.md](docs/testing.md).

<a id="where-it-stands"></a>
## Где мы сейчас

EffectCraft молод: первый коммит был 1 октября 2026. Обширный набор возможностей
уже есть, включая 308 эффектов, но широта — это ещё не полная зрелость в каждом крайнем
случае. Сегодня это хорошее место, чтобы попробовать и рассказать нам, что ломается. Пока мы не рекомендуем его
для заказной производственной работы. В частности:

- **Собственный формат проекта.** Проекты сохраняются как `.ecproj`, читаемый версионированный JSON. Закрытые
  форматы проектов и подключаемые модули After Effects SDK не поддерживаются.
- **Точность ещё уточняется.** Автоматические испытания визуализации сейчас сосредоточены на небольших
  композициях, поэтому сообщайте о визуальных расхождениях и неожиданном поведении.
- **macOS — самая испытанная платформа.** В Linux и Windows пользователи сталкивались с простыми ошибками взаимодействия,
  их мы исправляем в первую очередь.
- **Обученные модели новые.** Кисть ротоскопии может использовать MobileSAM (необязательная загрузка 40 МБ в
  Настройки ▸ Кисть ротоскопии), а слежение за лицом — Google MediaPipe Face Landmarker (необязательная
  загрузка 3,8 МБ в Настройки ▸ Слежение за лицом). Оба сейчас активно оцениваются и настраиваются.

EffectCraft в **альфе**: около 91% возможностей, учтённых в
[docs/target-app-parity.md](docs/target-app-parity.md), уже есть, и мы оцениваем путь к полной готовности
для профессиональной производственной работы примерно в 45%. План — в [ROADMAP](ROADMAP.md),
измерение — в [docs/target-app-parity.md](docs/target-app-parity.md), а каждый известный пробел — в [docs/gaps.md](docs/gaps.md).
Веб-сборка ([docs/web.md](docs/web.md)) запускает полную программу в браузере.
[Сообщения об ошибках](https://github.com/storytold/effectcraft/issues) сейчас для нас самое полезное,
что вы можете прислать.

<a id="how-its-made"></a>
## Как это устроено

- **Сначала движок.** Стопка небольших крейтов со строгой слоистостью. Интерфейс (egui) сидит
  сверху, и ничто ниже от него не зависит.
- **Чистая комната.** Мы работаем по открытой документации и наблюдаемому поведению, никогда
  по закрытым файлам, значкам, наборам или коду. Код из GPL-проектов не копируется. Полные правила
  — в [AGENTS.md](AGENTS.md).
- **По умолчанию приватно.** Никакой телеметрии и никакого доступа к сети, пока вы об этом не попросите.
- **Одна семья.** EffectCraft разделяет с FilmCraft модель времени и устройство текстового движка и
  берёт у него видео- и аудиокодеки.

<a id="downloads"></a>
## Загрузки

**Впервые в EffectCraft?** Скачайте программу со [страницы EffectCraft на getartcraft.com](https://getartcraft.com/apps/effectcraft). Так установить проще всего.

**Нужна конкретная сборка или формат?** На GitHub в [последнем выпуске](https://github.com/storytold/effectcraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/effectcraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `effectcraft-<ver>-windows-x64.msi` | `effectcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `effectcraft-<ver>-windows-arm64.msi` | `effectcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `effectcraft-<ver>-windows-x86.msi` | `effectcraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы подписаны. Установщик спрашивает, для кого ставить EffectCraft и куда. По умолчанию он ставит только для вашей
учётной записи, в `%LOCALAPPDATA%\Programs\ArtCraft\EffectCraft`, без запроса прав администратора;
вариант «Все на этом компьютере» ставит в `C:\Program Files\ArtCraft\EffectCraft` (`Program Files (x86)` для 32-разрядной сборки). Последующие версии
ставятся в ту же папку. Чтобы установить молча
в выбранную папку: `msiexec /i effectcraft-<ver>-windows-x64.msi /qn INSTALLFOLDER="D:\Apps\EffectCraft"`.
Молчаливая установка по умолчанию — для одного пользователя. `INSTALLFOLDER` выбирает папку, а не то, для кого ставится программа;
добавьте `ALLUSERS=1` из повышенного терминала или средства развёртывания для установки для всех пользователей.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `effectcraft-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `effectcraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `effectcraft-<ver>-linux-x86_64.AppImage` | `effectcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `effectcraft-<ver>-linux-x86_64.flatpak` | `effectcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `effectcraft-<ver>-linux-x86_64.deb` | `effectcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `effectcraft-<ver>-linux-x86_64.rpm` | `effectcraft-<ver>-linux-aarch64.rpm` | |
| Архив | `effectcraft-<ver>-linux-x86_64.tar.gz` | `effectcraft-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

RISC-V 64-разрядный: `effectcraft-<ver>-linux-riscv64.tar.gz` (только архив; нужен glibc 2.39+, например Ubuntu 24.04+ или Debian 13+).

**Перетаскивание файлов в Linux:** текущая нативная подсистема Wayland в eframe/winit 0.30 не
доставляет события наведения и бросания файлов. В Hyprland и других нативных сеансах Wayland используйте
**Файл ▸ Импорт ▸ Файл…** (принимает несколько файлов) или запустите EffectCraft через XWayland, если
XWayland установлен и задан `DISPLAY`:

```sh
env -u WAYLAND_DISPLAY effectcraft
```

Когда подсистема доставляет события (X11/XWayland, Windows и macOS), бросание медиа в любое место
окна импортирует их, а при наведении появляется подсказка цели. В нативном Wayland программа
не может заметить попытку, которая не порождает событие; вместо этого при запуске показывается уведомление
с запасным путём «Файл ▸ Импорт».

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `effectcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `effectcraft-web-<ver>.zip` | Работает в современном браузере; разместите на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

EffectCraft — одно из приложений **Crafting Apps**: бесплатных творческих инструментов с открытым исходным кодом от команды
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
  <a href="https://getartcraft.com/apps/effectcraft">EffectCraft</a>
</p>

<a id="license-and-credits"></a>
## Лицензия и благодарности

EffectCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the EffectCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и EffectCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>

<a id="star-history"></a>
## История звёзд

[![Star History Chart](https://api.star-history.com/svg?repos=storytold/effectcraft&type=Date&legend=top-left)](https://www.star-history.com/?repos=storytold%2Feffectcraft&type=date&legend=top-left)
