# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/photocraft/blob/main/README.md
Репозиторий: https://github.com/storytold/photocraft
Коммит исходника (последний, в котором менялся README.md): b0e0bcc6c470d39a21fac74fcdf966604a000af7
Дата коммита: 13 ноября 2026, 20:03 (America/Los_Angeles, PT); в исходнике 2026-11-14T04:03:16Z
SHA256 исходника: 2b013c9bd785a107c3a21e366c67e978a2f3df48078675c252ee1f491bf485d9
Git blob SHA: 04508f9637c73e9dc775861137208c21737eedec
Размер исходника: 36767 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/photocraft/b0e0bcc6c470d39a21fac74fcdf966604a000af7/README.md
На момент снятия (20 ноября 2026, PT) содержимое README.md на ветке main совпадает с этим коммитом (HEAD main: 877d58844029967b80e36a964902d309de1be158).
Перевод выполнен локально; авторам не отправлялся. Строки-переключателя языков нет: в репозитории photocraft нет других README.<код>.md.
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
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.photocraft.png" width="128" height="128" alt="Значок PhotoCraft: гравированная девятихвостая лиса на синей плитке">
</p>

<h1 align="center">PhotoCraft</h1>

<p align="center">
  <b>Редактирование изображений: открытая реимплементация Adobe Photoshop по принципу чистой комнаты, заново написанная на чистом Rust.</b><br>
  Слои, маски, корректирующие слои, стили слоя, текст, векторы, кисти и настоящие файлы PSD<br>
  в нативной программе, целиком написанной на Rust. Открытая, офлайн и ваша.
</p>

<p align="center">
  <img alt="100% Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="macOS · Windows · Linux · FreeBSD · Web" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-native-2f7bf5?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-3a3a3a?style=flat-square">
  <img alt="Status: early alpha" src="https://img.shields.io/badge/status-early%20alpha-d69e2e?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_photocraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/photocraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/photocraft"><b>PhotoCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/photocraft-demo.jpg" alt="Редактирование в PhotoCraft «Большой волны» Хокусая: карточка подписи с тенью, текстовые слои Title и Credit, корректирующие слои Vibrance и «Кривые», и редактор кривых поверх гистограммы изображения" width="100%">
  <br>
  <sub>Карточка подписи с тенью, живым текстом и корректирующими слоями Vibrance и «Кривые», с открытым редактором кривых.<br>
  <i>The Great Wave off Kanagawa</i>, Katsushika Hokusai, c. 1831</sub>
</p>

