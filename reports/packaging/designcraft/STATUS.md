# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# designcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/designcraft [проверено: git clone --depth 1]
- Коммит источника (main): `4000591c6681d01386b9576f9a050b8460e6f2e3` от 2026-11-20 09:52 PT [проверено: git log]
- Локальный клон: `packaging/src/designcraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 3 files changed, 16 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.designcraft.desktop`
- `packaging/linux/ai.storyteller.designcraft.metainfo.xml.in`
- `packaging/linux/ai.storyteller.designcraft.mime.xml`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 9 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate ai.storyteller.designcraft.desktop rc=0 OK
    appstreamcli ai.storyteller.designcraft.metainfo.xml.in rc=0 I: ai.storyteller.designcraft:15: description-first-para-too-short 
    xmlparse ai.storyteller.designcraft.metainfo.xml.in OK
    xmlparse ai.storyteller.designcraft.mime.xml OK
    mime-structure ai.storyteller.designcraft.mime.xml types=2 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-designcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/flatpak/ai.storyteller.designcraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.designcraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: есть ru
- `packaging/windows/designcraft.wxs`
- `packaging/windows/installer-ui.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- <keywords> в metainfo скопированы из PhotoCraft — ошибка исходника, перевод зеркалит [проверено: файл].
- I: description-first-para-too-short — есть и на main [проверено: appstreamcli].

## Патч
`designcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/designcraft.patch`.
Команда: `git -C packaging/src/designcraft diff main..l10n-ru-packaging --stat`
