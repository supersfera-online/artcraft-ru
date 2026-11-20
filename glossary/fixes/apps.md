# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
> Внимание: это черновик первой сверки (более широкий захват, возможны ложные срабатывания). Для передачи исполнителям «Локализация: CLI и ошибки» (MaterialCraft, GridCraft, CADCraft) см. `fixes/cli-materialcraft-gridcraft-cadcraft.md`; для исполнителя SolidCraft — `fixes/solidcraft.md`. Пометка решений: «решил координатор 20.11 (поручение правообладателя подтверждено им лично)». Пометки отдела на момент сверки.

# Список правок — Локализация: каталоги программ

Составлено терминологом отдела «Локализация ArtCraft» 20.11.2026 (America/Los_Angeles). Пометки отдела на момент сверки.

Зона: **Локализация: каталоги программ**. Рабочие файлы: репозитории в `apps/*` (LightCraft JSON, FigCraft TOML, Rust-таблицы, TSV в репо). Каталоги, которые живут только в craft-i18n, в этот файл не дублируются.

Источник нормы: `glossary/glossary.tsv` и `glossary/decisions-20261120.md` после утверждения координатором 20.11 (все 97 спорных + поправки 1–5). Это **решение координатора, со слов координатора, поручение правообладателя подтверждено им лично**.

Колонки: файл (путь от ``), ключ, сейчас, надо, основание. Форму команд и род/число с тем же корнем («как в программе») сюда не включали. Расхождения только по «ё» в интерфейсе — включали (в интерфейсе только «ё»).

Число правок в этом файле: **315**.

