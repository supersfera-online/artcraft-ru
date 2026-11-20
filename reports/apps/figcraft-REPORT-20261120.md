# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# FigCraft: русские строки — отчёт 20.11.2026

Бот «Локализация: упаковка». Задания 4 и 5 координатора (Стек: Фотокрафт). Часовой пояс: America/Los_Angeles (PT).

**Итог: готово** для секции `[ui]` (~177 ключей), выравнивания «фрейм» → Frame, и недостающих `[commands]` (38) и `[menu]` (3). Наружу ничего не отправлялось, на компьютер правообладателя ничего не ставилось. [проверено]

## Цифры

Замер до работы — из `apps/gaps.md` на коммите `8320b66` (20.11.2026, 10:02 AM PT): `[ui]` en 2033, ru 1856, недоставало 177. Пересчёт после — разбор `en.toml` / `ru.toml` парсером `tomllib`; объединение `[commands]` / `[menu]` — по всем локалям в `crates/ui-egui/locales/`. [проверено]

| Секция | источник | ru до | после задания 4 | после задания 5 | добавлено всего | осталось |
|---|---|---:|---:|---:|---:|---:|
| `[ui]` | `en.toml`, 2033 | 1856 | 2033 | 2033 | **177** | **0** |
| `[commands]` | нет в `en.toml`; объединение других языков | 613 | 613 | 651 | **38** | **0** |
| `[menu]` | нет в `en.toml`; объединение | 31 | 31 | 34 | **3** | **0** |

Лишних ключей относительно источника / объединения нет. Метаданные (`[meta] name = "Русский"`) не менялись. [проверено]

Выравнивание терминов (задание 5):

- «фрейм» во всех формах → латинское `Frame`: **7 строк, 8 вхождений** (в одной строке «по своему фрейму» и «внутри фрейма»). «вайрфреймов» в «Набор вайрфреймов» (Wireframe kit) не трогалось. [проверено]
- «пресет»: авторы уже пишут «пресет»; в наших 177 новых UI-строках «Набор» в значении Preset не было. Замен **0**. На glossary.tsv («Набор») не выравнивали, как просил координатор для этой программы. [проверено]

## Задание 4 — недостающие `[ui]`

- Клон: `apps/figcraft`, исходный `main` на `8320b6699e3f837c1f2af4c3166c4862526fb754`, рабочее дерево было чистым. Ветка `l10n-ru-figcraft` не существовала, взята это имя. Worktree не понадобился. [проверено]
- Документация авторов: `docs/translating.md` — ключи как в коде, плейсхолдеры как в английском, «…» как в источнике, плюралы русского `one`/`few`/`many`/`other` с `{n}` в каждой форме, Frame и Smart animate как привычные имена, кавычки « ». [проверено]
- В начало `crates/ui-egui/locales/ru.toml` добавлена шапка-комментарий `Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0`. Файл уже содержал чужой русский каталог (вычитан VanTan; поздние строки — машинный черновик авторов). TOML комментарий в первой строке допускает, `tomllib` файл принимает. [проверено]
- 177 недостающих ключей `[ui]` дописаны в конец секции, перед `[commands]` (коммит `cb3a375`, 20.11.2026, 11:34 AM PT). [проверено]
- Форма команд как уже в программе: краткие инфинитивы. Frame в новых UI-строках латиницей. Smart animate в том наборе ключей не встречался. [проверено]
- Чистая комната: перевод от смысла английских строк и уже стоящего `ru.toml`, не из Figma и т.п. [проверено: правило]

## Задание 5 — Frame и недостающие команды / меню

Отдельным коммитом `fc247b6` (20.11.2026, 11:42 AM PT) в 7 уже стоящих UI-строках «фрейм» заменён на несклоняемое `Frame`, грамматика подправлена («по своему Frame», «внутри Frame», «снимки Frame или векторов», «импортированы как Frame» / «как пустые Frame»). [проверено]

Отдельным коммитом `879e881` (20.11.2026, 11:42 AM PT) дописаны 38 подписей `[commands]` и 3 коротких `[menu]`. Английские подписи взяты из `spec!` в движке; русские — в форме уже стоящих команд UI. Уже стоящие ключи не менялись. [проверено]

Добавленные команды (id → английская подпись `spec!` → русский):

