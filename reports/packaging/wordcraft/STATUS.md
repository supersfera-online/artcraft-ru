# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# wordcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/wordcraft [проверено: git clone --depth 1]
- Коммит источника (main): `f2e6234c5240737c84926e19d8c8a421ea010ca9` от 2026-11-20 09:00 PT [проверено: git log]
- Локальный клон: `packaging/src/wordcraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 2 files changed, 15 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.wordcraft.desktop`
- `packaging/linux/ai.storyteller.wordcraft.metainfo.xml.in`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 7 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate ai.storyteller.wordcraft.desktop rc=0 OK
    appstreamcli ai.storyteller.wordcraft.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.wordcraft.metainfo.xml.in OK
    xmlparse ai.storyteller.wordcraft.mime.xml OK
    mime-structure ai.storyteller.wordcraft.mime.xml types=0 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-wordcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/flatpak/ai.storyteller.wordcraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.wordcraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: ключа нет
- `packaging/windows/wordcraft.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- Ранее API на packaging/linux давал 403; `git clone --depth 1` прошёл без ошибок [проверено: clone 20.11.2026].
- mime XML в репозитории нет [проверено: git ls-files].

## Патч
`wordcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/wordcraft.patch`.
Команда: `git -C packaging/src/wordcraft diff main..l10n-ru-packaging --stat`