| файл | ключ | сейчас | надо | основание |
|---|---|---|---|---|
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Baseline | Базовый | Базовая линия | glossary.tsv: Baseline → «Базовая линия». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Binary assets added | Добавленные двоичные ресурсы | Добавленные бинарные ресурсы | glossary.tsv: Binary assets added → «Добавленные бинарные ресурсы». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Binary assets removed | Удалённые двоичные ресурсы | Удалённые бинарные ресурсы | glossary.tsv: Binary assets removed → «Удалённые бинарные ресурсы». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Bold | Жирный | Полужирный | glossary.tsv: Bold → «Полужирный». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Box | Параллелепипед | Рамка | glossary.tsv: Box → «Рамка». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Center | Центр | По центру | glossary.tsv: Center → «По центру». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Circle | Круг | Окружность | поправка координатора 20.11 (4): в CADCraft и SolidCraft Circle = «Окружность». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Company | Организация | Компания | glossary.tsv: Company → «Компания». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Dark | Темная | Тёмная | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Dark → «Тёмная». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Edit | Редактирование | Правка | glossary.tsv: Edit (меню) → «Правка» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Edit… | Изменить… | Правка | glossary.tsv: Edit (меню) → «Правка» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Export | Экспортировать | Экспорт | glossary.tsv: Export → «Экспорт». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Grab bag | Список | Разное | glossary.tsv: Grab bag → «Разное». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | History | Журнал | История | glossary.tsv: History (panel) → «История». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Horizontal | Горизонтальность | Горизонтально | glossary.tsv: Horizontal → «Горизонтально». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Import | Импортировать | Импорт | glossary.tsv: Import → «Импорт». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Insert | Вставка | Вставить | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Justify | Выравнивание | По ширине | glossary.tsv: Justify → «По ширине». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Layout | Лист | Макет | glossary.tsv: Layout (страница настроек / Reset layout) → «Макет». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Leading | Начальные | интерлиньяж | glossary.tsv: leading → «интерлиньяж». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Line | Отрезок | Линия | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Line delta | Изменение количества строк | Разница строк | glossary.tsv: Line delta → «Разница строк». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Midpoint | Середина | Средняя точка | glossary.tsv: Midpoint → «Средняя точка». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Modify | Модификация | Изменить | glossary.tsv: Modify → «Изменить». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Name | Название | Имя | glossary.tsv: Name → «Имя». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Off | Выключено | Выкл | glossary.tsv: Off → «Выкл». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | On | Включено | Вкл | glossary.tsv: On → «Вкл». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Pattern | Шаблон | Узор | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Previous | Предыдущий | Назад | glossary.tsv: Previous → «Назад». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Render | Тонирование | визуализировать | glossary.tsv: render (проза help; имя — контракт) → «визуализировать». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Replace | Replace | Заменить | glossary.tsv: Replace → «Заменить». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Replace All | Replace All | Заменить все | glossary.tsv: Replace All → «Заменить все». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Reverse the order | Изменить порядок на обратный | Обратный порядок | glossary.tsv: Reverse the order → «Обратный порядок». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Select All | Выделить все | Выделить всё | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Select All → «Выделить всё». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Settings | Параметры | Настройки | glossary.tsv: Settings → «Настройки». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Settings... | Параметры... | Настройки | glossary.tsv: Settings → «Настройки». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Shape | Форма | Фигура | glossary.tsv: Shape → «Фигура». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Smooth | Сглаживание | Сгладить | glossary.tsv: Smooth → «Сгладить». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Trim | Обрезать | подрезать | glossary.tsv: Trim → «подрезать». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Vertical | Вертикальность | Вертикально | glossary.tsv: Vertical → «Вертикально». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | Zoom | Показать | Масштаб | glossary.tsv: Zoom → «Масштаб». со слов координатора 20.11.2026, лично не проверено |
| apps/cadcraft/crates/ui-egui/src/i18n/ru.tsv | menu | Модификация | Изменить | glossary.tsv: Modify → «Изменить». со слов координатора 20.11.2026, лично не проверено |
| apps/craft-launcher/crates/ui-egui/src/i18n/ru.tsv | Move down | Ниже | Переместить вниз | glossary.tsv: Move down → «Переместить вниз». со слов координатора 20.11.2026, лично не проверено |
| apps/craft-launcher/crates/ui-egui/src/i18n/ru.tsv | Move up | Выше | Переместить вверх | glossary.tsv: Move up → «Переместить вверх». со слов координатора 20.11.2026, лично не проверено |
| apps/craft-launcher/crates/ui-egui/src/i18n/ru.tsv | Status | Статус | Состояние | glossary.tsv: Status → «Состояние». со слов координатора 20.11.2026, лично не проверено |
| apps/craft-launcher/crates/ui-egui/src/i18n/ru.tsv | Website | Веб-сайт | Сайт | glossary.tsv: Website → «Сайт». со слов координатора 20.11.2026, лично не проверено |
| apps/craft-launcher/crates/ui-egui/src/i18n/ru.tsv | designcraft | Вёрстка и издательское дело | Вёрстка и публикация | glossary.tsv: Page layout and publishing → «Вёрстка и публикация». со слов координатора 20.11.2026, лично не проверено |
| apps/craft-launcher/crates/ui-egui/src/i18n/ru.tsv | filmcraft | Монтаж видео, цветокоррекция и звук | Монтаж видео, цвет и звук | glossary.tsv: Video editing, color and sound → «Монтаж видео, цвет и звук». со слов координатора 20.11.2026, лично не проверено |
| apps/craft-launcher/crates/ui-egui/src/i18n/ru.tsv | lightcraft | Фотобиблиотека и проявка RAW | Библиотека фотографий и проявление raw | glossary.tsv: Photo library and raw development → «Библиотека фотографий и проявление raw». со слов координатора 20.11.2026, лично не проверено |
| apps/craft-launcher/crates/ui-egui/src/i18n/ru.tsv | pdfcraft | Чтение, упорядочивание и защита PDF | Чтение, организация и защита PDF | glossary.tsv: Reading, organizing and protecting PDFs → «Чтение, организация и защита PDF». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Advanced | Расширенное | Дополнительно | glossary.tsv: Advanced → «Дополнительно». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Align | Выравнивание | Выровнять | glossary.tsv: Align → «Выровнять». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Align Center | По центру | Выровнять по центру | glossary.tsv: Align center → «Выровнять по центру». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Align Left | По левому краю | Выровнять по левому краю | glossary.tsv: Align left → «Выровнять по левому краю». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Align Right | По правому краю | Выровнять по правому краю | glossary.tsv: Align right → «Выровнять по правому краю». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Appearance | Оформление | Внешний вид | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Bring Forward | Переложить вперед | Переместить вперёд | glossary.tsv: Bring Forward → «Переместить вперёд». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Change | Заменить | Изменить | glossary.tsv: Change → «Изменить». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Columns | Колонки | Столбцы | glossary.tsv: Columns → «Столбцы». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Dark | Темная | Тёмная | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Dark → «Тёмная». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Distribute | Распределить | распределение | glossary.tsv: distribute → «распределение». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Drop Shadow | Тень | Внешняя тень | glossary.tsv: Drop Shadow → «Внешняя тень». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Edit | Редактирование | Правка | glossary.tsv: Edit (меню) → «Правка» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Fade | Выцветание | затухание | glossary.tsv: Fade (клип DAW / видео) → «затухание». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Font Size | Кегль | Размер шрифта | glossary.tsv: Font Size → «Размер шрифта». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | General | Основные | Общие | glossary.tsv: General → «Общие». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Native | Согласно языку | нативный / нативно | glossary.tsv: native → «нативный / нативно». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Notes | Заметки | Примечания | glossary.tsv: Notes (table) → «Примечания». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Output | Вывод | выход | glossary.tsv: output (порт графа) → «выход». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Package | Упаковать | пакет | glossary.tsv: package (контейнер графов MaterialCraft) → «пакет». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Package… | Упаковать… | пакет | glossary.tsv: package (контейнер графов MaterialCraft) → «пакет». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Paste Into | Вставить внутрь | Вставить в | glossary.tsv: Paste Into → «Вставить в». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Paste in Place | Вставить на то же место | Вставить на место | glossary.tsv: Paste in Place → «Вставить на место». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Preferences | Установки | Настройки | glossary.tsv: Preferences → «Настройки». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Preferences… | Установки… | Настройки | glossary.tsv: Preferences → «Настройки». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Render | Визуализация | визуализировать | glossary.tsv: render (проза help; имя — контракт) → «визуализировать». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Satin | Глянец | Атлас | glossary.tsv: Satin → «Атлас». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Scale | Масштабировать | Масштаб | glossary.tsv: Scale → «Масштаб». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Select All | Выделить все | Выделить всё | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Select All → «Выделить всё». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Selection | Выделенное | Выделение | glossary.tsv: Selection → «Выделение». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Sort | Сортировать | Сортировка | glossary.tsv: Sort → «Сортировка». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Standard | Стандарт | Стандартный | glossary.tsv: Standard → «Стандартный». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Strikethrough | Зачеркивание | Зачёркивание | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Strikethrough → «Зачёркивание». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Transform | Трансформирование | Трансформировать | glossary.tsv: Transform → «Трансформировать». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Transform Again | Повторить трансформирование | Трансформировать снова | glossary.tsv: Transform Again → «Трансформировать снова». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Trim | Область обрезки | подрезать | glossary.tsv: Trim → «подрезать». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Underline | Подчеркивание | Подчёркивание | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Underline → «Подчёркивание». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | View | Просмотр | Вид | glossary.tsv: View (меню) → «Вид» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Wipe | Вытирание | вытеснение | glossary.tsv: Wipe (переход) → «вытеснение». со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | Yellow | Желтый | Жёлтый | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Yellow → «Жёлтый». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | line | строка | Линия | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/designcraft/crates/ui-egui/src/i18n/ru.rs | selection | выделенное | Выделение | glossary.tsv: Selection → «Выделение». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Appearance | Оформление | Внешний вид | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Binary assets added | Добавлено двоичных файлов | Добавленные бинарные ресурсы | glossary.tsv: Binary assets added → «Добавленные бинарные ресурсы». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Binary assets removed | Удалено двоичных файлов | Удалённые бинарные ресурсы | glossary.tsv: Binary assets removed → «Удалённые бинарные ресурсы». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Blend Mode | Режим наложения | режим смешивания | glossary.tsv: blend mode → «режим смешивания». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Custom | Свой | Пользовательский | glossary.tsv: Custom → «Пользовательский». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Custom... | Настраиваемое... | Пользовательский | glossary.tsv: Custom → «Пользовательский». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | General | Основные | Общие | glossary.tsv: General → «Общие». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Green | Зеленый | Зелёный | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Green → «Зелёный». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Line delta | Сальдо строк | Разница строк | glossary.tsv: Line delta → «Разница строк». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Off | Выключено | Выкл | glossary.tsv: Off → «Выкл». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Pen Tool | Инструмент «Перо» | Перо | glossary.tsv: Pen tool → «Перо». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Preview | Предварительный просмотр | Просмотр | glossary.tsv: Preview → «Просмотр». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Render | Визуализировать | визуализация | glossary.tsv: Render (EffectCraft / очереди) → «визуализация». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Reverse the order | Обратить порядок | Обратный порядок | glossary.tsv: Reverse the order → «Обратный порядок». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Select | Выделить | Выбрать | glossary.tsv: Select → «Выбрать». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Snapping | Привязывание | привязка | glossary.tsv: snapping → «привязка». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Stop | Стоп | Остановить | glossary.tsv: Stop → «Остановить». со слов координатора 20.11.2026, лично не проверено |
| apps/effectcraft-ru.patch | Transform | Трансформирование | Трансформировать | glossary.tsv: Transform → «Трансформировать». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Align | Выравнивание | Выровнять | glossary.tsv: Align → «Выровнять». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Bend | Изгиб | гиб | glossary.tsv: bend → «гиб». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Binary assets added | Добавлено бинарных ресурсов | Добавленные бинарные ресурсы | glossary.tsv: Binary assets added → «Добавленные бинарные ресурсы». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Binary assets removed | Удалено бинарных ресурсов | Удалённые бинарные ресурсы | glossary.tsv: Binary assets removed → «Удалённые бинарные ресурсы». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Blend mode | Режим наложения | режим смешивания | glossary.tsv: blend mode → «режим смешивания». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Bring forward | На уровень вперёд | Переместить вперёд | glossary.tsv: Bring Forward → «Переместить вперёд». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Crop | Обрезка | Обрезать | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Download | Загрузить | Скачать | glossary.tsv: Download → «Скачать». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Flatten | Свести | сведение | glossary.tsv: flatten → «сведение». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Grab bag | Список имён | Разное | glossary.tsv: Grab bag → «Разное». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Inspect | Инспектор | проверить | glossary.tsv: inspect (проза help; имя — контракт) → «проверить». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Layout | Компоновка | Макет | glossary.tsv: Layout (страница настроек / Reset layout) → «Макет». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Move | Перемещение | Переместить | glossary.tsv: Move → «Переместить». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Paint bucket | Заливка области | Ведро заливки | glossary.tsv: Paint Bucket → «Ведро заливки». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Pattern | Паттерн | Узор | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Preview | Предпросмотр | Просмотр | glossary.tsv: Preview → «Просмотр». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Replace all | Заменить всё | Заменить все | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Replace All → «Заменить все». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Reverse the order | Обратить порядок | Обратный порядок | glossary.tsv: Reverse the order → «Обратный порядок». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Status | Статус | Состояние | glossary.tsv: Status → «Состояние». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Subtract | Вычитание | Вычесть | glossary.tsv: Subtract → «Вычесть». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | System | Системный | Система | glossary.tsv: System → «Система». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Tile | Повторение | тайл | glossary.tsv: tile (copy-on-write) → «тайл». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | Transform | Трансформация | Трансформировать | glossary.tsv: Transform → «Трансформировать». со слов координатора 20.11.2026, лично не проверено |
| apps/figcraft/crates/ui-egui/locales/ru.toml | What it's for | Назначение | Для чего | glossary.tsv: What it's for → «Для чего». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Align center | По центру | Выровнять по центру | glossary.tsv: Align center → «Выровнять по центру». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Align left | По левому краю | Выровнять по левому краю | glossary.tsv: Align left → «Выровнять по левому краю». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Align right | По правому краю | Выровнять по правому краю | glossary.tsv: Align right → «Выровнять по правому краю». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Anchor Point | Точка привязки | опорная точка | glossary.tsv: anchor point → «опорная точка». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Appearance | Оформление | Внешний вид | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Appearance… | Оформление… | Внешний вид | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Baseline | Базовый | Базовая линия | glossary.tsv: Baseline → «Базовая линия». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Binary assets added | Двоичные ресурсы добавлены | Добавленные бинарные ресурсы | glossary.tsv: Binary assets added → «Добавленные бинарные ресурсы». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Binary assets removed | Двоичные ресурсы удалены | Удалённые бинарные ресурсы | glossary.tsv: Binary assets removed → «Удалённые бинарные ресурсы». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Blend Mode | Режим наложения | режим смешивания | glossary.tsv: blend mode → «режим смешивания». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Bottom | По нижнему краю | Снизу | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Bring to Front | Переместить на передний план | На передний план | glossary.tsv: Bring to Front → «На передний план». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Center | Центр | По центру | glossary.tsv: Center → «По центру». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Crop | Обрезка | Обрезать | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Desaturate | Обесцвечивание | Обесцветить | glossary.tsv: Desaturate → «Обесцветить». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Distribute | Распределить | распределение | glossary.tsv: distribute → «распределение». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Drop Shadow | Тень | Внешняя тень | glossary.tsv: Drop Shadow → «Внешняя тень». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Easing | Сглаживание | сглаживание движения | glossary.tsv: Easing (анимация) → «сглаживание движения». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Edit… | Изменить… | Правка | glossary.tsv: Edit (меню) → «Правка» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Essential Graphics | Основные графические элементы | основная графика | glossary.tsv: Essential Graphics → «основная графика». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Flatten | Свести | сведение | glossary.tsv: flatten → «сведение». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Frame | Кадр | Frame | glossary.tsv: Frame → «Frame». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Fuzz | Фузз | Ворс | glossary.tsv: Fuzz → «Ворс». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Highlight | Светлые участки | Света | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Hue | Тон | Цветовой тон | glossary.tsv: Hue → «Цветовой тон». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Info | Инфо | Информация | glossary.tsv: Info → «Информация». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Line delta | Изменение числа строк | Разница строк | glossary.tsv: Line delta → «Разница строк». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Link | Связать | Ссылка | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Look | Художественный стиль | Look | glossary.tsv: Look (OCIO Look Transform) → «Look». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Mix | Микс | Микшер | glossary.tsv: Mix (окно SoundCraft) → «Микшер». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Next | Следующий | Далее | glossary.tsv: Next → «Далее». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | On | Включено | Вкл | glossary.tsv: On → «Вкл». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Paint Bucket | Заливка | Ведро заливки | glossary.tsv: Paint Bucket → «Ведро заливки». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Paragraph Text | Текст абзаца | абзацный текст | glossary.tsv: paragraph text → «абзацный текст». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Point Text | Точечный текст | текст из точки | glossary.tsv: point text → «текст из точки». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Preset | Пресет | Набор | glossary.tsv: Preset → «Набор». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Previous | Предыдущий | Назад | glossary.tsv: Previous → «Назад». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Progress | Прогресс | ход выполнения | glossary.tsv: progress → «ход выполнения». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Reference | Эталон | Базовое ребро | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Reset | Сброс | Сбросить | glossary.tsv: Reset → «Сбросить». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Select | Выделение | Выбрать | glossary.tsv: Select → «Выбрать». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Select All | Выделить все | Выделить всё | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Select All → «Выделить всё». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Select all | Выбрать всё | Выделить всё | glossary.tsv: Select All → «Выделить всё». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Send to Back | Переместить на задний план | На задний план | glossary.tsv: Send to Back → «На задний план». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Shadow | Тень | Тени | glossary.tsv: Shadow(s) → «Тени». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Shot | План | кадр | glossary.tsv: shot → «кадр». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Show All | Показать всё | Показать все | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Show All → «Показать все». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Smooth | Плавный | Сгладить | glossary.tsv: Smooth → «Сгладить». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Subtract | Вычитание | Вычесть | glossary.tsv: Subtract → «Вычесть». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Title | Название | Заголовок | glossary.tsv: Title → «Заголовок». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Top | По верхнему краю | Сверху | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Transform | Трансформация | Трансформировать | glossary.tsv: Transform → «Трансформировать». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Trim | Подрезка | подрезать | glossary.tsv: Trim → «подрезать». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Trim… | Подрезка… | подрезать | glossary.tsv: Trim → «подрезать». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Type Tool | Текст | инструмент «Текст» | glossary.tsv: Type tool → «инструмент «Текст»». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | Vibrance | Сочность | Vibrance | glossary.tsv: Vibrance → «Vibrance». со слов координатора 20.11.2026, лично не проверено |
| apps/filmcraft/crates/ui-egui/src/i18n/ru.tsv | View | Просмотр | Вид | glossary.tsv: View (меню) → «Вид» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Bottom | Нижняя | Снизу | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Change | Заменить | Изменить | glossary.tsv: Change → «Изменить». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Compact | Сжатый | компактный | glossary.tsv: compact (JSON) → «компактный». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Company | Организация | Компания | glossary.tsv: Company → «Компания». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Edit | Изменение | Правка | glossary.tsv: Edit (меню) → «Правка» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Edit… | Изменить… | Правка | glossary.tsv: Edit (меню) → «Правка» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Group | Группировать | Сгруппировать | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Histogram | Гистограмма распределения | гистограмма | glossary.tsv: histogram → «гистограмма». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Horizontal | По горизонтали | Горизонтально | glossary.tsv: Horizontal → «Горизонтально». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Info | Сведения | Информация | glossary.tsv: Info → «Информация». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Input | Ввод | вход | glossary.tsv: input (порт графа) → «вход». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Line | График | Линия | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Locked | Заблокированная | Заблокировано | glossary.tsv: Locked → «Заблокировано». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Move Down | Вниз | Переместить вниз | glossary.tsv: Move down → «Переместить вниз». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Move Up | Вверх | Переместить вверх | glossary.tsv: Move up → «Переместить вверх». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Notes | Заметки | Примечания | glossary.tsv: Notes (table) → «Примечания». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Output | Вывод | выход | glossary.tsv: output (порт графа) → «выход». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Page Break Preview | Предварительный просмотр разрывов страниц | Страничный режим | glossary.tsv: Page Break Preview → «Страничный режим». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Recent | Последние | Недавние | glossary.tsv: Recent → «Недавние». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Select | Выделить | Выбрать | glossary.tsv: Select → «Выбрать». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | System | Системная | Система | glossary.tsv: System → «Система». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Text | Текстовый | Текст | glossary.tsv: Text → «Текст». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Threaded Comments | Комментарии с ветками | комментарии в ветках | glossary.tsv: Threaded comments → «комментарии в ветках». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Title | Название | Заголовок | glossary.tsv: Title → «Заголовок». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Top | Верхняя | Сверху | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru.rs | Vertical | По вертикали | Вертикально | glossary.tsv: Vertical → «Вертикально». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru_functions.rs | bottom | низ | Снизу | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru_functions.rs | dimension | измерение | Размер | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru_functions.rs | pattern | шаблон | Узор | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru_functions.rs | timeline | временной_ряд | Шкала времени | glossary.tsv: Timeline → «Шкала времени». со слов координатора 20.11.2026, лично не проверено |
| apps/gridcraft/crates/ui-egui/src/i18n/ru_functions.rs | top | верх | Сверху | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Appearance | Оформление | Внешний вид | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Center | Центр | По центру | glossary.tsv: Center → «По центру». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Color Overlay | Цветное наложение | Наложение цвета | glossary.tsv: Color Overlay → «Наложение цвета». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Contrast | Контрастность | Контраст | glossary.tsv: Contrast → «Контраст». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Custom | Свои | Пользовательский | glossary.tsv: Custom → «Пользовательский». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Custom… | Свои… | Пользовательский | glossary.tsv: Custom → «Пользовательский». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Download | Загрузить | Скачать | glossary.tsv: Download → «Скачать». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Export As… | Экспортировать как… | Экспорт как | glossary.tsv: Export As → «Экспорт как». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Get Started | Начать | С чего начать | glossary.tsv: Get started → «С чего начать». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Grab bag | Случайная подборка | Разное | glossary.tsv: Grab bag → «Разное». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Horizontal | По горизонтали | Горизонтально | glossary.tsv: Horizontal → «Горизонтально». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Hue | Тон | Цветовой тон | glossary.tsv: Hue → «Цветовой тон». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Location | Местоположение | Расположение | glossary.tsv: Location → «Расположение». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Matte | Матовый | мат | glossary.tsv: Matte (композиция / кеинг) → «мат». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Merge | Слияние | объединение | glossary.tsv: merge (layers) → «объединение». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Name | Название | Имя | glossary.tsv: Name → «Имя». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | OK | OK | ОК | glossary.tsv: OK → «ОК». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Preset | Пресет | Набор | glossary.tsv: Preset → «Набор». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Reference | Эталон | Базовое ребро | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Select All | Выбрать все | Выделить всё | glossary.tsv: Select All → «Выделить всё». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Select all | Выбрать все | Выделить всё | glossary.tsv: Select All → «Выделить всё». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Shadow | Тень | Тени | glossary.tsv: Shadow(s) → «Тени». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Shape | Форма | Фигура | glossary.tsv: Shape → «Фигура». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Sharpen | Повысить резкость | Резкость | glossary.tsv: Sharpen → «Резкость». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Tracking | Слежение | трекинг | glossary.tsv: tracking → «трекинг». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Vertical | По вертикали | Вертикально | glossary.tsv: Vertical → «Вертикально». со слов координатора 20.11.2026, лично не проверено |
| apps/lightcraft/crates/ui-egui/locales/ru.json | Vibrance | Красочность | Vibrance | glossary.tsv: Vibrance → «Vibrance». со слов координатора 20.11.2026, лично не проверено |
| apps/materialcraft/crates/ui-egui/src/i18n/ru.rs | Appearance | Оформление | Внешний вид | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/materialcraft/crates/ui-egui/src/i18n/ru.rs | Select all | Выделить все | Выделить всё | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Select All → «Выделить всё». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/materialcraft/crates/ui-egui/src/i18n/ru.rs | Zoom in | Приблизить | Увеличить | glossary.tsv: Zoom In → «Увеличить». со слов координатора 20.11.2026, лично не проверено |
| apps/materialcraft/crates/ui-egui/src/i18n/ru.rs | Zoom out | Отдалить | Уменьшить | glossary.tsv: Zoom Out → «Уменьшить». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Appearance | Оформление | Внешний вид | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Center | Центр | По центру | glossary.tsv: Center → «По центру». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Key | Тональность | ключ | glossary.tsv: Key (эффект кеинга) → «ключ». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Mix | Микс | Микшер | glossary.tsv: Mix (окно SoundCraft) → «Микшер». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Path | Путь | контур | glossary.tsv: path (vector) → «контур». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Render | Просчитать | визуализировать | glossary.tsv: render (проза help; имя — контракт) → «визуализировать». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Tile | Рядом | тайл | glossary.tsv: tile (copy-on-write) → «тайл». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | Trim | Подрезка | подрезать | glossary.tsv: Trim → «подрезать». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | custom | свой | Пользовательский | glossary.tsv: Custom → «Пользовательский». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | cut | вырезание | Вырезать | glossary.tsv: Cut → «Вырезать». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | insert | вставка | Вставить | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | invert | инверсия | Инвертировать | glossary.tsv: Invert → «Инвертировать». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | notes | ноты | Примечания | glossary.tsv: Notes (table) → «Примечания». со слов координатора 20.11.2026, лично не проверено |
| apps/soundcraft/crates/ui-egui/locales/ru/mod.rs | trim | подстройка | подрезать | glossary.tsv: Trim → «подрезать». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Align Center | Выровнять по середине | Выровнять по центру | glossary.tsv: Align center → «Выровнять по центру». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Batch | Пакет | пакетная обработка | glossary.tsv: batch (проза help; имя — контракт) → «пакетная обработка». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Black & White | Черно-белое | Чёрно-белое | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Black & White → «Чёрно-белое». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Bottom | Внизу | Снизу | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Bring Forward | На один уровень вперёд | Переместить вперёд | glossary.tsv: Bring Forward → «Переместить вперёд». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Center | Центр | По центру | glossary.tsv: Center → «По центру». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Clipping Mask | Маска обрезки | обтравочная маска | glossary.tsv: clipping mask → «обтравочная маска». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Distribute | Распределить | распределение | glossary.tsv: distribute → «распределение». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Drop Shadow | Тень | Внешняя тень | glossary.tsv: Drop Shadow → «Внешняя тень». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Drop Shadow… | Тень… | Внешняя тень | glossary.tsv: Drop Shadow → «Внешняя тень». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Edit | Редактирование | Правка | glossary.tsv: Edit (меню) → «Правка» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Edit… | Редактировать… | Правка | glossary.tsv: Edit (меню) → «Правка» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Expand | Разобрать | Развернуть | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Expand… | Разобрать… | Развернуть | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Export As | Экспортировать как | Экспорт как | glossary.tsv: Export As → «Экспорт как». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Export As… | Экспортировать как… | Экспорт как | glossary.tsv: Export As → «Экспорт как». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Fit | Подгонка | Вписать | glossary.tsv: Fit (view) → «Вписать». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Flatten | Объединить | сведение | glossary.tsv: flatten → «сведение». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Get started | Начало работы | С чего начать | glossary.tsv: Get started → «С чего начать». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Grab bag | Произвольный набор | Разное | glossary.tsv: Grab bag → «Разное». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Hue | Оттенок | Цветовой тон | glossary.tsv: Hue → «Цветовой тон». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Justify | Выравнивание по ширине | По ширине | glossary.tsv: Justify → «По ширине». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Link | Связать | Ссылка | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Locked | Заблокированные | Заблокировано | glossary.tsv: Locked → «Заблокировано». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Merge | Слить | объединение | glossary.tsv: merge (layers) → «объединение». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Output | Вывод | выход | glossary.tsv: output (порт графа) → «выход». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Package | Упаковать | пакет | glossary.tsv: package (контейнер графов MaterialCraft) → «пакет». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Package… | Упаковать… | пакет | glossary.tsv: package (контейнер графов MaterialCraft) → «пакет». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Pen Tool | Инструмент «Перо» | Перо | glossary.tsv: Pen tool → «Перо». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Point Text | Точечный текст | текст из точки | glossary.tsv: point text → «текст из точки». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | RECENT | ПОСЛЕДНИЕ | Недавние | glossary.tsv: Recent → «Недавние». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Recent | Последние | Недавние | glossary.tsv: Recent → «Недавние». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Remove | Убрать | Удалить | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Scale | Масштабировать | Масштаб | glossary.tsv: Scale → «Масштаб». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Scale… | Масштабировать… | Масштаб | glossary.tsv: Scale → «Масштаб». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Select | Выделение | Выбрать | glossary.tsv: Select → «Выбрать». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Settings… | Параметры… | Настройки | glossary.tsv: Settings → «Настройки». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Show All | Показать всё | Показать все | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Show All → «Показать все». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Sort | Сортировать | Сортировка | glossary.tsv: Sort → «Сортировка». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Tile | Плитка | тайл | glossary.tsv: tile (copy-on-write) → «тайл». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Top | Вверху | Сверху | glossary.tsv. со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Unsharp Mask | Нерезкая маска | Контурная резкость | glossary.tsv: Unsharp Mask → «Контурная резкость». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | Unsharp Mask… | Нерезкая маска… | Контурная резкость | glossary.tsv: Unsharp Mask → «Контурная резкость». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | View | Просмотр | Вид | glossary.tsv: View (меню) → «Вид» (ключ рядом с меню File/Window/Help). со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | arrowhead | Перо | Растушёвка | glossary.tsv: Feather → «Растушёвка». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | diagnostics | отрисовка | визуализировать | glossary.tsv: render (проза help; имя — контракт) → «визуализировать». со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | swatch | Желтый | Жёлтый | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Yellow → «Жёлтый». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |
| apps/vectorcraft/crates/ui-egui/src/i18n/ru.tsv | swatch | Зеленый | Зелёный | поправка координатора 20.11 (2): в интерфейсе только «ё». glossary.tsv: Green → «Зелёный». со слов координатора 20.11.2026, лично не проверено со слов координатора 20.11.2026, лично не проверено |

