# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/craft-launcher/blob/main/README.md
Репозиторий: https://github.com/storytold/craft-launcher
Коммит исходника (последний, в котором менялся README.md): 59e3f27f9e27a5b71f4798f60ae35c186b94b315
Дата коммита: 19 ноября 2026, 01:16 (America/Los_Angeles, PT); в исходнике 2026-11-19T09:16:49Z
SHA256 исходника: 1d19263b0dbd67e18ec865c724b589b25e3bc124b2401be419ffbaca6cdaded8
Git blob SHA: 3e41bc8226314289217d135acb443b6ed6dde141
Размер исходника: 29500 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/craft-launcher/main/README.md
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.artcraft-launcher.png" width="128" height="128" alt="Значок ArtCraft Launcher: стилизованная синяя буква A">
</p>

<h1 align="center">ArtCraft Launcher</h1>

<p align="center">
  <b>Одно место, чтобы установить, обновить и открыть каждое приложение Craft App Suite, заново написанное на чистом Rust.</b><br>
  PhotoCraft, LightCraft, FilmCraft, DesignCraft, VectorCraft, PdfCraft, EffectCraft, AniCraft, WordCraft,<br>
  DeckCraft, GridCraft, CADCraft, SoundCraft, FigCraft, Craft Anything, TextureCraft, MaterialCraft и приложения сообщества SolidCraft и MailCraft: нужная сборка для вашего компьютера, которая остаётся актуальной.
</p>

<p align="center">
  <img alt="100% Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="macOS · Windows · Linux · FreeBSD · Web" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-native-26282e?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-3a3a3a?style=flat-square">
  <img alt="Status: early alpha" src="https://img.shields.io/badge/status-early%20alpha-d69e2e?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_craft-launcher"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/craft-launcher?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://github.com/storytold/craft-launcher/releases/latest"><b>Скачать ArtCraft Launcher</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">The Craft App Suite</a>
</p>

