# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# Источники глоссария

Сняты 20.11.2026 около 10:25–10:30 (America/Los_Angeles) только чтением: локальный клон и raw.githubusercontent.com / api.github.com без авторизации. Время коммитов ниже переведено в America/Los_Angeles.

## Использованные

| Источник | Путь | Коммит (main) | Дата коммита, PT | Лицензия | Что взято |
|---|---|---|---|---|---|
| storytold/craft-i18n (локальный клон) | `craft-i18n` — `GLOSSARY.md`, `locales/ru/*.tsv` (common, cadcraft, craft-launcher, filmcraft, pdfcraft, photocraft, vectorcraft, wordcraft), `ATTRIBUTION.md` | b5b2805795f3d98b8fef4484db75db0cefbdc630 | 20.11.2026 06:03 | Apache-2.0 (GitHub), README: MIT OR Apache-2.0 | 2 принятых ru-термина (Diagram → Схема, Decorative Text → Декоративный текст); все пары ru-каталогов |
| storytold/photocraft | `docs/localization-ru.md` | 877d58844029967b80e36a964902d309de1be158 | 20.11.2026 10:17 | Apache-2.0 | таблица терминов (22 строки) и правила стиля |
| storytold/figcraft | `docs/translating.md`, `crates/ui-egui/locales/ru.toml` [ui] | 8320b6699e3f837c1f2af4c3166c4862526fb754 | 20.11.2026 10:02 | Apache-2.0 | Frame / Smart animate латиницей, «ёлочки», plural; пары [ui] |
| storytold/lightcraft | `crates/ui-egui/locales/ru.json`, `docs/localization-ru.md` | 968b0428fc158eb7daa4cbc21a0617c6073d491d | 20.11.2026 10:18 | Apache-2.0 | пары |
| storytold/vectorcraft | `crates/ui-egui/src/i18n/ru.tsv` | 063f55080244009e0e4bf28c24068479089481ac | 20.11.2026 09:45 | Apache-2.0 | пары (живой каталог) |
| storytold/filmcraft | `crates/ui-egui/src/i18n/ru.tsv` | 960a661001767a887dc4402c51e24f0436176705 | 20.11.2026 06:05 | Apache-2.0 | пары |
| storytold/cadcraft | `crates/ui-egui/src/i18n/ru.tsv` | 1d92bb275c756fcb1f068fea1ec478d50c3cbb14 | 20.11.2026 09:11 | Apache-2.0 | пары |
| storytold/craft-launcher | `crates/ui-egui/src/i18n/ru.tsv` | bbb3844954d90e64c70a89ea493d0e7270478553 | 20.11.2026 03:08 | Apache-2.0 | пары |
| storytold/craft-anything | `crates/ui-egui/src/i18n/ru.tsv` | 827be601e781daea91ce2013fa0f64d658abd028 | 20.11.2026 05:42 | Apache-2.0 | пары |
| storytold/designcraft | `crates/ui-egui/src/i18n/ru.rs` | 4000591c6681d01386b9576f9a050b8460e6f2e3 | 20.11.2026 09:52 | Apache-2.0 | пары |
| storytold/gridcraft | `crates/ui-egui/src/i18n/ru.rs` | 442a40ecb14e1aede497092820ea616a6ec08db6 | 20.11.2026 08:59 | Apache-2.0 | пары |
| tangency-labs/solidcraft | `docs/book/src/reference/glossary.md`, `assets/locales/en.json` + `ru.json`, `docs/localization.md` | 0301073f3e45d19618ccd9bb986418184282245a | 20.11.2026 09:49 | Apache-2.0 | английские термины глоссария + их ru из ru.json; таблица многозначных слов |

Оговорка: SHA взят через API сразу после скачивания raw-файлов из `main`; если между этими запросами был новый коммит, файл мог быть на коммит новее **[не проверено построчно]**.
Копии скачанных файлов: `tmp/l10n-src/`.

Кто переводил ru в craft-i18n (из ATTRIBUTION.md): в основном участники с ИИ, «not recorded as native-reviewed»; носитель с ИИ — Kirill M. (@JaffarSk24, 41 общая + 30 строк WordCraft, 27.10.2026). Русский FigCraft одобрен VanTan, поздние строки — машинный черновик **[проверено: ATTRIBUTION.md, ru.toml]**. То есть «принят» в нашем смысле ≠ проверено носителем.

## Как отбирались частотные термины [проверено: скрипт gen.py/gen2.py]

