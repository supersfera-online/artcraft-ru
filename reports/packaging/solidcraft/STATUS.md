# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# solidcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/tangency-labs/solidcraft [проверено: git clone --depth 1]
- Коммит источника (main): `0301073f3e45d19618ccd9bb986418184282245a` от 2026-11-20 09:49 PT [проверено: git log]
- Локальный клон: `packaging/src/solidcraft/`, ветка `l10n-ru-packaging` (2 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 3 files changed, 20 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `assets/platforms/linux/io.tangencylabs.solidcraft.desktop`
- `assets/platforms/linux/io.tangencylabs.solidcraft.metainfo.xml.in`
- `assets/platforms/linux/io.tangencylabs.solidcraft.mime.xml`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 12 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate io.tangencylabs.solidcraft.desktop rc=0 OK
    appstreamcli io.tangencylabs.solidcraft.metainfo.xml.in rc=0 
    xmlparse io.tangencylabs.solidcraft.metainfo.xml.in OK
    xmlparse io.tangencylabs.solidcraft.mime.xml OK
    mime-structure io.tangencylabs.solidcraft.mime.xml types=1 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-solidcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `assets/platforms/macos/Info.plist.in` — CFBundleLocalizations: ключа нет
- `assets/platforms/windows/solidcraft.en-us.wxl` — локализация WiX, только en-US
- `assets/platforms/windows/solidcraft.wxs`
- `packaging/freebsd/package.sh`
- `packaging/linux/AppRun`
- `packaging/linux/flatpak/io.tangencylabs.solidcraft.bundle.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/linux/snap/snapcraft.yaml`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- Ранее API packaging/linux давал 403; клон прошёл. Файлы упаковки лежат не в packaging/linux, а в `assets/platforms/linux/` [проверено].
- CI (`.github/workflows/packaging-lint.yml`) прогоняет desktop-file-validate и appstreamcli validate --no-net [проверено: файл].
- design → «Дизайн» (глоссарий: спорный, выбран самый частый вариант) — mime «Дизайн SolidCraft» [из файла].
- Pattern в CAD-смысле → «массивы» (как в ru.json SolidCraft «Массив»), а в глоссарии Pattern = «Узор» (смысл PhotoCraft) — нужен отдельный смысл [из файла].

## Патч
`solidcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/solidcraft.patch`.
Команда: `git -C packaging/src/solidcraft diff main..l10n-ru-packaging --stat`
