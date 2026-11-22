# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# artcraft-ru

**Русская локализация** программ [ArtCraft](https://getartcraft.com) (Storytold) и [SolidCraft](https://github.com/tangency-labs/solidcraft) (Tangency Labs).

© 2026 SuperSfera LLC. Распространяется на условиях **MIT OR Apache-2.0** (на выбор получателя). Это **не** официальный проект авторов программ.

ArtCraft Russian localization for the Storytold Crafting Apps and for SolidCraft (Tangency Labs), © 2026 SuperSfera LLC, licensed under MIT OR Apache-2.0. This is not an official project of Storytold or Tangency Labs.

Названия программ — товарные знаки их владельцев. Логотипы, значки и материалы оформления в этот репозиторий не входят (для SolidCraft см. их LICENSE-BRAND).

Срез содержимого: **2026-11-20 12:09 PST** (America/Los_Angeles), с дополнением **2026-11-21**: в `translations/craft-i18n/locales/ru/` записаны каталоги ветки `ru-catalog-20261120`, с которыми 21 ноября собраны 18 программ; добавлен каталог интерфейса Craft Anything.

## Состояние программ

Дополнены русские каталоги интерфейса (наши новые строки). В снимке от 20.11 уже существовавшие авторские русские строки в каталогах программ оставлялись в редакции авторов; каталоги craft-i18n от 21.11 совпадают с собранными бинарями и включают словарные правки, см. ниже:

- SoundCraft, LightCraft, DesignCraft, FilmCraft, ArtCraft Launcher, FigCraft, VectorCraft, EffectCraft, GridCraft, MaterialCraft, CADCraft, SolidCraft, Craft Anything.
- Общий каталог [craft-i18n](https://github.com/storytold/craft-i18n): AniCraft, DeckCraft, TextureCraft; дополнения PdfCraft, PhotoCraft, WordCraft и common. В каталогах от 21.11 есть словарные правки (щёлк-/щёлч-, PhotoCraft «Проявка», PdfCraft «Переместить вниз» и др.), совпадающие с собранными бинарями.

Упаковка Linux (`.desktop` / AppStream / MIME) переведена для программ набора, которые входят в этот репозиторий.

Командная строка и man-страницы **не переводились**: у программ нет штатного механизма i18n для CLI, а генераторы man берут текст из английской справки.

## Каталоги интерфейса (строки в файле)

Версии — те, с которыми 21 ноября 2026 собраны 18 программ. «Строк» — число строк файла (`wc -l`). У DeckCraft каталог готов, но в код загрузчик craft-i18n ещё не подключён, поэтому бинарь с переводом не собирался.

| Программа | Версия | Файл перевода | Строк |
|---|---|---|---:|
| PhotoCraft | 0.23.1 | `translations/craft-i18n/locales/ru/photocraft.tsv` | 4061 |
| PdfCraft | 0.21.1 | `translations/craft-i18n/locales/ru/pdfcraft.tsv` | 4636 |
| WordCraft | 0.18.1 | `translations/craft-i18n/locales/ru/wordcraft.tsv` | 2816 |
| AniCraft | 0.3.0 | `translations/craft-i18n/locales/ru/anicraft.tsv` | 1711 |
| TextureCraft | 0.6.1 | `translations/craft-i18n/locales/ru/texturecraft.tsv` | 901 |
| ArtCraft Launcher | 0.19.2 | `translations/craft-launcher/crates/ui-egui/src/i18n/ru.tsv` | 485 |
| ArtCraft Launcher | 0.19.2 | `translations/craft-i18n/locales/ru/craft-launcher.tsv` | 286 |
| MaterialCraft | 0.4.1 | `translations/materialcraft/crates/ui-egui/src/i18n/ru.rs` | 759 |
| SoundCraft | 0.20.1 | `translations/soundcraft/crates/ui-egui/locales/ru/mod.rs` | 2343 |
| LightCraft | 0.21.1 | `translations/lightcraft/crates/ui-egui/locales/ru.json` | 3840 |
| LightCraft | 0.21.1 | `translations/lightcraft/crates/ui-egui/locales/ru-formats.json` | 334 |
| DesignCraft | 0.21.0 | `translations/designcraft/crates/ui-egui/src/i18n/ru.rs` | 3073 |
| FigCraft | 0.18.1 | `translations/figcraft/crates/ui-egui/locales/ru.toml` | 2735 |
| CADCraft | 0.21.0 | `translations/cadcraft/crates/ui-egui/src/i18n/ru.tsv` | 2268 |
| CADCraft | 0.21.0 | `translations/craft-i18n/locales/ru/cadcraft.tsv` | 891 |
| EffectCraft | 0.24.1 | `translations/effectcraft/crates/ui-egui/src/i18n/ui.rs` | 12205 |
| EffectCraft | 0.24.1 | `translations/effectcraft/crates/ui-egui/src/i18n/effects.rs` | 2826 |
| FilmCraft | 0.20.1 | `translations/filmcraft/crates/ui-egui/src/i18n/ru.tsv` | 3765 |
| FilmCraft | 0.20.1 | `translations/craft-i18n/locales/ru/filmcraft.tsv` | 327 |
| GridCraft | 0.19.1 | `translations/gridcraft/crates/ui-egui/src/i18n/ru.rs` | 1380 |
| GridCraft | 0.19.1 | `translations/gridcraft/crates/ui-egui/src/i18n/ru_functions.rs` | 971 |
| VectorCraft | 0.24.1 | `translations/vectorcraft/crates/ui-egui/src/i18n/ru.tsv` | 11283 |
| VectorCraft | 0.24.1 | `translations/craft-i18n/locales/ru/vectorcraft.tsv` | 3995 |
| Craft Anything | 0.6.1 | `translations/craft-anything/crates/ui-egui/src/i18n/ru.tsv` | 1505 |
| SolidCraft | 0.45.0 | `translations/solidcraft/assets/locales/ru.json` | 7419 |
| SolidCraft | 0.45.0 | `translations/solidcraft/crates/ui-text/locales/ru.json` | 256 |
| DeckCraft | 0.19.0 | `translations/craft-i18n/locales/ru/deckcraft.tsv` | 1093 |
| общее craft-i18n | — | `translations/craft-i18n/locales/ru/common.tsv` | 1305 |

Общий `common.tsv` подключается через craft-i18n вместе с каталогом программы.

## Лицензия

- [LICENSE-MIT](LICENSE-MIT)
- [LICENSE-APACHE](LICENSE-APACHE)

Правообладатель перевода — SuperSfera LLC. Лицензионные файлы самих программ не изменялись. В файлах перевода, где формат позволяет комментарий, стоит строка:

`Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0`

В JSON комментариев нет: отметка только в этом README, в лицензиях и в сообщении коммита.

Часть строк в каталогах `craft-i18n` существовала раньше и принадлежит их авторам на условиях MIT OR Apache-2.0; добавления SuperSfera LLC — на тех же условиях.

## Структура

- `translations/<программа>/` — готовые файлы перевода по исходным путям внутри каждой программы (каталоги интерфейса, `.desktop` / AppStream / MIME, `README.ru.md` где есть).
- `patches/` — один патч на каждый изменённый репозиторий, относительно merge-base с `origin` плюс неотслеживаемые файлы. Каталоги интерфейса взяты из рабочих копий отдела (без правок уже существовавших авторских строк). Из клонов упаковки в патч входят только файлы `.desktop` / metainfo / MIME, если каталог интерфейса брался из отдельной рабочей копии.
- `glossary/` — общий словарь терминов и решения по спорным словам.
- `docs/` — черновики `README.ru.md` и политика перевода.
- `review/` — инструменты проверки и чеклисты для снимков экрана (без чужих исходников).
- `reports/` — текстовые итоги по упаковке, CLI, каталогам и SolidCraft.
- `plan-ru-localization.md` — план работ.

Исходники программ (клоны, каталоги `target/`, история `.git`) в этот репозиторий не входят.

## Программы

ArtCraft / Storytold: AniCraft, CADCraft, Craft Anything, ArtCraft Launcher, DeckCraft, DesignCraft, EffectCraft, FigCraft, FilmCraft, GridCraft, LightCraft, MaterialCraft, PdfCraft, PhotoCraft, SoundCraft, TextureCraft, VectorCraft, WordCraft, и общий каталог [craft-i18n](https://github.com/storytold/craft-i18n).

Отдельно: SolidCraft (Tangency Labs).

## Авторство

Коммиты этого репозитория выполняются от имени GitHub-аккаунта [supersfera-online](https://github.com/supersfera-online). Правообладатель — SuperSfera LLC.
