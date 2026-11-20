# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# artcraft-ru

**Русская локализация** программ [ArtCraft](https://getartcraft.com) (Storytold) и [SolidCraft](https://github.com/tangency-labs/solidcraft) (Tangency Labs).

© 2026 SuperSfera LLC. Распространяется на условиях **MIT OR Apache-2.0** (на выбор получателя). Это **не** официальный проект авторов программ.

ArtCraft Russian localization for the Storytold Crafting Apps and for SolidCraft (Tangency Labs), © 2026 SuperSfera LLC, licensed under MIT OR Apache-2.0. This is not an official project of Storytold or Tangency Labs.

Названия программ — товарные знаки их владельцев. Логотипы, значки и материалы оформления в этот репозиторий не входят (для SolidCraft см. их LICENSE-BRAND).

Срез содержимого: **2026-11-20 11:25 PST** (America/Los_Angeles). Перевод ещё продолжается; это снимок на указанный момент, а не окончательная версия.

## Лицензия

- [LICENSE-MIT](LICENSE-MIT)
- [LICENSE-APACHE](LICENSE-APACHE)

Правообладатель перевода — SuperSfera LLC. Лицензионные файлы самих программ не изменялись. В файлах перевода, где формат позволяет комментарий, стоит строка:

`Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0`

В JSON комментариев нет: отметка только в этом README, в лицензиях и в сообщении коммита.

Часть строк в каталогах `craft-i18n` существовала раньше и принадлежит их авторам на условиях MIT OR Apache-2.0; добавления SuperSfera LLC — на тех же условиях.

## Структура

- `translations/<программа>/` — готовые файлы перевода по исходным путям внутри каждой программы (каталоги интерфейса, `.desktop` / AppStream / MIME, `README.ru.md` где есть).
- `patches/` — один патч на каждый изменённый репозиторий, относительно merge-base с `origin` плюс неотслеживаемые файлы. Каталоги SolidCraft, GridCraft и EffectCraft взяты из актуальных рабочих копий, не из устаревших клонов упаковки; из клонов упаковки в патч этих трёх программ входят только файлы `.desktop` / metainfo / MIME.
- `glossary/` — общий словарь терминов и решения по спорным словам.
- `docs/` — черновики `README.ru.md` и политика перевода.
- `review/` — инструменты проверки и чеклисты для снимков экрана (без чужих исходников).
- `reports/` — текстовые итоги по упаковке, CLI, каталогам и SolidCraft.
- `plan-ru-localization.md` — план работ.

Исходники программ (клоны, каталоги `target/`, история `.git`) в этот репозиторий не входят.

## Программы

ArtCraft / Storytold: AniCraft, CADCraft, Craft Anything, ArtCraft Launcher, DeckCraft, DesignCraft, EffectCraft, FigCraft, FilmCraft, GridCraft, LightCraft, MaterialCraft, PdfCraft, PhotoCraft, SoundCraft, TextureCraft, VectorCraft, WordCraft, и общий каталог [craft-i18n](https://github.com/storytold/craft-i18n).

Отдельно: SolidCraft (Tangency Labs).

Командная строка и man-страницы в этом срезе **не переводились**: у программ нет штатного механизма i18n для CLI, а генераторы man берут текст из английской справки.

## Авторство

Коммиты этого репозитория выполняются от имени GitHub-аккаунта [supersfera-online](https://github.com/supersfera-online). Правообладатель — SuperSfera LLC.