> [!NOTE]
> **ArtCraft — это сообщество художников из самых разных сфер.** Живописцы, фотографы,
> кинематографисты, иллюстраторы, дизайнеры, аниматоры, любители и те, кто взял карандаш
> на прошлой неделе. Если вы что-то создаёте, вы один из нас. **[Заходите поздороваться в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#what-it-does">Что делает</a> ·
  <a href="#features">Возможности</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#build-from-source">Сборка из исходников</a> ·
  <a href="#the-craft-app-suite">Craft App Suite</a> ·
  <a href="https://discord.gg/artcraft">Discord</a>
</p>

<p align="center">
  <img src="docs/screenshots/artcraft-launcher-grid.png" alt="ArtCraft Launcher в macOS в виде сетки (тёмная тема): карточка каждого приложения Craft с его значком, состоянием, версией, датой выпуска и кнопкой «Установить» или «Открыть»" width="900">
</p>
<p align="center">
  <img src="docs/screenshots/artcraft-launcher-table.png" alt="Те же приложения в виде таблицы (светлая тема), со столбцами состояния, установленной и последней версий и даты выпуска" width="900"><br>
  <sub>Переключайтесь между сеткой и сортируемой таблицей.</sub>
</p>

<a id="what-it-does"></a>
## Что делает

Приложения Craft поставляют собственные сборки для каждой платформы. ArtCraft Launcher избавляет вас от
поиска по десятку страниц выпусков: он перечисляет каждое приложение набора, показывает, какие у вас есть
и какой версии, ставит нужную сборку для вашей операционной системы и процессора и сообщает,
когда вышло обновление. Это небольшая нативная программа, которая может жить в строке меню или в системном лотке.

<a id="features"></a>
## Возможности

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>📦 Установка в один щелчок</h3>
      Выбирает нужную загрузку для вашей ОС и процессора (DMG, MSI, AppImage, .deb, .rpm и другие), сверяет её с контрольными суммами SHA-256 выпуска и устанавливает.
    </td>
    <td width="33%" valign="top">
      <h3>🔄 Всегда актуальные версии</h3>
      Проверяет выпуски GitHub каждого приложения и обновляет те, что у вас установлены. Уведомление сообщает, когда появилось что-то новое.
    </td>
    <td width="33%" valign="top">
      <h3>🧭 Всегда под рукой</h3>
      Открывает любое приложение Craft из одного окна или из значка в лотке и строке меню. Нативный egui, без Electron и без веб-представления.
    </td>
  </tr>
</table>

Веб-версия показывает тот же каталог в браузере, с последней загрузкой для каждого приложения.

<a id="interface-languages"></a>
## Языки интерфейса

Интерфейс доступен на английском, боснийском (Bosanski), бразильском португальском (Português (Brasil)), чешском
(Čeština), французском (Français), грузинском (ქართული), немецком (Deutsch), венгерском (Magyar), японском
(日本語), польском (Polski), русском (Русский), упрощённом китайском (简体中文), традиционном китайском
(繁體中文), испанском (Español) или украинском (Українська). **Авто**, значение по умолчанию, следует языку системы или
браузера; **Настройки → Язык** выбирает один язык и переключает сразу, выбор сохраняется
между запусками. Боснийские локали (`bs`, `bs-BA`, `bs_BA.UTF-8`…) выбирают боснийский, чешские (`cs-CZ`,
`cs_CZ.UTF-8`…) — чешский, грузинские (`ka`, `ka-GE`, `ka_GE.UTF-8`…) — грузинский, немецкие (`de-DE`,
`de-AT`, `de-CH`, `de_DE.UTF-8`…) — немецкий, французские (`fr-FR`, `fr-CA`…) — французский, венгерские
(`hu`, `hu-HU`, `hu_HU.UTF-8`…) — венгерский, японские (`ja`, `ja-JP`, `ja_JP.UTF-8`…) — японский,
польские (`pl`, `pl-PL`, `pl_PL.UTF-8`) — польский, украинские (`uk`, `uk-UA`, `uk_UA.UTF-8`…) —
украинский, испанские (`es-ES`, `es-MX`, `es-419`…) — испанский, а португальские (`pt-BR` и
пока тоже `pt-PT`) — бразильский португальский. Локали упрощённого китайского (`zh-CN`, `zh-SG`, `zh-Hans`
и формы POSIX вроде `zh_CN.UTF-8`) выбирают упрощённый китайский; локали традиционного китайского (`zh-TW`,
`zh-HK`, `zh-MO`, `zh-Hant` и формы POSIX вроде `zh_TW.UTF-8`) выбирают традиционный китайский, причём
явное указание письменности важнее региона. Чтобы попробовать язык, не меняя настройку, запустите
настольную программу с `ARTCRAFT_LAUNCHER_LOCALE=pt-BR` или добавьте `?lang=ru` к веб-адресу.

Языки CJK рисуются системным шрифтом CJK (Hiragino Sans или PingFang в macOS,
Yu Gothic, Meiryo или Microsoft YaHei в Windows, Noto Sans CJK, IPA, Takao или WenQuanYi в Linux и
FreeBSD); для традиционного китайского предпочтительны установленный Noto Sans CJK TC, затем PingFang TC, Microsoft
JhengHei или MingLiU. Грузинский рисуется так же, системным грузинским шрифтом (SF Georgian или
Arial Unicode в macOS, Sylfaen в Windows, Noto Sans Georgian или DejaVu Sans в Linux и FreeBSD).
Если в системе нет шрифта для одного из них, а также в веб-версии, интерфейс остаётся на английском, и
в «Настройках» сказано почему. Имена продуктов и заметки к выпуску остаются как опубликованы; текст без перевода
отступает на английский. Каталог традиционного китайского и сведения о шрифтах — в [`docs/localization-zh-hant.md`](docs/localization-zh-hant.md).

<a id="where-apps-are-installed"></a>
## Куда устанавливаются приложения

ArtCraft Launcher ставит каждое приложение туда, где система обычно хранит программы, используя
официальный пакет выпуска приложения, поэтому приложение, установленное запускателем, совпадает с тем, что вы
установили вручную (и запускатель находит приложения, которые вы установили сами):

| Система | Куда | Как |
|---|---|---|
| macOS | `/Applications/<App>.app` | Копируется из подписанного и нотариально заверенного DMG выпуска |
| Windows | `C:\Program Files\ArtCraft\<App>` (`Program Files (x86)` для 32-разрядной сборки) | MSI выпуска через Windows Installer, для всех на компьютере (с пунктом в меню «Пуск» и записью в «Приложения и возможности»). Windows запрашивает права администратора для каждой новой установки. Приложение, уже установленное только для вашей учётной записи (`%LOCALAPPDATA%\Programs\ArtCraft\<App>`), при обновлении сохраняет папку и область действия; чтобы перенести его, удалите и установите снова |
| Linux | `/usr/bin`, `/usr/share/applications` | `.deb` выпуска (apt) или `.rpm` (dnf, zypper), с запросом пароля системы. Без них — Flatpak или AppImage в `~/Applications` |
| Linux, внутри Flatpak запускателя, без Flatpak на узле | `~/.var/app/ai.storyteller.artcraft-launcher/data/artcraft-launcher/apps/<app>` | Архив выпуска, распакованный в собственную папку запускателя и запущенный в той же песочнице, с настройками в папке `home/` рядом. На узел ничего не ставится, и конфигурация каждого приложения остаётся в песочнице |
| FreeBSD | `/usr/local` | Дерево выпуска, с запросом пароля (polkit); `~/.local`, если polkit не установлен |

ArtCraft Launcher поддерживает в актуальном состоянии и себя: когда выходит новая версия, **Обновить и перезапустить**
скачивает её, проверяет, ставит туда, где установлена эта копия (`.app`, пакет Windows Installer
или переносная папка, AppImage или `.deb`/`.rpm`) и открывает снова.

Обновления используют тот же формат, которым приложение было установлено. Каждая загрузка сверяется с
опубликованным SHA-256 выпуска перед установкой, а работающее приложение никогда не подменяется.

Запускатель пишет журнал в `logs/artcraft-launcher.log` в своей папке данных
(`~/.local/share/artcraft-launcher` в Linux, `~/Library/Application Support/ArtCraft Launcher`
в macOS, `%LOCALAPPDATA%\ArtCraft Launcher` в Windows, `ArtCraftLauncherData` рядом с
исполняемым файлом переносного zip) и хранит два предыдущих запуска как `artcraft-launcher.1.log` и
`artcraft-launcher.2.log`. `RUST_LOG` меняет, что записывается (`debug`, `info,zbus=warn`, …).

<a id="downloads"></a>
## Загрузки

Скачайте сборку для вашего компьютера из [последнего выпуска](https://github.com/storytold/craft-launcher/releases/latest) или просмотрите [все выпуски](https://github.com/storytold/craft-launcher/releases). В каждом выпуске есть `SHA256SUMS.txt`, с которым можно сверить файлы. `<ver>` — номер версии, например `0.1.0`.

**Windows** (10 и 11)

| Файл | Что это |
|---|---|
| `artcraft-launcher-<ver>-windows-x64.msi` | Установщик для большинства ПК (Intel и AMD, 64-разрядные). Ставит для текущего пользователя, права администратора не нужны |
| `artcraft-launcher-<ver>-windows-arm64.msi` | Установщик для Windows on Arm (Snapdragon и другие ARM-ПК) |
| `artcraft-launcher-<ver>-windows-x86.msi` | Установщик для 32-разрядной Windows |
| `artcraft-launcher-<ver>-windows-{x64,arm64,x86}-portable.zip` | Без установки: распакуйте и запустите `artcraft-launcher.exe`. Настройки хранятся в папке |

**macOS** (11 Big Sur или новее)

| Файл | Что это |
|---|---|
| `artcraft-launcher-<ver>-macos-universal.dmg` | Универсальная программа для Mac на Apple silicon и Intel, подписана и нотариально заверена. Перетащите ArtCraft Launcher в Applications |

**Linux** (x86_64 и aarch64; glibc 2.35 или новее, например Ubuntu 22.04+, Debian 12+, Fedora 36+)

| Файл | Что это |
|---|---|
| `artcraft-launcher-<ver>-linux-{x86_64,aarch64}.AppImage` | Запускается почти на любом дистрибутиве без установки; `chmod +x` и запустите. Рядом лежащий `.AppImage.zsync` позволяет AppImageUpdate скачать только то, что изменилось |
| `artcraft-launcher-<ver>-linux-{x86_64,aarch64}.deb` | Debian, Ubuntu, Mint, Pop!_OS: `sudo apt install ./artcraft-launcher-…deb` |
| `artcraft-launcher-<ver>-linux-{x86_64,aarch64}.rpm` | Fedora, openSUSE, RHEL: `sudo dnf install ./artcraft-launcher-…rpm` |
| `artcraft-launcher-<ver>-linux-{x86_64,aarch64}.flatpak` | Пакет Flatpak: `flatpak install --user artcraft-launcher-…flatpak`. Внутри песочницы запускатель ставит приложения как Flatpak на узле через `flatpak-spawn --host`; если на узле нет Flatpak, он отступает к архиву выпуска каждого приложения, распаковывает и запускает его в песочнице, храня настройки приложения внутри неё. В любом случае он достигает узла только настолько, насколько позволяет это разрешение; рекомендуемый способ запускать запускатель в Linux — сборки AppImage, .deb и .rpm |
| `artcraft-launcher-<ver>-linux-{x86_64,aarch64}.tar.gz` | Обычное дерево (`bin/`, `share/`) для всех остальных и для сценариев |

RISC-V (riscv64): `artcraft-launcher-<ver>-linux-riscv64.{deb,rpm,tar.gz}`, сборка против Ubuntu 24.04 (нужен glibc 2.39+).

Значок в лотке использует стандарт StatusNotifierItem: его показывают KDE, Xfce, Cinnamon и большинство других рабочих столов; в GNOME установите расширение AppIndicator.

**FreeBSD** (14, x86_64)

| Файл | Что это |
|---|---|
| `artcraft-launcher-<ver>-freebsd-x86_64.tar.gz` | Дерево, разложенное как `/usr/local` |

```sh
pkg install libxkbcommon wayland libX11 libXcursor libXrandr libXi libxcb mesa-libs vulkan-loader fontconfig freetype2
tar -xzf artcraft-launcher-<ver>-freebsd-x86_64.tar.gz --strip-components 1 -C /usr/local
artcraft-launcher
```

**Веб (WebAssembly)**

| Файл | Что это |
|---|---|
| `artcraft-launcher-web-<ver>.zip` | Каталог как статический сайт, который можно разместить где угодно; см. [`packaging/web/README.md`](packaging/web/README.md) |

<a id="build-from-source"></a>
## Сборка из исходников

Нужен свежий стабильный Rust (1.90 или новее). В Linux сначала установите заголовочные файлы оконной системы
(Debian/Ubuntu: `sudo apt install libxkbcommon-dev libwayland-dev libx11-dev libxrandr-dev libxi-dev libgl1-mesa-dev`).

```sh
git clone https://github.com/storytold/craft-launcher
cd craft-launcher
cargo run --release -p artcraft-launcher   # the desktop app
cargo xtask ci                             # fmt, clippy, tests and the wasm check
```

Веб-версия собирается с [trunk](https://trunk-rs.github.io/trunk/):

```sh
rustup target add wasm32-unknown-unknown
cd apps/artcraft-launcher-web && trunk serve
```

<a id="nix-experimental"></a>
### Nix (экспериментально)

`flake.nix` даёт оболочку разработки (`nix develop`, затем команды cargo выше) и пакет:

```sh
nix run github:storytold/craft-launcher
```

В NixOS это использует системные графические драйверы. В других дистрибутивах программа, собранная Nix, не может загрузить
драйверы GPU узла, поэтому окно может не открыться. Запускайте её через
[nixGL](https://github.com/nix-community/nixGL) (для NVIDIA нужна соответствующая разновидность nixGL для NVIDIA)
или используйте выпуск AppImage, `.deb` или `.rpm`:

```sh
nix run --impure github:nix-community/nixGL -- nix run github:storytold/craft-launcher
```

<a id="installing-your-own-builds"></a>
### Установка собственных сборок

Чтобы устанавливать и обновлять приложения Craft из копий на вашей машине, а не с GitHub, клонируйте их
рядом с этим репозиторием (`../photocraft`, `../wordcraft`, …) и выполните:

```sh
cargo xtask local sync      # git pull every app, build and package each new version into ../local-mirror
cargo xtask local serve     # serve the builds and a release feed on http://127.0.0.1:8787/
ARTCRAFT_LAUNCHER_DOWNLOAD_BASE=http://127.0.0.1:8787/ cargo run --release -p artcraft-launcher --features local-mirror
```

Снова запустите `sync`, когда понадобятся обновления, или поручите это серверу: `cargo xtask local serve
--sync-every 1h` забирает и собирает с этим интервалом, пока раздаёт. Приложение пересобирается, когда версии
его копии ещё нет в зеркале (`--rebuild` принуждает), и следующая проверка запускателя
его подхватывает. Добавьте `--every-commit`, чтобы собирать каждый новый коммит, как версию разработки между
выпусками (`0.4.0` собирается как `0.4.1-dev.<commit time>`), которую запускатель предлагает как обновление. Пока
задано `ARTCRAFT_LAUNCHER_DOWNLOAD_BASE` (только адреса loopback), запускатель спрашивает только
зеркало, никогда GitHub. Его читают только сборки с возможностью `local-mirror`; в выпусках её никогда нет. `cargo xtask local help` перечисляет параметры (`--only`, `--no-pull`, `--arch`, …).

Новым участникам и ИИ-агентам: начните с [`AGENTS.md`](AGENTS.md). Упаковка выпусков живёт в
[`packaging/`](packaging/) и [`.github/workflows/release.yml`](.github/workflows/release.yml).

> [!IMPORTANT]
> **Состояние:** ArtCraft Launcher — новая программа и находится в ранней альфе. Ожидайте шероховатости и, пожалуйста, заводите
> сообщения о проблемах (укажите ОС, какое приложение устанавливали и файл журнала запускателя) или расскажите нам в
> [Discord](https://discord.gg/artcraft).

<a id="the-craft-app-suite"></a>
## The Craft App Suite

ArtCraft Launcher устанавливает **Craft App Suite**: бесплатные творческие инструменты с открытым исходным кодом от команды
[ArtCraft](https://getartcraft.com/), каждый написан с нуля на Rust и каждый может
работать сам по себе.

|                                                                                                                                                                                            | Программа                 | Для чего                                         | Код                                                  | Подробнее                                                 |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------|:------------------------------------------------------|:------------------------------------------------------|:-----------------------------------------------------------|
| <img src="https://raw.githubusercontent.com/storytold/photocraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.photocraft.png" alt="" width="32" height="32">                     | **PhotoCraft**      | Редактирование изображений: слои, маски, текст и настоящие файлы PSD| [GitHub](https://github.com/storytold/photocraft)     | [Сайт](https://getartcraft.com/apps/photocraft)         |
| <img src="https://raw.githubusercontent.com/storytold/vectorcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.vectorcraft.png" alt="" width="32" height="32">                   | **VectorCraft**     | Векторная иллюстрация                                 | [GitHub](https://github.com/storytold/vectorcraft)    | [Сайт](https://getartcraft.com/apps/vectorcraft)        |
| <img src="https://raw.githubusercontent.com/storytold/filmcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.filmcraft.png" alt="" width="32" height="32">                       | **FilmCraft**       | Монтаж видео, цвет и звук                             | [GitHub](https://github.com/storytold/filmcraft)      | [Сайт](https://getartcraft.com/apps/filmcraft)          |
| <img src="https://raw.githubusercontent.com/storytold/lightcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.lightcraft.png" alt="" width="32" height="32">                     | **LightCraft**      | Библиотека фотографий и проявление raw                | [GitHub](https://github.com/storytold/lightcraft)     | [Сайт](https://getartcraft.com/apps/lightcraft)         |
| <img src="https://raw.githubusercontent.com/storytold/pdfcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.pdfcraft.png" alt="" width="32" height="32">                         | **PdfCraft**        | Чтение, организация и защита PDF                      | [GitHub](https://github.com/storytold/pdfcraft)       | [Сайт](https://getartcraft.com/apps/pdfcraft)           |
| <img src="https://raw.githubusercontent.com/storytold/effectcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.effectcraft.png" alt="" width="32" height="32">                   | **EffectCraft**     | Моушн-графика и визуальные эффекты                    | [GitHub](https://github.com/storytold/effectcraft)    | [Сайт](https://getartcraft.com/apps/effectcraft)        |
| <img src="https://raw.githubusercontent.com/storytold/AniCraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.anicraft.png" alt="" width="32" height="32">                         | **AniCraft**        | 2D-векторная анимация                                 | [GitHub](https://github.com/storytold/AniCraft)       | [Страница проекта](https://github.com/storytold/anicraft)     |
| <img src="https://raw.githubusercontent.com/storytold/designcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.designcraft.png" alt="" width="32" height="32">                   | **DesignCraft**     | Вёрстка и публикация                                  | [GitHub](https://github.com/storytold/designcraft)    | [Сайт](https://getartcraft.com/apps/designcraft)        |
| <img src="https://raw.githubusercontent.com/storytold/figcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.figcraft.png" alt="" width="32" height="32">                         | **FigCraft**        | Дизайн интерфейсов и прототипирование                 | [GitHub](https://github.com/storytold/figcraft)       | [Сайт](https://getartcraft.com/apps/figcraft)           |
| <img src="https://raw.githubusercontent.com/storytold/wordcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.wordcraft.png" alt="" width="32" height="32">                       | **WordCraft**       | Текстовый процессор и документы                       | [GitHub](https://github.com/storytold/wordcraft)      | [Сайт](https://getartcraft.com/apps/wordcraft)          |
| <img src="https://raw.githubusercontent.com/storytold/soundcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.soundcraft.png" alt="" width="32" height="32">                     | **SoundCraft**      | Запись и редактирование звука                         | [GitHub](https://github.com/storytold/soundcraft)     | [Сайт](https://getartcraft.com/apps/soundcraft)         |
| <img src="https://raw.githubusercontent.com/storytold/deckcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.deckcraft.png" alt="" width="32" height="32">                       | **DeckCraft**       | Презентации и слайд-колоды                            | [GitHub](https://github.com/storytold/deckcraft)      | [Сайт](https://getartcraft.com/apps/deckcraft)          |
| <img src="https://raw.githubusercontent.com/storytold/cadcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.cadcraft.png" alt="" width="32" height="32">                         | **CADCraft**        | Автоматизированное проектирование                     | [GitHub](https://github.com/storytold/cadcraft)       | [Сайт](https://getartcraft.com/apps/cadcraft)           |
| <img src="https://raw.githubusercontent.com/storytold/gridcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.gridcraft.png" alt="" width="32" height="32">                       | **GridCraft**       | Электронные таблицы и данные                          | [GitHub](https://github.com/storytold/gridcraft)      | [Сайт](https://getartcraft.com/apps/gridcraft)          |
| <img src="https://raw.githubusercontent.com/storytold/texturecraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.texturecraft.png" alt="" width="32" height="32">                 | **TextureCraft**    | Рисование 3D-текстур                                  | [GitHub](https://github.com/storytold/texturecraft)   | [Сайт](https://getartcraft.com/apps/texturecraft)       |
| <img src="https://raw.githubusercontent.com/storytold/materialcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.materialcraft.png" alt="" width="32" height="32">               | **MaterialCraft**   | Процедурное проектирование материалов                 | [GitHub](https://github.com/storytold/materialcraft)  | [Сайт](https://getartcraft.com/apps/materialcraft)      |
| <img src="https://raw.githubusercontent.com/storytold/craft-anything/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.craft-anything.png" alt="" width="32" height="32">             | **Craft Anything**  | Смотрите, как устроена любая программа, и собирайте свою| [GitHub](https://github.com/storytold/craft-anything) | [Сайт](https://getartcraft.com/apps/craft-anything)     |
| <img src="https://raw.githubusercontent.com/tangency-labs/solidcraft/main/assets/icons/app/linux/exports/hicolor/64x64/apps/io.tangencylabs.solidcraft.png" alt="" width="32" height="32"> | **SolidCraft**      | Параметрический 3D CAD от Tangency Labs (приложение сообщества)| [GitHub](https://github.com/tangency-labs/solidcraft) |                                                            |
| <img src="https://raw.githubusercontent.com/UCS-Care-Group/mailcraft/main/assets/app-icon/hicolor/64x64/apps/io.github.billsecond.mailcraft.png" alt="" width="32" height="32"> | **MailCraft** | Почта, календарь и контакты от UCS Care Group (приложение сообщества)| [GitHub](https://github.com/UCS-Care-Group/mailcraft) | [Сайт](https://mailcraft.work) |


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
  <a href="https://getartcraft.com/apps">The Craft App Suite</a> ·
  <a href="https://github.com/storytold/craft-launcher">ArtCraft Launcher</a>
</p>

---

<a id="thanks"></a>
## Благодарности

Сообщество собрало запускатели для Craft App Suite раньше нас, и ArtCraft Launcher многому
у них научился. Спасибо их авторам:

| Проект | Автор | Чему мы у него научились |
|---|---|---|
| [ArtCraft Suite Updater](https://github.com/Lyraedan/ArtCraft-Suit-Updater) | [@Lyraedan](https://github.com/Lyraedan) | Обнаружение приложений, установленных или удалённых вне средства обновления, тихим фоновым повторным сканированием; распознавание установок Arch и AUR через pacman; выбор платформы, где перечислены загрузки для каждой ОС |
| [craftcenter](https://github.com/avokadosauce/craftcenter) | [@avokadosauce](https://github.com/avokadosauce) | Поиск последнего выпуска без расхода квоты API (перенаправление `releases/latest` плюс `SHA256SUMS.txt`) и проверка каждого файла |
| [CRAFTSPACE](https://github.com/emircesur/CRAFTSPACE) | [@emircesur](https://github.com/emircesur) | Подхват уже установленных приложений, корректный запасной путь при ограничении частоты GitHub, фоновые уведомления об обновлениях |
| [GetCraft](https://github.com/mbirnbach/getcraft) | [@mbirnbach](https://github.com/mbirnbach) | Выбор нужной загрузки для каждой ОС и процессора, распознавание установок Windows Installer и macOS, собственный запускатель на Rust/egui |
| [CraftHub](https://github.com/CraftHubLauncher/CraftHub) | [CraftHubLauncher](https://github.com/CraftHubLauncher) | Строгая проверка источника загрузок, понятные сообщения об ограничении частоты, приложение никогда не подменяется, пока оно запущено |
| [artcraft-suite](https://github.com/erikerikerik/artcraft-suite) | [@erikerikerik](https://github.com/erikerikerik) | Проверка выпусков с кэшем ETag и установки, которые чисто восстанавливаются после прерывания |
| [Craft Apps Launcher & Installer](https://github.com/ZifuM/Craft-apps-launcher-installer) | [@ZifuM](https://github.com/ZifuM) | Запасные пути через страницу выпуска и запуск приложений AppImage в чистом окружении |
| [ArtCraft Launcher](https://github.com/EricVogt93/artcraft-launcher) | [@EricVogt93](https://github.com/EricVogt93) | Интеграция AppImage в рабочий стол и аккуратно продуманное самообновление |
| [LandingCraft](https://github.com/rallegretti/LandingCraft) | [@rallegretti](https://github.com/rallegretti) | Прямая работа с Windows Installer и предложение только стабильных выпусков |
| [Craft Apps Manager](https://github.com/CryptoKey98/craft-apps-manager) | [@CryptoKey98](https://github.com/CryptoKey98) | Плановые фоновые проверки обновлений и параметры запуска для каждого приложения |
| [ArtCraft Hub Launcher](https://github.com/tinyplayerss/artcraft-hub-launcher) | [@tinyplayerss](https://github.com/tinyplayerss) | Удобный однооконный центр для всего набора |
| [CraftHub](https://github.com/MegaTheLEGEND/CraftHub) | [@MegaTheLEGEND](https://github.com/MegaTheLEGEND) | Раздача веб-сборок приложений из самостоятельно размещённого запускателя |


<a id="license-and-credits"></a>
## Лицензия и благодарности

ArtCraft Launcher распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the ArtCraft Launcher contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Значки приложений Craft (`assets/app-icons/`) — это собственный значок каждого приложения, скопированный без изменений
из его репозитория и лицензированный как само приложение (MIT OR Apache-2.0).

**Имя ArtCraft, логотип и знак «A» не лицензируются на условиях MIT или Apache-2.0.** Они (всё
в [`docs/brand/`](docs/brand/), плюс значок программы в [`assets/app-icon/`](assets/app-icon/),
логотип в шапке запускателя и значок «A» в лотке)
являются товарными знаками ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и ArtCraft Launcher, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>
