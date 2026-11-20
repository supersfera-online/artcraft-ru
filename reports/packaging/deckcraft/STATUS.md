# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# deckcraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/deckcraft [проверено: git clone --depth 1]
- Коммит источника (main): `b16257a8b20eadd68e9b512ff0a2398641f5e932` от 2026-11-20 09:52 PT [проверено: git log]
- Локальный клон: `packaging/src/deckcraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <users.noreply.github.com>`, без remote-ветки) [проверено]
- Изменения: 3 files changed, 20 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.deckcraft.desktop`
- `packaging/linux/ai.storyteller.deckcraft.metainfo.xml.in`
- `packaging/linux/ai.storyteller.deckcraft.mime.xml`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 9 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint на box нет.
    desktop-file-validate ai.storyteller.deckcraft.desktop rc=0 OK
    appstreamcli ai.storyteller.deckcraft.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.deckcraft.metainfo.xml.in OK
    xmlparse ai.storyteller.deckcraft.mime.xml OK
    mime-structure ai.storyteller.deckcraft.mime.xml types=1 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-deckcraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/flatpak/ai.storyteller.deckcraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.deckcraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: ключа нет
- `packaging/windows/deckcraft.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- Тест в `apps/deckcraft/src/main.rs` читает из .desktop только MimeType — правка не мешает [проверено: чтение кода].
- Diagram = «Схема» (принят, craft-i18n GLOSSARY) [проверено].

## Патч
`deckcraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/deckcraft.patch`.
Команда: `git -C packaging/src/deckcraft diff main..l10n-ru-packaging --stat`

## Авторство перевода (20.11.2026, дополнение)

Правила из `RULES-AUTHORSHIP.md` применены к уже сделанному черновику. История не переписывалась. [проверено]

- Ветка по-прежнему `l10n-ru-packaging`. Новый коммит на кончике: `280779e supersfera-online <users.noreply.github.com>`.
- Во все наши переводные `.desktop` / metainfo / mime (где есть русский) добавлен комментарий `Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0`: в `.desktop` — первой строкой, до `[Desktop Entry]`; в XML — сразу после `<?xml ...?>`, авторский комментарий про AppStream оставлен следующим, без изменений. Лицензионные файлы авторов и JSON не трогались.
- `desktop-file-validate` и `appstreamcli validate --no-net --pedantic` снова прошли с rc=0 (те же подсказки авторов, что и раньше). [проверено]
- Патч и `files/` обновлены с кончика ветки. Наружу ничего не отправлялось.

Коммиты на ветке `main..HEAD` (старые имена авторов не переписывались):

```
280779e supersfera-online <users.noreply.github.com> l10n(ru): add translation copyright comments
14a6ea9 отдел локализации <users.noreply.github.com> packaging: черновой русский перевод .desktop, AppStream и mime (ru)
```
