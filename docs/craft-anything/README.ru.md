# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/craft-anything/blob/main/README.md
Репозиторий: https://github.com/storytold/craft-anything
Коммит исходника (последний, в котором менялся README.md): 946f2522db92320fc27ac2a7e0b1653691134d12
Дата коммита: 16 ноября 2026, 02:01 (America/Los_Angeles, PT); в исходнике 2026-11-16T10:01:18Z
SHA256 исходника: 9ea16e568980c2430ad610228c6095f5dcee010ff4f60d06348a7be5b45ac57b
Git blob SHA: ae799016240e49c70ec988062d919227a236c5fd
Размер исходника: 27878 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/craft-anything/main/README.md
Перевод выполнен локально; авторам не отправлялся. Переключатель языков добавлен по образцу уже существующих README.<код>.md этого репозитория.
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.craft-anything.png" width="128" height="128" alt="Значок Craft Anything: гравированный ворон на синей плитке">
</p>

<h1 align="center">Craft Anything</h1>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh.md">简体中文</a> · <a href="README.zh-hant.md">繁體中文</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.pt.md">Português</a> · <a href="README.th.md">ไทย</a> · <a href="README.tr.md">Türkçe</a> · <b>Русский</b>
</p>

<p align="center">
  <b>Смотрите, как устроен любой сайт, программа или игра, и пусть ИИ соберёт вашу собственную версию; открытый движок «чистой комнаты» на чистом Rust.</b><br>
  Укажите цель, скажите, что хотите, и программа изучит оригинал настоящими инструментами осмотра,<br>
  поручит агенту-программисту собрать новый проект, сверит результат с оригиналом и доработает его.
</p>

