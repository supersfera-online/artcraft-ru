# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# texturecraft: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/texturecraft [проверено: git clone --depth 1]
- Коммит источника (main): `9be964a00eb4781dd40909a39322e5807d752359` от 2026-11-20 10:19 PT [проверено: git log]
- Локальный клон: `packaging/src/texturecraft/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <users.noreply.github.com>`, без remote-ветки) [проверено]
- Изменения: 3 files changed, 31 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.texturecraft.desktop`
- `packaging/linux/ai.storyteller.texturecraft.metainfo.xml.in`
- `packaging/linux/ai.storyteller.texturecraft.mime.xml`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 22 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint на box нет.
    desktop-file-validate ai.storyteller.texturecraft.desktop rc=0 OK
    appstreamcli ai.storyteller.texturecraft.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.texturecraft.metainfo.xml.in OK
    xmlparse ai.storyteller.texturecraft.mime.xml OK
    mime-structure ai.storyteller.texturecraft.mime.xml types=12 OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-texturecraft.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/AppRun`
- `packaging/linux/flatpak/ai.storyteller.TextureCraft.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.TextureCraft.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: ключа нет
- `packaging/windows/texturecraft.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- Mesh → «сетка», но в глоссарии Grid → «Сетка» (предложен) — коллизия для терминолога [из файла].

## Патч
`texturecraft.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/texturecraft.patch`.
Команда: `git -C packaging/src/texturecraft diff main..l10n-ru-packaging --stat`

## Авторство перевода (20.11.2026, дополнение)

Правила из `RULES-AUTHORSHIP.md` применены к уже сделанному черновику. История не переписывалась. [проверено]

- Ветка по-прежнему `l10n-ru-packaging`. Новый коммит на кончике: `5e4b3c0 supersfera <223132313+supersfera-online@users.noreply.github.com>`.
- Во все наши переводные `.desktop` / metainfo / mime (где есть русский) добавлен комментарий `Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0`: в `.desktop` — первой строкой, до `[Desktop Entry]`; в XML — сразу после `<?xml ...?>`, авторский комментарий про AppStream оставлен следующим, без изменений. Лицензионные файлы авторов и JSON не трогались.
- `desktop-file-validate` и `appstreamcli validate --no-net --pedantic` снова прошли с rc=0 (те же подсказки авторов, что и раньше). [проверено]
- Патч и `files/` обновлены с кончика ветки. Наружу ничего не отправлялось.

Коммиты на ветке `main..HEAD` (старые имена авторов не переписывались):

```
5e4b3c0 supersfera <223132313+supersfera-online@users.noreply.github.com> l10n(ru): add translation copyright comments
a0d3291 отдел локализации <users.noreply.github.com> packaging: черновой русский перевод .desktop, AppStream и mime (ru)
```
