# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# craft-anything: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/craft-anything [проверено: git clone --depth 1]
- Коммит источника (main): `827be601e781daea91ce2013fa0f64d658abd028` от 2026-11-20 05:42 PT [проверено: git log]
- Локальный клон: `packaging/src/craft-anything/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 2 files changed, 19 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.craft-anything.desktop`
- `packaging/linux/ai.storyteller.craft-anything.metainfo.xml.in`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 10 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate ai.storyteller.craft-anything.desktop rc=0 OK
    appstreamcli ai.storyteller.craft-anything.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.craft-anything.metainfo.xml.in OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-craft-anything.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/AppRun`
- `packaging/linux/flatpak/ai.storyteller.craft-anything.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.craft-anything.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: ключа нет
- `packaging/windows/craft-anything.en-us.wxl` — локализация WiX, только en-US
- `packaging/windows/craft-anything.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- mime XML нет [проверено].
- GenericName «Исследование программ» (Software Explorer) [догадка].

## Патч
`craft-anything.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/craft-anything.patch`.
Команда: `git -C packaging/src/craft-anything diff main..l10n-ru-packaging --stat`
