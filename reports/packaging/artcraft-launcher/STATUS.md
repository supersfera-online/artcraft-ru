# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
# artcraft-launcher: русская упаковка — STATUS (20.11.2026)

Статус: **готово (черновик, локально)**. Ничего не отправлялось наружу.

- Репозиторий: https://github.com/storytold/craft-launcher [проверено: git clone --depth 1]
- Коммит источника (main): `bbb3844954d90e64c70a89ea493d0e7270478553` от 2026-11-20 03:08 PT [проверено: git log]
- Локальный клон: `packaging/src/craft-launcher/`, ветка `l10n-ru-packaging` (1 коммит(а), автор `отдел локализации <users.noreply.github.com>`, без remote-ветки) [проверено]
- Изменения: 2 files changed, 18 insertions(+) [проверено: git diff --shortstat]

## Файлы (итоговый вид в `files/`)
- `packaging/linux/ai.storyteller.artcraft-launcher.desktop`
- `packaging/linux/ai.storyteller.artcraft-launcher.metainfo.xml.in`

## Что добавлено
- .desktop: `Name[ru]` (= имя продукта, не переводится), `GenericName[ru]`, `Comment[ru]`, `Keywords[ru]` (с `;` в конце). Секций Actions в файле нет [проверено].
- metainfo: `xml:lang="ru"` для summary, каждого `<p>`/`<li>` в description, caption снимка, каждого `<keyword>`; `<name>` (продукт и разработчик) не переводились. Всего строк с xml:lang="ru" (вместе с mime): 9 [проверено].
- mime XML: `<comment xml:lang="ru">` к каждому `<comment>` (если файл есть).
- Авторы не используют itstool/gettext для metainfo (шаблон .in подставляет только @VERSION@/@DATE@ через sed) — встроенный xml:lang уместен [проверено: package.sh, git grep itstool/msgfmt].

## Валидация (ветка l10n-ru-packaging; @VERSION@/@DATE@ подставлены как в package.sh)
Инструменты: desktop-file-validate (системный), appstreamcli 1.0.5 `validate --no-net --pedantic` (распакован без sudo из .deb в tools-local), python xml.dom.minidom + lxml для mime. xmllint на box нет.
    desktop-file-validate ai.storyteller.artcraft-launcher.desktop rc=0 /tmp/l10nval.QDdl/ai.storyteller.artcraft-launcher.desktop: hint: value item "PackageManager" in key "Categories" in group "Desktop Entry" can be extended with another category among the following categories: Settings
    appstreamcli ai.storyteller.artcraft-launcher.metainfo.xml.in rc=0 
    xmlparse ai.storyteller.artcraft-launcher.metainfo.xml.in OK
Те же проверки на main дают тот же результат (лог `logs/validate-main-craft-launcher.log`). Валидация на appstream 0.15 (Ubuntu 22.04, как в CI авторов) — [не проверено].

## Man-страницы
нет: файлов *.1/*.5/*.8, каталогов man/ и clap_mangen/mangen в репозитории нет [проверено: git ls-files + git grep]. Перевод man в этот заход не делался.

## Установщик / лаунчер вне UI
- `packaging/freebsd/package.sh`
- `packaging/linux/AppRun`
- `packaging/linux/flatpak/ai.storyteller.artcraft-launcher.bundle.yml`
- `packaging/linux/flatpak/ai.storyteller.artcraft-launcher.yml`
- `packaging/linux/nfpm.yaml` — description пакета deb/rpm только по-английски
- `packaging/linux/postinst.sh` — echo/printf-сообщений нет
- `packaging/macos/Info.plist.in` — CFBundleLocalizations: ключа нет
- `packaging/windows/artcraft-launcher.en-us.wxl` — локализация WiX, только en-US
- `packaging/windows/artcraft-launcher.wxs`
Переводы сюда не вносились (в задании — только инвентарь) [проверено: git ls-files, grep].

## Пометки
- Пакет artcraft-launcher, репозиторий craft-launcher [из файла: план].
- mime XML нет [проверено].
- Лаунчер сам пишет .desktop для установленных программ (`crates/native/src/desktop_entry.rs`, Comment из tagline) и автозапуск (`login.rs`, Comment по-английски) — эти записи [ru] не получат; правка кода вне этого захода [проверено: grep].

## Патч
`craft-launcher.patch` (git format-patch main..l10n-ru-packaging), копия в `../patches/craft-launcher.patch`.
Команда: `git -C packaging/src/craft-launcher diff main..l10n-ru-packaging --stat`

## Авторство перевода (20.11.2026, дополнение)

Правила из `RULES-AUTHORSHIP.md` применены к уже сделанному черновику. История не переписывалась. [проверено]

- Ветка по-прежнему `l10n-ru-packaging`. Новый коммит на кончике: `f76ee5e supersfera-online <users.noreply.github.com>`.
- Во все наши переводные `.desktop` / metainfo / mime (где есть русский) добавлен комментарий `Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0`: в `.desktop` — первой строкой, до `[Desktop Entry]`; в XML — сразу после `<?xml ...?>`, авторский комментарий про AppStream оставлен следующим, без изменений. Лицензионные файлы авторов и JSON не трогались.
- `desktop-file-validate` и `appstreamcli validate --no-net --pedantic` снова прошли с rc=0 (те же подсказки авторов, что и раньше). [проверено]
- Патч и `files/` обновлены с кончика ветки. Наружу ничего не отправлялось.

Коммиты на ветке `main..HEAD` (старые имена авторов не переписывались):

```
f76ee5e supersfera-online <users.noreply.github.com> l10n(ru): add translation copyright comments
4bdb0b9 отдел локализации <users.noreply.github.com> packaging: черновой русский перевод .desktop, AppStream и mime (ru)
```
