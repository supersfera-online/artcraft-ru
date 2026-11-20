# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# filmcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/filmcraft [проверено: git clone --depth 1]
- Коммит источника (main): `960a661001767a887dc4402c51e24f0436176705` от 2026-11-20 06:05 PT [проверено: git log]
- Локальный клон: `packaging/src/filmcraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 4 files changed, 19 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `apps/filmcraft/src/dev_icon.rs`
- `packaging/linux/ai.storyteller.filmcraft.desktop`
- `packaging/linux/ai.storyteller.filmcraft.metainfo.xml.in`
- `packaging/linux/ai.storyteller.filmcraft.mime.xml`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 9 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate ai.storyteller.filmcraft.desktop rc=0 OK
    appstreamcli ai.storyteller.filmcraft.metainfo.xml.in rc=0 I: ai.storyteller.filmcraft:15: description-first-para-too-short 
    xmlparse ai.storyteller.filmcraft.metainfo.xml.in OK
    xmlparse ai.storyteller.filmcraft.mime.xml OK
    mime-structure ai.storyteller.filmcraft.mime.xml types=1 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-filmcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/flatpak/ai.storyteller.filmcraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.filmcraft.yml`
- `packaging/linux/install.sh`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: есть ru
- `packaging/windows/filmcraft.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- Кроме упаковки правлен `apps/filmcraft/src/dev_icon.rs`: тест `desktop_file_matches_the_packaged_fields` сравнивает упакованный .desktop построчно с генерируемым кодом; без правки тест упал бы. Добавлены те же 4 строки [ru]. Проверено отдельной сборкой rustc этих двух функций и теста → PASS [проверено: /tmp/fc_test.rs]; полный `cargo test` не запускался [не проверено].
- Timeline здесь = «таймлайн» (так в живом ru.tsv FilmCraft) [из файла].
- В исходном тексте description = summary без точки — перевод зеркалит; appstreamcli даёт I: description-first-para-too-short и на main [проверено].

## Патч
`filmcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/filmcraft.patch`.
Команда: `git -C packaging/src/filmcraft diff main..l10n-ru-packaging --stat`
