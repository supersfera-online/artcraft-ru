# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/soundcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/soundcraft
Коммит исходника (последний, в котором менялся README.md): a02d892f831f0a4e1220e0357c7b941030b9cd6f
Дата коммита: 18 ноября 2026, 17:37 (America/Los_Angeles, PT); в исходнике 2026-11-19T01:37:06Z
SHA256 исходника: 091a183bf77f6fa1c5abba4bdab96304c934a218954613632b4e3a9ff8550420
Git blob SHA: 05e51da1143ff4797b67e2abd5552d9c1505e088
Размер исходника: 29855 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/soundcraft/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.soundcraft.png" width="128" height="128" alt="Значок SoundCraft: поющая птица на синей плитке">
</p>

<h1 align="center">SoundCraft</h1>

<p align="center">
  <b>Запись, правка и сведение звука; современная цифровая аудиостанция (DAW) с открытым исходным кодом, построенная на чистом Rust.</b>
</p>

<p align="center">
  Полноценная цифровая аудиостанция, которая работает нативно в macOS, Windows, Linux и FreeBSD и
  в браузере. Многодорожечный монтаж, полный микшер с подключаемыми модулями, посылами и автоматизацией, MIDI, запись
  и сведение, и каждое действие можно задать сценарием из командной строки или ИИ-агентом.
</p>

<p align="center">
  <img alt="Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="egui" src="https://img.shields.io/badge/UI-egui-14a9c4?style=flat-square">
  <img alt="Platforms" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-0b7385?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue?style=flat-square">
  <img alt="Status: pre-alpha" src="https://img.shields.io/badge/status-pre--alpha-orange?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_soundcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/soundcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/soundcraft"><b>SoundCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<p align="center">
  <img alt="Окно «Правка» SoundCraft с сеансом из девяти дорожек: ударные, бас, пэд, клавиши и соло, вспомогательная дорожка реверберации и фейдер мастера" src="docs/images/edit.png" width="100%">
  <br>
  <sub>Окно «Правка»: дорожки, формы волны, MIDI, линейки, маркеры и транспорт; играет встроенная демонстрационная песня (каждый звук в ней синтезирован самим SoundCraft).</sub>
</p>

