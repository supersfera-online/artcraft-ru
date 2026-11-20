# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# gridcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/gridcraft [проверено: git clone --depth 1]
- Коммит источника (main): `442a40ecb14e1aede497092820ea616a6ec08db6` от 2026-11-20 08:59 PT [проверено: git log]
- Локальный клон: `packaging/src/gridcraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 3 files changed, 26 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.gridcraft.desktop`
- `packaging/linux/ai.storyteller.gridcraft.metainfo.xml.in`
- `packaging/linux/ai.storyteller.gridcraft.mime.xml`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 14 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate ai.storyteller.gridcraft.desktop rc=0 OK
    appstreamcli ai.storyteller.gridcraft.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.gridcraft.metainfo.xml.in OK
    xmlparse ai.storyteller.gridcraft.mime.xml OK
    mime-structure ai.storyteller.gridcraft.mime.xml types=6 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-gridcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/flatpak/ai.storyteller.gridcraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.gridcraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: есть ru
- `packaging/windows/gridcraft.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- mime-комментарии для стандартных типов (xlsx, ods, csv…) переопределяют shared-mime-info — переведены, но системная база их тоже переводит [догадка].

## Патч
`gridcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/gridcraft.patch`.
Команда: `git -C packaging/src/gridcraft diff main..l10n-ru-packaging --stat`
