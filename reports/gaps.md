# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# Пробелы ru в craft-i18n — цифры «до»

Дата замера: 2026-11-20 10:30 PST (America/Los_Angeles).  
Репозиторий: `craft-i18n/`  
HEAD: `b5b2805795f3d98b8fef4484db75db0cefbdc630` (2026-11-20 06:03:54 America/Los_Angeles). **[проверено: git log]**

**Важно:** каталога `locales/en/` в репозитории нет. Английский — колонка-ключ в каждом TSV. Эталон «всего» ниже — объединение ключей `(context, source)` по всем `locales/*/«файл».tsv`, как в `tools/new_locale.py`. Рядом — максимум по одной локали, как в штатном `coverage_report`. **[проверено: docs/catalog-format.md, new_locale.py, замер]**

«Не переведено» = ключ есть в эталоне-объединении, но его нет в `locales/ru/«файл».tsv` (или самого ru-файла нет).  
«Лишних» = ключ есть в ru и ни в одной другой локали (везде 0).  
«Сломанных плейсхолдеров» = расхождение `{name}` или хвостового `…` между en и ru (правила CI). Для отсутствующих файлов — н/д.

| Файл | Эталон (объед. = «всего») | Макс. одна локаль | В ru | Не переведено (нет в ru-файле) | Лишних | Сломанных плейсхолдеров (CI) |
|---|---:|---:|---:|---:|---:|---:|
| common | 1291 | 1291 (lv) | 1287 | 4 | 0 | 0 |
| photocraft | 4841 | 4682 (ka) | 3843 | 998 | 0 | 0 |
| pdfcraft | 4984 | 4559 (fr) | 4053 | 931 | 0 | 0 |
| wordcraft | 3216 | 3160 (ka) | 2590 | 626 | 0 | 0 |
| anicraft | 1697 | 1697 (pt-br) | 0 (файла нет) | 1697 | 0 | н/д |
| texturecraft | 997 | 962 (ar) | 0 (файла нет) | 997 | 0 | н/д |
| deckcraft | 1084 | 1084 (de) | 0 (файла нет) | 1084 | 0 | н/д |

Дополнительно (не колонки CI, но важно для работы):

| Файл | Уже покрыто ru/common при lookup | Реально без перевода на экране | Совпадают с en | Несовпадение `\n` (CI не ловит) |
|---|---:|---:|---:|---:|
| common | — | 4 | 25 | 0 |
| photocraft | 794 | 204 | 81 | 0 |
| pdfcraft | 361 | 570 | 62 | 0 |
| wordcraft | 415 | 211 | 17 | 4 (см. отчёт) |
| anicraft | 0 | 1697 | — | — |
| texturecraft | 110 | 887 | — | — |
| deckcraft | 5 | 1079 | — | — |

Подробности, правила формата, вывод штатных проверок и выписки из плана cutover/пинов: `craft-i18n-report-20261120.md`.  
Списки ключей «не переведено» (объединение, формат `context<TAB>en<TAB>`): `craft-i18n-missing/<программа>.tsv`.

Пустых переводов в существующих ru-файлах нет. **[проверено]**



## Цифры «после» (на 2026-11-20 11:38 PST (America/Los_Angeles))

Локальная ветка `ru-catalog-20261120` (без push). Исходный HEAD клона: `b5b2805795f3d98b8fef4484db75db0cefbdc630`. Штатная проверка `cargo test -p craft-i18n-tests --test locales --locked --offline`: **17 passed** после каждого коммита каталога, после шапки авторства и в конце. `python3 -m unittest discover -s tools -v`: **41 passed** после шапки. `cargo test -p craft-i18n-tests --test language_data --locked --offline`: **5 passed** после правки ATTRIBUTION.md и после шапки. **[проверено: cargo / unittest]**

«Lookup-дыры» = ключи эталона-объединения, которых нет ни в `locales/ru/«файл».tsv`, ни в `locales/ru/common.tsv`. Остаток «нет в ru-файле» при нулевых lookup-дырах уже покрыт common (CI запрещает идентичный override).

| Файл | Эталон (объед.) | ru до | ru после (файл) | Нет в ru-файле после | Lookup-дыры после | coverage_report (ru / largest) | Коммит каталога |
|---|---:|---:|---:|---:|---:|---|---|
| common | 1291 | 1287 | **1291** | 0 | **0** | **1291/1291** (lv) | `16fa24561c3a100c4b3221b6153a391dd15f75d9` `ru: common catalog` |
| photocraft | 4841 | 3843 | **4045** | 796 (все уже в ru/common) | **0** | 4045/4682 (ka) | `d492ac556aea87c2fb7223414adb14461fe6029f` `ru: photocraft catalog` |
| pdfcraft | 4984 | 4053 | **4622** | 362 (все уже в ru/common) | **0** | **4622/4622** (ru стала крупнейшей) | `2b7a1108aa71a8f6d9c6ff41478afa06cb5b6ef7` `ru: pdfcraft catalog` |
| wordcraft | 3216 | 2590 | **2800** | 416 (все уже в ru/common) | **0** | 2800/3160 (ka) | `1959f9b294c265ab8a628e95ff04ca372a0dde58` `ru: wordcraft catalog` |
| anicraft | 1697 | 0 | **1697** | 0 | **0** | **1697/1697** (pt-br) | `7019a436fe9dd596b4dae1f6a55e86e9c49526db` `ru: anicraft catalog` |
| texturecraft | 997 | 0 | **887** | 110 (все уже в ru/common) | **0** | 887/962 (ar) | `3ba8a6561a99e014fd5fd21bb5d44a712054a62f` `ru: texturecraft catalog` |
| deckcraft | 1084 | 0 | **1079** | 5 (уже в ru/common: Center, Clear All, Crop, Duration, Outline) | **0** | 1079/1084 (de) | `6d2a44f884d059a603e613eaa6d73be494058c3b` `ru: deckcraft catalog` |

Прочие коммиты ветки (историю старых не переписывали):

- `2071961823051770d2522646a8fdd2c3a2018ca4` `ru: record AI assistance in ATTRIBUTION.md` — отметка ИИ перенесена со строки `bg` на `ru` (тогда ещё без AniCraft/TextureCraft/DeckCraft).
- `a6d31fca4aab2a71462620dca0f37b66645543da` `ru: fix review findings (pdfcraft, wordcraft)`.
- `2a019387b4564e323ff7d7514761fd4b09a0a69d` `ru: yo and style pass`.
- `f60c0e461ab877391d8480bd5d330fdebbd0b4db` `ru: update ATTRIBUTION.md credit` — автор и коммитер `supersfera`; в нашей части строки `ru` убрано «SuperSfera LLC», кредит SuperSfera LLC, охват всех семи каталогов; чужие записи строки не менялись.
- `b7d41ae402c4e3f745dea80e439a8aaf4ae780e3` `ru: translation copyright header` — автор и коммитер `supersfera`; вторая строка семи наших ru-файлов.

Текущий HEAD ветки: `b7d41ae402c4e3f745dea80e439a8aaf4ae780e3`. Рабочее дерево чистое. Наружу ничего не отправлялось.

Оставшееся вне этой ветки: проверка носителем ещё нужна; ru-файлы других авторов (cadcraft, craft-launcher, filmcraft, vectorcraft) не трогались — ждём решения правообладателя; push/PR/fork не делались; авторство ранних коммитов (`SuperSfera LLC`) не переписывалось.