> [!NOTE]
> **ArtCraft — это сообщество художников из самых разных сфер.** Живописцы, фотографы,
> кинематографисты, иллюстраторы, дизайнеры, аниматоры, любители и те, кто взял карандаш
> на прошлой неделе. Если вы что-то создаёте, вы один из нас. **[Заходите поздороваться в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#what-it-does">Что делает</a> ·
  <a href="#getting-started">С чего начать</a> ·
  <a href="#for-agents-and-scripts">Агенты и сценарии</a> ·
  <a href="#how-its-built">Как это устроено</a> ·
  <a href="#status-and-roadmap">Состояние</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">Лицензия</a>
</p>

<a id="what-it-does"></a>
## Что делает

SoundCraft следует рабочему процессу, который звукорежиссёры уже знают: **окно «Правка»** для компоновки и
монтажа, **окно «Микшер»** для баланса, режимы правки, инструменты, плейлисты, точки памяти, обработка
AudioSuite и всё остальное. Если вы годы работали в таком процессе, руки уже должны знать,
где что находится.

<table>
  <tr>
    <td width="50%"><img alt="Окно «Микшер» с канальными линейками, инсертами, посылами, входами и выходами, ручками панорамы, фейдерами и измерителями и окном подключаемого модуля эквалайзера" src="docs/images/mix.png"></td>
    <td width="50%"><img alt="Редактор MIDI: соло-мелодия в виде фортепианной ленты с дорожкой велосити" src="docs/images/midi.png"></td>
  </tr>
  <tr>
    <td><b>Окно «Микшер».</b> Десять инсертов и десять посылов на дорожку, шины и вспомогательные входы, фейдеры мастера, VCA, папки маршрутизации, solo-in-place с неявным соло и измерители с удержанием пика.</td>
    <td><b>Редактор MIDI.</b> Инструментальные дорожки со встроенными синтезаторами, фортепианная лента с дорожкой велосити, пошаговый ввод, квантование, транспонирование, импорт и экспорт Standard MIDI File.</td>
  </tr>
  <tr>
    <td width="50%"><img alt="Автоматизация громкости, нарисованная на дорожке Pad, с открытыми окнами «Точки памяти» и «Большой счётчик»" src="docs/images/automation.png"></td>
    <td width="50%"><img alt="Значок приложения SoundCraft: поющий соловей на бирюзовом поле" src="assets/app-icon/soundcraft-1024.png" width="70%"></td>
  </tr>
  <tr>
    <td><b>Автоматизация и маркеры.</b> Автоматизация точками для громкости, панорамы, отключения звука, посылов и каждого параметра подключаемого модуля, запись вживую в режимах Write, Touch и Latch, плюс точки памяти и большой счётчик.</td>
    <td><b>Везде.</b> Подписанные сборки для macOS (универсальные), Windows (x64, x86, Arm), Linux (AppImage, deb, rpm, Flatpak), FreeBSD и сборка WebAssembly, которая работает в браузере.</td>
  </tr>
  <tr>
    <td width="50%"><img alt="Окно «Видео» с тестовым роликом цветных полос и впечатанным таймкодом, над видеодорожкой с миниатюрами в окне «Правка»" src="docs/images/video.png"></td>
    <td width="50%"><img alt="Окно «Рендерер» со схемой акустики 7.1.4 и двумя объектными дорожками, рядом с окном «Микшер» с панорамами окружения и кнопками Object/Bed" src="docs/images/surround.png"></td>
  </tr>
  <tr>
    <td><b>Видео.</b> Дорожка изображения с миниатюрами и окно «Видео», которое следует за головкой воспроизведения, декодирование H.264, ProRes и Motion JPEG на чистом Rust, с впечатыванием таймкода и смещением синхронизации.</td>
    <td><b>Окружение и иммерсивный звук.</b> Форматы основной шины и шин от стерео до 9.1.6 и Ambisonics, панорама окружения с расхождением и высотой, маршрутизация объект/подложка и окно «Рендерер» с живыми уровнями колонок.</td>
  </tr>
  <tr>
    <td width="50%"><img alt="Редактор партитуры: соло-мелодия в стандартной нотации на скрипичном и басовом стане" src="docs/images/score.png"></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Нотация.</b> Редактор партитуры для MIDI-дорожек, экспорт MusicXML для Sibelius и других нотных программ и печатные гравированные партитуры.</td>
    <td><b>И ваши подключаемые модули тоже.</b> CLAP, VST3 и Audio Units, с собственными редакторами, состоянием, сохранённым в сеансе, и каждым экземпляром, создаваемым вне звукового потока.</td>
  </tr>
</table>

<a id="feature-tour"></a>
### Обзор возможностей

- **Монтаж:** режимы Shuffle, Slip, Spot и Grid; инструменты Smart, Selector, Grabber, Trim, Pencil, Zoom и
  Scrubber; вырезать, копировать, вставить, дублировать, повторить, сдвинуть, вставить тишину, разделить (по
  выделенному, по сетке, по транзиентам), срастить, консолидировать, убрать тишину, подтолкнуть; затухания и
  перекрёстные затухания пяти форм, рисуемые прямо из углов клипа; плейлисты с дорожками компиляции;
  линии усиления клипа; группы правки; одноклавишные сочетания Commands Focus; прокрутка тачпадом, которая
  следует за пальцами, и масштабирование щипком вокруг указателя; отмена для всего.
- **Сведение:** фейдер и панорама с автоматизацией, посылы pre/post, шины, вспомогательные входы, фейдеры мастера,
  мастера VCA, папки маршрутизации, режимы соло, группы отключения звука и соло, инверсия фазы и подрезка, эффекты
  клипа и автоматическая компенсация задержки подключаемых модулей.
- **Автоматизация:** громкость, панорама, отключение звука, посыл и каждый параметр подключаемого модуля; проходы Write, Touch, Latch и
  Trim, записываемые вживую с фейдеров; прореживание, скольжение, слияние и перевод в усиление клипа.
- **Подключаемые модули:** 7-полосный и 1-полосный эквалайзер, компрессор/лимитер, экспандер/гейт, деэссер, максимайзер,
  канальная линейка, комнатные и пластинчатые ревербераторы, модуляционная задержка, автопанорама, хорус, фленжер, фейзер, кольцевой
  модулятор, сдвиг частоты, сатуратор, lo-fi, выпрямитель, субгармоник, сдвиг высоты, сдвиг
  времени, усиление, подрезка, инверсия, удаление постоянной составляющей, генератор сигнала, дизеринг, субтрактивный синтезатор, барабанный
  синтезатор и сэмплер (играет любой WAV, AIFF, FLAC, MP3 или OGG по клавиатуре) — всё оригинальное.
  **Подключаемые модули CLAP** тоже загружаются. Любой процессор работает офлайн как AudioSuite, а пользовательские пресеты сохраняются
  для каждого модуля.
- **MIDI:** инструментальные и MIDI-дорожки, редактор MIDI с фортепианной лентой и дорожкой велосити, список
  событий, вид партитуры, пошаговый ввод, квантование, транспонирование, свойства в реальном времени, Standard MIDI File
  и Audio-to-MIDI из спетой или сыгранной мелодии. MIDI-клавиатуры играют инструменты вживую и
  записываются в MIDI-клипы ([как](docs/midi-input.md)).
- **Запись:** включение записи по выделенному или на лету, предварительный и последующий прогон, запись в цикле с
  плейлистом на каждый дубль, контроль входа через всю канальную линейку и автосохранение с восстановлением.
- **Время и темп:** такты|доли, мин:сек, таймкод (каждая частота, включая drop-frame),
  футы+кадры и сэмплы; карты темпа и размера с редактором темпа; линейные, параболические и
  S-образные рампы темпа; тональности и распознанные аккорды; анализ долей и определение доли;
  деформация Elastic Audio с сохранением высоты.
- **Звуковые файлы:** WAV/BWF/RF64, AIFF/AIFC и FLAC на вход и выход; MP3, Ogg Vorbis, AAC, ALAC, CAF
  и звук фильмов MP4/MOV на вход. Любая частота дискретизации и разрядность.
- **Сведение в файл:** микс или стемы в WAV, AIFF или FLAC при 16/24/32-bit float с необязательным дизерингом и
  нормализацией, с отчётом пика, истинного пика и интегрированной громкости (LUFS).
- **Быстро:** параллельный движок сведения, отмена с копированием при записи и интерфейс, который держит 120 кадров в секунду
  при воспроизведении семидесяти с лишним дорожек.

<a id="getting-started"></a>
## С чего начать

Скачайте сборку со [страницы выпусков](https://github.com/storytold/soundcraft/releases) или соберите
из исходников на Rust 1.95 или новее:

```sh
git clone https://github.com/storytold/soundcraft
cd soundcraft
cargo run --release -p soundcraft -- --demo     # opens the demo song
```

В Linux нужны заголовки ALSA (`libasound2-dev` в Debian/Ubuntu, `alsa-lib-devel` в Fedora).

Веб-сборка:

```sh
cd apps/soundcraft-web && trunk serve --release   # then open http://127.0.0.1:8080
```

Полезные сочетания: <kbd>Space</kbd> воспроизведение/стоп, <kbd>⌘</kbd><kbd>=</kbd> Микшер/Правка,
<kbd>F1</kbd>–<kbd>F4</kbd> режимы правки, <kbd>F5</kbd>–<kbd>F10</kbd> инструменты, <kbd>⌘</kbd><kbd>E</kbd>
разделить, <kbd>⌘</kbd><kbd>D</kbd> дублировать, <kbd>Enter</kbd> новый маркер, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>N</kbd>
новые дорожки. **Настройка › Сочетания клавиш** перечисляет их все.

В **«Новые дорожки»** у каждой строки свои число, формат, тип, шкала времени «сэмплы/тики» и имя.
**+** добавляет строку ниже, **−** удаляет её; **Создать** создаёт все строки по порядку, одним
шагом отмены (до 128 дорожек за создание). Последняя строка остаётся доступной. Ширина раскрывающихся списков
подстраивается под самый длинный вариант и остаётся фиксированной при смене выбора.

В macOS **⌘←/→** меняет формат активной строки, **⌘↑/↓** — её тип (также с **⌃**),
а **⌥⌘↑/↓** — шкалу времени. **⇧⌃⌘↓/↑** добавляет или удаляет активную строку, также с **⌥**;
работает и **⇧⌘↓/↑**. В Windows/Linux для **⌘** используется **Ctrl**. Активная строка следует за
полем, по которому вы щёлкнули. У новой строки сразу выделено и в фокусе число; Enter создаёт, Escape отменяет.

<a id="midi-keyboards"></a>
### MIDI-клавиатуры

Подключите клавиатуру, включите запись на инструментальной дорожке (её кнопка **R**) и играйте: клавиатура
слышится через инструмент дорожки, а проход записи превращает игру в MIDI-клип.
**Настройка › Движок воспроизведения…** перечисляет MIDI-устройства, у каждого свой переключатель (**Настройка › MIDI › Устройства
ввода MIDI…** открывает то же окно), а селектор входа дорожки выбирает устройство и
канал. Пока опробовано в Linux; в macOS и Windows собирается, но с устройством не проверялось,
а ввода MIDI нет в FreeBSD и в вебе. Руководство —
[docs/midi-input.md](docs/midi-input.md).

<a id="logs"></a>
### Журнал

Настольная программа пишет записи `log` в стандартный поток ошибок и в `logs/soundcraft.log` в каталоге
настроек, рядом с `ui.json`, `Autosave/` и `Presets/` (Linux `~/.config/soundcraft/logs/`
или `$XDG_CONFIG_HOME/soundcraft/logs/`; macOS `~/Library/Application Support/SoundCraft/logs/`;
Windows `%APPDATA%\SoundCraft\logs\`). Запуск из меню рабочего стола или Dock не даёт
терминала, поэтому к сообщению об ошибке прикладывайте этот файл: отчёт паники движка, звуковые устройства, которые не
открылись или сломались, подключаемые модули, которые отказались от сохранённого состояния, собственные сообщения модулей CLAP и файлы,
которые не открылись, попадают туда. Каждый запуск переносит предыдущий журнал в `soundcraft.1.log` (а тот — в
`soundcraft.2.log`), так что журнал аварийного запуска переживает следующий старт. Файл перестаёт
расти на 16 MiB. `--version` файл не пишет, а запуски с `SOUNDCRAFT_NO_PREFS` пишут только в стандартный
поток ошибок.

| Переменная | Действие |
|---|---|
| `RUST_LOG` | Уровни журнала для стандартного потока ошибок и файла журнала. По умолчанию: `info` для собственных крейтов SoundCraft, `warn` для всего остального. Директивы в стиле env_logger подменяют это, например `RUST_LOG=debug`, `RUST_LOG=warn,soundcraft_mix=trace` или `RUST_LOG=info,wgpu_core=warn`; директива, оканчивающаяся на `*`, покрывает все цели, которые с неё начинаются (`soundcraft*=debug`). |
| `SOUNDCRAFT_NO_PREFS` | `1`: настройки не читаются и не пишутся, файла журнала нет (тестовые запуски агентов). |

Поток звука реального времени сам запись не пишет: журнал держит первую, которую регистрирует
(не ожидая и не выделяя память), считает остальные, а поток интерфейса их записывает. Журнал —
`apps/soundcraft/src/logging.rs`. Веб-программа вместо этого пишет в консоль браузера.

<a id="for-agents-and-scripts"></a>
## Для агентов и сценариев

Всё, что можно нажать, — это ещё и команда с идентификатором и параметрами JSON, и те же команды
доступны из меню, клавиатуры, командной строки, канала управления JSON и сервера
[MCP](https://modelcontextprotocol.io). Программные вызовы никогда не открывают диалоги, а
`session.inspect` сообщает точно, что изменилось, так что агент может проверить свою работу.

```sh
# Headless: load the demo, turn the kick down, add an EQ, bounce.
soundcraft-cli run --demo \
  --cmd 'mix.volume={"track":"Kick","db":-6}' \
  --cmd 'mix.insert={"track":"Bass","plugin":"eq_7band"}' \
  --bounce mix.wav

# Drive the running app.
soundcraft --demo --control 7801 &
soundcraft-cli app --port 7801 transport.play
soundcraft-cli app --port 7801 ui.screenshot '{"path":"shot.png"}'

# Give Claude a DAW.
claude mcp add soundcraft -- soundcraft-cli mcp --demo

# Or keep the agent to some folders (reads and writes are separate roots).
soundcraft-cli mcp --automation-read-root DIR --automation-write-root DIR
```

См. [`docs/cli.md`](docs/cli.md) про инструмент командной строки (подкоманды, коды выхода, переменные
окружения, страницы руководства и дополнения), [`docs/control-protocol.md`](docs/control-protocol.md) и
[`docs/mcp.md`](docs/mcp.md). `soundcraft-cli commands` перечисляет каждую команду (`--json` даёт параметры
и сведения каждой в JSON).

Откройте **SoundCraft › Состояние звука сеанса**, чтобы проверить доступность загруженного звука, несовпадение
частоты дискретизации и границы источников клипов во всех плейлистах, включая альтернативные дубли. Отчёт
предлагает кнопку обновления и подсказывает, как устранить каждую проблему. Сценарии могут получить тот же отчёт JSON
командой `soundcraft-cli run --demo --cmd 'session.audio_health={}'`. Это проверяет загруженные носители,
а не файлы на диске, уровни сигнала, подключаемые модули или маршрутизацию.

<a id="how-its-built"></a>
## Как это устроено

SoundCraft — это Cargo workspace из небольших крейтов со строгой слоистостью: всё ниже интерфейса ничего не знает
об egui, поэтому интерфейс можно заменить на другой.

| Крейт | Что делает |
|---|---|
| `soundcraft-time` | Совместимый реэкспорт API индексов сэмплов SoundCraft из `craft-time` |
| `soundcraft-midi` | Standard MIDI File и операции MIDI |
| `soundcraft-dsp` | Подключаемые модули, офлайн-обработка, измерители, громкость, FFT |
| `soundcraft-model` | Совместимый реэкспорт схемы, проверки и JSON API `craft-scraft-format` |
| `soundcraft-mix` | Движок сведения (его разделяют режим реального времени и офлайн) |
| `soundcraft-engine` | Команды, отмена, монтаж, импорт/экспорт, сведение в файл |
| `soundcraft-playback` | Звуковые устройства (CoreAudio, WASAPI, ALSA, WebAudio), устройства ввода MIDI и запись |
| `soundcraft-automation` | Сервер MCP и клиент канала управления |
| `soundcraft-ui-egui` | Пользовательский интерфейс |

Код никогда не паникует на неверном вводе: ошибки — это значения, а испорченный файл или плохой вызов агента
дают сообщение, никогда не сбой. `cargo xtask ci` запускает форматирование, clippy, тесты, проверки ресурсов
и слоёв и сборку WebAssembly.

<a id="status-and-roadmap"></a>
## Состояние и план

SoundCraft находится в **пре-альфе**: покрывает 94 % пунктов меню предшественника (измерено), около 70 %
его возможностей по наличию и примерно на 40 % готов заменить его в настоящей работе: запись,
монтаж, сведение и выгрузка микса работают от начала до конца, но выбор звукового интерфейса и размера буфера,
запись MIDI с контроллера и обмен сеансами (AAF/OMF) ещё отсутствуют, и это
список для альфы.

**Переводы:** каталог бразильского португальского (`pt-BR`) **на 100 % готов** для каждой фиксированной
строки интерфейса, найденной в текущих исходниках — меню, диалоги и кнопки, подсказки (включая те, что
локализованы внутри кнопок и переключателей), имена доступности, строка состояния окна «Правка», вопрос
об удалении сеанса, форматированные сообщения, шаблоны ошибок движка и текст ошибок движка в момент
показа. Все эти записи покрыты тестом, заполнители совпадают, ключи уникальны, и каталог
`pt-BR` выбирается автоматически, когда `ui.language` равен `pt-BR` (или «Portuguese (Brazil)»)
в `Setup › Appearance`. Ошибки движка сохраняют значения времени выполнения и десятичную запятую в
`pt-BR`. Оставшаяся работа по локализации — проверка формулировок носителем языка (человеком) плюс запасные шрифты CJK /
деванагари / арабские и вёрстка RTL — а не новый перевод интерфейса. Состояние, этап
и наши оценки трудозатрат — в [`ROADMAP.md`](ROADMAP.md); полная оценка — в
[`docs/target-app-parity.md`](docs/target-app-parity.md), ранжированный список того, чего не хватает — в
[`docs/gaps.md`](docs/gaps.md), а сравнение меню за меню — в
[`docs/parity-checklist.md`](docs/parity-checklist.md). Сообщения об ошибках и списки пожеланий
очень приветствуются, в вопросах или в Discord.

<a id="downloads"></a>
## Загрузки

**Скачайте SoundCraft** с GitHub: в [последнем выпуске](https://github.com/storytold/soundcraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/soundcraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `soundcraft-<ver>-windows-x64.msi` | `soundcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `soundcraft-<ver>-windows-arm64.msi` | `soundcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `soundcraft-<ver>-windows-x86.msi` | `soundcraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы подписаны.

**Если программа не открывается в Windows:** настольная программа по умолчанию инициализирует только DirectX 12.
Если позволить wgpu ещё и создать экземпляр OpenGL, некоторые графические драйверы (например,
`atio6axx.dll` AMD) могут аварийно завершиться до появления окна, и программа мелькнёт в «Диспетчере задач» и выйдет.
`WGPU_BACKEND` подменяет значение по умолчанию для диагностики (например `dx12` или `vulkan`). В
PowerShell, из папки с исполняемым файлом:

```powershell
$env:WGPU_BACKEND = "vulkan"
& .\soundcraft.exe
Remove-Item Env:WGPU_BACKEND                     # restore the default for later launches
```

Явная подмена `gl` может вернуть сбой драйвера на затронутых системах. Значения подсистемы по умолчанию для macOS, Linux
и веба не менялись.

Шейдеры DirectX 12 компилируются FXC, который входит в Windows, поэтому `dxcompiler.dll` и
`dxil.dll` не нужны («Parent device is lost» при старте, #185). `$env:WGPU_DX12_COMPILER = "dxc"`
(или `"auto"`) снова выбирает обработку DXC в wgpu для диагностики.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `soundcraft-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `soundcraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `soundcraft-<ver>-linux-x86_64.AppImage` | `soundcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `soundcraft-<ver>-linux-x86_64.flatpak` | `soundcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `soundcraft-<ver>-linux-x86_64.deb` | `soundcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `soundcraft-<ver>-linux-x86_64.rpm` | `soundcraft-<ver>-linux-aarch64.rpm` | |
| Архив | `soundcraft-<ver>-linux-x86_64.tar.gz` | `soundcraft-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

RISC-V (riscv64): только архив `soundcraft-<ver>-linux-riscv64.tar.gz` (glibc 2.39+, например Ubuntu 24.04).

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `soundcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `soundcraft-web-<ver>.zip` | Работает в современном браузере; разместите на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

SoundCraft — одно из приложений **Crafting Apps**: бесплатные творческие инструменты с открытым исходным кодом от команды
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
  <a href="https://getartcraft.com/apps/soundcraft">SoundCraft</a>
</p>

<a id="license-and-credits"></a>
## Лицензия и благодарности

SoundCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the SoundCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Каждый значок интерфейса нарисован в коде, значок программы оригинален, а демонстрационная песня и звук
снимков экрана синтезированы самим SoundCraft, поэтому в этом репозитории нет сэмплов и художественных материалов
от кого-либо ещё.

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и SoundCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>

Дорожки и группы, «Клипы», «Редактор MIDI», «Точки памяти» и «История отмен» используют перемещаемые панели. «Правка» и «Микшер» сохраняют отдельные раскладки; «Клипы» и «Редактор MIDI» относятся к «Правке». Транспорт, окна подключаемых модулей и специальные служебные окна сохраняют свои прежние хозяева. Перетащите заголовок панели к целевому краю или к другому заголовку. Его контекстное меню предлагает «Открепить панель», «Переместить панель в группу» и «Закрыть панель»; меню группы вкладок добавляет «Открепить группу вкладок» и «Закрыть группу вкладок». Существующие переключатели панелей снова открывают панели в сохранённом месте; «Сбросить раскладку панелей» восстанавливает раскладку программы. Плавающие панели остаются внутри текущего окна программы.
