# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# photocraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/photocraft [проверено: git clone --depth 1]
- Коммит источника (main): `877d58844029967b80e36a964902d309de1be158` от 2026-11-20 10:17 PT [проверено: git log]
- Локальный клон: `packaging/src/photocraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 3 files changed, 23 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.photocraft.desktop`
- `packaging/linux/ai.storyteller.photocraft.metainfo.xml.in`
- `packaging/linux/ai.storyteller.photocraft.mime.xml`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 15 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate ai.storyteller.photocraft.desktop rc=0 OK
    appstreamcli ai.storyteller.photocraft.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.photocraft.metainfo.xml.in OK
    xmlparse ai.storyteller.photocraft.mime.xml OK
    mime-structure ai.storyteller.photocraft.mime.xml types=4 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-photocraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
генератор clap_mangen: `apps/photocraft-cli/examples/man-and-completions.rs` → `photocraft-cli.1` + по странице на подкоманду; кладётся в пакеты Linux и FreeBSD (`packaging/linux/package.sh`, `packaging/freebsd/package.sh`). Объём: ~204 строк `///` в 10 файлах `apps/photocraft-cli/src`, ~18 атрибутов `#[command(` [проверено: grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/AppRun`
- `packaging/linux/flatpak/ai.storyteller.photocraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.photocraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: есть ru
- `packaging/windows/photocraft.en-us.wxl` — локализация WiX, только en-US
- `packaging/windows/photocraft.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- —

## Патч
`photocraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/photocraft.patch`.
Команда: `git -C packaging/src/photocraft diff main..l10n-ru-packaging --stat`
