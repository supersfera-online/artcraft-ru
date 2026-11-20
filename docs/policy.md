# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# Политика приёма переведённых человеческих документов

Составлено 20 ноября 2026, зона America/Los_Angeles (PT, UTC−8). Только чтение: issue, PR, комментарии, форки, звёзды, письма и Discord не создавались и не отправлялись; на компьютеры правообладателя никто не заходил; существующие файлы не перезаписывались и не удалялись.

Вопрос: принимают ли авторы ArtCraft (организация [storytold](https://github.com/storytold)) и SolidCraft (организация [tangency-labs](https://github.com/tangency-labs)) переведённые *человеческие* документы (README, книги в `book/`, справка F1, docs, сайт, wiki) и в каком виде их класть.

Это не про перевод строк интерфейса (каталоги TSV/JSON). Каталоги UI описаны в плане `plan-ru-localization.md` и здесь упоминаются только когда без них нельзя понять путь для документов.

Пометки: **[проверено: источник]** — публичная страница, API GitHub или файл в клоне / raw; **[из файла: путь]** — локальная база раздела; **[догадка]**; **[не проверено]**.

## Краткий вывод

1. Отдельного письменного правила «мы принимаем перевод README/книг/wiki на русский и класть его сюда» ни у Storytold, ни у Tangency Labs **не найдено**. **[проверено: поиск CONTRIBUTING/README и docs по всем публичным репозиториям обеих организаций, 20.11.2026]**
2. Образец перевода README в Storytold уже есть, но не на русском: файлы вида `README.<код>.md` рядом с английским `README.md` и переключатель языков в шапке. Так сделано в [craft-anything](https://github.com/storytold/craft-anything) (10 языков, `README.ru.md` нет) и в [lightcraft](https://github.com/storytold/lightcraft) (только `README.zh-hans.md` и `README.zh-hant.md`). В остальных проверенных репозиториях, включая photocraft и solidcraft, переводных README нет. **[проверено: корни репозиториев и code search `filename:README.ru.md` / `README.es.md`, org:storytold]**
3. Книги (mdBook) сейчас одноязычные: `language = "en"`. У PhotoCraft ещё `multilingual = false`. Отдельных `book/ru/` или `docs/ru/` нет. **[проверено: book.toml / docs/book/book.toml]**
4. Официальный живой путь пользовательской справки Storytold — сайт [craft.wiki](https://craft.wiki), репозиторий [storytold/craft-wiki](https://github.com/storytold/craft-wiki). Править можно pull request'ом в GitHub или визуальным редактором (Sveltia CMS). В конфиге Starlight локалей нет, папок перевода нет. **[проверено: README и astro.config.mjs craft-wiki; живая страница https://craft.wiki/apps/photocraft/getting-started/ ]**
5. Задуманный путь пользовательских страниц на getartcraft.com — каталог `docs/user/` в репозитории программы, URL вида `https://getartcraft.com/docs/photocraft/...`. Так написано в `docs/user/AGENTS.md` у photocraft, lightcraft, designcraft и effectcraft. На главной ветке сайта (`artcraft-services`, приложение `artcraft-website-next`) маршрута `/docs` нет, а живые URL `/docs` и `/docs/photocraft` 20.11.2026 отвечают **404**. **[проверено: AGENTS.md; дерево frontend/apps/artcraft-website-next/src/app; HTTP 404]**
6. Weblate у Storytold относится к **каталогам интерфейса** в craft-i18n (TSV → ветка `weblate` с PO-файлами, ADR 0006), не к README/книгам/wiki. Публичного адреса инстанса не найдено; в README craft-i18n для переводчиков по-прежнему указан pull request. Crowdin не найден. **[проверено: локальный клон craft-i18n, ADR 0006, workflow weblate.yml, ветка origin/weblate; README; проверка типичных URL Weblate]**
7. Отдельного CLA (Contributor License Agreement) в корне репозиториев нет. Вклад обычно принимают под той же лицензией, что и проект (у программ Storytold и SolidCraft чаще всего MIT OR Apache-2.0), фразой вроде «by contributing you agree…». **[проверено: поиск файла CLA.md во всех публичных репо; тексты CONTRIBUTING у craft-anything и solidcraft]**
8. Запрос «перевод UI и документации» SolidCraft на сербский ([issue #7811](https://github.com/tangency-labs/solidcraft/issues/7811)) сопровождающие закрыли только для каталога интерфейса; про книгу и docs они в ответах не сказали. **[проверено: тело issue и три комментария]**

Следствие для работы: формат `README.ru.md` разумно брать как *образец уже принятых переводов* в двух репозиториях, но не как объявленное правило для всех. Куда класть русский текст книги, `docs/user`, craft.wiki и сайта — открытый вопрос, его можно решить только письмом авторам (письмо в этой работе не писалось).

## Что уже было в плане (разделы 4.5–4.6)

Из `plan-ru-localization.md` (сохранены и затем проверены заново):

- у photocraft есть английская книга `book/src/`; **[из файла; подтверждено деревом main 20.11.2026]**
- у многих программ есть `docs/localization*.md`, в том числе русские заметки у photocraft и lightcraft (это заметки о переводе *интерфейса*, не перевод руководства); **[из файла; подтверждено]**
- у craft-anything переведены README на несколько языков, русского нет; **[из файла; подтверждено, список языков расширен — см. ниже]**
- справка F1 отдельно не разбиралась; **[из файла; в этой работе разобрана, см. раздел «Справка F1»]**
- сайт getartcraft.com и репозитории artcraft / craft-wiki в плане были помечены «не проверено»; **[из файла; в этой работе проверены]**

---

## Storytold / ArtCraft

### Организации и объём проверки

Публичных репозиториев организации storytold на 20.11.2026: **69**. **[проверено: GitHub search org:storytold]** Среди них комплекты Craft-программ, общие библиотеки, сайт, wiki — и более старые, к комплекту не относящиеся (плагины Unreal, mocap, fakeyou и т.п.; часть в архиве).

У каждого из 69 проверено наличие в корне `README.md`, `CONTRIBUTING.md`, `README.ru.md`, `README.es.md`, `CLA.md` и `docs/contributing.md` (GET raw GitHub, ветка по умолчанию). **[проверено]**

`README.ru.md` нет ни в одном. `CLA.md` нет ни в одном. `README.es.md` есть только у craft-anything. **[проверено]**

Организационный репозиторий [storytold/.github](https://github.com/storytold/.github) даёт только шаблон описания pull request (`.github/pull_request_template.md`) и короткий README; общего `CONTRIBUTING.md` по умолчанию нет. Шаблон отсылает к [craft-contrib standards/pull-requests.md](https://github.com/storytold/craft-contrib/blob/main/standards/pull-requests.md). **[проверено: https://github.com/storytold/.github и raw файлы]**

### Лицензия вклада и CLA

- У большинства Craft-программ лицензия **MIT OR Apache-2.0**. **[из файла: plan-ru-localization.md; подтверждено SPDX в карточках репозиториев]**
- [craft-anything/CONTRIBUTING.md](https://github.com/storytold/craft-anything/blob/main/CONTRIBUTING.md): «Code is dual-licensed under MIT or Apache-2.0 … by contributing you agree your work is licensed the same way.» Отдельного CLA нет. Также: «Everything is our own work: no code, names or wording copied from other projects.» **[проверено]**
- [photocraft/docs/contributing.md](https://github.com/storytold/photocraft/blob/main/docs/contributing.md): вклады MIT OR Apache-2.0; логотипы в `docs/brand/` не открыты; правило чистой комнаты (не копировать код и ресурсы из Photoshop и т.п.). Про перевод README/книги там нет. **[проверено]**
- То же правило чистой комнаты для *строк интерфейса* в [craft-i18n/README.md](https://github.com/storytold/craft-i18n/blob/main/README.md): писать от смысла английской строки, не подглядывать в чужую локализацию; если пользовали ИИ — написать в ATTRIBUTION.md; желательна проверка носителем. Это про каталоги TSV, не про документы, но авторы, скорее всего, ожидают то же и для текстов. **[проверено README; отнесение к документам — догадка]**
- Поиск файлов `CLA` / «Contributor License» по org:storytold в плане уже давал пустой результат, кроме vendored-кода. **[из файла: plan-ru-localization.md]** В этой работе файла `CLA.md` в корнях публичных репо нет; полный текст *всех* CONTRIBUTING у старых не-Craft репозиториев не вычитывался построчно, только наличие файла. **[проверено наличие; полный текст всех файлов — не проверено, как и в плане]**

Корневой `CONTRIBUTING.md` есть у: autocraft, craft-ai-integrations, craft-anything, effectcraft, filmcraft, indd-utils. У photocraft — только `docs/contributing.md`. У filmcraft — и корень, и `docs/contributing.md`. У большинства остальных Craft-репозиториев отдельного CONTRIBUTING нет. **[проверено: raw, 20.11.2026]**

Кто ревьюит вклады в GitHub: сопровождающие репозитория, через pull request. В шаблоне PR — разделы What / Test / Verification по стандарту craft-contrib. Требования обязательного ревью в craft-i18n «пока нет» (это сказано в ADR 0006 про main). **[проверено: ADR 0006 и шаблон PR]**

Пометки «проверено / не проверено» для *перевода документов* не найдены. В `docs/user/` поле frontmatter `verified:` — это версия программы, по которой страницу сверили, не статус перевода. **[проверено: photocraft/docs/user/AGENTS.md и страницы]** В ATTRIBUTION.md craft-i18n переводчик сам указывает, смотрел ли носитель — снова про каталоги UI. **[проверено: README craft-i18n]**

### Weblate / Crowdin / craft-i18n

Репозиторий [storytold/craft-i18n](https://github.com/storytold/craft-i18n) — общее место **каталогов интерфейса** (TSV), не человеческих документов. README предлагает править `locales/<язык>/*.tsv` и открывать PR; частичные каталоги принимаются. **[проверено: локальный клон origin https://github.com/storytold/craft-i18n.git, README.md]**

ADR 0006 (`docs/adr/0006-suggestions-in-self-hosted-weblate.md`, коммит 3c42e286, 8 ноября 2026 UTC) описывает *свой* Weblate: предложения и голоса, принятие делает Reviewer локали, в `main` попадает только через PR; git/TSV остаётся источником правды; конвертер TSV↔PO; внешние MT и общая память перевода выключены из-за чистой комнаты; runbook `docs/weblate-runbook.md` «пишется до запуска». Этого runbook на `main` нет. **[проверено: файл ADR и отсутствие runbook в клоне]**

На `main` есть workflow `.github/workflows/weblate.yml` и инструменты `tools/weblate_bridge.py`. Ветка `origin/weblate` существует и обновляется экспортом: последний видимый коммит `e2828310`, сообщение «Export from main@b5b28057…», **20 ноября 2026, 14:04 UTC (06:04 PT)**. На ветке PO-файлы (`common/ru.po` и каталоги программ). **[проверено: git в локальном клоне]**

README на `main` Weblate как способ перевода *не упоминает*. Проверенные публичные адреса (`weblate.getartcraft.com`, `translate.getartcraft.com`, `i18n.getartcraft.com`, `weblate.storyteller.ai`, `translate.storyteller.ai`) не открылись (нет ответа). Страницы hosted.weblate.org/projects/{storytold,artcraft,craft-i18n} вернули HTTP 403 (возможна блокировка бота, не доказательство, что проекта нет). **[проверено попыткой HTTP; наличие публичного инстанса — не подтверждено]**

Вывод: инфраструктура экспорта в Weblate для **каталогов UI** уже есть; запущен ли публичный инстанс и принимают ли там работу — по открытым страницам не видно. К человеческим документам Weblate по ADR 0006 не относится («Only catalogs whose source of truth is here are offered»). Crowdin в репозиториях и ADR не найден. **[проверено; публичный URL — не проверено до конца]**

### Образцы перевода README (куда класть, если делать как уже принято)

Единственный найденный формат уже влитых переводов README:

`README.<код языка>.md` в **корне того же репозитория**, плюс строка-переключатель в шапке английского README (и зеркально в переводах — **[не проверено построчно для всех файлов, проверено для шапки английского]**).

| Репозиторий | Файлы | Русский | Объём (байты, main) |
|---|---|---|---|
| [storytold/craft-anything](https://github.com/storytold/craft-anything) | `README.md` (англ., 27878), `README.ja.md` (32055), `README.zh.md` (24886), `README.zh-hant.md` (29014), `README.ko.md` (33344), `README.es.md` (29486), `README.fr.md` (31591), `README.vi.md` (32929), `README.pt.md` (31134), `README.th.md` (53569), `README.tr.md` (30705) | нет `README.ru.md` | см. слева |
| [storytold/lightcraft](https://github.com/storytold/lightcraft) | `README.md` (53913), `README.zh-hans.md` (42856), `README.zh-hant.md` (48694) | нет | см. слева |

**[проверено: listing корня craft-anything; raw lightcraft; code search filename:README.es.md — только craft-anything; filename:README.ru.md — 0 по org:storytold]**

В CONTRIBUTING этих репозиториев отдельной инструкции «добавьте README.ru.md» нет. **[проверено: CONTRIBUTING.md craft-anything; у lightcraft корневого CONTRIBUTING.md нет]**

У остальных Craft-программ, включая photocraft, pdfcraft, wordcraft, vectorcraft, solidcraft, переключателя языков в начале README и файлов `README.*.md` не видно. **[проверено пробой raw и разбором начала README у списка Craft-репо]**

### Таблица: человеческие документы по репозиториям Storytold (комплект и связанные)

«Куда класть перевод», если авторы согласятся, ниже — по *существующему образцу* или «официального формата нет». Это не разрешение публиковать PR.

| Репозиторий | README / CONTRIBUTING | Книга / user-docs | Официального формата перевода документов | Замечание |
|---|---|---|---|---|
| photocraft | README.md 36767 байт; `docs/contributing.md` 13906; корневого CONTRIBUTING нет | mdBook `book/` (`language=en`, `multilingual=false`); `docs/user/` задуман для сайта | Образца перевода нет. Если как у craft-anything — `README.ru.md`. Для книги и docs/user формата нет | Подробный список — раздел «PhotoCraft, с чего начать» |
| lightcraft | README + zh-hans/zh-hant; `docs/localization.md`, `docs/localization-ru.md`; `docs/user/` | `docs/user/` → задумано `https://getartcraft.com/docs/lightcraft` (сейчас 404) | README: `README.ru.md` по образцу уже принятых zh-файлов | |
| craft-anything | CONTRIBUTING.md + 10 переводных README, без ru | `docs/localization.md` (UI) | README: `README.ru.md` + ссылка в шапке | Самый явный прецедент |
| designcraft, effectcraft | README; у effectcraft есть CONTRIBUTING.md | есть `docs/user/` и AGENTS.md с URL getartcraft.com/docs/&lt;app&gt; (живые URL не проверялись все; шаблон тот же, что у photocraft) | Формата перевода нет | Предположительно тот же незапущенный конвейер сайта |
| pdfcraft, wordcraft, vectorcraft, filmcraft, cadcraft, figcraft, gridcraft, deckcraft, soundcraft, texturecraft, materialcraft, craft-launcher | README есть; CONTRIBUTING — у filmcraft и effectcraft (см. выше); у остальных часто нет | отдельных book/ и docs/user/ в пробе не найдено | Формата нет; wiki живёт в craft-wiki | Localization-заметки (UI) есть у части (pdfcraft, cadcraft и др.) |
| anicraft | README 25290; `docs/localisation.md` (UI/CLI: часть вещей нарочно не переводят) | Встроенная книга `docs/guide/` (~419 КБ, 23 md), см. F1 | Формата перевода книги нет | F1 открывает эту книгу, не wiki |
| craft-i18n | README, без CONTRIBUTING | docs/ — формат каталогов и ADR, не user guide | Перевод UI: TSV + PR (и, возможно, будущий Weblate). Документы репозитория — только по-английски | |
| craft-wiki | README 17820, CONTRIBUTING нет | это и есть wiki | Локалей в Starlight нет, формата перевода нет | См. раздел craft-wiki |
| artcraft-services | README 14131, лицензия в карточке NOASSERTION; vendored CONTRIBUTING в чужом SDK | исходники сайта getartcraft.com | i18n-каталогов и локалей Next.js нет | См. раздел сайта |
| artcraft | README 15505, homepage getartcraft.com | `docs/` — внутренние заметки (performance, website-login); frontend — приложение, не маркетинг-сайт | папок i18n/locale нет | Путать с artcraft-services не следует |
| craft-libs, craft-fonts, craft-extensions, craft-contrib, craft-skills, craft-common-actions, autocraft, craft-ai-integrations, корпуса, launcher-assets и пр. | README есть (кроме отдельных пустых/архивных) | книги пользовательской справки не искались так же подробно, как у приложений | формата перевода документов нет | Не первый приоритет для ru-доков |
| Старые репо (Unreal, mocap, fakeyou, html_test, voder-proxy и т.д.) | у большинства короткий README, CONTRIBUTING нет (кроме vendored в storyteller-ml и indd-utils) | к комплекту ArtCraft у правообладателя не относятся | — | Проверено только наличие файлов в корне |

**[проверено: проба raw и деревья; строки «формата нет» означают, что готовой схемы перевода документов в репозитории не видно, а не то, что авторы заранее откажутся]**

---

## Справка F1 (откуда текст, где лежит)

Поведение **разное в разных программах**. Общего механизма «F1 всегда открывает одну папку» нет. **[проверено сравнением нескольких репо]**

### AniCraft — встроенная книга, F1 привязан к разделам

- Клавиша F1 и пункт «Help › Help for This» открывают *руководство пользователя* на разделе про текущий инструмент, панель, диалог или команду. Карта ссылок — `src/context_help.rs` (ADR 0096). **[проверено: текст модуля и docs/adr/0096-guide-search-and-context-help.md]**
- Текст глав лежит в репозитории **`docs/guide/`** (Markdown). Крейт `anicraft-guide` (`crates/guide`) собирает эти главы в книгу (`include_str!`, ADR 0069: «The user guide, bundled for Help › User Guide»). В веб-сборке книга отдаётся страницами. **[проверено: Cargo.toml, ADR 0069, дерево docs/guide/]**
- Объём `docs/guide/`: **23 файла, ≈419 КБ** Markdown, в том числе сгенерированный `docs/guide/reference/commands.md` (≈110 КБ). **[проверено: размеры blob в дереве main]**
- Формата перевода этой книги (например `docs/guide/ru/`) в репозитории нет. **[проверено: дерево, один английский каталог]**

### MaterialCraft (и похожие ссылки в TextureCraft) — браузер на craft.wiki

Файл [materialcraft/crates/ui-egui/src/help_links.rs](https://github.com/storytold/materialcraft/blob/main/crates/ui-egui/src/help_links.rs): пункты меню Help открывают HTTPS-страницы, не встроенные файлы. Примеры: документация → `https://craft.wiki/apps/materialcraft/overview/`, обучение → `.../getting-started/`, требования → `.../install-update/`, устранение проблем → `.../troubleshooting/`; ещё GitHub releases/issues, Discord, `https://getartcraft.com/support` и страница приложения на сайте. **[проверено: исходник]** У TextureCraft в поиске кода есть те же идентификаторы `ui.help.docs` в меню. **[проверено: search ui.help.docs]**

### PhotoCraft — отдельной привязки F1 к книге в индексе кода не видно

- Поиск `Key::F1` по org:storytold нашёл привязки у wordcraft, vectorcraft, cadcraft, soundcraft, effectcraft, anicraft, gridcraft, figcraft, designcraft, texturecraft и в craft-libs; **photocraft в этой выдаче нет**. **[проверено: GitHub code search]** Это не доказательство, что F1 в программе ничего не делает (общая библиотека меню могла перехватить клавишу иначе), но отдельного «F1 → глава руководства» в репозитории photocraft, как у AniCraft, не видно. **[догадка в скобках; факт — отсутствие попадания в поиск и отсутствие help_links.rs / docs/guide]**
- Меню Help есть (TOP_MENUS включает "Help"). В `menus/items.rs` комментарий: сначала пункты-ссылки и проверка обновлений, разделитель, затем System Info и About. Обработчики в `menus/invoke.rs` явно разобраны для `help.checkForUpdates`, `help.systemInfo`, `help.about`. Страница `docs/user/troubleshooting/get-help.md` описывает **Help › Report an Issue…** и **Help › System Info…**. Точный список URL пунктов-ссылок в этой работе из каталога команд полностью не выписан. **[проверено: menus/bar.rs, items.rs, invoke.rs, get-help.md; полный список ссылок — не проверено]**
- Тексты для людей в репозитории: `book/` (mdBook), `docs/user/` (задуманы для сайта), плюс страницы программы на craft.wiki (другой репозиторий). Ни один из этих наборов в коде photocraft как цель F1 не подключён в найденных файлах. **[проверено в пределах указанных файлов]**

### SolidCraft — онлайн-книга в браузере

`crates/ui-egui/src/help.rs`: пункт Documentation меню Help (кнопка «?») делает `open_url` на постоянный адрес `https://docs.solidcraft.io/`. Это не встроенный Markdown внутри окна. **[проверено: raw help.rs, константа DOCS_URL]** Живой сайт отвечает 200; `https://tangency-labs.github.io/solidcraft/` перенаправляет на `docs.solidcraft.io`. **[проверено: HTTP]** Исходники книги: `docs/book/` в [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft). Связь именно клавиши F1 с этим пунктом в help.rs не расписана (меню вызывается по «?»); отдельный поиск `Key::F1` по org:tangency-labs в одном из запросов не дал разобранного результата (ошибка/пустой ответ инструмента). **[не проверено: привязка именно F1 у SolidCraft]**

---

## getartcraft.com (откуда собирается, есть ли исходники)

- Публичный сайт [getartcraft.com](https://getartcraft.com). Страница [ /support](https://getartcraft.com/support) — по-английски: Discord, почта hello@storyteller.ai, FAQ. **[проверено: выборка страницы 20.11.2026]**
- Исходники маркетингового сайта — не storytold/artcraft, а **[storytold/artcraft-services](https://github.com/storytold/artcraft-services)**, приложение `frontend/apps/artcraft-website-next` (Next.js). Есть также `artcraft-desktop-website`, `artcraft-webapp`, `artcraft-dashboard` и скрипты `script/website/`. **[проверено: дерево репозитория; ссылки на craft.wiki в site-nav/site-footer; редиректы в next.config.ts на /apps/…]**
- В `next.config.ts` **нет** `i18n.locales` и нет каталогов `i18n/` / `locales/` в этом приложении. **[проверено: next.config.ts и обход дерева]**
- Маршруты `src/app/`: `/`, `/apps`, `/apps/[slug]`, `/support`, `/faq`, `/news`, `/tutorials`, `/download`, `/linux`, `/pricing`, `/studio`, `/press-kit` и зеркала пакетных репозиториев. **Маршрута `src/app/docs` нет.** **[проверено: список файлов src/app]**
- При этом `docs/user/AGENTS.md` в photocraft, lightcraft, designcraft, effectcraft утверждает, что страницы из `docs/user/` публикуются на `https://getartcraft.com/docs/<приложение>/...`, и что проверщик живёт в `artcraft-services/.../scripts/docs/core.mjs`, «CI появится, когда это попадёт на main». На main этих скриптов в `scripts/` приложения сайта нет. Живые `https://getartcraft.com/docs/`, `/docs/photocraft`, `/docs/photocraft/` и `/docs/craft-launcher` 20.11.2026 дают **404**. **[проверено]**
- Репозиторий artcraft-services в карточке GitHub с лицензией NOASSERTION; в корне есть LICENSE.md. Это, скорее всего, не полностью «как MIT-приложение». Вклады в тексты сайта без письма авторам неясны ещё и из-за этого. **[проверено карточку и наличие LICENSE.md; юридический вывод — не проверено]**

Итого по сайту: официальный *задуманный* путь для пользовательских гайдов описан в `docs/user/AGENTS.md` (править Markdown в репозитории программы, публикация на getartcraft.com/docs/…). Официального *работающего* конвейера на сегодняшнем main сайта нет. Перевода сайта и схемы `/ru/` или locale-префикса нет. Писать авторам сайта в этой работе нельзя.

Репозиторий [storytold/artcraft](https://github.com/storytold/artcraft) — это в первую очередь само приложение ArtCraft Studio (Rust + frontend), не генератор getartcraft.com. **[проверено: дерево и docs/]**

---

## craft-wiki (где живёт, как правится)

- Репозиторий: [storytold/craft-wiki](https://github.com/storytold/craft-wiki). Сайт: [https://craft.wiki](https://craft.wiki). **[проверено: README, homepage репозитория, живые страницы]**
- Стек: Astro + Starlight, деплой через GitHub Actions hook → Cloudflare Workers Builds, Worker отдаёт статику и вход в редактор. **[проверено: README, wrangler.jsonc, .github/workflows/deploy.yml]**
- Содержание: Markdown/MDX в `src/content/docs/`. Страницы приложений — `src/content/docs/apps/<slug>/`, URL `/apps/<slug>/...`. В сайдбаре, среди прочих, PhotoCraft, остальные Craft-приложения, **SolidCraft**, MailCraft и гайд «Connect an AI assistant». **[проверено: astro.config.mjs]**
- Как править (официальный путь, уже описан авторами):
  1. Pull request в GitHub в этот репозиторий (обычные Markdown-файлы).
  2. Визуальный редактор Sveltia CMS: `/edit/` → `/admin/`. Backend GitHub, ветка `main`, `open_authoring: true`, `publish_mode: editorial_workflow`. Коллекции по приложениям в `public/admin/config.yml`. **[проверено: README и config.yml]**
  3. Вход через Discord: роль **Senior Contributor** на сервере ArtCraft, без GitHub-аккаунта; коммиты делает GitHub App «Craft Wiki[bot]», только в `src/content/docs/apps/` и `public/assets/uploads/`. Либо вход токеном GitHub для тех, у кого есть write, либо через fork (в README прямо сказано, что контрибьюторам нужно право создавать форк). **[проверено: README раздел Visual editor]**
- i18n: в `astro.config.mjs` нет `locales` / `defaultLocale` Starlight. Дерево контента без `src/content/docs/ru` или языковых префиксов. **[проверено]**
- Пометки перевода «проверено/не проверено» в схеме CMS нет (поля: title, description, sidebar, body; у части приложений type/category/cover). **[проверено: config.yml]**
- Объём исходников (только `src/content/docs/apps/*`, байты blob, без картинок public/): vectorcraft заметно больше остальных (~1,9 МБ, 137 файлов); photocraft — **7 файлов, 47205 байт** (`overview`, `getting-started`, `install-update`, `workflows`, `troubleshooting`, `file-formats`, `automation`). SolidCraft на wiki — 5 файлов, ≈27 КБ (это не замена docs.solidcraft.io). **[проверено: дерево main craft-wiki]**
- Как это соотносится с `docs/user/` в photocraft: это **разные** наборы (другая структура папок и другие тексты; вики-getting-started не совпадает с docs/user). Синхронизации между ними в найденных файлах нет. **[проверено сравнением путей и выборки страниц]**

Официальный путь *править английскую wiki* есть. Официального пути *положить русский перевод* (подкаталог, отдельный сайт, Starlight locales) нет.

---

## Tangency Labs / SolidCraft

Публичных репозиториев org:tangency-labs на 20.11.2026: **17**. **[проверено]** У всех, кроме `design` и пустого `solidcraft-plugins`, есть README; корневой CONTRIBUTING.md есть у solidcraft, solidcore, solidcraft-library, fieldcraft, pcbcraft. Файлов `CLA.md` и `README.ru.md` нет. **[проверено: raw-проба]**

### SolidCraft (главный проект)

- Репозиторий [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft), сайт продукта [solidcraft.io](https://solidcraft.io), книга [docs.solidcraft.io](https://docs.solidcraft.io). Лицензия **Apache-2.0** в карточке; CONTRIBUTING говорит «licensed as MIT OR Apache-2.0» (нужно не путать формулировки). **[проверено: карточка, CONTRIBUTING раздел Licence, HTTP 200 для обоих сайтов]**
- [CONTRIBUTING.md](https://github.com/tangency-labs/solidcraft/blob/main/CONTRIBUTING.md): чистая комната (не копировать help text и tooltip'ы чужих CAD); «By contributing you agree that your contribution is licensed as MIT OR Apache-2.0»; для бренда/интерфейса — ещё LICENSE-BRAND. Отдельного CLA нет. Есть раздел «Pictures in the user guide» (`docs/book/src/media/`, скрипт `examples/demo/doc_shots.py`) — про английские иллюстрации, не про перевод. **[проверено]**
- `docs/localization.md` озаглавлен **«UI localization»**: JSON-каталоги `assets/locales/*.json`, регистрация языка, покрытие, RTL. Это не политика перевода книги. **[проверено: заголовки и начало файла]**
- Книга: `docs/book/book.toml` — `language = "en"`, `src = "src"`, публикация с `edit-url-template` на GitHub, сборка в `target/book`. Оглавление `docs/book/src/SUMMARY.md`: user guide, developer guide, reference (включая `reference/glossary.md`). Страница contributing в книге — включение корневого CONTRIBUTING.md. **[проверено]** Многоязычного mdBook (`[language.xx]` или второй src) нет.
- Меню Help открывает онлайн-книгу, см. выше.
- Исходники маркетингового сайта Tangency — [tangency-labs/website](https://github.com/tangency-labs/website) (MIT), не i18n в README. **[проверено: README]**
- [Issue #7811](https://github.com/tangency-labs/solidcraft/issues/7811) (27 октября 2026 UTC): автор просит перевод «The UI and documentation» на сербскую кириллицу. Сопровождающий (COLLABORATOR) ответил только про каталог `assets/locales` и регистрацию в `i18n.rs`; 2 ноября сообщил, что локаль уже в интерфейсе 0.30.0 как «Српски» (`sr.json`). Про книгу / documentation в ответах ни слова. Issue остаётся открытым, label needs-triage к моменту чтения комментариев 2 ноября ещё фигурировал в метаданных поиска. **[проверено: issue и комментарии]** Это нельзя читать как «документацию переводить не принимают» — только как «на этот вопрос не ответили».

Куда класть перевод документов SolidCraft: официального формата нет. Кандидаты, если авторы согласятся: параллельная книга (потребует изменить book.toml), отдельные файлы, или страницы на craft.wiki (там уже есть короткий английский раздел SolidCraft — другой издатель и другой сайт). Что они выберут — только письмом. Не класть перевод в `assets/locales/*.json`: это UI, не главы книги.

### Другие репозитории Tangency

| Репозиторий | Документы | Перевод документов |
|---|---|---|
| fieldcraft | mdBook `docs/book.toml`, `language=en`, сайт https://tangency-labs.github.io/fieldcraft/ ; есть CONTRIBUTING.md | Формата перевода нет **[проверено book.toml]** |
| design | mdBook `book.toml`, `language=en`, GitHub Pages включены; корневого README.md нет (404) | Формата нет |
| pcbcraft, solidcore, solidcraft-library | CONTRIBUTING + README; у pcbcraft — карта документации и проверка ссылок в docs | Про перевод документов в CONTRIBUTING не сказано (проверка ссылок — английские docs) **[проверено выборочно]** |
| website, solidcraft-app, homebrew-tap, models, leaderboard, solidcore-* | README (кроме plugins) | Не user guide комплекта; формата перевода нет |

---

## PhotoCraft: документы-кандидаты, с которых начинать перевод

Приоритет, как в плане (этап 3): сначала там, где уже есть образцы перевода README (это не photocraft, а craft-anything/lightcraft) и книга PhotoCraft. Ниже — только photocraft, с путями и объёмом по ветке `main` на 20.11.2026. Объём — размер исходного файла в байтах (UTF-8, в основном английский Markdown), не «листы».

### 1. README (образец формата — `README.ru.md`)

| Путь | Байты | Замечание |
|---|---|---|
| [README.md](https://github.com/storytold/photocraft/blob/main/README.md) | 36767 | Перевода нет; в шапке нет переключателя языков, в отличие от craft-anything и lightcraft |

Класть, *если авторы согласятся по уже принятому образцу*: `README.ru.md` в корне и ссылка в шапке. Письменного приглашения именно для photocraft нет.

### 2. Книга mdBook `book/` (первый крупный кандидат)

`book/book.toml`: title «PhotoCraft Documentation», `language = "en"`, **`multilingual = false`**. Сборка в `book/output`, правка через GitHub edit URL. **[проверено: book.toml]**

Всего исходников книги ≈ **94 КБ** (включая book.toml 649 байт; главы ≈ **93378 байт**). Отдельного `book/ru` нет.

| Путь | Байты |
|---|---|
| book/book.toml | 649 |
| book/src/README.md | 2208 |
| book/src/SUMMARY.md | 1678 |
| book/src/getting-started/installation.md | 1148 |
| book/src/getting-started/building.md | 1188 |
| book/src/getting-started/contributing.md | 1559 |
| book/src/formats/overview.md | 1190 |
| book/src/formats/pcraft.md | 3316 |
| book/src/formats/psd-psb.md | 1583 |
| book/src/formats/raster-formats.md | 9883 |
| book/src/formats/svg.md | 2402 |
| book/src/formats/affinity.md | 2321 |
| book/src/architecture/overview.md | 1887 |
| book/src/architecture/crates.md | 1886 |
| book/src/architecture/command-engine.md | 1972 |
| book/src/architecture/rendering.md | 1460 |
| book/src/architecture/automation.md | 1636 |
| book/src/automation/overview.md | 1448 |
| book/src/automation/cli.md | 8394 |
| book/src/automation/mcp.md | 5469 |
| book/src/automation/control-protocol.md | 2947 |
| book/src/automation/security-model.md | 4837 |
| book/src/development/testing.md | 1115 |
| book/src/development/dependencies.md | 1164 |
| book/src/development/fuzzing.md | 827 |
| book/src/development/release-security.md | 1549 |
| book/src/security/overview.md | 3317 |
| book/src/security/threat-model.md | 3894 |
| book/src/security/trust-boundaries.md | 2356 |
| book/src/security/automation-security.md | 7823 |
| book/src/security/parser-hardening.md | 2375 |
| book/src/security/secure-file-handling.md | 3043 |
| book/src/security/fuzzing.md | 2062 |
| book/src/security/vulnerability-reporting.md | 1069 |
| book/src/project/roadmap.md | 951 |
| book/src/project/licenses.md | 879 |
| book/src/project/credits.md | 542 |

**[проверено: дерево storytold/photocraft main]** Книга смешана: getting-started и formats полезны художнику; architecture / development / security / automation — скорее разработчикам и агентам. Имеет смысл начинать с `getting-started/` и `formats/`, если авторы примут перевод, и спросить их про формат (включать ли `multilingual` mdBook).

### 3. Пользовательские страницы `docs/user/` (задуманы для getartcraft.com)

По AGENTS.md публикуется всё в папке, кроме AGENTS.md, CLAUDE.md и README.md. Живой URL пока 404. Сумма публикуемых `.md` ≈ **34514 байт** (20 файлов).

| Путь | Байты |
|---|---|
| docs/user/index.md | 1646 |
| docs/user/getting-started/index.md | 1085 |
| docs/user/getting-started/install.md | 4336 |
| docs/user/guides/index.md | 524 |
| docs/user/guides/open-and-save-files.md | 2647 |
| docs/user/guides/adjust-colors-with-adjustment-layers.md | 1999 |
| docs/user/guides/select-and-mask.md | 2168 |
| docs/user/guides/add-and-style-text.md | 2155 |
| docs/user/guides/export-an-image.md | 2085 |
| docs/user/troubleshooting/index.md | 477 |
| docs/user/troubleshooting/photocraft-does-not-start.md | 4716 |
| docs/user/troubleshooting/taskbar-turns-black.md | 2108 |
| docs/user/troubleshooting/canvas-size-white-border.md | 1975 |
| docs/user/troubleshooting/text-moves-when-editing.md | 2174 |
| docs/user/troubleshooting/get-help.md | 1062 |
| docs/user/faq/index.md | 327 |
| docs/user/faq/is-photocraft-free.md | 633 |
| docs/user/faq/open-photoshop-files.md | 1266 |
| docs/user/faq/replace-photoshop.md | 1131 |
| docs/user/AGENTS.md | 2818 (не публикуется) |
| docs/user/CLAUDE.md | 69 (не публикуется) |

Формата `docs/user/ru/` в правилах нет. Пока конвейер сайта не работает, перевод этих страниц всё равно куда-то нужно будет согласовать.

### 4. Страницы PhotoCraft на craft.wiki (другой репозиторий)

`src/content/docs/apps/photocraft/` в storytold/craft-wiki, **7 файлов, 47205 байт**:

| Путь в craft-wiki | Байты | Живой URL |
|---|---|---|
| …/overview.md | 3710 | https://craft.wiki/apps/photocraft/overview/ |
| …/getting-started.md | 2702 | https://craft.wiki/apps/photocraft/getting-started/ |
| …/install-update.md | 7180 | https://craft.wiki/apps/photocraft/install-update/ |
| …/workflows.md | 17223 | https://craft.wiki/apps/photocraft/workflows/ |
| …/troubleshooting.md | 8280 | https://craft.wiki/apps/photocraft/troubleshooting/ |
| …/file-formats.md | 3581 | https://craft.wiki/apps/photocraft/file-formats/ |
| …/automation.md | 4529 | https://craft.wiki/apps/photocraft/automation/ |

Официальный путь *править английский текст* есть (PR или CMS). Пути для русского перевода нет.

### Что не брать за «руководство» PhotoCraft без отдельного решения

- `docs/localization.md` и `docs/localization-ru.md` (4358 байт) — заметки о переводе *интерфейса* и терминов, не user guide. **[проверено по роли файлов в плане и именам]**
- Большие внутренние docs (`docs/architecture.md`, `docs/development.md`, parity/performance, integration-testing) — для разработчиков, в этап «документы для людей» плана не входили как старт.
- Man-страниц в `packaging/linux` у проверенных программ план уже не нашёл. **[из файла: план §4.4]**

---

## Открытые вопросы, которые можно решить только письмом авторам

Письма, issue и PR в этой работе **не отправлялись**. Ниже — только список вопросов, когда правообладатель даст прямое «да» на конкретную отправку.

**Storytold**

1. Принимают ли перевод README программ, где его ещё нет, в формате `README.ru.md` и переключателе в шапке — как уже сделано в craft-anything и lightcraft?
2. Как класть перевод книги PhotoCraft (`book/`, сейчас `multilingual = false`): второй src, mdBook multilingual, `book/ru/`, или книгу не переводят?
3. Когда заработает `https://getartcraft.com/docs/photocraft` и есть ли в этом конвейере место для языка (префикс, отдельные файлы)? Стоит ли пока переводить `docs/user/`?
4. Как переводить craft.wiki: Starlight locales, параллельные файлы, отдельный раздел, или wiki остаётся только английской? Кто ревьюит перевод (сопровождающие, Senior Contributor, носитель)?
5. Нужно ли встраивать переведённую справку в F1 у программ вроде AniCraft (`docs/guide/`), или достаточно внешней wiki/сайта?
6. Weblate: есть ли уже публичный адрес и касается ли он когда-нибудь документов, или только TSV?
7. Нужен ли отдельный CLA для текстовых вкладов, или достаточно «same licence as the repo» и чистой комнаты? Нужно ли помечать ИИ и проверку носителем, как в ATTRIBUTION.md каталогов?
8. Репозиторий artcraft-services / тексты сайта: принимают ли внешние переводы и под какой лицензией?

**Tangency Labs**

1. Принимают ли перевод user guide SolidCraft и куда его класть (`docs/book`, отдельный язык в mdBook, craft.wiki, docs.solidcraft.io/ru)?
2. Вопрос из issue #7811 про *documentation* (не только UI) — какое решение?
3. Нужны ли переводы fieldcraft book и сайта solidcraft.io / tangency-labs/website?

---

## Источники

Локальные (прочитаны в начале работы):

- `plan-ru-localization.md` (особенно §§4.5–4.6, 8)
- `findings-20261120-ru.md`
- `` — на момент чтения каталоги `docs/` и `glossary/` были пусты; рядом лежал клон `craft-i18n`

Публичные (чтение, 20.11.2026 PT):

- GitHub org:storytold (69 репо) и org:tangency-labs (17 репо); raw и Contents/Trees API; code search; issues #7811 и комментарии
- Локальный клон storytold/craft-i18n (README, ROADMAP, ADR 0006, ветки weblate и docs/translation-platform)
- https://getartcraft.com/support , https://getartcraft.com/docs/photocraft (404), https://craft.wiki/apps/photocraft/getting-started/ , https://docs.solidcraft.io/ , https://solidcraft.io/