Из 42 361 пары en→ru (14 каталогов) взяты английские строки 1–3 слова, только латинские буквы/дефис/пробел, без плейсхолдеров в ru; регистр и конечные «…»/«.» не учитываются. Термин берётся, если встречается в 3+ каталогах; сортировка по числу программ. В колонку `ru` — вариант, встречающийся в наибольшем числе программ. Строки с контекстом `@plural/@id/@msg` пропущены. Скрипт не различает смыслы (глагол/существительное, тема/источник света) — поэтому часть «спорных» на деле законна **[догадка]**.

## Найдено, но не использовано как источник

- `pc-ru-work/glossary.tsv` (502 строки, 20.11 02:30) — выжимка из старого PhotoCraft `ru.tsv` v0.11.1 с частотами; устарела относительно craft-i18n; в примечаниях есть ссылки на меню Photoshop — не использовано: происхождение перевода отдельно не проверялось (само упоминание продукта не доказывает копирования) **[проверено: содержимое файла]**.
- `exports/translations/*/glossary_*.md`, `series/*/glossary` — глоссарии других проектов (книги), к ArtCraft не относятся **[проверено: пути; содержимое не читалось]**.
- `home-assistant/rust/src-craft/crates/ui-egui/src/glossary.rs` — встроенные английские пояснения craft-anything, не перевод **[проверено]**.

## Где лежит прежняя/чужая работа по ru (для будущей сверки ревизором)

План (разд. 6) только **предлагает**, сведения об их создании/результатах в самом плане отсутствуют **[из файла: план]**. На box найдено:
- `pc-ru` — клон storytold/photocraft, локальный коммит a6a91c42c 21.10.2026 «ru: translate 1222 missing UI strings»; `pc-ru-work` (рабочие куски, `ru.tsv`, `ru-translation.patch`), `pc-ru-final` (`ru.tsv`) **[проверено: ls, git log]**. Отправлялось ли это наружу — **не проверено**.
- `home-assistant/rust/src-craft` — клон craft-anything с каталогами i18n (сборка 20.11 10:22 по `craft-build-p2.log`) **[проверено: ls, лог]**.
- `craft-i18n` — клон craft-i18n (появился 20.11 10:24, создан не мной) **[проверено: ls]**.

## Не найдено / не проверено

- Русских терминов в самом глоссарии SolidCraft нет — он только английский (с заметками для переводчиков) **[проверено]**. Русские варианты взяты из ru.json.
- Термины глоссария SolidCraft, для которых в ru.json нет строки с тем же английским текстом: abbe number, airfoil, bill of materials type, caustic, chromatic dispersion, construction entity, construction plane, construction axis, construction point, design file, end cap, folder, gather radius, group, item number, leader, note, occurrence, opaque path lighting, operations panel, pattern instance, personal sheet metal rule, reference edge, rollback marker, section plane, sketch entity, standard steel size, thin-film interference, timeline, turn (of two rounds), virtual component, web browser, Clearance (hole) [ui.hole_clearance: нет в ru.json], Fit (clearance fit) [ui.clearance_fit: нет в ru.json]. Их русский — открыт для этапа 2 **[проверено поиском по en.json/ru.json]**.
- Каталоги без русского вовсе: anicraft, texturecraft, deckcraft, soundcraft, materialcraft, effectcraft **[из файла: план, разд. 3]** — в глоссарий не входят.
- wordcraft и pdfcraft — только копии в craft-i18n (собственные каталоги этих репо не скачивались) **[не проверено]**.
- SolidCraft `packaging/linux` (403 по плану) — не смотрелся.
- Глоссарии/termbase у Storytold кроме GLOSSARY.md и docs/localization*.md отдельных программ — поиск по org не делался **[не проверено]**.

## Папки смежных заходов в dept/l10n (появились 20.11 10:24–10:28, во время сборки глоссария) — для будущей сверки

Содержимое не читалось и не правилось, только список **[проверено: ls 20.11 ~10:31 PT]**:
- `apps/<программа>/` — 12 программ (cadcraft, craft-anything, craft-launcher, designcraft, effectcraft, figcraft, filmcraft, gridcraft, lightcraft, materialcraft, soundcraft, vectorcraft) — вероятно каталоги Storytold **[догадка]**.
- `craft-i18n-missing/*.tsv` (anicraft, common, deckcraft, pdfcraft, photocraft, texturecraft, wordcraft) — вероятно каталоги craft-i18n **[догадка]**.
- `solidcraft/` — `terms-solidcraft-ru.tsv`, `NOTES-rules.md`, `gaps.md`, `work/` — заход SolidCraft; **его terms-solidcraft-ru.tsv надо свести с этим глоссарием** (следующий шаг терминолога).
- `review/20261120-baseline-craft-i18n-ru-*.tsv` — ревизор (базовые проверки плейсхолдеров, многоточий, plural и т.п.).
- `packaging/`, `cli/`, `docs/` (пусто) — упаковка, CLI, документация.

