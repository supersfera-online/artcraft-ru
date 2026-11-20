# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# Список правок — FilmCraft, ArtCraft Launcher, LightCraft, SoundCraft

Адресат: **Локализация: каталоги программ**.

Составлено терминологом отдела «Локализация ArtCraft» 20.11.2026 (America/Los_Angeles). Пометки отдела на момент сверки; рассылку делает координатор.

Сверка готовых каталогов на ветке `ru-l10n` (рабочие копии на box, без переключения веток и без коммитов; незакоммиченных изменений в этих четырёх репозиториях не было).

Коммиты `HEAD` на `ru-l10n` (проверено: `git rev-parse` / `git log -1`):

- filmcraft `dec1d25` — *Add missing Russian strings and translation copyright header.*
- craft-launcher `00da9e9` — *Add missing Russian strings and translation copyright header.*
- lightcraft `b4c9c30` — *Spell щелчок without ё in our new catalog strings only.* (на `ru-l10n` поверх `d72d08a`)
- soundcraft `511c249` — *Spell the noun щелчок without ё; keep click verbs with ё.* (на `ru-l10n` поверх `2c4e9f3`)

Файлы: `apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv`, `apps/craft-launcher/crates/ui-egui/src/i18n/ru.tsv`, `apps/lightcraft/crates/ui-egui/locales/ru.json`, `apps/soundcraft/crates/ui-egui/locales/ru/mod.rs`.

На момент сверки в LightCraft и SoundCraft на `ru-l10n` уже лежали отдельные коммиты, которые приводят существительное «щелчок» к написанию через «е» и оставляют глаголы с «ё». По текущим рабочим копиям вхождений гнезда, расходящихся со словарём, не осталось (FilmCraft 21 строка, LightCraft 65, SoundCraft 19 — все совпадают со словарём). ArtCraft Launcher вхождений гнезда не содержит.

Норма: `glossary/glossary.tsv`. Исключения программ; форма команд как в программе. Буква «ё» — по словарю, без исключений (указал правообладатель лично 20.11.2026, 11:51 PT, чат SolidCraft; проверено): щёлкнуть, щёлкните, щёлкать, щёлкайте, защёлка, щёлк — через «ё»; щелчок, щелчка, щелчком, щелчки, щелчков — через «е». «Все» и «всё» — разные слова, не орфография.

В правки **не** включались: расхождения только по форме команды/рода с тем же корнем; «все»/«всё»; разные смыслы одного английского ключа (вынесены в раздел «Проверить», если это небезопасно автоматически).

Число правок в этом файле: **1** (FilmCraft 1, ArtCraft Launcher 0, LightCraft 0, SoundCraft 0).

| файл | ключ | сейчас | надо | основание |
|---|---|---|---|---|
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | View | Просмотр | Вид | glossary.tsv: View (меню) → «Вид». В каталоге ключ стоит в ряду меню File/Edit/Window/Help. решил координатор 20.11 (поручение правообладателя подтверждено им лично) |

## Проверить

Сюда вынесены случаи, где автоматическая сверка с общим термином глоссария столкнулась с другим правдоподобным смыслом или с уже стоящей в каталоге формой. Это **не** список обязательных правок.

| файл | ключ | сейчас | зачем проверить |
|---|---|---|---|
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Preset | Пресет | общее Preset → «Набор»; в живом каталоге FilmCraft уже «Пресет». Исключение программы не заведено. Правило (а)? |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Preset | Пресет | то же: в каталоге LightCraft уже «Пресет», в глоссарии общее «Набор». |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Look | Художественный стиль | похоже на художественный «лук», не OCIO Look Transform и не подпись PdfCraft «Вид». |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Vibrance | Красочность | в глоссарии имя корректировки оставлено латиницей; в каталоге LightCraft уже «Красочность» (а?). |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Matte | Матовый | скорее свойство поверхности («матовый»), не мат/маска кеинга. |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Shape | Форма | в фотоконтексте «форма» может быть законным смыслом, не объект «фигура». |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Mix | Микс | исключение глоссария — «Микшер» для окна; в каталоге ключ Mix = «Микс» (другой смысл?). |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Key | Тональность | в DAW это музыкальная тональность, не кеинг. Не менять на «ключ». В glossary.tsv добавлена строка Key (тональность, SoundCraft). |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Rate | Частота | скорее частота дискретизации, не Rate из Liquify. В glossary.tsv добавлена строка Rate (частота, SoundCraft). |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | notes | ноты | скорее музыкальные ноты, не примечания. В glossary.tsv добавлена строка notes (музыка, SoundCraft). |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Crop | Обрезка | в видео может быть обрезка кадра, не фотокадрирование. |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Highlight | Светлые участки | близко по смыслу; унифицировать ли с PhotoCraft «Света» — не однозначно. |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Bottom | По нижнему краю | в глоссарии Bottom → «Снизу»; здесь, похоже, выравнивание «по нижнему краю», не то же значение. |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Top | По верхнему краю | в глоссарии Top → «Сверху»; здесь, похоже, выравнивание. |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Link | Связать | в глоссарии Link — «Ссылка / связывание»; в каталоге глагол «Связать» (форма как в программе?). |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Reference | Эталон | в глоссарии Reference — «Базовое ребро / Ссылка»; в видео/цвете «эталон» правдоподобен. |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Reference | Эталон | то же: «эталон» в фотоконтексте vs «Базовое ребро / Ссылка». |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Render | Просчитать | в глоссарии Render → «визуализировать»; в DAW «просчитать» — правдоподобный смысл. |

В glossary.tsv по итогам сверки добавлены строки-разведения смысла для SoundCraft: Key (тональность), Rate (частота), notes (музыка), чтобы не смешивать их с кеингом, Rate из Liquify и «примечаниями».

