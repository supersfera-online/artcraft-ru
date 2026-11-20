#!/usr/bin/env python3
# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
"""Пишет review/screenshot-checklists/<программа>.md (19 программ) по фактам из клонов в рабочей копии.

Ручные сведения (как включить русский, что не переводится) — в таблице PROGRAMS ниже, у каждого
источник; автоматические (ярлык .desktop, длинные строки, слова с «ё», термины глоссария) берутся
из файлов и последних отчётов review/reports. Перезапуск перезаписывает только эти чеклисты.
"""
from __future__ import annotations

import collections
import csv
import datetime as _dt
import glob
import os
import re

L10N = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(L10N, "review", "screenshot-checklists")
PKG = os.path.join(L10N, "packaging", "src")
REPORTS = os.path.join(L10N, "review", "reports")
GLOSSARY = os.path.join(L10N, "glossary", "glossary.tsv")

V, G, N = "проверено", "догадка", "не проверено"
# name: (Название, как включить язык, статус+источник, ru в коде?, где каталог, панели для снимка, что не переводится + источник, примечания)
PROGRAMS = {
 "anicraft": ("AniCraft", "Preferences › Appearance › Language (или запуск с `--lang ru`)", f"{V}: docs/localisation.md:22",
   f"ru в списке READY в коде; каталога ru в репозитории программы нет, черновик `craft-i18n/locales/ru/anicraft.tsv` есть только локально (не в сборке) — {V}: клон craft-i18n, git status",
   "craft-i18n `locales/ru/anicraft.tsv` (вшивается при сборке через `CRAFT_I18N_DIR`)",
   ["Шкала времени (Timeline)", "Слои", "Библиотека символов"],
   f"документы пользователя (имена слоёв, символов, сцен), ID команд и параметры, формат `.anicraft`, `anicraft-cli`, `serve`, MCP, журнал, `--help`; пока не переводятся сообщения движка (тело ошибок и отчётов импорта; заголовки и кнопки переводятся) — {V}: docs/localisation.md:12-17",
   "Установленная версия, скорее всего, русского ещё не покажет: русского каталога в выпуске нет (догадка по состоянию репозиториев)."),
 "cadcraft": ("CADCraft", "Edit → Interface Language", f"{V}: docs/localization.md:3", f"ru зарегистрирован — {V}: код ui-egui",
   "репозиторий программы `crates/ui-egui/src/i18n/ru.tsv`; копия в craft-i18n `locales/ru/cadcraft.tsv`",
   ["Командная строка", "Свойства", "Слои"],
   f"ответы CLI/MCP и история команд, ключевые слова подсказок, SPDX; сообщения движка и строки вне каталога — по-английски — {V}: docs/localization-parity.md:30,73,100", ""),
 "craft-anything": ("Craft Anything", "Settings → General → Language", f"{V}: docs/STATUS.md:330", f"ru зарегистрирован — {V}: код ui-egui",
   "репозиторий программы, TSV из двух колонок `ru.tsv`",
   ["Боковая панель проекта", "Окно анализа"],
   f"названия режимов **Clean room** и **Deep**, имена инструментов и движков (Ghidra, Unity, Unreal…) — {V}: docs/localization.md:127", ""),
 "craft-launcher": ("ArtCraft Launcher", "Settings → Language", f"{V}: README.md:98", f"ru зарегистрирован — {V}: код ui-egui",
   "репозиторий программы `ru.tsv`; копия в craft-i18n `locales/ru/craft-launcher.tsv`",
   ["Список приложений", "Страница обновлений"],
   f"названия продуктов (ArtCraft Launcher, Craft App Suite, PhotoCraft…); где нет шрифта и в веб-версии интерфейс остаётся английским — {V}: docs/development.md:41, README.md:116", ""),
 "deckcraft": ("DeckCraft", "переключателя языка нет — интерфейс только на английском", f"{V}: docs/localization-parity.md:5",
   f"ru не зарегистрирован — {V}; в craft-i18n лежит `deckcraft.tsv` у других языков, ru — только локальный черновик в рабочей копии",
   "пока нет (craft-i18n `locales/ru/deckcraft.tsv` — черновик, программа его не читает)",
   ["Панель слайдов", "Инспектор"],
   f"всё (английский интерфейс) — {V}: docs/localization-parity.md:5",
   "Снимки нужны только как исходное состояние: подтвердить, что русского выбора нет. Остальные пункты пометить «нет русского»."),
 "designcraft": ("DesignCraft", "Preferences ▸ General ▸ Interface Language", f"{V}: docs/target-app-parity.md:391", f"ru зарегистрирован — {V}: код ui-egui",
   "репозиторий программы `crates/ui-egui/src/i18n/ru.rs` (таблица Rust)",
   ["Страницы", "Абзацные стили", "Свойства"],
   f"непереведённое показывается по-английски — {V}: docs/localization-parity.md:15,22; отдельного списка «не переводить» не найдено ({N})", ""),
 "effectcraft": ("EffectCraft", "Settings ▸ General ▸ Language", f"{V}: docs/preferences.md:33",
   f"ru в CATALOG_CODES, меню-каталог `RUSSIAN` в `crates/ui-egui/src/i18n.rs` (~630 строк) — {V}: код; панели ru нет",
   "репозиторий программы `crates/ui-egui/src/i18n.rs` (таблица RUSSIAN)",
   ["Таймлайн", "Эффекты и шаблоны", "Элементы управления эффектом"],
   f"нигде пока не переведены: имена параметров эффектов (~1650), текст движка (свойства, ошибки, отмена), часть домашнего экрана, уроки и справка — {V}: docs/localization-parity.md:52-54",
   "Ожидаемо: меню по-русски, панели по-английски (у ru есть только меню-каталог) — догадка по коду."),
 "figcraft": ("FigCraft", "Preferences ▸ Language", f"{V}: docs/localization-parity.md:33", f"ru зарегистрирован — {V}: код ui-egui",
   "репозиторий программы `crates/ui-egui/locales/ru.toml`",
   ["Слои", "Дизайн (инспектор)", "Прототип"],
   f"ID команд, CLI, MCP, канал управления; сообщения движка и значения Dev Mode; **Frame** и **Smart animate** остаются латиницей — {V}: docs/localization-parity.md:28-32, docs/gaps.md:228, глоссарий (принят только для FigCraft)", ""),
 "filmcraft": ("FilmCraft", "Edit ▸ Language (также Settings ▸ General)", f"{V}: docs/localization-parity.md:11", f"ru зарегистрирован — {V}: код ui-egui",
   "репозиторий программы `ru.tsv` (живой каталог); копия в craft-i18n `locales/ru/filmcraft.tsv`",
   ["Таймлайн", "Инспектор", "Цвет", "Микшер"],
   f"канал управления, CLI и MCP — {V}: docs/localization-parity.md:23", ""),
 "gridcraft": ("GridCraft", "View → Interface language", f"{V}: README.md:119", f"ru зарегистрирован — {V}: код ui-egui",
   "репозиторий программы `crates/ui-egui/src/i18n/ru.rs`",
   ["Строка формул", "Мастер функций", "Сводная таблица"],
   f"сообщения незнакомой формы (RaTeX, химия) — по-английски — {V}: docs/localization-parity.md:22,149,154; имена функций формул — {N}", ""),
 "lightcraft": ("LightCraft", "Настройки → Общие → Язык → Русский (или переменная `LIGHTCRAFT_LANGUAGE=ru`)", f"{V}: docs/localization-ru.md:3", f"ru зарегистрирован — {V}: код ui-egui",
   "репозиторий программы `crates/ui-egui/locales/ru.json` и `ru-formats.json`",
   ["Библиотека", "Обработка (Develop)", "Метаданные"],
   f"технические ошибки нижних уровней, строки вне каталога; ID команд, имена файлов, метаданные пользователя — {V}: docs/localization-ru.md:8-9, docs/localization.md:60",
   "Окончания множественного числа через приём `{:.0}` — проверить фразы с числами (1, 2, 5, 21 фото)."),
 "materialcraft": ("MaterialCraft", "живой выбор языка в Preferences", f"{V}: docs/localization-parity.md", f"в выпущенном коде ru нет, есть только ar — {V}: клон packaging/src/materialcraft-r2 (`ar.rs`); локальный черновик в рабочей копии (apps/materialcraft, не закоммичен, 20.11.2026 ~11:08 PST) добавляет `crates/ui-egui/src/i18n/ru.rs` (711 строк) и правит i18n.rs — {V}: git status",
   "пока нет", ["Граф узлов", "Библиотека", "Свойства узла"],
   f"не найдено в docs ({N})", "Снимки — исходное состояние: подтвердить, что русского в списке нет."),
 "pdfcraft": ("PdfCraft", "Меню › Edit › Preferences… › Interface language; «Auto» следует LC_ALL / LC_MESSAGES / LANG", f"{V}: docs/localization.md:3,7", f"ru зарегистрирован — {V}: код ui-egui",
   "craft-i18n `locales/ru/pdfcraft.tsv`",
   ["Миниатюры страниц", "Комментарии", "Формы"],
   f"детали ошибок движка и ОС внутри переведённого окна; справки нет — {V}: docs/localization.md:25,53",
   "Найдено скриптом в каталоге: строка «Переместить вdownarrow» (Move down) — проверить на снимке меню страниц."),
 "photocraft": ("PhotoCraft", "Edit › Preferences › Interface › Language", f"{V}: docs/localization-ka.md, docs/localization-zh-hans.md (тот же путь для всех языков)", f"ru зарегистрирован — {V}: код ui-egui",
   "craft-i18n `locales/ru/photocraft.tsv` + `common.tsv`",
   ["Слои", "Инструменты", "Коррекция", "Camera Raw"],
   f"ошибки движка и часть статусных сообщений; ID команд; названия технологий (Camera Raw, OpenType, sRGB, Wayland) — {V}: docs/localization-ru.md:60, docs/localization-es.md:73",
   "Термины PhotoCraft (Света, Полутона, Тени, Растушёвка, Монтажная область) — принятые в глоссарии."),
 "solidcraft": ("SolidCraft", "Preferences… › General › Interface language (по умолчанию «system»)", f"{V}: crates/ui-egui/src/prefs/general.rs:12, assets/locales/en.json (`Preferences…`, `prefs.general`, `prefs.interface_language`), docs/localization.md:8", f"ru зарегистрирован — {V}: docs/localization.md:4",
   "репозиторий программы `assets/locales/ru.json` (+ `crates/ui-text/locales/ru.json`)",
   ["Дерево построения", "Эскиз", "Свойства элемента"],
   f"ID команд, горячие клавиши, форматы файлов, единицы, имена пользователя; устоявшиеся Loft, Sweep, Spline, Offset — {V}: docs/localization.md:97-100",
   f"Ярлык `.desktop` у SolidCraft без [ru] — {V}: assets/platforms/linux/io.tangencylabs.solidcraft.desktop."),
 "soundcraft": ("SoundCraft", "Appearance ▸ Language (или команда `ui.language`)", f"{V}: docs/localization-parity.md:47-49", f"в выпущенном коде ru нет, есть только pt-BR — {V}: клон packaging/src/soundcraft; локальный черновик в рабочей копии (apps/soundcraft, не закоммичен, 20.11.2026 11:05 PST) добавляет `crates/ui-egui/locales/ru/mod.rs` и правит localization.rs, menus.rs — {V}: git status",
   "пока нет", ["Микшер", "Аранжировка", "Браузер"],
   f"не найдено в docs ({N})", "Снимки — исходное состояние: подтвердить, что русского в списке нет."),
 "texturecraft": ("TextureCraft", "Edit ▸ Settings ▸ Language (переключается сразу)", f"{V}: docs/localization-parity.md:10", f"ru не зарегистрирован — {V}; ru-каталог в craft-i18n только локальный черновик в рабочей копии",
   "пока нет (craft-i18n `locales/ru/texturecraft.tsv` — черновик)", ["Слои", "Свойства кисти", "Наборы текстур"],
   f"имена ассетов библиотеки (материалы, смарт-маски, альфы, окружения), содержимое пользователя, форматы и технические имена (sRGB8, L16F, RGB, OpenGL, DirectX), детали ошибок движка — {V}: docs/localization-parity.md:39-41",
   "Снимки — исходное состояние: подтвердить, что русского в списке нет."),
 "vectorcraft": ("VectorCraft", "Edit › Preferences › User Interface › Language (macOS: VectorCraft › Language)", f"{V}: docs/development.md:276", f"ru зарегистрирован — {V}: код ui-egui",
   "репозиторий программы `crates/ui-egui/src/i18n/ru.tsv` (живой); копия в craft-i18n",
   ["Слои", "Образцы", "Символы", "Монтажные области"],
   f"данные пользователя (слои, образцы, шрифты, документы), цветовой режим в заголовке вкладки, ID команд и имена параметров в сообщениях; статусная строка и ошибки движка — {V}: docs/development.md:297,324", ""),
 "wordcraft": ("WordCraft", "File › Options › Interface language (или `WORDCRAFT_LANGUAGE=ru`)", f"{V}: docs/localization-bs.md:5", f"ru зарегистрирован — {V}: код ui-egui",
   "craft-i18n `locales/ru/wordcraft.tsv`",
   ["Лента (Главная)", "Стили", "Навигация"],
   f"орфография, грамматика и переносы — только английские (это перевод интерфейса) — {V}: docs/localization-sv.md:87",
   "Найдено скриптом: в 4 строках каталога расходится число переводов строки `\\n` (строки 63, 944, 1983, 2143) — смотреть в диалогах с многострочным текстом."),
}


