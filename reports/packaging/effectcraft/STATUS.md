# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# effectcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/effectcraft [проверено: git clone --depth 1]
- Коммит источника (main): `c561e7352f6047d335db75a32cda45553ed34cf0` от 2026-11-20 08:54 PT [проверено: git log]
- Локальный клон: `packaging/src/effectcraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 2 files changed, 16 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.effectcraft.desktop`
- `packaging/linux/ai.storyteller.effectcraft.metainfo.xml.in`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 7 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate ai.storyteller.effectcraft.desktop rc=0 /tmp/l10nval.dI0O/ai.storyteller.effectcraft.desktop: hint: value "AudioVideo;Video;Graphics;2DGraphics;" for key "Categories" in group "Desktop Entry" contains more than one main category; application might appear more than once in the application menu
    appstreamcli ai.storyteller.effectcraft.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.effectcraft.metainfo.xml.in OK
    xmlparse ai.storyteller.effectcraft.mime.xml OK
    mime-structure ai.storyteller.effectcraft.mime.xml types=0 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-effectcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/flatpak/ai.storyteller.effectcraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.effectcraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: есть ru
- `packaging/windows/effectcraft.wxs`
- `packaging/windows/installer-ui.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- mime XML нет [проверено].
- <keywords> в metainfo скопированы из PhotoCraft — ошибка исходника, перевод зеркалит [проверено].
- `apps/effectcraft/src/appimage.rs` пишет свой .desktop для AppImage (Name/Comment по-английски) — [ru] туда не попадёт [проверено: grep].
- В Info.plist.in CFBundleLocalizations уже есть `ru`, хотя русского UI-каталога нет (по плану) [проверено: файл; план — из файла].

## Патч
`effectcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/effectcraft.patch`.
Команда: `git -C packaging/src/effectcraft diff main..l10n-ru-packaging --stat`
