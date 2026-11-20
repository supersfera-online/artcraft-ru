# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# pdfcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/pdfcraft [проверено: git clone --depth 1]
- Коммит источника (main): `df18640982f6ff918ff6a5507d1267b6c78d105b` от 2026-11-20 09:22 PT [проверено: git log]
- Локальный клон: `packaging/src/pdfcraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <users.noreply.github.com>`, без remote-ветки) [проверено]
- Изменения: 2 files changed, 15 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.pdfcraft.desktop`
- `packaging/linux/ai.storyteller.pdfcraft.metainfo.xml.in`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 7 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint на box нет.
    desktop-file-validate ai.storyteller.pdfcraft.desktop rc=0 OK
    appstreamcli ai.storyteller.pdfcraft.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.pdfcraft.metainfo.xml.in OK
    xmlparse ai.storyteller.pdfcraft.mime.xml OK
    mime-structure ai.storyteller.pdfcraft.mime.xml types=0 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-pdfcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/flatpak/ai.storyteller.pdfcraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.pdfcraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: есть ru
- `packaging/windows/installer-ui.wxs`
- `packaging/windows/pdfcraft.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- mime XML в репозитории нет — переводить нечего [проверено: git ls-files].
- «redact» переведено описательно («скрывайте … конфиденциальные фрагменты»); в pdfcraft.tsv Redact = «Скрыть» [из файла] — терминологу.

## Патч
`pdfcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/pdfcraft.patch`.
Команда: `git -C packaging/src/pdfcraft diff main..l10n-ru-packaging --stat`

## Авторство перевода (20.11.2026, дополнение)

Правила из `RULES-AUTHORSHIP.md` применены к уже сделанному черновику. История не переписывалась. [проверено]

- Ветка по-прежнему `l10n-ru-packaging`. Новый коммит на кончике: `0029ee4 supersfera <223132313+supersfera-online@users.noreply.github.com>`.
- Во все наши переводные `.desktop` / metainfo / mime (где есть русский) добавлен комментарий `Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0`: в `.desktop` — первой строкой, до `[Desktop Entry]`; в XML — сразу после `<?xml ...?>`, авторский комментарий про AppStream оставлен следующим, без изменений. Лицензионные файлы авторов и JSON не трогались.
- `desktop-file-validate` и `appstreamcli validate --no-net --pedantic` снова прошли с rc=0 (те же подсказки авторов, что и раньше). [проверено]
- Патч и `files/` обновлены с кончика ветки. Наружу ничего не отправлялось.

Коммиты на ветке `main..HEAD` (старые имена авторов не переписывались):

```
0029ee4 supersfera <223132313+supersfera-online@users.noreply.github.com> l10n(ru): add translation copyright comments
c45cae5 отдел локализации <users.noreply.github.com> packaging: черновой русский перевод .desktop, AppStream и mime (ru)
```
