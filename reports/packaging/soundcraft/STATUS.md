# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# soundcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/soundcraft [проверено: git clone --depth 1]
- Коммит источника (main): `85623f28f99a9a788123f0f6b48829f95f07962f` от 2026-11-20 08:32 PT [проверено: git log]
- Локальный клон: `packaging/src/soundcraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 3 files changed, 22 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.soundcraft.desktop`
- `packaging/linux/ai.storyteller.soundcraft.metainfo.xml.in`
- `packaging/linux/ai.storyteller.soundcraft.mime.xml`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 14 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate ai.storyteller.soundcraft.desktop rc=0 OK
    appstreamcli ai.storyteller.soundcraft.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.soundcraft.metainfo.xml.in OK
    xmlparse ai.storyteller.soundcraft.mime.xml OK
    mime-structure ai.storyteller.soundcraft.mime.xml types=1 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-soundcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
генератор clap_mangen: `apps/soundcraft-cli/examples/man-and-completions.rs`; в пакетах Linux/FreeBSD. Объём: ~125 строк `///` в 12 файлах, ~8 `#[command(` [проверено: grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/flatpak/ai.storyteller.soundcraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.soundcraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: ключа нет
- `packaging/windows/soundcraft.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- Окна «Edit» и «Mix» названы «Правка» и «Микшер» [догадка]: русского каталога у SoundCraft нет, Edit в глоссарии спорный.

## Патч
`soundcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/soundcraft.patch`.
Команда: `git -C packaging/src/soundcraft diff main..l10n-ru-packaging --stat`