- `board.grid` — Board grid — Сетка доски
- `board.reshape` — Reshape connector — Изменить форму соединителя
- `collab.reconnect` — Reconnect live session — Переподключить сеанс
- `comment.prompt` — Copy comments for AI — Копировать комментарии для ИИ
- `data.fill` — Fill copies with data — Заполнить копии данными
- `effect.copy` / `effect.paste` — Copy/Paste effect — Копировать/Вставить эффект
- `file.fontReport` — Inspect document fonts — Проверить шрифты документа
- `file.markSaved` — Mark saved — Отметить как сохранённый
- `fill.copy` / `fill.paste` — Copy/Paste fill — Копировать/Вставить заливку
- `font.download` — Download font — Загрузить шрифт
- `font.downloads` — Font downloads — Загрузки шрифтов
- `image.crop` — Crop image — Обрезать изображение
- `image.replace` — Replace image — Заменить изображение
- `layout.removeAll` — Remove all auto layout — Убрать весь автолейаут
- `library.check` — Check team libraries for updates — Проверить обновления библиотек команды
- `pref.invertZoom` — Invert zoom direction — Инвертировать направление масштабирования
- `pref.uiScaleDown` — Smaller interface — Меньший интерфейс
- `pref.uiScaleReset` — Default interface size — Размер интерфейса по умолчанию
- `pref.uiScaleUp` — Larger interface — Больший интерфейс
- `proto.linkNotice` — Notice before leaving for a link — Уведомление перед переходом по ссылке
- `selection.createColorStyle` — Create selection color style — Создать стиль цвета из выделения
- `stroke.copy` / `stroke.paste` — Copy/Paste stroke — Копировать/Вставить обводку
- `text.direction` — Text direction — Направление текста
- `text.directionAuto` — Text direction: auto — Направление текста: авто
- `text.directionLtr` — Text direction: left to right — Направление текста: слева направо
- `text.directionRtl` — Text direction: right to left — Направление текста: справа налево
- `text.fit` — Fit text to its box — Вписать текст в блок
- `text.openLink` — Open link — Открыть ссылку
- `text.wrapStyle` — Wrap style — Стиль переноса
- `tool.annotation` — Annotation — Аннотация
- `tool.crosshair` — Move the placement crosshair — Переместить перекрестие размещения
- `tool.textOnPath` — Text on a path — Текст по контуру
- `variable.extendCollection` — Extend collection — Расширить коллекцию
- `view.minimize` — Minimize the interface — Свернуть интерфейс
- `widget.hover` — Hover widget — Виджет наведения

Короткие подписи меню (как в уже стоящем `[menu]` и в шведском каталоге — краткие формы):

- `text.directionAuto` — Авто
- `text.directionLtr` — Слева направо
- `text.directionRtl` — Справа налево

## Проверка

- Пересчёт ключей `[ui]` / `[commands]` / `[menu]` до и после; все ключи `[ui]` есть в `en.toml`; плейсхолдеры совпадают; плюралы разобраны парсером (словари `one`/`few`/`many`/`other`). Новые команды и меню без плейсхолдеров. `tomllib` принимает файл. [проверено: tomllib]
- Штатный `cargo test -p figcraft-ui-egui i18n` / `cargo xtask i18n-report` **не запускался**: в клоне нет `target/`, это тяжёлая сборка. Тулчейн на машине есть. [проверено: отсутствие target/]
- Вычитки носителем не было.

## Термины

Новые и спорные: `glossary/from-figcraft.md`. `glossary.tsv` не правился. Терминолога не ждал.

## Пути

- Ветка и клон: `apps/figcraft` (`l10n-ru-figcraft`)
- Коммиты (автор и коммитер `supersfera <223132313+supersfera-online@users.noreply.github.com>`; со старым `users.noreply.github.com` не коммитилось):
  - `cb3a37585264bf5e13e4faff7497527963068b2a` — Add missing Russian UI strings for the FigCraft catalog (20.11.2026, 11:34 AM PT)
  - `fc247b621c486c7c0e4c3a7dee9957bf18cbc46e` — Use Frame in Latin in remaining Russian catalog strings (20.11.2026, 11:42 AM PT)
  - `879e881ca540cebdd13d8592e1a8a614d8bf66e6` — Add missing Russian command labels and menu wordings (20.11.2026, 11:42 AM PT)
- Патч (все три коммита относительно `main`): `apps/figcraft-ru.patch`
- Отчёт: `apps/figcraft-REPORT-20261120.md`
- Термины: `glossary/from-figcraft.md`

История не переписывалась, push не выполнялся.

## Атрибуция

Черновик перевода составлен отделом локализации (упаковка) (локально, 20.11.2026, PT) для передачи авторам. Правообладатель перевода — SuperSfera LLC, лицензия MIT OR Apache-2.0. Большая часть файла — уже стоящий русский каталог (ревью VanTan и поздний машинный черновик авторов); в задании 4 эти строки не менялись, в задании 5 в 7 UI-строках «фрейм» заменён на `Frame`.

## Дополнение: решение по «щелк-/щелч-» (20.11.2026, PT)

Пишем через «е». В `ru.toml` (и в авторских, и в наших строках) форм «щёлк-/щёлч-» нет; менять было нечего. Отдельный коммит в FigCraft для этого не нужен. [проверено]

## Итоговое правило «щёлк-/щелч-» (20.11.2026, 11:55 AM PT)

Два предыдущих указания отменены. По словарю: глаголы через «ё», «щелчок»-формы через «е», включая авторские строки.

В `crates/ui-egui/locales/ru.toml` (и в авторских, и в наших строках) форм «щёлк-/щелч-» **нет**. Менять было нечего, отдельный коммит в каталоге FigCraft не создавался. Keywords упаковки этих слов тоже не содержат. [проверено]