> [!NOTE]
> **ArtCraft — сообщество художников из самых разных сфер.** Цифра, генеративное искусство, музыка,
> игры &mdash; если вы что-то создаёте, вы один из нас. **[Заходите поздороваться в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#features">Возможности</a> ·
  <a href="#everything-in-the-box">Всё в комплекте</a> ·
  <a href="#psd-without-compromise">PSD</a> ·
  <a href="#built-for-agents">Агенты</a> ·
  <a href="#under-the-hood">Под капотом</a> ·
  <a href="#get-started">С чего начать</a> ·
  <a href="#downloads">Загрузки</a> ·
  <a href="#the-crafting-apps">Crafting Apps</a> ·
  <a href="https://discord.gg/artcraft">Discord</a>
</p>

<br>

<table>
  <tr>
    <td width="25%" valign="top">
      <h3>🎛️ Привычно по устройству</h3>
      Меню, сочетания клавиш, панели и инструменты — там, где их ждут руки, от ⌘J до ⇧⌘D. Если вы знаете Photoshop, вы уже знаете PhotoCraft.
    </td>
    <td width="25%" valign="top">
      <h3>⚡ Нативно и быстро</h3>
      GPU-композитор на wgpu (Metal, Vulkan, DX12, WebGPU), тайлы с копированием при записи и многопоточные фильтры. Никакого Electron, никакого web view, никакого ожидания.
    </td>
    <td width="25%" valign="top">
      <h3>🗂️ Настоящие файлы PSD</h3>
      Открывайте, изменяйте и сохраняйте многослойные документы Photoshop. При повторном сохранении отрисовка сохраняется у 307 из 309 тестовых файлов psd-tools.
    </td>
    <td width="25%" valign="top">
      <h3>🤖 Готово к агентам</h3>
      Каждое действие — это команда, поэтому один и тот же движок можно вести из интерфейса, из CLI, по каналу управления JSON или через MCP-сервер.
    </td>
  </tr>
</table>

<br>

<a id="features"></a>
## Возможности

Каждый снимок экрана здесь — это настоящая программа за работой над произведениями из общественного достояния, отрисованными вне экрана через канал управления.

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/images/photocraft-adjustments.jpg" alt="«Впечатление. Восходящее солнце» Моне с корректирующими слоями «Уровни» и Vibrance; справа открыты редактор уровней и панель «Гистограмма» со средним, стандартным отклонением и медианой" width="100%">
      <br>
      <sub>Корректирующие слои «Уровни» и Vibrance и живая панель «Гистограмма».<br><i>Impression, Sunrise</i>, Claude Monet, 1872</sub>
      <h3>Изменяйте без сожалений</h3>
      Корректирующие слои оставляют каждое изменение живым. Сложите «Уровни», «Кривые», Vibrance, «Цветовой тон/Насыщенность» и ещё с десяток, наложите на них маску на область, переставьте их или выключите — исходные пиксели при этом не меняются.
      <br><br>
      <b>16 корректирующих слоёв</b>, которые также применяются напрямую к пикселям, в том числе «Кривые» с правкой по каналам, «Уровни» с живой гистограммой, «Чёрно-белое», «Микшер каналов», «Карта градиента», «Фотофильтр», «Выборочный цвет» и Color Lookup (.cube, .3dl, .look). Плюс «Тени/Света», «Заменить цвет», «Подобрать цвет», «Тонирование HDR», «Обесцветить» и «Эквализовать».
    </td>
    <td width="50%" valign="top">
      <img src="docs/images/photocraft-layer-styles.jpg" alt="Диалог «Стиль слоя» правит «Внешнее свечение» на текстовом слое EARTHRISE, также включена «Обводка», поверх фотографии «Восход Земли» Apollo 8" width="100%">
      <br>
      <sub>«Внешнее свечение» и «Обводка» на живом текстовом слое в диалоге «Стиль слоя».<br><i>Earthrise</i>, William Anders / NASA, 1968</sub>
      <h3>Стили, от которых кадр выигрывает</h3>
      «Внешняя тень», «Внутренняя тень», «Внешнее» и «Внутреннее свечение», «Скос и рельеф», «Атлас», «Обводка» и наложения «Цвет», «Градиент» и «Узор» — живьём на любом слое, в том числе текстовом. Узоры берутся из библиотеки (встроенные, Изменить › Определить узор, импорт/экспорт <code>.pat</code>) и блоков <code>Patt</code> в PSD.
      <br><br>
      Копируйте и вставляйте стили между слоями, скрывайте все эффекты сразу и открывайте стили прямо из своих PSD — они отрисовываются так, чтобы совпадать с Photoshop.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/images/photocraft-masks.jpg" alt="«Девушка с жемчужной серёжкой» Вермеера: эллиптическое выделение вокруг лица и слой «Цветовой тон/Насыщенность» с эллиптической маской, из‑за которой всё за пределами лица становится серым" width="100%">
      <br>
      <sub>Эллиптическое выделение становится маской слоя «Цветовой тон/Насыщенность», поэтому цвет остаётся только у лица.<br><i>Girl with a Pearl Earring</i>, Johannes Vermeer, c. 1665</sub>
      <h3>Выделения, которые понимают изображение</h3>
      Рамки выделения, лассо и «Волшебная палочка» — для точности; «Быстрое выделение», «Выделение объекта» и «Выделить основной объект», когда обводку должен сделать компьютер; «Выделение и маска», чтобы уточнить тончайшие края вроде волос.
      <br><br>
      Растушёвка, расширить, сузить, сгладить, нарастить, выделить снова. Превратите любое выделение в маску слоя, векторный контур или фигуру. Умное выделение работает на вашей машине, без облака и без учётной записи.
    </td>
    <td width="50%" valign="top">
      <img src="docs/images/photocraft-type.jpg" alt="«Среди гор Сьерра-Невада» Бирштадта: на холсте правится заголовок SIERRA NEVADA шрифтом Georgia, подпись автора и абзац подписи; открыты параметры «Символ» и «Абзац»" width="100%">
      <br>
      <sub>Заголовок, правленый на месте, с подписью автора и абзацем основного текста.<br><i>Among the Sierra Nevada, California</i>, Albert Bierstadt, 1868</sub>
      <h3>Текст, который красиво набирается</h3>
      Текст из точки и абзацный текст, который правится прямо на холсте, с полными параметрами «Символ» и «Абзац»: шрифт, начертание, размер, интерлиньяж, трекинг, выравнивание и цвет. <a href="docs/color-picker.md">Полная пипетка цвета текста</a> также умеет брать образец с экрана через пиксельную лупу.
      <br><br>
      Текстовые слои остаются редактируемыми, принимают стили слоя и проходят полный цикл через PSD.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/images/photocraft-vector.jpg" alt="Значок лотоса из слоёв-фигур (Lotus, Water, Sun, Badge и Dotted Ring) поверх «Водяных лилий» Моне, с выделенными опорными точками контура лотоса" width="100%">
      <br>
      <sub>Значок из слоёв-фигур: лотос с градиентной заливкой, звезда и пунктирное кольцо.<br><i>Water Lilies</i>, Claude Monet, 1906</sub>
      <h3>Векторы с точностью до пикселя</h3>
      Инструменты «Прямоугольник», «Эллипс», «Треугольник», «Многоугольник», «Линия», а также «Перо», «Свободное перо» и «Перо кривизны»; независимые от разрешения слои-фигуры, градиентные заливки и пунктирные, выровненные обводки.
      <br><br>
      Объединяйте фигуры (объединение, вычесть, пересечение, исключение), храните контуры на панели «Контуры», используйте их как векторные маски либо обводите и заливайте. 116 из 116 слоёв-фигур в нашем корпусе PSD совпадают с пикселями Photoshop.
    </td>
    <td width="50%" valign="top">
      <img src="docs/images/photocraft-filters.jpg" alt="Диалог фильтра «Скручивание» на угле 320 градусов с живым просмотром внутри эллиптического выделения на «Звёздной ночи» Ван Гога" width="100%">
      <br>
      <sub>«Скручивание» показывает живой просмотр на холсте, только внутри выделения.<br><i>The Starry Night</i>, Vincent van Gogh, 1889</sub>
      <h3>Смотрите, прежде чем применить</h3>
      Каждый диалог фильтра показывает живой просмотр на холсте, через ваше выделение. Размытия (гауссово, блочное, в движении, радиальное, поверхностное, умное, линзовое, по фигуре и галерея размытия: тилт-шифт, диафрагма, поле, вращение, контур), резкость, «Уменьшить шум», искажения («Скручивание», «Волна», «Рябь», «Смещение», «Сдвиг», «Зигзаг»…), «Пикселизация», «Стилизация» («Масляная краска», «Ветер», «Выдавливание»…), «Рендер» («Облака», «Волокна», «Блик линзы», «Световые эффекты») и другие.
      <br><br>
      Запускайте фильтры на умном объекте — они остаются редактируемыми: их можно изменить, скрыть, переставить или маскировать в любой момент.
      <br><br>
      Размытия с большим радиусом идут проходами блочной суммы с накоплением по всем ядрам: гауссово размытие радиуса 180 на 3,6 МП занимает меньше секунды.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/images/photocraft-transform.jpg" alt="Маркеры свободного трансформирования вокруг повёрнутой копии «Титон и реки Снейк» Анселя Адамса; на панели «История» перечислены «Открыть», «Дублировать слой», «Свободное трансформирование» и другие шаги" width="100%">
      <br>
      <sub>«Свободное трансформирование» повёрнутого отпечатка, каждый шаг перечислен в «Истории».<br><i>The Tetons and the Snake River</i>, Ansel Adams, 1942</sub>
      <h3>Придавайте любую форму</h3>
      «Свободное трансформирование» с масштабом, поворотом, скосом, искажением и перспективой; точные повороты на 90° и 180° и отражения; «Трансформировать снова». Слои, текст, фигуры, маски и выделения трансформируются вместе.
      <br><br>
      Полная история, «Переключить последнее состояние» и «Кисть истории» позволяют отменить каждый шаг, даже по одному мазку кисти.
    </td>
    <td width="50%" valign="top">
      <img src="docs/images/photocraft-export-light.jpg" alt="Диалог «Экспорт как» в светлой теме поверх «Поцелуя» Климта: JPG с качеством 90, масштаб 50 процентов, с просмотром и оценкой размера около 684K" width="100%">
      <br>
      <sub>«Экспорт как» в светлой теме, с просмотром и оценкой размера файла.<br><i>The Kiss</i>, Gustav Klimt, 1907–1908</sub>
      <h3>Отправляйте куда угодно</h3>
      «Экспорт как» с форматом, качеством, прозрачностью и масштабом, плюс просмотр и мгновенная оценка размера файла. «Быстрый экспорт» в PNG в один щелчок.
      <br><br>
      Выберите тёмную тему Pro, воздушные темы Studio или вид Classic.
    </td>
  </tr>
</table>

<br>

<a id="everything-in-the-box"></a>
## Всё в комплекте

<table>
  <tr>
    <td width="33%" valign="top">
      <h4>🧰 69 инструментов</h4>
      Переместить · Монтажная область · Прямоугольное и эллиптическое выделение · Выделение одной строки · Выделение одного столбца · Лассо · Многоугольное лассо · Магнитное лассо · Выделение объекта · Быстрое выделение · Волшебная палочка · Обрезать · Обрезка перспективы · Фрагмент · Выделение фрагмента · Рамка · Пипетка · Проба цвета · Линейка · Заметка · Количество · Удалить · Точечная восстанавливающая кисть · Восстанавливающая кисть · Заплатка · Перемещение с учётом содержимого · Красные глаза · Кисть · Карандаш · Микс-кисть · Замена цвета · Штамп клонирования · Узорный штамп · Кисть истории · Кисть истории искусства · Ластик · Фоновый ластик · Волшебный ластик · Градиент · Ведро заливки · Размытие · Резкость · Палец · Осветлитель · Затемнитель · Губка · Перо · Свободное перо · Перо кривизны · Добавить опорную точку · Удалить опорную точку · Преобразовать точку · Горизонтальный и вертикальный текст · Горизонтальная и вертикальная маска текста · Выделение контура · Прямое выделение · Прямоугольник · Эллипс · Треугольник · Многоугольник · Звезда · Линия · Пользовательская фигура · Рука · Поворот вида · Масштаб
    </td>
    <td width="33%" valign="top">
      <h4>🖌️ Настоящий движок кисти</h4>
      Динамика формы, рассеивание, текстура, двойная кисть, динамика цвета, перенос, положение кисти, мокрые края, нарастание и сглаживание (включая «Натянутую нить»), управляемые нажимом, наклоном, поворотом и направлением пера. Наборы кистей, «Определить кисть из выделения» и детерминированные, воспроизводимые мазки.
    </td>
    <td width="33%" valign="top">
      <h4>🗃️ Слои как положено</h4>
      Группы, обтравочные маски, пиксельные и векторные маски, слои заливки (сплошная, градиент и узор), корректирующие слои, живые умные объекты с умными фильтрами и трансформированием и деформацией без потерь, выделение нескольких слоёв с выравниванием, распределением и связыванием, альфа-каналы и быстрая маска, 27 режимов смешивания Photoshop плюс шесть вариантов Paint.NET, непрозрачность и заливка, блокировки, цветовые метки, фильтр по типу слоя, объединение, сведение, растрирование, «Слой копированием/вырезанием», «Вставить в».
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <h4>🎨 Любой цвет, любая глубина</h4>
      Документы RGB, градаций серого, CMYK и Lab с 8, 16 и 32 битами на канал. Разрядность и цветовая модель — данные времени выполнения, поэтому каждый инструмент работает на любой глубине.
      <br><br>
      Настоящее управление цветом ICC на чистом Rust: встроенные профили, «Назначить профиль» и «Преобразовать в профиль» со всеми четырьмя целями рендеринга и компенсацией чёрной точки, экранная цветопроба (⌘Y) и «Предупреждение о цветовом охвате» (⇧⌘Y) на GPU.
    </td>
    <td width="33%" valign="top">
      <h4>🗂️ Форматы</h4>
      PSD и PSB, многослойный TIFF (данные слоёв Photoshop внутри TIFF, чтение и запись в любом порядке байтов), <a href="docs/pdn.md">Paint.NET PDN3 (чтение, с редактируемыми слоями и всеми 14 режимами смешивания)</a>, <a href="docs/ora.md">OpenRaster (чтение и запись, со слоями, группами и режимами смешивания, для Krita, MyPaint и GIMP)</a>, <a href="docs/xcf.md">GIMP XCF (чтение, со слоями, группами, масками, режимами смешивания, каналами и выделением)</a>, <a href="docs/kra.md">Krita .kra (чтение, со слоями рисования, группами, режимами смешивания и масками прозрачности)</a>, SVG (открывается как слои-фигуры, помещается как векторный умный объект), плюс плоские PNG, JPEG, TIFF, WebP (с потерями и без потерь), GIF, BMP, TGA, ICO, QOI, PNM, OpenEXR, Radiance HDR и FITS (астрономические изображения: 8/16-бит и 32-битное вещественное, серое или RGB, заголовок сохраняется), и собственный формат <code>.pcraft</code>. Плоские форматы сохраняют поддерживаемую ими глубину: PNG сохраняет 8/16-битные отсчёты, TIFF сохраняет 8/16-битные и 32-битные вещественные отсчёты, а OpenEXR сохраняет отсчёты half/float; JPEG, WebP и прочие 8-битные форматы понижают отсчёты большей глубины с предупреждением при экспорте. См. <a href="https://github.com/storytold/craft-libs/tree/main/crates/image-codecs#capability-matrix-default-build">матрицу возможностей кодеков</a> по каждому формату. Фотографии HEIC с iPhone и Mac только для чтения (входят в официальные сборки; для сборки из исходников необязательный флаг <code>--features heif</code>). AVIF только для записи с необязательной функцией сборки <code>avif</code>; декодирование AVIF и JPEG XL недоступны. Документы Affinity (<code>.af</code>, <code>.afdesign</code>, <code>.afphoto</code>, <code>.afpub</code>) открываются нативно, только для чтения, с монтажными областями, слоями, векторами, текстом, изображениями и масками; эффекты, коррекции и прочие неподдерживаемые части перечисляются в предупреждении, экспорт в Affinity недоступен.
    </td>
    <td width="33%" valign="top">
      <h4>🪄 Повседневное необходимое</h4>
      Автотон, автоконтраст и автоцвет · Эквализовать · Размер изображения и холста · Обрезать и подрезать · Показать всё · Правка › Заливка и обводка · Копировать объединённое · Вставить на место · направляющие, линейки, сетка и привязка · запись и воспроизведение действий · палитра команд (⌘F).
    </td>
  </tr>
</table>

<br>

<a id="psd-without-compromise"></a>
## PSD без компромиссов

Поддержка PSD в PhotoCraft — отдельный crate, написанный по открытой спецификации Adobe и проверенный на корпусе реальных файлов.

- **Верный полный цикл:** открытие и повторное сохранение документа даёт ту же отрисовку для 307 из 309 файлов в тестовом наборе psd-tools и для 169 из 170 в нашем смешанном наборе ag-psd/psd-tools (`crates/io/tests/it/corpus.rs`; набор psd-tools можно получить командой `cargo xtask corpus --psd-tools`), а всё, что мы ещё не моделируем (сырые блоки, дескрипторы, дополнения), переносится дальше, а не отбрасывается. Повторно сохранённый файл не совпадает с источником побайтно: PhotoCraft переписывает ресурсы изображения, записи слоёв и композит. Только отдельный crate `craft-psd`, разбирающий и записывающий файл без модели документа, воспроизводит каждый разбираемый файл корпуса байт в байт (`craft-psd/tests/it/corpus.rs`).
- **Пиксели совпадают:** оракул композита сравнивает нашу отрисовку с собственным сведённым изображением Photoshop и покрывает интерполяцию градиентов (Classic, Perceptual и линейную), эффекты слоя, обводки фигур, обтравку и непрозрачность заливки.
- **Крупные документы:** PSB, 16- и 32-битные файлы, а также документы CMYK и Lab открываются нативно.

<a id="built-for-agents"></a>
## Сделано для агентов

Каждый пункт меню, инструмент и диалог запускает команду из одного реестра из 500+ команд. Интерфейс, CLI, канал управления JSON и MCP-сервер вызывают одни и те же команды, поэтому всё, что можно нажать, может сделать и сценарий, и ИИ-агент.

```sh
# Headless: open, edit, save
photocraft-cli run wave.psd \
  --cmd filter.sharpen.smartSharpen     --params '{"amount":80}' \
  --cmd layer.newAdjustmentLayer.curves --params '{"points":[[0,0],[64,48],[192,212],[255,255]]}' \
  --out wave-final.png

# Apply one action list to a folder of images
photocraft-cli batch --actions grade.json --in ./raw --out ./graded

# Every subcommand explains itself
photocraft-cli batch --help

# Let an agent drive it over MCP (headless, or bridged to the running app)
photocraft-cli mcp
```

Настольная программа также даёт аутентифицированный канал управления только на loopback (`photocraft --control`) для осмотра состояния интерфейса, управления инструментами событиями указателя и внеэкранных снимков. Каждое изображение в этом README отрисовано именно так. См. [`docs/control-protocol.md`](docs/control-protocol.md).

<a id="under-the-hood"></a>
## Под капотом

- **Сначала движок:** модель документа из чистых данных и командный движок, поверх — тонкий интерфейс на egui. Архитектурное разделение по слоям проверяется на этапе сборки во всех 24 crate.
- **Два композитора:** CPU-композитор служит эталонным оракулом, а композитор на wgpu выводит холст на GPU. Их проверяют друг против друга.
- **Тайлы с копированием при записи:** разреженные тайлы 256² делают отмену дешёвой, а огромные холсты — лёгкими, и карты эффектов кэшируются для каждого состояния слоя.
- **Работает в браузере:** весь движок и интерфейс компилируются в WebAssembly.
- **Чистая комната:** реализация только по открытым спецификациям и наблюдаемому поведению. Никакого проприетарного кода, шейдеров или ресурсов.
- **Проверено тестами:** больше 1700 тестов, включая полный цикл PSD, синтетические генераторы, оракулы композитора и проверки на нескольких глубинах.

<a id="get-started"></a>
## С чего начать

```sh
git clone https://github.com/storytold/photocraft
cd photocraft
cargo run --release -p photocraft -- image.psd   # the desktop app
cargo test --workspace                           # the test suite
```

Японские шрифты для интерфейса и инструмента «Текст» берутся из [craft-fonts](https://github.com/storytold/craft-fonts), необязательного компонента сборки (в настольных релизных сборках он всегда включён). Без него PhotoCraft использует системные шрифты CJK:

```sh
git clone https://github.com/storytold/craft-fonts ../craft-fonts
CRAFT_FONTS_DIR="$PWD/../craft-fonts" cargo run --release -p photocraft
```

Новым участникам и ИИ-агентам: начните с [`AGENTS.md`](AGENTS.md), затем [`docs/`](docs/).

Установщики для macOS, Windows, Linux, FreeBSD и веба приложены к каждому [релизу на GitHub](https://github.com/storytold/photocraft/releases). В Linux можно выбрать AppImage, `.deb`, `.rpm`, tarball или пакет Flatpak. Пакету нужна среда выполнения freedesktop с [Flathub](https://flathub.org/setup); `flatpak` предлагает поставить её вместе с пакетом:

```sh
flatpak install --user photocraft-<version>-linux-x86_64.flatpak   # or -linux-aarch64
flatpak run ai.storyteller.photocraft
```

Flatpak печатает через сокет CUPS хоста («Файл › Печать» говорит с ним напрямую по IPP, `lp` не нужен); без CUPS или без принтера «Файл › Печать» открывает системный диалог печати через портал печати. См. [печать](docs/printing.md).

AppImage не требует установки: при первом запуске он регистрирует значок запуска и пункт меню в `~/.local/share`, чтобы в доке на Wayland отображался значок PhotoCraft. Чтобы пропустить это, задайте `PHOTOCRAFT_NO_DESKTOP_INTEGRATION=1`, а как отменить уже сделанное — см. [`docs/releasing.md`](docs/releasing.md) › Linux.

Чтобы пользоваться входящим в пакет CLI, запустите `./photocraft-<version>-linux-x86_64.AppImage --cli --help` или `--cli mcp`, чтобы поднять MCP-сервер на stdio. Запуски CLI пропускают интеграцию с рабочим столом. Симлинк с именем `photocraft-cli` тоже выбирает CLI; см. [`docs/development.md`](docs/development.md#headless-cli).

В сеансе Wayland файлы, перетащенные на окно, пока не открываются: у winit 0.30, библиотеки окон под egui, нет перетаскивания на Wayland (#386). Пользуйтесь «Файл › Открыть» или скопируйте изображение в файловом менеджере и вставьте его сочетанием Ctrl+V. Чтобы перетаскивать файлы, запускайте PhotoCraft под XWayland: `WAYLAND_DISPLAY= photocraft`, `WAYLAND_DISPLAY= ./photocraft-<version>-linux-x86_64.AppImage` или `flatpak run --nosocket=wayland --socket=x11 ai.storyteller.photocraft`. На Wayland PhotoCraft показывает команду для вашей установки в уведомлении, пока вы его не закроете. «Настройки › Производительность › Сервер отображения Linux» = X11 делает то же при каждом запуске. При дробном масштабе экрана (125%, 150%, 175%) окно XWayland рисуется в меньшем разрешении и увеличивается оконным композитором, поэтому интерфейс там размыт; нативный Wayland остаётся резким (#1072).

На macOS инструмент командной строки поставляется как `photocraft-cli-<version>-macos-universal.zip`. Двоичный файл подписан тем же Developer ID, что и программа, и нотаризован Apple. Голый двоичный файл не может нести прикреплённый талон нотаризации так, как это делает DMG, поэтому при первом запуске macOS проверяет нотаризацию через сеть. Это можно подтвердить самостоятельно:

```sh
ditto -x -k photocraft-cli-<version>-macos-universal.zip .
spctl --assess --type install -vv photocraft-cli-<version>-macos-universal/photocraft-cli
# ... accepted, source=Notarized Developer ID
```

На FreeBSD 14 (x86_64) в релизе есть tarball с раскладкой как у `/usr/local`. Поставьте библиотеки времени выполнения, затем распакуйте архив туда:

```sh
pkg install libxkbcommon wayland libX11 libXcursor libXrandr libXi libxcb mesa-libs vulkan-loader gtk3 fontconfig freetype2 alsa-lib
tar -xzf photocraft-<version>-freebsd-x86_64.tar.gz --strip-components 1 -C /usr/local
photocraft
```

Сопровождающим: в [`docs/releasing.md`](docs/releasing.md) описано, как релизы собираются, подписываются и публикуются.

> [!IMPORTANT]
> **Состояние:** PhotoCraft находится в ранней альфе, и мы хотим прямо сказать, где программа сейчас: большая часть поверхности возможностей Photoshop в том или ином виде есть, но **это ещё не замена Photoshop для повседневной профессиональной работы**. Главные пробелы — функции ИИ и генеративные возможности, 15 недостающих инструментов, глубина в типографике и профессиональных сценариях, а также совместимость с плагинами. Каждый пункт меню Photoshop подключён к команде ([`docs/parity-checklist.md`](docs/parity-checklist.md)), но это измеряет проводку, а не поведение. Честная картина по каждому измерению и то, куда мы идём дальше, — в [плане работ](ROADMAP.md) и в [оценке паритета](docs/target-app-parity.md). Ожидайте шероховатости и, пожалуйста, оформляйте issue (укажите ОС, размер документа, число слоёв и снимок экрана). О том, что сломалось, можно также написать в [Discord](https://discord.gg/artcraft).

<a id="community-packages"></a>
## Пакеты сообщества

Эти установщики сопровождают участники сообщества, а не команда PhotoCraft.

В Gentoo [оверлей ::snakebyte](https://github.com/switch87/snakebyte-overlay) упаковывает Linux-релиз как `media-gfx/photocraft-bin`:

```sh
eselect repository add snakebyte git https://github.com/switch87/snakebyte-overlay.git
emaint sync -r snakebyte
echo 'media-gfx/photocraft-bin ~amd64' >> /etc/portage/package.accept_keywords/photocraft
emerge --ask media-gfx/photocraft-bin
```

<a id="documentation"></a>
## Документация

Документация для разработчиков, по архитектуре, автоматизации, форматам и безопасности ведётся в [книге документации PhotoCraft](book/).

Чтобы самостоятельно разместить браузерную версию в Docker, см. [размещение веба в Docker](packaging/web/README.md#docker).

<a id="security"></a>
## Безопасность

Архитектура безопасности, моделирование угроз, укрепление разборщиков, фаззинг и сообщение об уязвимостях описаны в [документации по безопасности](book/src/security/) и в [политике безопасности](SECURITY.md) репозитория.

<a id="test-corpora"></a>
## Тестовые корпуса

PhotoCraft проверяется на реальных файлах: наших собственных эталонных PSD, подготовленных в Photoshop, в
[photocraft-corpus](https://github.com/storytold/photocraft-corpus), плюс наборы psd-tools, ag-psd и PngSuite, закреплённые и
проверенные по sha256. Их можно получить командой `cargo xtask corpus --all`, а тесты запустить командой
`cargo xtask test-corpus` (подробности в [docs/development.md](docs/development.md#test-corpora)).

<a id="downloads"></a>
## Загрузки

**Впервые в PhotoCraft?** Скачайте программу со [страницы PhotoCraft на getartcraft.com](https://getartcraft.com/apps/photocraft). Так её проще всего установить.

**Нужна конкретная сборка или формат?** На GitHub в [последнем релизе](https://github.com/storytold/photocraft/releases/latest) перечислены все сборки ниже, а в [списке всех релизов](https://github.com/storytold/photocraft/releases) — предыдущие версии и заметки к ним. `<ver>` в именах файлов — номер версии, а `SHA256SUMS.txt` содержит контрольную сумму для каждого файла.

<a id="windows"></a>
### Windows

| Сборка | Установщик | Переносная версия |
|---|---|---|
| x64 (64-разрядные Intel/AMD) | `photocraft-<ver>-windows-x64.msi` | `photocraft-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon и другие ARM-ПК) | `photocraft-<ver>-windows-arm64.msi` | `photocraft-<ver>-windows-arm64-portable.zip` |
| x86 (32-разрядная) | `photocraft-<ver>-windows-x86.msi` | `photocraft-<ver>-windows-x86-portable.zip` |

Установщики и исполняемые файлы имеют цифровую подпись.

<a id="macos"></a>
### macOS

| Сборка | Файл | Примечания |
|---|---|---|
| Программа, универсальная (Apple silicon + Intel) | `photocraft-<ver>-macos-universal.dmg` | Подписана и нотаризована |
| Инструмент командной строки, универсальный | `photocraft-cli-<ver>-macos-universal.zip` | Подписан и нотаризован |

<a id="linux"></a>
### Linux

| Формат | x86_64 | aarch64 (ARM64) | Примечания |
|---|---|---|---|
| AppImage | `photocraft-<ver>-linux-x86_64.AppImage` | `photocraft-<ver>-linux-aarch64.AppImage` | Запускается где угодно; обновляется сам через [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (файлы `.zsync`) |
| Flatpak | `photocraft-<ver>-linux-x86_64.flatpak` | `photocraft-<ver>-linux-aarch64.flatpak` | В песочнице; `flatpak install --user <file>` |
| Debian/Ubuntu | `photocraft-<ver>-linux-x86_64.deb` | `photocraft-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `photocraft-<ver>-linux-x86_64.rpm` | `photocraft-<ver>-linux-aarch64.rpm` | |
| Tarball | `photocraft-<ver>-linux-x86_64.tar.gz` | `photocraft-<ver>-linux-aarch64.tar.gz` | Распаковать куда угодно |

RISC-V (riscv64): только `photocraft-<ver>-linux-riscv64.tar.gz`, собран против Ubuntu 24.04 (нужен glibc 2.39+).

<a id="freebsd"></a>
### FreeBSD

| Сборка | Файл |
|---|---|
| x86_64 | `photocraft-<ver>-freebsd-x86_64.tar.gz` |

<a id="web-webassembly"></a>
### Веб (WebAssembly)

| Сборка | Файл | Примечания |
|---|---|---|
| Статический сайт | `photocraft-web-<ver>.zip` | Работает в современном браузере; размещается на любом статическом сервере |

<a id="the-crafting-apps"></a>
## The Crafting Apps

PhotoCraft — одно из приложений **Crafting Apps**: бесплатных творческих инструментов с открытым исходным кодом от команды
[ArtCraft](https://getartcraft.com/), каждое написано с нуля на Rust и каждое может работать само по себе.

| | Приложение | Для чего | Код | Подробнее |
|:-:|---|---|---|---|
| <img src="https://raw.githubusercontent.com/storytold/photocraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.photocraft.png" alt="" width="32" height="32"> | **PhotoCraft** | Редактирование изображений: слои, маски, текст и настоящие файлы PSD | [GitHub](https://github.com/storytold/photocraft) | [Сайт](https://getartcraft.com/apps/photocraft) |
| <img src="https://raw.githubusercontent.com/storytold/vectorcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.vectorcraft.png" alt="" width="32" height="32"> | **VectorCraft** | Векторная иллюстрация | [GitHub](https://github.com/storytold/vectorcraft) | [Сайт](https://getartcraft.com/apps/vectorcraft) |
| <img src="https://raw.githubusercontent.com/storytold/filmcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.filmcraft.png" alt="" width="32" height="32"> | **FilmCraft** | Монтаж видео, цвет и звук | [GitHub](https://github.com/storytold/filmcraft) | [Сайт](https://getartcraft.com/apps/filmcraft) |
| <img src="https://raw.githubusercontent.com/storytold/lightcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.lightcraft.png" alt="" width="32" height="32"> | **LightCraft** | Библиотека фотографий и проявление raw | [GitHub](https://github.com/storytold/lightcraft) | [Сайт](https://getartcraft.com/apps/lightcraft) |
| <img src="https://raw.githubusercontent.com/storytold/pdfcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.pdfcraft.png" alt="" width="32" height="32"> | **PdfCraft** | Чтение, организация и защита PDF | [GitHub](https://github.com/storytold/pdfcraft) | [Сайт](https://getartcraft.com/apps/pdfcraft) |
| <img src="https://raw.githubusercontent.com/storytold/effectcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.effectcraft.png" alt="" width="32" height="32"> | **EffectCraft** | Моушн-графика и визуальные эффекты | [GitHub](https://github.com/storytold/effectcraft) | [Сайт](https://getartcraft.com/apps/effectcraft) |
| <img src="https://raw.githubusercontent.com/storytold/designcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.designcraft.png" alt="" width="32" height="32"> | **DesignCraft** | Вёрстка и публикация | [GitHub](https://github.com/storytold/designcraft) | [Сайт](https://getartcraft.com/apps/designcraft) |
| <img src="https://raw.githubusercontent.com/storytold/figcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.figcraft.png" alt="" width="32" height="32"> | **FigCraft** | Дизайн интерфейсов и прототипирование | [GitHub](https://github.com/storytold/figcraft) | [Сайт](https://getartcraft.com/apps/figcraft) |
| <img src="https://raw.githubusercontent.com/storytold/wordcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.wordcraft.png" alt="" width="32" height="32"> | **WordCraft** | Текстовый процессор и документы | [GitHub](https://github.com/storytold/wordcraft) | [Сайт](https://getartcraft.com/apps/wordcraft) |
| <img src="https://raw.githubusercontent.com/storytold/soundcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.soundcraft.png" alt="" width="32" height="32"> | **SoundCraft** | Запись и редактирование звука | [GitHub](https://github.com/storytold/soundcraft) | [Сайт](https://getartcraft.com/apps/soundcraft) |
| <img src="https://raw.githubusercontent.com/storytold/deckcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.deckcraft.png" alt="" width="32" height="32"> | **DeckCraft** | Презентации и слайд-колоды | [GitHub](https://github.com/storytold/deckcraft) | [Сайт](https://getartcraft.com/apps/deckcraft) |
| <img src="https://raw.githubusercontent.com/storytold/cadcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.cadcraft.png" alt="" width="32" height="32"> | **CADCraft** | Автоматизированное проектирование | [GitHub](https://github.com/storytold/cadcraft) | [Сайт](https://getartcraft.com/apps/cadcraft) |
| <img src="https://raw.githubusercontent.com/storytold/gridcraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.gridcraft.png" alt="" width="32" height="32"> | **GridCraft** | Электронные таблицы и данные | [GitHub](https://github.com/storytold/gridcraft) | [Сайт](https://getartcraft.com/apps/gridcraft) |
| <img src="https://raw.githubusercontent.com/storytold/texturecraft/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.texturecraft.png" alt="" width="32" height="32"> | **TextureCraft** | Рисование 3D-текстур | [GitHub](https://github.com/storytold/texturecraft) | [Сайт](https://getartcraft.com/apps/texturecraft) |
| <img src="https://raw.githubusercontent.com/storytold/craft-anything/main/assets/app-icon/hicolor/64x64/apps/ai.storyteller.craft-anything.png" alt="" width="32" height="32"> | **Craft Anything** | Смотрите, как устроена любая программа, и собирайте свою | [GitHub](https://github.com/storytold/craft-anything) | [Сайт](https://getartcraft.com/apps/craft-anything) |
| <img src="https://raw.githubusercontent.com/tangency-labs/solidcraft/main/assets/icons/app/linux/exports/hicolor/64x64/apps/io.tangencylabs.solidcraft.png" alt="" width="32" height="32"> | **SolidCraft** | Параметрический 3D CAD от Tangency Labs (приложение сообщества) | [GitHub](https://github.com/tangency-labs/solidcraft) | |

И сам [**ArtCraft**](https://getartcraft.com/) — наша ИИ-студия изображений и видео для художников, которым нужен настоящий контроль.

Приложения Crafting Apps разделяют одни и те же соглашения: принцип чистой комнаты и чистый Rust, нативно на macOS, Windows и Linux, в браузере через WebAssembly и полностью управляются агентами.

<br>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<h3 align="center">Приходите творить с нами</h3>

<p align="center">
  Наш Discord — место, где собираются художники всех направлений: те, кто пишет красками, снимает, рисует, монтирует
  кино, набирает текст, и те, кто ещё ищет, что им нравится делать. Покажите, над чем работаете,
  попросите помощи, расскажите, что сломалось, или чего вы ждёте от этих инструментов.
  В каком бы материале вы ни работали и сколько бы вы этим ни занимались, вам здесь рады.
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><b>discord.gg/artcraft</b></a> ·
  <a href="https://getartcraft.com/">getartcraft.com</a> ·
  <a href="https://getartcraft.com/apps">The Crafting Apps</a> ·
  <a href="https://getartcraft.com/apps/photocraft">PhotoCraft</a>
</p>

---

<a id="license-and-credits"></a>
## Лицензия и благодарности

PhotoCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the PhotoCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Встроенные шрифты, значки, изображения и прочие ресурсы сохраняют свои открытые лицензии; каждый указан
с автором, источником и лицензией в [ATTRIBUTION.md](ATTRIBUTION.md).

Все показанные произведения находятся в общественном достоянии (Wikimedia Commons, NASA, U.S. National Archives); источники перечислены в [`docs/images/SOURCES.md`](docs/images/SOURCES.md).

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и PhotoCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<sub>Adobe, Photoshop, Illustrator, Premiere Pro, Lightroom, Acrobat, After Effects и InDesign являются товарными знаками или зарегистрированными товарными знаками Adobe Inc. в Соединённых Штатах и/или других странах. PhotoCraft — независимый проект с открытым исходным кодом и не связан с Adobe Inc., не спонсируется и не одобряется ею; эти имена используются только для описания рабочих процессов, с которыми программа совместима.</sub>

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="docs/brand/artcraft-mark.svg" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>

<a id="star-history"></a>
## История звёзд

[![Star History Chart](https://api.star-history.com/svg?repos=storytold/photocraft&type=Date&legend=top-left)](https://www.star-history.com/?repos=storytold%2Fphotocraft&type=date&legend=top-left)