def desktop(prog: str) -> tuple[str, dict]:
    if prog == "solidcraft":
        paths = glob.glob(os.path.join(L10N, "solidcraft", "solidcraft", "assets", "platforms", "linux", "*.desktop"))
    else:
        paths = glob.glob(os.path.join(PKG, prog, "packaging", "linux", "*.desktop")) or \
            glob.glob(os.path.join(PKG, prog + "-r2", "packaging", "linux", "*.desktop"))
    if not paths:
        return "", {}
    vals = {}
    with open(paths[0], encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^(Name|GenericName|Comment)(\[ru\])?=(.*)$", line.strip())
            if m and (m.group(1) + (m.group(2) or "")) not in vals:
                vals[m.group(1) + (m.group(2) or "")] = m.group(3)
    return os.path.relpath(paths[0], L10N), vals


def latest_tsv(prefixes: list[str]) -> str | None:
    for pre in prefixes:
        c = sorted(glob.glob(os.path.join(REPORTS, f"*-{pre}.tsv")))
        if c:
            return c[-1]
    return None


def long_strings(prog: str, n: int = 6):
    tsv = latest_tsv(["craft-i18n"]) if prog in ("photocraft", "pdfcraft", "wordcraft", "anicraft") else \
        latest_tsv([f"apps-{prog}", f"packaging-{prog}", prog])
    if not tsv:
        return None, []
    rows = []
    with open(tsv, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE):
            if r["check"] != "length-abs":
                continue
            if tsv.endswith("-craft-i18n.tsv") and r["program"] not in (f"craft-i18n:{prog}",):
                continue
            rows.append((len(r["ru"]), r["en"], r["ru"]))
    rows.sort(reverse=True)
    return os.path.relpath(tsv, L10N), rows[:n]


def catalog_files(prog: str) -> list[str]:
    out = []
    ci = os.path.join(L10N, "craft-i18n", "locales", "ru", prog + ".tsv")
    if os.path.exists(ci):
        out.append(ci)
        if prog in ("photocraft", "pdfcraft", "wordcraft", "anicraft", "deckcraft", "texturecraft"):
            return out  # программа читает перевод только из craft-i18n
    for base in ([os.path.join(L10N, "solidcraft", "solidcraft")] if prog == "solidcraft" else
                 [os.path.join(L10N, "apps", prog), os.path.join(PKG, prog)]):
        if os.path.isdir(base):
            for pat in ("crates/ui-egui/src/i18n/ru.*", "crates/ui-egui/locales/ru*.*", *(["crates/ui-egui/src/i18n.rs"] if prog == "effectcraft" else []),
                        "assets/locales/ru.json", "crates/*/src/i18n/ru.tsv", "crates/ui-egui/src/i18n/ru.tsv"):
                out += [p for p in glob.glob(os.path.join(base, pat)) if os.path.isfile(p)]
            if out:
                break
    return sorted(set(out))


def yo_words(files: list[str], n: int = 8) -> list[str]:
    c = collections.Counter()
    for f in files:
        with open(f, encoding="utf-8", errors="replace") as fh:
            c.update(w.lower() for w in re.findall(r"[А-Яа-яЁё]*[Ёё][А-Яа-яЁё]*", fh.read()))
    return [w for w, _ in c.most_common(n)]


def glossary_terms(prog: str):
    acc, prop = [], []
    if not os.path.exists(GLOSSARY):
        return acc, prop
    with open(GLOSSARY, encoding="utf-8") as fh:
        rows = list(csv.reader(fh, delimiter="\t", quoting=csv.QUOTE_NONE))
    for r in rows[1:]:
        if len(r) < 5:
            continue
        en, ru, where, _src, note = r[:5]
        scope = where.lower()
        hit = prog in scope or (prog == "craft-launcher" and "launcher" in scope)
        common = "common" in scope and prog in ("photocraft", "pdfcraft", "wordcraft", "anicraft", "cadcraft", "filmcraft", "vectorcraft", "craft-launcher")
        if not (hit or common):
            continue
        if note.startswith("принят"):
            if "только для" in note and prog not in note.lower():
                continue
            acc.append((en, ru))
        elif note.startswith("предложен") and hit:
            prop.append((en, ru))
    return acc[:10], prop[:4]


def chars(n: int) -> str:
    w = "знак" if n % 10 == 1 and n % 100 != 11 else "знака" if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else "знаков"
    return f"{n} {w}"


def esc(s: str) -> str:
    return s.replace("|", "\\|")


def write(prog: str) -> str:
    title, switch, switch_src, reg, catalog, panels, untr, notes = PROGRAMS[prog]
    dpath, dv = desktop(prog)
    lsrc, longs = long_strings(prog)
    files = catalog_files(prog)
    yo = yo_words(files)
    acc, prop = glossary_terms(prog)
    has_ru = not (reg.startswith("ru не зарегистрирован") or reg.startswith("в выпущенном коде ru нет"))
    shots = []
    def shot(slug, what):
        shots.append((f"{prog}-{len(shots)+1:02d}-{slug}.png", what))
    shot("language", f"окно, где выбирается язык ({switch}); виден пункт «Русский» или его отсутствие")
    shot("menu-file", "открытое меню «Файл» (File)")
    shot("menu-edit", "открытое меню «Правка» (Edit)")
    shot("menu-view", "открытое меню «Вид» (View); если такого меню нет — снимок строки меню целиком")
    for i, p in enumerate(panels):
        shot(f"panel-{i+1}", f"панель/палитра «{p}» (название панели — {G}, по смыслу программы; снять ближайшую по смыслу)")
    shot("settings", "диалог настроек целиком (вкладка «Общие» или первая)")
    shot("error", f"любое сообщение об ошибке: например, открыть файл неподдерживаемого типа или повреждённый файл ({G}: способ вызвать ошибку)")
    shot("long-text", "диалог или подсказка с длинным текстом (см. список длинных строк ниже) — не обрезано ли")
    shot("plural", f"фраза с числом: выделить 1, 2, 5 и 21 объект (или файл), если программа это показывает ({G}: где именно видно)")
    shot("start-menu", "ярлык в меню приложений: название и подпись (наведённая подсказка/описание)")
    shot("about", "окно «О программе» (версия на снимке нужна, чтобы сверять с клонами)")

    L = [f"# {title} — чеклист скриншотов (русский интерфейс)", ""]
    L.append(f"Создан скриптом `review/tools/gen_checklists.py` {_dt.date.today():%d.%m.%Y}. Снимки делает правообладатель на своём компьютере; отдел локализации туда не заходит. "
             "Пометки: **проверено (источник)** / **догадка** / **не проверено**.")
    L.append("")
    L.append("## 1. Как включить русский")
    L.append("")
    L.append(f"- Путь: {switch} — **{switch_src}**")
    L.append(f"- Состояние в коде: {reg}")
    L.append(f"- Где лежит перевод: {catalog}")
    if not has_ru:
        L.append("- **Русского в программе пока нет** — снимки ниже фиксируют исходное (английское) состояние.")
    L.append("- Нужен ли перезапуск после смены языка: **не проверено** — отметить по факту: [ ] сменился сразу  [ ] нужен перезапуск")
    L.append("- Версия программы на компьютере: ____________ (из «О программе»)")
    L.append("")
    L.append("## 2. Снимки")
    L.append("")
    L.append("Имя файла — как в списке (номер не менять, даже если пункт пропущен: тогда отметить «нет»).")
    L.append("")
    for fn, what in shots:
        L.append(f"- [ ] `{fn}` — {what}")
    L.append("")
    L.append("## 3. На что смотреть на каждом снимке")
    L.append("")
    L.append("- [ ] нет английских слов там, где рядом русские (кроме списка «не переводится» ниже)")
    L.append("- [ ] текст не обрезан, не вылезает за кнопку/колонку, нет «…» посреди слова")
    L.append("- [ ] буква «ё» рисуется (нет квадратиков и пустых мест)")
    L.append("- [ ] числа с подписями склоняются: 1 файл / 2 файла / 5 файлов / 21 файл")
    L.append("- [ ] горячие клавиши и подчёркнутые буквы меню не пропали")
    L.append("- [ ] многоточие «…» у пунктов, которые открывают окно, стоит так же, как в английском")
    L.append("")
    L.append("## 4. Ярлык в меню приложений")
    L.append("")
    if dpath:
        L.append(f"Файл в клоне: `{dpath}` — **{V}** (чтение файла в рабочей копии).")
        L.append("")
        L.append("| Поле | English | Русский в клоне |")
        L.append("|---|---|---|")
        for k in ("Name", "GenericName", "Comment"):
            L.append(f"| {k} | {esc(dv.get(k, '—'))} | {esc(dv.get(k + '[ru]', 'нет'))} |")
        L.append("")
        if any(k.endswith("[ru]") for k in dv):
            L.append("Русские поля добавлены локальной черновой правкой в рабочей копии (коммит «отдел локализации packaging: черновой русский перевод .desktop, AppStream и mime», 20.11.2026) — "
                     f"**{V}: git log клона**. В установленной у правообладателя версии их, скорее всего, нет (по плану 4.1 на установленной системе полей не было) — снимок фиксирует, что видно сейчас.")
    else:
        L.append(f"Файл `.desktop` в клоне не найден — **{N}**.")
    L.append("")
    L.append("- [ ] в меню приложений видно название и подпись; записать, на каком языке: ________")
    L.append("")
    L.append("## 5. Длинные строки — где чаще всего режется текст")
    L.append("")
    if longs:
        L.append(f"Из отчёта `{lsrc}` (английский ≤ 25 знаков, русский > 40) — **{V}: подсчёт скрипта**. Найти на экране хотя бы 2–3 из них:")
        L.append("")
        for n, en, ru in longs:
            L.append(f"- [ ] «{esc(en)}» → «{esc(ru)}» ({chars(n)})")
    else:
        L.append(f"Отчёта или длинных строк нет ({'русского каталога нет' if not has_ru else 'скрипт не нашёл строк длиннее порога'}).")
    L.append("")
    L.append("## 6. «ё» в каталоге")
    L.append("")
    if yo:
        L.append(f"Самые частые слова с «ё» в русском каталоге ({', '.join('`' + os.path.relpath(f, L10N) + '`' for f in files)}) — **{V}: подсчёт по файлам**. Поймать хотя бы одно на снимке:")
        L.append("")
        L.append("- [ ] " + ", ".join(f"«{w}»" for w in yo))
    else:
        if files:
            L.append(f"В каталоге ({', '.join('`' + os.path.relpath(f, L10N) + '`' for f in files)}) нет ни одной «ё» — **{V}: подсчёт по файлу**. "
                     "Записать, как на экране пишутся слова вроде «ещё», «всё», «её»: [ ] через «е» везде  [ ] вперемешку")
        else:
            L.append("Русского каталога нет — проверить нечего.")
    L.append("")
    L.append("## 7. Термины глоссария")
    L.append("")
    if acc or prop:
        L.append("Из `glossary/glossary.tsv` (колонка где_встречается упоминает программу или общий каталог) — **проверено: файл глоссария**.")
        L.append("")
        for en, ru in acc:
            L.append(f"- [ ] {esc(en)} → **{esc(ru)}** (принят)")
        for en, ru in prop:
            L.append(f"- [ ] {esc(en)} → {esc(ru)} (только предложен — отметить, как написано на экране)")
    else:
        L.append("Терминов, привязанных к этой программе, в глоссарии нет.")
    L.append("")
    L.append("## 8. Что должно остаться как есть (не переводится)")
    L.append("")
    L.append(f"- {untr}")
    L.append("- имена файлов и документов пользователя, единицы измерения, названия форматов — общее правило авторов (проверено для большинства программ по их docs)")
    L.append("- [ ] на снимках это осталось по-английски / как было")
    L.append("")
    if notes:
        L.append("## 9. Особо проверить")
        L.append("")
        L.append(f"- [ ] {notes}")
        L.append("")
    L.append("## Итог (заполняет правообладатель или ревизор по снимкам)")
    L.append("")
    L.append("- Снимков сделано: __ из " + str(len(shots)))
    L.append("- Найдено проблем: __ (перечислить: снимок — что не так)")
    path = os.path.join(OUT, f"{prog}.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    return path


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    for prog in PROGRAMS:
        print(write(prog))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