<p align="center">
  <img alt="100% Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="macOS · Windows · Linux · FreeBSD · Web" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-native-2d81ff?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-3a3a3a?style=flat-square">
  <img alt="Status: early alpha" src="https://img.shields.io/badge/status-early%20alpha-d69e2e?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_craft-anything"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/craft-anything?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="#downloads"><b>Скачать Craft Anything</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/project-website.png" alt="Проект сайта в Craft Anything: проверка перечисляет, что ещё не совпадает, и насколько похожа каждая страница, сборщик сообщает, что его версия готова, карточка разрешения спрашивает перед запуском команды, а в плане выполнены два шага из четырёх" width="100%">
  <br>
  <sub>Проект сайта: каждая проверка говорит, насколько сборка похожа на оригинал, вы подтверждаете всё, что выходит за правила, а план показывает, что осталось.</sub>
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Живописцы, фотографы,
> кинематографисты, иллюстраторы, дизайнеры, аниматоры, любители и те, кто взял карандаш
> в руки только на прошлой неделе. Если вы что-то создаёте, вы один из нас. **[Загляните в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#how-it-works">Как это работает</a> ·
  <a href="#two-ways-to-use-it">Два способа</a> ·
  <a href="#ai">ИИ</a> ·
  <a href="#built-for-agents">Агенты</a> ·
  <a href="#under-the-hood">Под капотом</a> ·
  <a href="#get-started">С чего начать</a> ·
  <a href="#status">Состояние</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="https://discord.gg/artcraft">Discord</a>
</p>

<br>

<table>
  <tr>
    <td width="25%" valign="top">
      <h3>🔍 Изучайте что угодно</h3>
      Сайты, настольные и телефонные программы, игры и файлы: настоящие инструменты осмотра выясняют, как они устроены и что делают, и за каждым ответом стоит свидетельство.
    </td>
    <td width="25%" valign="top">
      <h3>🛠️ Собирайте своё</h3>
      Скажите, что хотите («Воссоздать этот сайт», «Воссоздать игровой процесс этой игры на Rust»), и агент-программист соберёт новый проект в том стеке, который вы назовёте.
    </td>
    <td width="25%" valign="top">
      <h3>✅ Проверено, а не угадано</h3>
      Каждая сборка сравнивается с оригиналом (страницы в трёх ширинах экрана, собственный автотест игры, запуски программы) и дорабатывается, пока не станет близкой.
    </td>
    <td width="25%" valign="top">
      <h3>🤖 Для агентов</h3>
      320 инструментов, каждый из них — команда CLI и инструмент MCP, так что любой агент может управлять тем же движком, что и программа. Чтобы осматривать, ИИ не нужен.
    </td>
  </tr>
</table>

<br>

<a id="how-it-works"></a>
## Как это работает

Направьте Craft Anything на цель, скажите, что хотите, и нажмите «Старт». Работа идёт в четыре шага,
и программа простыми словами спрашивает вас, когда решение за вами:

1. **Изучить:** осмотреть оригинал: его страницы в любой ширине, код, файлы, как он запускается.
2. **Собрать:** агент-программист собирает новый проект на языке, фреймворке или движке, который
   назван в запросе (или на разумном значении по умолчанию).
3. **Проверить:** сравнить сборку с оригиналом и перечислить, что ещё не совпадает.
4. **Готово:** открыть, поиграть или посмотреть результат, либо попросить правки — и программа доработает его.

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/images/make.png" alt="Экран «Сделать»: выберите сайт, программу или игру для воссоздания, введите адрес, выберите «Чистая комната» или Deep, скажите, что хотите, и нажмите «Старт»" width="100%"><br>
      <sub><b>Сделать:</b> выберите, что воссоздать, скажите, что хотите, нажмите «Старт».</sub>
    </td>
    <td width="50%" valign="top">
      <img src="docs/images/project-game.png" alt="Законченный проект игры «змейка»: все шаги выполнены, есть кнопка «Играть»" width="100%"><br>
      <sub><b>Готово:</b> поиграйте в игру или попросите правки ниже.</sub>
    </td>
  </tr>
</table>

<a id="two-ways-to-use-it"></a>
## Два способа работы

- **Простой** (по умолчанию): «Что вы хотите сделать?» Выберите сайт, программу или игру, опишите её,
  нажмите «Старт». Страница проекта показывает четыре шага (Изучить → Собрать → Проверить → Готово), простыми словами — что
  делает агент, карточки вопросов и разрешений, насколько результат похож, и
  кнопки, чтобы открыть результат или его папку. Правки пишите в поле внизу.
  «Только заглянуть внутрь» открывает цель для вопросов, ничего не собирая (в режиме Deep).
- **Расширенный**: полный верстак: все инструменты (Ctrl/Cmd+K), функции, строки, псевдо-C,
  дизассемблирование, hex, графы вызовов, свидетельства, неизвестное, задания, журналы и консоль агента.

Оба режима управляют одним и тем же движком.

<a id="clean-room-or-deep"></a>
## Чистая комната или Deep

- **Чистая комната** (по умолчанию): внутри оригинала ничего не читается — ни код, ни файлы, ни исходный код
  страницы. Craft Anything работает с тем, что можно увидеть: с картинками, которые вы добавляете, с сайтом так, как его видит посетитель
  (снимки экрана, видимый текст, измеренная вёрстка, цвета, шрифты и интервалы, открытые меню)
  и, если вы разрешите, со снимком окна программы. Инструменты, которые заглянули бы внутрь, отклоняются
  и подсказывают, как включить режим Deep.
- **Deep**: используются все инструменты, для вашего личного применения. Код и файлы программы читаются встроенными
  движками (и Ghidra, если она установлена), читается JavaScript сайта, за его стартовой
  страницей ведётся наблюдение, и сборщик может использовать всё это.

«Чистая комната» — это правило о том, что Craft Anything предлагает и в чём отказывает. Это не песочница
операционной системы: она не изолирует ваш компьютер. Агент-программист, которого вы запускаете, по-прежнему действует от вашего имени, а что ему можно
читать, писать или запускать, зависит от его собственных разрешений. Какие из собственных инструментов агента Craft Anything может
отклонить, зависит от агента; про инструменты Claude Code в чатах и вопросах см.
[`docs/claude-code.md`](docs/claude-code.md).

Переключайте в строке заголовка или в «Настройках», командой `settings_set deep_mode true` или для одного запуска CLI ключом
`--deep` (или `--clean-room`).

<p align="center">
  <img src="docs/images/workbench.png" alt="Расширенный верстак: список функций, псевдо-C выбранной функции, агент отвечает на вопрос вызовом инструмента, и журнал свидетельств" width="100%">
  <br>
  <sub><b>Расширенный:</b> функции, псевдо-C, агент и свидетельства за каждым ответом.</sub>
</p>

<a id="ai"></a>
## ИИ

Чтобы собирать, на компьютере нужен агент-программист. **Claude Code** поддерживается первым: Craft
Anything запускает вашу собственную, неизменённую программу `claude`, которая использует ваш вход; Craft Anything
никогда не видит и не обрабатывает вашу учётную запись. Пользование ею идёт по вашему соглашению с
Anthropic. Как и почему — в [docs/claude-code.md](docs/claude-code.md). Адаптер Codex
есть, но на настоящей установке его ещё не проверяли. **GitHub Copilot** может использовать установленный
у вас Copilot CLI через ACP: войдите отдельно командой `copilot login`. **Grok Build** может использовать установленную
у вас программу `grok` через ACP (`grok agent stdio`): войдите отдельно командой `grok login`.
См. [docs/grok.md](docs/grok.md). Других агентов, которые говорят по ACP (Gemini CLI,
Qwen Code, opencode, goose, Hermes, Maki, Devin), можно переключить на него в каждом подключении; из них вживую запускались Maki
и Devin (Devin входит с ключом, сохранённым у подсистемы, — его собственный вход в CLI
через ACP не считается). Anthropic, OpenAI, OpenRouter, xAI (Grok, когда задан `XAI_API_KEY`)
и локальные серверы, совместимые с OpenAI, доступны для вопросов и анализа (Настройки → ИИ).

<a id="built-for-agents"></a>
## Создано для агентов

Каждый инструмент — это также подкоманда CLI и инструмент MCP, так что агент может изучить цель или провести
полную пересборку без программы:

```sh
craft-anything-cli commands                                   # every tool, by toolset
craft-anything-cli mcp                                        # serve them to any MCP client
craft-anything-cli rebuild https://example.com "Recreate this website"
```

Результаты — записи свидетельств с уверенностью, покрытием и ограничениями; большие сначала приходят
как краткое изложение и листаются через `core_evidence_browse`. `craft-anything-cli setup`
подключает Craft Anything к программам агентов-программистов.

<a id="under-the-hood"></a>
## Под капотом

Движок реверс-инжиниринга на чистом Rust с 320 инструментами (300 в движке, остальные — из слоёв ИИ и
настройки) для нативных программ, .NET, Java, Android, Apple, Electron/JavaScript, сайтов,
прошивок, перехватов пакетов, баз данных и игровых файлов. Собственные декодеры, дизассемблер и
декомпилятор работают без внешней программы; режим Deep использует их все, а также Ghidra, если она
установлена. Им питаются настольная программа (egui), CLI и MCP-сервер, а часть работает в
браузере как WebAssembly. Полный список — в [docs/tools.md](docs/tools.md).

<a id="get-started"></a>
## С чего начать

Нужен Rust **1.97 или новее** (его требует зависимость; `rustup update`). В Debian или Ubuntu
настольной программе также нужны:

```sh
sudo apt-get install build-essential libxkbcommon-dev libxkbcommon-x11-0 libwayland-dev libx11-dev libxrandr-dev libxi-dev libgl1-mesa-dev libgtk-3-dev
```

Затем:

```sh
git clone https://github.com/storytold/craft-anything && cd craft-anything
cargo run --release -p craft-anything                # the desktop app
cargo install --path apps/craft-anything-cli         # the CLI, as `craft-anything-cli`
craft-anything-cli doctor                            # checks the install, coding agents and engines
```

Чтобы собирать, на компьютере должен быть выполнен вход в агент-программист (см. [ИИ](#ai)); `doctor` скажет, чего
не хватает. Пересборка из командной строки (вопросы задаются в терминале):

```sh
craft-anything-cli rebuild https://example.com "Recreate this website"
craft-anything-cli rebuild - "A snake game in Rust" --rounds 1
craft-anything-cli rebuild https://example.com "Make the header blue" --continue-in "<project folder>"
craft-anything-cli rebuild - "Add a contact form" --project-folder "<your folder>" --existing edit
```

Новые проекты попадают в `Documents/Craft Anything` (это меняется в Настройки → Общие). В каждой папке
проекта лежат `craft.json` (запрос, цель, состояние и история), `capture/` (то, что записано
с цели), `app/` (порождённый проект), `checks/` (каждое сравнение с
оригиналом), `investigation.cany/` (свидетельства) и `inbox/` (открытые вопросы).

Проект можно также начать в выбранной вами папке («Выбрать папку…» под «Старт» или `--project-folder`).
Если в ней уже есть файлы, вы говорите, что это: сама программа, которую сборщик правит на месте,
или материал для старта, а программа собирается в `app/` рядом с ними (Настройки → Общие могут
запомнить ответ). Настройки → Общие также перечисляют проекты из других папок; удаление
только снимает его со списка.

<a id="status"></a>
## Состояние

> [!IMPORTANT]
> **Состояние:** Craft Anything в ранней альфе. Что уже работает, что частично и что дальше:
>
> - **Уже работает:** настольная программа (простой и расширенный режимы), CLI и MCP-сервер;
>   процесс Изучить → Собрать → Проверить → Готово для сайтов, программ и игр с Claude Code в роли
>   сборщика; проверки сайтов в трёх ширинах экрана; пересборки игр в Unity, Unreal или Godot; режим Deep
>   с Ghidra; порождённые картинки и 3D-модели (по желанию, ваш ключ fal.ai); подключаемые модули (MCP-серверы
>   и компоненты WASM в сборках с опцией `wasm-plugins`).
> - **Частично:** сборка по ключам API и с другими агентами-программистами (сделано, вживую ещё не запускалось),
>   проверки поведения программ и игр, несколько инструментов движка испытаны только на заменителях.
> - **Выпущено:** открытые выпуски с установщиками для Windows, macOS, Linux и FreeBSD публикуются
>   на [странице выпусков](https://github.com/storytold/craft-anything/releases); они
>   по-прежнему альфа.
> - **Дальше:** управляемый тариф.
>
> Подробности и то, как каждая часть проверялась, — в [docs/STATUS.md](docs/STATUS.md),
> поинструментный список — в [docs/tool-status.md](docs/tool-status.md), а
> план по пунктам — в [docs/ROADMAP.md](docs/ROADMAP.md). Пишите обращения или расскажите, что
> сломалось, в [Discord](https://discord.gg/artcraft).

**Ответственное использование.** Пользуйтесь Craft Anything с программами, которые вам принадлежат или которые вам разрешено изучать. Он никогда
не обходит DRM, входы и античит. Пересборки воссоздают вёрстку, стиль и поведение по свидетельствам;
агенту сказано не копировать логотипы, фотографии и текст, пока вы не подтвердите, что они ваши или что
у вас есть разрешение.

**Установка зависимостей запускает код.** Когда сборщик ставит зависимости проекта, команды
выполняются на вашем компьютере, и пакеты могут запускать код во время установки. npm по умолчанию выполняет
установочные сценарии каждого пакета, а сборочные сценарии Rust и исходные пакеты Python запускают свой
код подготовки. Craft Anything спрашивает перед командой такого рода, которую ещё не видел в этом проекте (`npm`, `cargo`…).
Выбор «всегда разрешать» для `npm` позволяет всем последующим командам npm выполняться без вопроса, поэтому делайте так
только в проекте, чьим зависимостям вы доверяете. Чтобы ставить пакеты npm без их установочных сценариев,
выполните `npm install --ignore-scripts`.

<a id="downloads"></a>
## Загрузки

На GitHub в [последнем выпуске](https://github.com/storytold/craft-anything/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/craft-anything/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `craft-anything-<ver>-windows-x64.msi` | `craft-anything-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `craft-anything-<ver>-windows-arm64.msi` | `craft-anything-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `craft-anything-<ver>-windows-x86.msi` | `craft-anything-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы подписаны. Переносной zip хранит настройки рядом с программой.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `craft-anything-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `craft-anything-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен; см. ниже, если macOS его блокирует |

В версиях после 0.2.0 инструмент командной строки входит в программу, поэтому отдельный
zip для сборок не нужен. Он нужен только чтобы пользоваться командной строкой без программы.

Загрузка zip через браузер может остановиться с сообщением «Apple could not verify craft-anything-cli» (одиночная
программа не может унести с собой нотаризацию, поэтому macOS должна проверить её через сеть). Загрузка из
терминала так не проверяется, поэтому используйте это:

```sh
ver=0.2.0   # change this to the version you want
curl -fLO "https://github.com/storytold/craft-anything/releases/download/v$ver/craft-anything-cli-$ver-macos-universal.zip"
ditto -x -k "craft-anything-cli-$ver-macos-universal.zip" .
mkdir -p ~/.local/bin
mv "craft-anything-cli-$ver-macos-universal/craft-anything-cli" ~/.local/bin/
~/.local/bin/craft-anything-cli --version
```

Чтобы запускать его просто как `craft-anything-cli`, добавьте `~/.local/bin` в свой `PATH`.

Если у вас уже есть заблокированная копия, нажмите «Готово» (не «Переместить в корзину»), затем выполните
`xattr -d com.apple.quarantine <path to craft-anything-cli>` или разрешите её в «Настройки системы» →
«Конфиденциальность и безопасность» → «Всё равно открыть».

<a id="checking-that-a-mac-download-is-signed-and-notarized"></a>
#### Как проверить, что загрузка для Mac подписана и нотариально заверена

Каждый выпуск для Mac подписан сертификатом Developer ID и нотариально заверен Apple. Чтобы проверить загрузку
самостоятельно, выполните в «Терминале» (подставьте вместо `<ver>` номер версии, а пути — свои):

```sh
# The disk image: "accepted" and "source=Notarized Developer ID" mean it passed
spctl --assess --type open --context context:primary-signature -v "craft-anything-<ver>-macos-universal.dmg"
# The notarization ticket is attached: prints "The validate action worked!"
xcrun stapler validate "craft-anything-<ver>-macos-universal.dmg"

# The app, after you open the disk image: the signature must verify
codesign --verify --deep --strict --verbose=2 "/Volumes/<disk image name>/Craft Anything.app"
spctl --assess --type execute --verbose "/Volumes/<disk image name>/Craft Anything.app"

# The command-line tool: a bare program can't carry a ticket, so macOS checks it online
codesign --verify --strict --verbose=2 ~/.local/bin/craft-anything-cli
codesign -dv --verbose=4 ~/.local/bin/craft-anything-cli 2>&1 | grep Authority
```

В строках `Authority` должно быть имя сертификата «Developer ID Application». Если проверка не проходит, не
запускайте файл; сообщите об этом вместе с выводом и меткой выпуска.

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `craft-anything-<ver>-linux-x86_64.AppImage` | `craft-anything-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `craft-anything-<ver>-linux-x86_64.flatpak` | `craft-anything-<ver>-linux-aarch64.flatpak` | В песочнице, поэтому не может открыть браузер на вашем компьютере, а изучение сайтов этого требует (для этого возьмите другой пакет); `flatpak install --user <file>` |
| Debian/Ubuntu | `craft-anything-<ver>-linux-x86_64.deb` | `craft-anything-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `craft-anything-<ver>-linux-x86_64.rpm` | `craft-anything-<ver>-linux-aarch64.rpm` | |
| Архив | `craft-anything-<ver>-linux-x86_64.tar.gz` | `craft-anything-<ver>-linux-aarch64.tar.gz` | Распакуйте куда угодно |

RISC-V (riscv64): `craft-anything-<ver>-linux-riscv64.tar.gz`, только архив.

AppImage несёт и CLI: запускайте `<AppImage> --cli <command>` (например
`<AppImage> --cli mcp` для MCP-клиента) или сделайте ссылку на AppImage с именем
`craft-anything-cli` и запускайте её.

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `craft-anything-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Просмотр в браузере | `craft-anything-web-<ver>.zip` | Говорит, что это за файл, в браузере (файл его не покидает); разместите папку на любом статическом веб-сервере ([packaging/web/README.md](packaging/web/README.md)) |

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
  <a href="https://github.com/storytold/craft-anything">Craft Anything</a>
</p>

---

<a id="the-craft-app-suite"></a>
## The Craft App Suite

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
| <img src="https://raw.githubusercontent.com/storytold/materialcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.materialcraft.png" alt="" width="32" height="32"> | **MaterialCraft** | Процедурные материалы на графах узлов | [GitHub](https://github.com/storytold/materialcraft) | [Сайт](https://getartcraft.com/apps/materialcraft) |
| <img src="https://raw.githubusercontent.com/storytold/craft-anything/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.craft-anything.png" alt="" width="32" height="32"> | **Craft Anything** | Смотрите, как устроена любая программа, и собирайте свою | [GitHub](https://github.com/storytold/craft-anything) | [Сайт](https://getartcraft.com/apps/craft-anything) |
| <img src="https://raw.githubusercontent.com/tangency-labs/solidcraft/main/assets/icons/app/linux/exports/hicolor/64x64/apps/io.tangencylabs.solidcraft.png" alt="" width="32" height="32"> | **SolidCraft** | Параметрический 3D CAD от Tangency Labs (приложение сообщества) | [GitHub](https://github.com/tangency-labs/solidcraft) | |


<a id="license-and-credits"></a>
## Лицензия и благодарности

Craft Anything распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the Craft Anything contributors ([CONTRIBUTORS.md](CONTRIBUTORS.md)). Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

На снимках экрана — образцовые проекты, сделанные для них: example.com, игра «змейка» и небольшая
программа-калькулятор.

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и Craft Anything, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