## Заход 20.11.2026 ~11:08 PT (решения по правилам координатора + упаковка/CLI)

- Правила решения переданы координатором как решения правообладателя; лично не проверялись.
- Упаковка: `glossary/from-packaging.md` (не удалялся; добавлены только поля Решение/Основание). Копия: `from-packaging.md.bak-20261120-1108`.
- CLI: `cli/terms-needed.md` (добавлены колонки Решение/Основание). Копия: `terms-needed.md.bak-20261120-1108`.
- SolidCraft спорные: `solidcraft/disputed-terms-for-terminolog.md` — учтён как источник; колонки решения нет, файл не менялся.
- Проверка исключений Pattern / Preset / Workspace — по `assets/locales/en.json` + `ru.json` SolidCraft, коммит 0301073 (копии в `tmp/l10n-src/`).
- `docs/interim-terms.tsv` сначала (~11:08 PT) ещё не было; файл появился около 11:11 PT (215 терминов: маски, корректирующие слои, инструменты, фильтры, стили слоя, Remove/Count и др.). Добавлены только колонки «Решение» и «Основание», строки не удалялись. Копия: `docs/interim-terms.tsv.bak-20261120-1112`.
- Копии glossary/conflicts/README/sources до правки: `*.bak-20261120-1103` и `*.bak-20261120-1108` (содержание исходников совпадало).

## Заход 20.11.2026 ~11:18 PT (ревизор Amount/Rasterize; terms-needed-apps; from-effectcraft; авторство)

- Rasterize и Amount уточнены: общее решение + исключения/разведение смыслов (PhotoCraft Amount «Величина», Rasterize «Растрировать»).
- Новый список: `cli/terms-needed-apps.md` (MaterialCraft, GridCraft). Копия: `terms-needed-apps.md.bak-20261120-1118`. Добавлены только колонки Решение/Основание.
- Новый список: `glossary/from-effectcraft.md`. Копия: `from-effectcraft.md.bak-20261120-1118`. Добавлены поля Решение/Основание.
- По RULES-AUTHORSHIP.md: в файлах отдела убраны отсылки к автоматическим исполнителям (замена на «терминолог отдела» / «из файла …»). В glossary.tsv строку-комментарий об авторстве не вставляли (сломала бы TSV). Ничего не публиковалось.

## Дополнение 20.11.2026 ~11:24 PT (America/Los_Angeles)

Координатор «Стек: Фотокрафт» сообщил, что правообладатель поручил ему решить спорные пункты. Все 97 пунктов «на взгляд правообладателя» утверждены как итоговые, с поправками: (1) Workspace в SolidCraft = «Рабочая область», выровнять `prefs.workspace`; (2) в Keywords дублировать форму без «ё», в интерфейсе только «ё»; (3) Timeline общее «Шкала времени», в FilmCraft — как в его каталоге (правило а); (4) Circle в CADCraft/SolidCraft «Окружность», в графических программах «Круг»; (5) Mesh = «сетка», если авторы уже так пишут, иначе «меш» (б). Для этой работы это **решение координатора, поручение правообладателя подтверждено им лично**. Обновлены `decisions-20261120.md`, `glossary.tsv`, колонки «Решение» в затронутых файлах-источниках. Списки расхождений для исполнителей отдела: `glossary/fixes/`. Ничего наружу не публиковалось.

## Дополнение 20.11.2026 (America/Los_Angeles) — VectorCraft, FigCraft, terms-to-check

В сверку включены `glossary/from-vectorcraft.md`, `glossary/from-figcraft.md` и `dept/l10n/terms-to-check.md`. Preset и Frame в FigCraft сверены с `apps/figcraft/crates/ui-egui/locales/ru.toml`: Preset везде «пресет» (исключение), ключ Frame = «Frame». Слова «щелк-/щёлк-» не решались (ждёт ответа правообладателя). Пометка решений: «решил координатор 20.11 (поручение правообладателя подтверждено им лично)». Ничего наружу не публиковалось.
