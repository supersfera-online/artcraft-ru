# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/filmcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/filmcraft
Коммит исходника (последний, в котором менялся README.md): 00fa496944fefa6a6fe93e38bda94a8697a51949
Дата коммита: 18 ноября 2026, 06:43 (America/Los_Angeles, PT); в исходнике 2026-11-18T14:43:15Z
SHA256 исходника: 78f6574157395a197c587f86da6dad2c079a730f01fc501478ef46fc5be1abdc
Git blob SHA: 721d82a6ddac390132da83e8d40c1261799766e4
Размер исходника: 39980 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/filmcraft/main/README.md
Перевод выполнен локально; авторам не отправлялся. Строки-переключателя языков нет: в репозитории нет других README.<код>.md.
-->
<!-- Перевод не проверен авторами -->
<p align="center">
  <a href="https://getartcraft.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/artcraft-logo-white.svg">
      <img alt="ArtCraft" src="docs/brand/artcraft-logo.svg" width="200">
    </picture>
  </a>
</p>


<p align="center">
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.filmcraft.png" width="128" height="128" alt="Значок FilmCraft: гравированная сова на фиолетовой плитке">
</p>

<h1 align="center">FilmCraft</h1>

<p align="center">
  <b>Монтаж видео, цвет и звук; профессиональный нелинейный видеоредактор с открытым исходным кодом, построенный на чистом Rust.</b>
</p>

<p align="center">
  Современный нелинейный монтаж видео с открытым исходным кодом: нативно в macOS, Windows и Linux и в браузере через WebAssembly.<br>
  Команда ArtCraft.
</p>

<p align="center">
  <a href="#license-and-credits"><img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%7C%20Apache--2.0-8b5cf6?style=flat-square"></a>
  <img alt="Written in pure Rust" src="https://img.shields.io/badge/pure-Rust-6a3fd6?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows and Linux" src="https://img.shields.io/badge/runs%20on-macOS%20%7C%20Windows%20%7C%20Linux-8b5cf6?style=flat-square">
  <a href="#status"><img alt="Status: young and moving fast" src="https://img.shields.io/badge/status-young%20and%20moving%20fast-6a3fd6?style=flat-square"></a>
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_filmcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/filmcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/filmcraft"><b>FilmCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/filmcraft-hero.png" alt="FilmCraft в рабочей среде «Цвет» посреди документального монтажа «Аполлона-11» из съёмок NASA: программный монитор с Saturn V, сходящим со стартовой башни, нижней третью Launch Complex 39A и субтитром земля–борт, панель эффектов с грейдингом и ключевыми кадрами Scale на кадре, панель грейдинга, корзины отборов NASA и таймлайн с 49 склейками изображения, закадровыми планами, титрами, дорожкой субтитров, звуком миссии, приглушённой музыкальной подложкой, именованными маркерами, просчитанным участком и живыми измерителями громкости" width="100%">
</p>

<p align="center"><sub><i>Apollo 11 - Tranquility</i>: трёхминутный документальный монтаж съёмок NASA 1969 года — старт, посадка и выход на Луну, с субтитрами по стенограмме миссии. Каждый кадр на этих снимках — кадры из общественного достояния, декодированные, скомпонованные и отгрейженные собственным кодом FilmCraft.</sub></p>

