# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# figcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/figcraft [проверено: git clone --depth 1]
- Коммит источника (main): `8320b6699e3f837c1f2af4c3166c4862526fb754` от 2026-11-20 10:02 PT [проверено: git log]
- Локальный клон: `packaging/src/figcraft/`, ветка `l10n-ru-packaging` (2 коммит(а), автор `отдел локализации <local@localhost>`, без remote-ветки) [проверено]
- Изменения: 3 files changed, 23 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.figcraft.desktop`
- `packaging/linux/ai.storyteller.figcraft.metainfo.xml.in`
- `packaging/linux/ai.storyteller.figcraft.mime.xml`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 14 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint в рабочей копии нет.
    desktop-file-validate ai.storyteller.figcraft.desktop rc=0 OK
    appstreamcli ai.storyteller.figcraft.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.figcraft.metainfo.xml.in OK
    xmlparse ai.storyteller.figcraft.mime.xml OK
    mime-structure ai.storyteller.figcraft.mime.xml types=2 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-figcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
генератор `apps/figcraft-cli/examples/man-and-completions.rs` (рекурсивные man-страницы, тест `tests/it/generated_docs.rs`, описан в `docs/cli.md`); в `packaging/linux/package.sh` man не устанавливается [проверено: grep man1/cli-docs — 0 совпадений]. Объём: ~156 строк `///` в 4 файлах, ~21 `#[command(` [проверено: grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/AppRun`
- `packaging/linux/flatpak/ai.storyteller.figcraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.figcraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: ключа нет
- `packaging/server/install.sh`
- `packaging/windows/figcraft.en-us.wxl` — локализация WiX, только en-US
- `packaging/windows/figcraft.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- Frame оставлен латиницей по глоссарию отдела («принят только для FigCraft») [из файла: glossary.tsv]; Auto layout = «Автолейаут», Inspect = «Инспектор» из ru.toml [из файла].

## Патч
`figcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/figcraft.patch`.
Команда: `git -C packaging/src/figcraft diff main..l10n-ru-packaging --stat`