> [!NOTE]
> **ArtCraft — это сообщество художников из самых разных сфер.** Цифровое искусство, генеративное, музыка,
> игры &mdash; если вы что-то создаёте, вы один из нас. **[Заходите поздороваться в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#edit">Монтаж</a> ·
  <a href="#color">Цвет</a> ·
  <a href="#effects-and-motion">Эффекты</a> ·
  <a href="#audio">Звук</a> ·
  <a href="#titles-and-captions">Титры</a> ·
  <a href="#formats-and-codecs">Форматы</a> ·
  <a href="#export">Экспорт</a> ·
  <a href="#interchange">Обмен</a> ·
  <a href="#built-for-agents">Агенты</a> ·
  <a href="#get-started">С чего начать</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#documentation">Документация</a> ·
  <a href="#status">Состояние</a>
</p>

<br>

FilmCraft — профессиональный нелинейный редактор: знакомые панели, рабочие среды, инструменты и сочетания, так что руки уже знают, где что находится. Под этим он новый с самого битового потока. Кодеки H.264, HEVC, ProRes и AAC — наши собственные, написанные на Rust по открытым спецификациям. GPU-компоновщик работает в линейном свете. Расчёт кадров идёт по точному целочисленному времени, поэтому склейки никогда не уезжают. И каждое действие в программе — команда, которой ИИ-агент может управлять так же точно, как вы.

<br>

<a id="edit"></a>
## Монтаж

<p align="center">
  <img src="docs/images/filmcraft-assembly.png" alt="Рабочая среда «Сборка»: корзины с миниатюрами плёнки, Carnival of Souls в исходном мониторе, кадр кладбища Night of the Living Dead в программном мониторе и трейлер на трёхдорожечном таймлайне с партитурой Шопена на A2 и измерителями громкости" width="100%">
</p>

<p align="center"><sub>Рабочая среда «Сборка»: монтаж трейлера к <i>Night of the Living Dead</i> (1968) со вставкой из <i>Carnival of Souls</i> (1962).</sub></p>

**Таймлайн, который вы уже знаете.** Исходный и программный мониторы, корзины с миниатюрами, многодорожечный таймлайн с кнопками патча и назначения, синхронными блокировками и связанным выделением. Рабочие среды «Монтаж», «Сборка», «Цвет», «Эффекты» и «Звук» на месте, и каждую панель можно закрепить где угодно.

- **Трёхточечный монтаж.** Отметьте вход и выход в исходном мониторе, затем вставьте (`,`) или наложите (`.`) на пропатченные дорожки. Поднять (`;`) и извлечь (`'`) убирают диапазоны обратно.
- **Каждая подрезка.** Инструменты ripple, roll, slip, slide, изменения скорости и бритвы. Режим подрезки выбирает точки склейки как ripple, roll или trim, сдвигает их по кадру (`⌥←` `⌥→`, ×5 с `⇧`), переключает тип подрезки клавишей `⌃T` и продлевает их до головки воспроизведения клавишей `E`. `Q` и `W` подрезают ripple до головки. **Монитор подрезки** показывает обе стороны склейки, **монитор slip** показывает кадры вокруг slip при перетаскивании (выход предыдущего клипа, новый вход и выход, вход следующего), а **динамическая подрезка** подрезает вживую во время воспроизведения: `L` вперёд, `J` назад, `K` чтобы остановить и зафиксировать одним шагом отмены.
- **Точное время.** Каждая правка считается в целочисленных тиках: 254 016 000 000 в секунду, что делится нацело на любую обычную частоту кадров и частоту дискретизации. 23,976, 29,97 drop-frame и 59,94 точны, а не приблизительны.
- **То, на что опираются профессионалы.** Маркеры с цветами, именами и длительностями; выгрузка замечаний к просмотру последовательности командой **Маркеры ▸ Экспортировать маркеры как CSV…**; добавить склейку (`⌘K`) на одну или все дорожки; вложенность; копировать, вставить и вставить со сдвигом; удалить ripple и закрыть промежуток; привязка; неограниченная отмена с панелью истории.
- **Ваши клавиши.** Редактор сочетаний клавиш (`⌥⌘K`) с нарисованной клавиатурой, сочетаниями для панелей, предупреждениями о конфликтах и пресетами раскладок FilmCraft и стандартных NLE.
- **Работа не пропадает.** Сохранения атомарны, автосохранение держит скользящий набор версий, а журнал восстановления после сбоя, записываемый примерно через секунду после каждой правки, возвращает несохранённые изменения после сбоя или отключения питания.

<p align="center">
  <img src="docs/images/filmcraft-timeline.png" alt="Крупный план таймлайна: кадры Night of the Living Dead с наплывами на V1, вставка Carnival of Souls на V2, ноктюрн Шопена зелёной формой волны на A2, цветные маркеры вдоль линейки и измеритель громкости с мгновенным, краткосрочным, интегрированным и истинно пиковым значениями" width="100%">
</p>

<p align="center"><sub>Вблизи: наплывы, вставка на V2, партитура на A2, цветные маркеры и измерители громкости справа.</sub></p>

<br>

<a id="color"></a>
## Цвет

<p align="center">
  <img src="docs/images/filmcraft-color.png" alt="Рабочая среда «Цвет» на Charade (1963): Кэри Грант и Одри Хепбёрн в программном мониторе, сигнал формы волны и вектороскоп слева, корзины трейлера и таймлайн внизу" width="100%">
</p>

<p align="center"><sub>Рабочая среда «Цвет» на <i>Charade</i> (1963), с живыми осциллографами рядом с программным монитором.</sub></p>

**Полная панель грейдинга**, в том порядке, в котором работает колорист:

- **Базовая коррекция:** температура и оттенок, экспозиция, контраст, света, тени, белые, чёрные, насыщенность.
- **Творческая:** восемь встроенных обликов с регулятором интенсивности, плюс выцветшая плёнка, резкость и Vibrance. Облики — цветовые преобразования, написанные в коде, а не файлы LUT.
- **Кривые:** редактор кривой RGB с монотонно-кубической интерполяцией (без перерегулирования) и цветовой тон против насыщенности, цветовой тон против цветового тона, цветовой тон против яркости, яркость против насыщенности и насыщенность против насыщенности.
- **Цветовые круги:** круги теней, средних тонов и светов, у каждого свой регулятор светлоты.
- **HSL Secondary:** ключ цвета по цветовому тону, насыщенности и яркости, просмотр ключа как матовой подложки и коррекция только выбранного.
- **Виньетка:** величина, середина, округлость и растушёвка.

<table>
  <tr>
    <td width="34%" valign="top" align="center">
      <img src="docs/images/filmcraft-color-panel.png" alt="Панель грейдинга на Charade (1963): ползунки базовой коррекции с цветными дорожками температуры и оттенка, свёрнутые разделы Creative и Curves, цветовые круги теней, средних тонов и светов и переключатели HSL Secondary и Vignette"><br>
      <sub><b>Панель грейдинга.</b> Базовая коррекция, цветовые круги и каждый другой раздел, у каждого свой выключатель.</sub>
    </td>
    <td width="66%" valign="top" align="center">
      <img src="docs/images/filmcraft-scopes.png" alt="Видеоосциллографы: зелёная форма волны яркости и вектороскоп кадра Charade (1963)"><br>
      <sub><b>Осциллографы, которые говорят правду.</b> Форма волны и вектороскоп считаются по отгрейженному кадру. Весь грейдинг идёт в линейном свете, в 32-bit float.</sub>
    </td>
  </tr>
</table>

<br>

<a id="effects-and-motion"></a>
## Эффекты и движение

<p align="center">
  <img src="docs/images/filmcraft-effects.png" alt="Рабочая среда «Эффекты»: панель эффектов с Motion, Opacity, Time Remapping и цветовым грейдом, Earth Views from the ISS NASA в программном мониторе и обозреватель эффектов, открытый на переходах Dissolve" width="100%">
</p>

<p align="center"><sub><i>Earth Views from the ISS</i> NASA с применённым обликом и обозреватель эффектов, открытый на наплывах.</sub></p>

- **Полная корзина видеоэффектов (более 90 эффектов в 16 категориях), эффекты совместимости плюс около 30 переходов.** Размытия (Bokeh, Focus, Compound), ключи (Ultra Key, Track Matte), искажения (Corner Pin, Turbulent Displace, Warp Stabilizer), Lights & Glows, эффекты иммерсивного видео (VR) на равнопромежуточной съёмке, Posterize Time, Echo и другие. Перекрёстный наплыв, уход в чёрное или белое, плёночный наплыв, шторки, диафрагмы, толчки, сдвиги, масштабы, сдирание страницы, вращение куба и другие.
- **Движение и непрозрачность на каждом клипе:** положение, масштаб, вращение, точка привязки и подавление мерцания, плюс 26 режимов наложения.
- **Продвинутые ключевые кадры:** линейные, Безье, авто и непрерывное Безье, удержание, плавный вход и плавный выход. Панель эффектов показывает дорожку ключевых кадров для каждого параметра под линейкой времени с ручкой головки воспроизведения, и каждый анимированный параметр открывается в **графики значения и скорости** с перетаскиваемыми манипуляторами влияния. Панель эффектов и панель свойств разделяют навигатор ключевых кадров (◀ ◆ ▶): добавить или удалить ключевой кадр на головке, шаг к предыдущему или следующему.
- **GPU-компоновщик** на wgpu (Metal, Vulkan, DirectX 12, WebGPU). Он берёт выборки YUV прямо из декодера со сверхдискретизацией следа и смешивает в линейном свете. Путь ЦП рисует те же кадры, и оба сверяются друг с другом.

<p align="center">
  <img src="docs/images/filmcraft-keyframes.png" alt="Панель эффектов с графиками значения и скорости плавного наезда Scale на титр Night of the Living Dead, программный монитор с титром над просёлочной дорогой и панель свойств с Transform и Crop" width="100%">
</p>

<p align="center"><sub>Плавный наезд на титр: график значения, график скорости и манипулятор влияния Безье.</sub></p>

<br>

<a id="audio"></a>
## Звук

- **Измерители громкости по вещательным стандартам.** Мгновенная, краткосрочная и интегрированная громкость и истинный пик по ITU-R BS.1770 и EBU R128 рядом с пиковыми измерителями. Наше интегрированное значение совпадает с фильтром `ebur128` ffmpeg до десятой доли LU.
- **Эффекты клипа на нашей собственной библиотеке DSP:** параметрический эквалайзер, фильтры верхних, нижних и полосовые, динамика, лимитер истинного пика, задержка, реверберация, DeNoise, DeHummer, инверсия и сдвиг высоты. Параметры можно задавать ключевыми кадрами. Эффекты непрерывны при прокрутке, воспроизведении и экспорте, с компенсацией задержки.
- **Микшер дорожек и микшер клипов:** фейдеры, панорама, отключение звука, соло, пять слотов инсерта на дорожку (до или после фейдера), посылы, подмиксы и дорожка Mix, всё с точностью до сэмпла и с компенсацией задержки. 24 дорожки с тремя эффектами каждая сводятся примерно в шесть раз быстрее реального времени на одном ядре.
- **Автоматизация как на пульте:** режимы Read, Latch, Touch и Write, записываемые вживую с микшера во время воспроизведения, показанные и правимые как ключевые кадры дорожки на таймлайне. Плюс диалог усиления звука (задать, скорректировать, нормализовать) и перекрёстные затухания постоянной мощности.
- **Воспроизведение по звуковым часам.** Звуковая карта — задающий генератор, поэтому изображение следует за звуком, а не наоборот.

<br>

<a id="titles-and-captions"></a>
## Титры и субтитры

- **Настоящий текстовый движок:** формирование OpenType с кернингом и лигатурами, двунаправленный текст, разрыв строк, трекинг и интерлиньяж, рисуется в линейном свете и остаётся чётким при любом масштабе и повороте.
- **Инструменты «Текст», «Фигура» и «Перо»** на программном мониторе: щелкните, чтобы набрать, правьте кареткой и выделением, растяните прямоугольники, эллипсы и контуры. Графические клипы держат слои текста и фигур с заливкой, штрихами, фоном и тенью, всё с ключевыми кадрами, и правятся в панели свойств.
- **Субтитры:** дорожки субтитров в форматах Subtitle, CEA-608, CEA-708 и телетекст; импорт и экспорт SRT, WebVTT и SCC с точностью до кадра; правка субтитров в панели текста и вжигание их в выгрузки.
<br>

<a id="formats-and-codecs"></a>
## Форматы и кодеки

Внутри нет FFmpeg. Видеокодеки, AAC, Opus и контейнеры — наш собственный код на Rust, реализованный по открытым спецификациям ITU-T, ISO и IETF и проверенный кадр за кадром против ffmpeg как внешнего эталона.

| | Декодирование | Кодирование | Примечания |
|---|:---:|:---:|---|
| **H.264 / AVC** | ✓ | ✓ | Декодер побитово точен на 37+ потоках, 500–600 кадр/с при 1080p. Кодировщик: профили High, Main и Baseline, CABAC, B-кадры, CRF/CBR/VBR/2 прохода |
| **HEVC / H.265** | ✓ | | Main и Main 10, побитово точен на 41 потоке (тайлы, WPP, PCM, долгосрочные ссылки), около 225 кадр/с при 1080p |
| **Apple ProRes** | ✓ | ✓ | Декодирует 422 Proxy до 4444 XQ; экспорт пишет 422 HQ |
| **AAC-LC** | ✓ | ✓ | |
| **VP8** | ✓ | | Каждый инструмент кодирования, версии битового потока 0–3, скрытые кадры altref, альфа-слой прозрачного WebM; побитово точен с libvpx на опубликованных тестовых векторах VP8; в WebM/Matroska и MP4 |
| **VP9** | ✓ | | Профили 0–3, 8/10/12 бит, 4:2:0–4:4:4, тайлы и суперкадры; побитово точен на 50+ потоках; в WebM/Matroska и MP4 |
| **Opus** | ✓ | | SILK, CELT, гибрид и многопотоковое окружение; точно по диапазону на каждом векторе соответствия RFC 8251; в WebM/Matroska и MP4 |
| **AV1** | ✓ | | Профиль Main, 8/10 бит 4:2:0 и монохром, каждый инструмент кодирования, включая зерно плёнки, superres и пространственные слои; побитово точен с libdav1d на проверенных векторах libaom; в MP4 и WebM/Matroska |
| **DNxHD / DNxHR** | ✓ | ✓ | Все CID SMPTE ST 2019-1 (от LB до 444, 8/10/12 бит); экспорт пишет DNxHR в MOV |
| **MJPEG, PCM** | ✓ | ✓ | |
| **MP3, FLAC, ALAC, Vorbis** | ✓ | | Пока через крейт [symphonia](https://github.com/pdeljanov/Symphonia) (MPL-2.0), будет заменён своим |
| **MP4 / MOV** | ✓ | ✓ | Фрагментированный MP4, списки монтажа, дорожки таймкода |
| **Matroska / WebM** | ✓ | | Lacing, Cues, снятие заголовков, цветовые метаданные HDR |
| **AVI** | ✓ | | AVI 1.0 и OpenDML (файлы больше 1 ГБ); Motion JPEG, H.264, HEVC и несжатые RGB / YUV с PCM, MP3, MP2 или AC-3. DivX / Xvid и DV пока нет |
| **Stills** | ✓ | ✓ | Импорт PNG, JPEG, GIF, WebP, TIFF и BMP (анимированные GIF, APNG и WebP как клипы, с прозрачностью); экспорт последовательностей PNG и анимированного GIF |


Также импортируются: видео MPEG-2 / MPEG-1, AC-3, MP2, MXF (OP1a / OP-Atom), транспортные и программные потоки MPEG (AVCHD, вещание, DVD), Ogg и последовательности изображений. Пока нет: экспорт AV1, camera RAW, E-AC-3. Аппаратное декодирование работает в macOS (VideoToolbox), Windows (Media Foundation) и, для H.264 и HEVC, в Linux (VA-API); экспорт H.264 может использовать кодировщик NVIDIA в Windows и Linux (по выбору), а экспорт H.265 (HEVC Main, 8 бит) идёт через него (NVENC в Windows, VideoToolbox в macOS) ([#30](https://github.com/storytold/filmcraft/issues/30)).

<br>

<a id="export"></a>
## Экспорт

<p align="center">
  <img src="docs/images/filmcraft-export.png" alt="Режим экспорта: слева назначения Media File, YouTube, Vimeo, TikTok, Instagram и FTP, в предварительном просмотре кадр Night of the Living Dead, справа параметры H.264 (1440x1080 при 23,976 кадр/с, стерео 48000 Гц, вся последовательность)" width="100%">
</p>

<p align="center"><sub>Режим экспорта, настроенный записать трейлер как H.264 MP4.</sub></p>

- **H.264 MP4 с AAC, нашими собственными кодировщиками.** Просчёт 6 секунд 960×540 занимает 1,3 секунды и декодируется в ffmpeg без единого предупреждения, со строгим обнаружением ошибок.
- **Также:** Apple ProRes 422 HQ и Motion JPEG в QuickTime, MXF OP1a и стандартный OP-Atom (DNxHR, ProRes или H.264 с PCM и начальным таймкодом), последовательности PNG, анимированный GIF и WAV.
- **Фоновые задания** с ходом выполнения и отменой, так что вы продолжаете монтировать, пока идёт просчёт.
- **Предварительные просчёты:** полоса просчёта помечает сегменты зелёным, жёлтым или красным; просчитанные предпросмотры кэшируются по содержимому, поэтому правка делает недействительным только то, что затронула, а отмена возвращает зелёный.

<br>

<a id="interchange"></a>
## Обмен

Переносите таймлайны между FilmCraft и любым другим редактором:

- **FCP 7 XML (xmeml):** отраслевой стандарт обмена таймлайнами. Переносит вложенные последовательности, переходы, генераторы, Motion, Opacity, Time Remap и уровни звука, с ключевыми кадрами.
- **FCPXML 1.9–1.11:** позвоночник, подключённые клипы как дорожки, переходы, пересчёт времени и составные клипы.
- **OpenTimelineIO:** открытый формат обмена киноиндустрии, с круговым обходом каждой детали FilmCraft через `metadata.filmcraft`.
- **CMX 3600 EDL:** старейший формат, который всё ещё в ходу, с таймкодом drop-frame, наплывами, шторками, изменениями скорости (`M2`) и одним EDL на дорожку.
- **AAF (Edit Protocol):** стандартный формат обмена таймлайном и звуком. Видео- и звуковые дорожки, наплывы и уходы, громкость клипа с ключевыми кадрами, маркеры и исходный таймкод; звук встроен или отдельными файлами WAV / AIFF, подрезан с захлёстами, с эффектами клипа, впечатанными и разложенными в моно, плюс необязательный видеомиксдаун. Импорт читает AAF обратно, извлекая встроенный звук.
- **OMF 2.0:** передача в звуковой постпродакшн: звуковые дорожки с перекрёстными затуханиями и усилением, с точностью до сэмпла, со звуком внутри или рядом.

Импорт вливает корзины, носители и последовательности документа в ваш проект одним отменяемым шагом и связывает каждый найденный на диске файл носителя.

<br>

<a id="built-for-agents"></a>
## Для агентов

Каждый пункт меню, кнопка, ползунок и перетаскивание в FilmCraft — это **команда** с идентификатором, типизированными параметрами и состоянием доступности. Команд движка больше 650 (`filmcraft-cli commands` их перечисляет), и новые команды добавляются постоянно. Интерфейс, CLI, канал управления JSON и **сервер MCP** направляют одни и те же команды, поэтому Claude или любой агент может резать, подрезать, грейдить, сводить и выгружать точно так же, как человек. Интерфейсом также можно управлять на уровне мыши и клавиатуры: у каждого виджета есть идентификатор автоматизации, и агенты могут щёлкать, перетаскивать, вводить и делать снимки экрана.

```jsonc
// over the control channel (JSON lines on TCP) or as MCP tool calls
{"method": "engine.execute", "params": {"command": "timeline.place",
  "params": {"item": 1, "track": "V1", "seconds": 0, "sourceIn": 284298240000000, "duration": 1270080000000}}}
{"method": "engine.execute", "params": {"command": "effects.setParam",
  "params": {"clip": 87, "effect": "lumetri", "param": "curve_luma", "value": [[0,0],[0.25,0.21],[0.75,0.82],[1,1]]}}}
{"method": "ui.screenshot", "params": {"path": "frame.png"}}
```

Трейлер и грейды на этих снимках собраны именно так: агент управлял запущенной программой.

<br>

<a id="everywhere"></a>
## Везде

- **Нативно** в macOS, Windows и Linux, с нативной строкой меню macOS.
- **Веб:** тот же движок и интерфейс работают в браузере через WebAssembly (`apps/filmcraft-web`, см. [docs/web.md](docs/web.md)); каждый выпуск поставляет его как `filmcraft-web-<version>.zip`.
- **Сменный интерфейс.** Интерфейс — один крейт (`ui-egui`) над движком, поэтому другую оболочку можно подставить, не трогая логику монтажа.

<br>

<a id="get-started"></a>
## С чего начать

Впервые монтируете в FilmCraft? Следуйте [«С чего начать: видеозатухания и ключевые кадры громкости звука»](docs/getting-started-fades.md).

```sh
cargo run --release -p filmcraft                           # the desktop app, with a demo project
cargo run --release -p filmcraft -- --control 9876         # plus the JSON-lines control server
cargo run --release -p filmcraft-cli -- commands           # list every engine command
cargo run --release -p filmcraft-cli -- mcp                # MCP server (headless)
```

Японский текст в интерфейсе и в титрах берётся из [craft-fonts](https://github.com/storytold/craft-fonts), необязательного входа сборки (сборки выпуска всегда его включают; без него FilmCraft использует свои и системные шрифты):

```sh
git clone https://github.com/storytold/craft-fonts ../craft-fonts
CRAFT_FONTS_DIR="$PWD/../craft-fonts" cargo run --release -p filmcraft
```

Протокол управления описан в [docs/control-protocol.md](docs/control-protocol.md). Застряли или хотите показать, что сделали? Спросите в [Discord](https://discord.gg/artcraft).

<a id="documentation"></a>
## Документация

| | |
|---|---|
| [CONTRIBUTING.md](CONTRIBUTING.md) · [docs/contributing.md](docs/contributing.md) | Установка, качественные проверки, соглашения о коммитах, как добавлять команды, эффекты, кодеки, панели и ресурсы |
| [AGENTS.md](AGENTS.md) | Правила, которым должен следовать каждый участник: ресурсы, чистая комната, лицензии |
| [docs/architecture.md](docs/architecture.md) | Слои, модель данных, шкала времени, система команд, конвейер просчёта и экспорта |
| [docs/testing.md](docs/testing.md) | Модульные, имущественные тесты и тесты эталона ffmpeg, критерии точности, эталоны производительности |
| [docs/agents.md](docs/agents.md) | Управление FilmCraft через MCP и канал управления; как агенты его развивают |
| [docs/control-protocol.md](docs/control-protocol.md) | Справка по каналу управления и MCP |
| [docs/project-files.md](docs/project-files.md) | Формат `.fcproj`, миграции схемы, автосохранение и восстановление после сбоя |
| [docs/graphics.md](docs/graphics.md) · [docs/captions.md](docs/captions.md) | Текстовый движок, графические клипы и инструменты; дорожки и форматы субтитров |
| [ROADMAP.md](ROADMAP.md) | Этап, числа сопоставимости, языки, что дальше и журнал хода |
| [docs/target-app-parity.md](docs/target-app-parity.md) · [docs/gaps.md](docs/gaps.md) · [docs/roadmap.md](docs/roadmap.md) | Оценка сопоставимости, ранжированный список пробелов, вехи и текущий фокус |
| [docs/codec-parity.md](docs/codec-parity.md) · [docs/file-format-parity.md](docs/file-format-parity.md) · [docs/hardware-parity.md](docs/hardware-parity.md) · [docs/ui-parity.md](docs/ui-parity.md) · [docs/localization-parity.md](docs/localization-parity.md) | Контрольные списки сопоставимости по измерениям |

<a id="status"></a>
## Состояние

FilmCraft молод и движется быстро. Монтаж, подрезка, мультикам, цвет, ключевые кадры, эффекты, титры, субтитры, сведение, кодеки и экспорт уже работают.

FilmCraft находится в **альфе**. Мы следим за двумя числами ([docs/target-app-parity.md](docs/target-app-parity.md), повторно измерено 10 октября 2026):

- **Ширина возможностей: ~86 %.** Пункты меню, эффекты, переходы, панели и форматы профессиональной NLE, которые есть в FilmCraft (меню 92 % и эффекты 100 %, измерено).
- **Готовность к настоящей работе: ~56 %.** Наша честная оценка того, насколько FilmCraft близок к полной производственной работе на настоящих проектах.

Самые большие пробелы сегодня:

- **Скорость на большом материале.** Аппаратное декодирование работает в macOS и Windows и для H.264 и HEVC в Linux (VA-API или NVDEC с драйвером NVIDIA; VP9 и AV1 там декодируются программно). Режимы наложения и самые частые эффекты идут на GPU, но грейдинг, ключи и просчёт экспорта всё ещё на ЦП; кодирование H.264 может использовать аппаратный кодировщик в macOS и в Windows и Linux с GPU NVIDIA (по выбору, Экспорт ▸ Аппаратное кодирование), а экспорт H.265 только аппаратный на обеих платформах (HDR-последовательности выгружаются как Main 10 PQ / HLG с NVENC; VideoToolbox пишет 8-битный SDR) ([#30](https://github.com/storytold/filmcraft/issues/30)).
- **Нативный импорт проектов `.prproj`.** Файлы `.prproj` пока открыть нельзя; переносите последовательности как FCP7 XML, AAF или OTIO.
- **Нет подключаемых модулей.** Нет размещения VST3 / Audio Units или OpenFX.
- **Кодеки доставки.** H.264 — наш единственный программный экспорт кодека доставки; H.265 выгружается только через аппаратный кодировщик (NVIDIA в Windows: Main 8-бит SDR и Main 10 HDR PQ / HLG; VideoToolbox в macOS: 8-битный Main, SDR); экспорта AV1 пока нет.
- **Реальные носители и платформы.** Наши декодеры побитово точны на потоках соответствия, но файлы камер и телефонов в поле проверены меньше. Windows и Linux испытываются гораздо меньше, чем macOS.
- **Возможности ИИ.** Пока немного; распознавание речи необязательно и по умолчанию выключено.

Сообщения об ошибках с настоящим материалом — самое полезное, что вы можете нам прислать: [откройте вопрос](https://github.com/storytold/filmcraft/issues) или расскажите в [Discord](https://discord.gg/artcraft).

<a id="architecture"></a>
## Архитектура

Многослойный Cargo workspace:

| Слой | Крейты |
|---|---|
| Кодеки и контейнеры | `h264`, `hevc`, `vp9`, `prores`, `aac`, `opus`, `isobmff`, `matroska`, `avi`, `bitstream` |
| Основы | `time`, `geom`, `color`, `frame`, `media`, `text`, `project`, `audio-dsp` |
| Монтаж и обмен | `edit`, `codecs`, `captions`, `format` (файлы проектов), `interchange` |
| Просчёт и вывод | `render`, `gpu`, `export` |
| Движок | `engine`: реестр команд, сеанс, отмена, задания |
| Оболочки | `ui-egui`, `automation` (MCP), `apps/filmcraft`, `apps/filmcraft-cli` |
| Поддержка тестов | `testkit` (эталоны ffmpeg, фикстуры), `golden` (тесты эталонных изображений) |

Ниже оболочек ничто не зависит от набора инструментов интерфейса или API ОС. `cargo xtask ci` проверяет форматирование, замечания, тесты, правила слоёв, указание ресурсов и сборку wasm.

<a id="downloads"></a>
## Загрузки

**Впервые в FilmCraft?** Скачайте программу со [страницы FilmCraft на getartcraft.com](https://getartcraft.com/apps/filmcraft). Так установить проще всего.

**Нужна конкретная сборка или формат?** На GitHub в [последнем выпуске](https://github.com/storytold/filmcraft/releases/latest) перечислены все сборки ниже, а в [списке всех выпусков](https://github.com/storytold/filmcraft/releases) — более ранние версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `filmcraft-<ver>-windows-x64.msi` | `filmcraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `filmcraft-<ver>-windows-arm64.msi` | `filmcraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `filmcraft-<ver>-windows-x86.msi` | `filmcraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы подписаны.

**Если программа не открывается в Windows:** настольная программа по умолчанию инициализирует только Vulkan и DirectX 12,
не OpenGL. Если позволить wgpu ещё и создать экземпляр OpenGL, некоторые графические драйверы (например,
`atio6axx.dll` AMD) могут аварийно завершиться до появления окна, и программа мелькнёт в «Диспетчере задач» и выйдет.
`WGPU_BACKEND` подменяет значение по умолчанию для диагностики (например `dx12` или `vulkan`). В
PowerShell, из папки с исполняемым файлом:

```powershell
$env:WGPU_BACKEND = "vulkan"
& .\filmcraft.exe
Remove-Item Env:WGPU_BACKEND                     # restore the default for later launches
```

Явная подмена `gl` может вернуть сбой драйвера на затронутых системах. Значения подсистемы по умолчанию для macOS, Linux
и веба не менялись.

ПК, у которого GPU установлены из разных пакетов драйверов одного поставщика (например ноутбук со
встроенным и дискретным GPU AMD), может перечислить один GPU дважды, по одному разу через каждую установленную
версию драйвера Vulkan, и окно, нарисованное через устаревший, падает внутри драйвера
(`amdvlk64.dll`, код выхода `0xc0000005`). FilmCraft рисует более новым и пишет об этом в
`%APPDATA%\FilmCraft\Logs\filmcraft.log`; установка одного пакета драйвера для каждого GPU убирает
дубликат. При одном драйвере на GPU адаптер тот, который выбирает wgpu, как и раньше.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `filmcraft-<ver>-macos-universal.dmg` | Подписана и нотариально заверена |
| Инструмент командной строки, универсальный | `filmcraft-cli-<ver>-macos-universal.zip` | Подписан и нотариально заверен |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `filmcraft-<ver>-linux-x86_64.AppImage` | `filmcraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `filmcraft-<ver>-linux-x86_64.flatpak` | `filmcraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `filmcraft-<ver>-linux-x86_64.deb` | `filmcraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `filmcraft-<ver>-linux-x86_64.rpm` | `filmcraft-<ver>-linux-aarch64.rpm` | |
| Архив | `filmcraft-<ver>-linux-x86_64.tar.gz` | `filmcraft-<ver>-linux-aarch64.tar.gz` | Распакуйте и запустите `./install.sh` |

RISC-V (riscv64): `filmcraft-<ver>-linux-riscv64.tar.gz` (только архив; нужен glibc 2.39+, например Ubuntu 24.04
или Debian 13).

Установщик архива размещает FilmCraft, его инструмент командной строки и интеграцию в рабочий стол в
`~/.local`, без прав администратора. Для всех пользователей выполните
`sudo ./install.sh --prefix /usr/local`. Повторный запуск установщика обновляет установку.

**Gentoo (сопровождается сообществом):** оверлей [::snakebyte overlay](https://github.com/switch87/snakebyte-overlay)
упаковывает выпуск для Linux как `media-video/filmcraft-bin`. Его сопровождает сообщество, а не команда
FilmCraft, поэтому о проблемах упаковки сообщайте оверлею:

```sh
eselect repository add snakebyte git https://github.com/switch87/snakebyte-overlay.git
emaint sync -r snakebyte
echo 'media-video/filmcraft-bin ~amd64' >> /etc/portage/package.accept_keywords/filmcraft
emerge --ask media-video/filmcraft-bin
```

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `filmcraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `filmcraft-web-<ver>.zip` | Работает в современном браузере; разместите на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

FilmCraft — одно из приложений **Crafting Apps**: бесплатные творческие инструменты с открытым исходным кодом от команды
[ArtCraft](https://getartcraft.com/), каждый написан с нуля на Rust и каждый может
работать сам по себе.

| | Программа | Для чего | Код | Подробнее |
|:-:|---|---|---|---|
| <img src="https://raw.githubusercontent.com/storytold/photocraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.photocraft.png" alt="" width="32" height="32"> | **PhotoCraft** | Редактирование изображений: слои, маски, текст и настоящие файлы PSD| [GitHub](https://github.com/storytold/photocraft) | [Сайт](https://getartcraft.com/apps/photocraft) |
| <img src="https://raw.githubusercontent.com/storytold/vectorcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.vectorcraft.png" alt="" width="32" height="32"> | **VectorCraft** | Векторная иллюстрация| [GitHub](https://github.com/storytold/vectorcraft) | [Сайт](https://getartcraft.com/apps/vectorcraft) |
| <img src="https://raw.githubusercontent.com/storytold/filmcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.filmcraft.png" alt="" width="32" height="32"> | **FilmCraft** | Монтаж видео, цвет и звук      | [GitHub](https://github.com/storytold/filmcraft) | [Сайт](https://getartcraft.com/apps/filmcraft) |
| <img src="https://raw.githubusercontent.com/storytold/lightcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.lightcraft.png" alt="" width="32" height="32"> | **LightCraft** | Библиотека фотографий и проявление raw| [GitHub](https://github.com/storytold/lightcraft) | [Сайт](https://getartcraft.com/apps/lightcraft) |
| <img src="https://raw.githubusercontent.com/storytold/pdfcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.pdfcraft.png" alt="" width="32" height="32"> | **PdfCraft** | Чтение, организация и защита PDF        | [GitHub](https://github.com/storytold/pdfcraft) | [Сайт](https://getartcraft.com/apps/pdfcraft) |
| <img src="https://raw.githubusercontent.com/storytold/effectcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.effectcraft.png" alt="" width="32" height="32"> | **EffectCraft** | Моушн-графика и визуальные эффекты | [GitHub](https://github.com/storytold/effectcraft) | [Сайт](https://getartcraft.com/apps/effectcraft) |
| <img src="https://raw.githubusercontent.com/storytold/designcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.designcraft.png" alt="" width="32" height="32"> | **DesignCraft** | Вёрстка и публикация       | [GitHub](https://github.com/storytold/designcraft) | [Сайт](https://getartcraft.com/apps/designcraft) |
| <img src="https://raw.githubusercontent.com/storytold/figcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.figcraft.png" alt="" width="32" height="32"> | **FigCraft** | Дизайн интерфейсов и прототипирование| [GitHub](https://github.com/storytold/figcraft) | [Сайт](https://getartcraft.com/apps/figcraft) |
| <img src="https://raw.githubusercontent.com/storytold/wordcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.wordcraft.png" alt="" width="32" height="32"> | **WordCraft** | Текстовый процессор и документы| [GitHub](https://github.com/storytold/wordcraft) | [Сайт](https://getartcraft.com/apps/wordcraft) |
| <img src="https://raw.githubusercontent.com/storytold/soundcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.soundcraft.png" alt="" width="32" height="32"> | **SoundCraft** | Запись и редактирование звука| [GitHub](https://github.com/storytold/soundcraft) | [Сайт](https://getartcraft.com/apps/soundcraft) |
| <img src="https://raw.githubusercontent.com/storytold/deckcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.deckcraft.png" alt="" width="32" height="32"> | **DeckCraft** | Презентации и слайд-колоды    | [GitHub](https://github.com/storytold/deckcraft) | [Сайт](https://getartcraft.com/apps/deckcraft) |
| <img src="https://raw.githubusercontent.com/storytold/cadcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.cadcraft.png" alt="" width="32" height="32"> | **CADCraft** | Автоматизированное проектирование| [GitHub](https://github.com/storytold/cadcraft) | [Сайт](https://getartcraft.com/apps/cadcraft) |
| <img src="https://raw.githubusercontent.com/storytold/gridcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.gridcraft.png" alt="" width="32" height="32"> | **GridCraft** | Электронные таблицы и данные| [GitHub](https://github.com/storytold/gridcraft) | [Сайт](https://getartcraft.com/apps/gridcraft) |
| <img src="https://raw.githubusercontent.com/storytold/texturecraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.texturecraft.png" alt="" width="32" height="32"> | **TextureCraft** | Рисование 3D-текстур| [GitHub](https://github.com/storytold/texturecraft) | [Сайт](https://getartcraft.com/apps/texturecraft) |
| <img src="https://raw.githubusercontent.com/storytold/craft-anything/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.craft-anything.png" alt="" width="32" height="32"> | **Craft Anything** | Смотрите, как устроена любая программа, и собирайте свою| [GitHub](https://github.com/storytold/craft-anything) | [Сайт](https://getartcraft.com/apps/craft-anything) |
| <img src="https://raw.githubusercontent.com/tangency-labs/solidcraft/main/assets/icons/app/linux/exports/hicolor/64x64/apps/io.tangencylabs.solidcraft.png" alt="" width="32" height="32"> | **SolidCraft** | Параметрический 3D CAD от Tangency Labs (приложение сообщества)| [GitHub](https://github.com/tangency-labs/solidcraft) | |


И сама [**ArtCraft**](https://getartcraft.com/) — наша студия изображений и видео на основе ИИ для художников, которым нужен настоящий контроль.

<br>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<h3 align="center">Приходите творить с нами</h3>

<p align="center">
  Наш Discord — место, где собираются художники любого рода: те, кто пишет, снимает, рисует, монтирует фильм,
  набирает текст, и те, кто ещё выясняет, что им нравится создавать. Покажите, над чем работаете,
  попросите помощи, расскажите, что сломано, или расскажите, что вы хотите, чтобы эти инструменты умели.
  Каким бы ни был ваш материал и как давно вы этим занимаетесь, вам здесь рады.
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><b>discord.gg/artcraft</b></a> ·
  <a href="https://getartcraft.com/">getartcraft.com</a> ·
  <a href="https://getartcraft.com/apps">The Crafting Apps</a> ·
  <a href="https://getartcraft.com/apps/filmcraft">FilmCraft</a>
</p>

<br>

<a id="license-and-credits"></a>
## Лицензия и благодарности

FilmCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the FilmCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md). Сборки с
[craft-fonts](https://github.com/storytold/craft-fonts) (все официальные выпуски) также встраивают его шрифты
(OFL-1.1), перечисленные в его [ATTRIBUTION.md](https://github.com/storytold/craft-fonts/blob/main/ATTRIBUTION.md).

**Съёмка и музыка на снимках экрана:** киноплёнка и телезапись NASA «Аполлон-11» с [images.nasa.gov](https://images.nasa.gov) (старт, Центр управления запуском, лунная поверхность и возвращение) и голосовая стенограмма земля–борт «Аполлона-11», все работы правительства США в общественном достоянии (NASA этот проект не поддерживает); *Night of the Living Dead* (1968), *Carnival of Souls* (1962) и *Charade* (1963), все в общественном достоянии США; *Earth Views from the ISS* NASA; Ноктюрн соч. 48 № 1 и Баллада № 1 Шопена в исполнении для Musopen, выпущенные на условиях CC0. Сами носители в этот репозиторий не входят. Источники и сведения о каждом ресурсе — в [ATTRIBUTION.md](ATTRIBUTION.md).

FilmCraft — независимая реализация. В нём нет закрытого кода, значков, изображений, пресетов или LUT и нет кода GPL или LGPL; каждый значок нарисован в коде, и каждый ресурс открыто лицензирован и указан ([AGENTS.md](AGENTS.md)), кроме имени и логотипов ArtCraft, которые являются товарными знаками ArtCraft Team и используются на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt). ffmpeg используется только как внешний эталон тестов.

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и FilmCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<br>

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>

<a id="star-history"></a>
## История звёзд

[![Star History Chart](https://api.star-history.com/svg?repos=storytold/filmcraft&type=Date&legend=top-left)](https://www.star-history.com/?repos=storytold%2Ffilmcraft&type=date&legend=top-left)
