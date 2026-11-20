# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
<!-- Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0 -->
<!--
Источник: https://github.com/storytold/figcraft/blob/main/README.md
Репозиторий: https://github.com/storytold/figcraft
Коммит исходника (последний, в котором менялся README.md): 3839fe4a0cb4897c1fed1fb03e0b60e191ff61cb
Дата коммита: 8 ноября 2026, 21:24 (America/Los_Angeles, PT); в исходнике 2026-11-09T05:24:44Z
SHA256 исходника: 884e7a57f099c1587f212d7a887fe1f1aac2eb0021f25f41bfc2b4e8f122665f
Git blob SHA: 7bbc4d5249cb705f0714a2c5dfee2ce8a8a7a89a
Размер исходника: 34371 байт
Снято чтением raw: https://raw.githubusercontent.com/storytold/figcraft/main/README.md
Перевод выполнен локально; авторам не отправлялся. Строки-переключателя языков нет: в репозитории нет других README.<код>.md.
-->
<!-- Перевод не проверен авторами -->
<p align="center">
  <a href="https://getartcraft.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/storytold/vectorcraft/main/docs/brand/artcraft-logo-white.png">
      <img alt="ArtCraft" src="https://raw.githubusercontent.com/storytold/vectorcraft/main/docs/brand/artcraft-logo.png" width="200">
    </picture>
  </a>
</p>

<p align="center">
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.figcraft.png" width="128" height="128" alt="Значок FigCraft: гравированный хамелеон на мятно-зелёной плитке">
</p>

<h1 align="center">FigCraft</h1>

<p align="center">
  <b>Дизайн интерфейсов и прототипирование: с открытым исходным кодом, совместная работа и чистый Rust.</b><br>
  Frames, автолейаут, компоненты и варианты, векторные сети, стили, переменные и прототипы<br>
  в нативной программе, которая открывается сразу и работает без сети. С открытым исходным кодом, и ваша.
</p>

<p align="center">
  <img alt="100% Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="macOS · Windows · Linux · FreeBSD · Web" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-native-0EA5C6?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-3a3a3a?style=flat-square">
  <img alt="Status: early alpha" src="https://img.shields.io/badge/status-early%20alpha-d69e2e?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_figcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/figcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/figcraft"><b>FigCraft на getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">Все Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/shot-1-hero.png" alt="FigCraft в тёмной теме правит приложение для походов Ridgeline: на холсте три экрана телефона (Home в светлом режиме, страница подробностей маршрута и Home в тёмном режиме), выбран экземпляр карточки Featured trail, панель слоёв показывает дерево автолейаута экрана, а панель «Дизайн» показывает заливку и размер автолейаута Hug экземпляра, режим переменной Theme и заливку, привязанную к переменной цвета поверхности" width="100%">
  <br><sub><b>Ridgeline</b>: экраны на автолейауте, собранные из компонентов, со светлым и тёмным режимами из одного набора цветовых переменных · <code>examples/ridgeline-app.figcraft</code></sub>
</p>

<br>

> [!NOTE]
> **ArtCraft — это сообщество художников из самых разных сфер.** Дизайнеры, иллюстраторы, разработчики,
> музыканты, создатели игр &mdash; если вы что-то создаёте, вы один из нас. **[Заходите поздороваться в Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#a-look-around">Обзор</a> ·
  <a href="#made-in-figcraft">Сделано в FigCraft</a> ·
  <a href="#features">Возможности</a> ·
  <a href="#built-for-agents">Агенты</a> ·
  <a href="#under-the-hood">Под капотом</a> ·
  <a href="#get-started">С чего начать</a> ·
  <a href="#the-crafting-apps">Crafting Apps</a> ·
  <a href="https://discord.gg/artcraft">Discord</a>
</p>

<br>

<table>
  <tr>
    <td width="25%" valign="top">
      <h3>🎛️ Привычно по замыслу</h3>
      Панель инструментов, панель слоёв, панель «Дизайн», меню и сочетания клавиш стоят там, где их ждут руки.
    </td>
    <td width="25%" valign="top">
      <h3>⚡ Нативно и быстро</h3>
      Движок на Rust с постоянной моделью документа: правки касаются только того, что изменилось, поэтому создание узла в файле на 20 000 узлов занимает долю миллисекунды. Без Electron и без веб-представления.
    </td>
    <td width="25%" valign="top">
      <h3>🔌 Без сети и приватно</h3>
      Ваши файлы — обычные архивы <code>.figcraft</code> на вашем диске. Нет учётной записи, нет телеметрии, и ничего не покидает компьютер, пока вы не откроете общий доступ к файлу (<a href="#privacy-and-online-sharing">что общий доступ куда отправляет</a>). SVG, PNG, JPG, WebP и PDF на вход и выход; файлы <code>.fig</code> открываются (по возможности), как и макеты, выгруженные как публичный JSON файлового REST API, вместе с прототипами и переменными.
    </td>
    <td width="25%" valign="top">
      <h3>🤖 Готово для агентов</h3>
      Каждый пункт меню, инструмент и перетаскивание — это команда, поэтому тот же движок работает из интерфейса, CLI, канала управления JSON или сервера MCP.
    </td>
  </tr>
</table>

<br>

<a id="a-look-around"></a>
## Обзор

<table>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/shot-2-components.png" alt="Открыта дизайн-система интерфейса Ridgeline: слева панель «Ресурсы» с живыми миниатюрами компонентов Button, Difficulty, Search field, Toggle и значков; выбран набор компонентов Button из девяти вариантов в сетке автолейаута три на три, а панель «Дизайн» перечисляет свойства вариантов Style (Primary, Tonal, Outline) и State (Default, Hover, Disabled)" width="100%">
  <p align="center"><sub><b>Компоненты и варианты</b>: наборы компонентов, свойства вариантов и панель «Ресурсы» · <code>examples/ridgeline-design-system.figcraft</code></sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-3-prototype.png" alt="Четыре экрана телефона онбординга на вкладке Prototype, соединённые зелёными кривыми от кнопок Get started, Continue, Allow location и Not now к следующим экранам; выбрана кнопка Get started, и панель Prototype показывает взаимодействие On click, Navigate to 2 Interests" width="100%">
  <p align="center"><sub><b>Прототипирование</b>: связи, переходы, действия «назад» и поток · <code>examples/ridgeline-onboarding.figcraft</code></sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/shot-4-devmode.png" alt="Режим разработчика на домашнем экране Ridgeline: на Frame значок Ready for dev, выноска аннотации Development указывает на карточку избранного маршрута, выбран экземпляр строки маршрута, а панель Inspect показывает предварительный просмотр Playground и сгенерированный код React с интерфейсом props TrailRow и значениями title и details экземпляра" width="100%">
  <p align="center"><sub><b>Режим разработчика</b>: состояние «готово для разработки», аннотации и код React, где свойства компонента становятся props · <code>examples/ridgeline-app.figcraft</code></sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-5-vector.png" alt="Режим правки вектора на контуре волны с градиентом и сужающимся штрихом переменной ширины: видны опорные точки, манипуляторы Безье и рамка преобразования выделенных точек, внизу панель инструментов правки вектора; выше — знак горы, собранный булевыми операциями, и узел из исключённых колец с угловым градиентом" width="100%">
  <p align="center"><sub><b>Векторные сети</b>: точки и манипуляторы, штрихи переменной ширины, булевы операции, которые остаются редактируемыми · <code>examples/glass-and-vectors.figcraft</code></sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/shot-6-dashboard-light.png" alt="Светлая тема интерфейса с веб-аналитической панелью вымышленного оператора маршрутов: тёмная боковая панель, карточки KPI со спарклайнами, групповая столбчатая диаграмма, кольцевая диаграмма, таблица лучших маршрутов и площадная диаграмма; 12-колоночная модульная сетка Frame видна тонированными колонками, а его заливка связана со стилем заливки" width="100%">
  <p align="center"><sub><b>Модульные сетки и стили, светлая тема</b>: 12-колоночная сетка, стили заливки, текста, эффектов и сетки, диаграммы из фигур · <code>examples/ridgeline-studio-dashboard.figcraft</code></sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-7-collab.png" alt="Живой сеанс из окна одного участника: справа сверху аватары трёх человек, баннер «Priya Nair is spotlighting» с кнопкой Follow, зелёный курсор и контур выделения Priya на карточке маршрута тёмного домашнего экрана и фиолетовый курсор и выделение Jonas Ortiz на кнопке Start hike с пузырьком чата у курсора, в котором он спрашивает, должна ли кнопка оставаться закреплённой при прокрутке" width="100%">
  <p align="center"><sub><b>Живые сеансы</b>: три программы на одном файле <code>figcraft-server</code>, с курсорами, выделениями, чатом у курсора и «прожектором»</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <img src="docs/images/shot-8-board.png" alt="Файл доски Sprint retro на точечной сетке: ретроспектива Sprint 14 из шаблона retrospective, с разделами Went well, To improve и Next steps из стикеров, числом голосов 3, 2, 1 и 1 на четырёх стикерах после окончания голосования, а ниже блок-схема запроса на слияние из шаблона flow chart, фигуры которой соединены прямыми и угловыми связями с подписями Yes и No; справа сверху «таблетка» таймера показывает оставшиеся 4:30 и кнопки паузы, добавить минуту, стоп и Results" width="100%">
  <p align="center"><sub><b>Доски</b>: вид файла «белая доска» со стикерами, шаблонами, соединителями, общим таймером и голосованием, в тех же живых сеансах</sub></p>
</td>
<td width="50%" valign="top">
  <img src="docs/images/shot-9-devmode-measure.png" alt="Режим разработчика на домашнем экране Ridgeline с выбранной карточкой избранного маршрута: красные размерные линии на холсте показывают 118,3 от карточки до поля поиска, 62,1 от карточки до первой строки маршрута и 256,3 вдоль левой стороны карточки, а раздел Measurements панели Inspect перечисляет эти три значения под меню Add measurement" width="100%">
  <p align="center"><sub><b>Измерения режима разработчика</b>: размерные линии между слоями или вдоль стороны, сохранённые в файле и следующие за слоями · <code>examples/ridgeline-app.figcraft</code></sub></p>
</td>
</tr>
</table>

<a id="made-in-figcraft"></a>
## Сделано в FigCraft

Каждый макет ниже собран целиком через командный API FigCraft — тот же, что сервер MCP
открывает агентам, — и выгружен в масштабе 2x собственным визуализатором FigCraft. Исходные файлы — в
[`examples/`](examples).

<table>
<tr>
<td width="33%" valign="top">
  <img src="docs/images/art-app-home.png" alt="Домашний экран Ridgeline в светлом режиме: приветствие, поле поиска, чипы фильтров, карточка избранного маршрута с иллюстрацией горного пейзажа, список ближайших маршрутов и полупрозрачная панель вкладок" width="100%">
  <p align="center"><sub><b>Главная, светлая</b></sub></p>
</td>
<td width="33%" valign="top">
  <img src="docs/images/art-app-trail.png" alt="Экран подробностей маршрута Ridgeline: иллюстрация гор на закате со стеклянными кнопками, лист с метками сложности, имя маршрута, статистика расстояния, набора высоты и длительности, диаграмма профиля высоты и кнопка Start hike" width="100%">
  <p align="center"><sub><b>Подробности маршрута</b></sub></p>
</td>
<td width="33%" valign="top">
  <img src="docs/images/art-app-home-dark.png" alt="Тот же домашний экран Ridgeline в тёмном режиме, цвета переключены режимом Dark коллекции переменных Theme" width="100%">
  <p align="center"><sub><b>Главная, тёмная</b>: тот же Frame в режиме Dark</sub></p>
</td>
</tr>
<tr>
<td colspan="3" valign="top">
  <img src="docs/images/art-dashboard.png" alt="Панель Ridgeline Studio: тёмно-синяя боковая панель с навигацией, карточки KPI по активным пешеходам, отметкам, средней оценке и открытым инцидентам со спарклайнами, групповая столбчатая диаграмма походов по дням с подсказкой, кольцевая диаграмма сложности, таблица лучших маршрутов со значками состояния и площадная диаграмма посетителей" width="100%">
  <p align="center"><sub><b>Ridgeline Studio</b>: настольная панель на 12-колоночной сетке, каждая диаграмма из фигур и векторов</sub></p>
</td>
</tr>
<tr>
<td colspan="2" valign="top">
  <img src="docs/images/art-glass-weather.png" alt="Стеклянный виджет погоды поверх размытых бирюзовых, фиолетовых, розовых и оранжевых цветовых полей: матовая карточка для Lake Louise с 14 градусами и переменной облачностью, градиентное солнце за облаком булева объединения, ряд почасового прогноза и меньшие стеклянные карточки качества воздуха, ветра и влажности" width="100%">
  <p align="center"><sub><b>Стеклянная погода</b>: стекло и размытие фона, цветовые поля с размытием слоя, булево облако</sub></p>
</td>
<td width="33%" valign="top">
  <img src="docs/images/art-vector-marks.png" alt="Три плитки на кремовом фоне: градиентный знак горы из объединения двух вершин и вычитания солнца, узел из трёх исключённых колец с угловым градиентом и сужающаяся градиентная волна с листом и светящейся четырёхконечной звездой" width="100%">
  <p align="center"><sub><b>Векторные знаки</b>: объединение, вычитание и исключение, угловой градиент, штрих переменной ширины</sub></p>
</td>
</tr>
<tr>
<td colspan="3" valign="top">
  <img src="docs/images/art-ds-colour.png" alt="Цветовые шкалы интерфейса Ridgeline: по шесть образцов Pine greens, Sunset oranges и Slate greys, каждый подписан именем и шестнадцатеричным значением" width="100%">
  <p align="center"><sub><b>Ridgeline UI</b>: цветовые шкалы, где каждый образец — стиль заливки, выгруженный через слайс</sub></p>
</td>
</tr>
</table>

<a id="features"></a>
## Возможности

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Раскладки, которые собираются сами</h3>
      Автолейаут в обоих направлениях, с переносом и сеткой (фиксированные дорожки, hug и `fr`, ячейки, которые охватывают несколько дорожек), внутренние отступы, промежутки, выравнивание включая базовые линии текста, размеры Hug / Fill / Fixed, минимальные и максимальные размеры, абсолютное позиционирование, манипуляторы перетаскивания отступов и интервалов прямо на холсте и клавиши стрелок, которые перемещают потомков по потоку, ячейкам сетки и вложенным Frame. Ограничения и модульные сетки для всего остального.
    </td>
    <td width="50%" valign="top">
      <h3>Компоненты, которые масштабируются</h3>
      Основные компоненты, экземпляры с переопределениями, которые переживают правки, наборы компонентов с вариантами, свойства, замена экземпляра, отсоединение, сброс переопределений и переход к основному компоненту, и панель «Ресурсы» с живыми миниатюрами, поиском и перетаскиванием на холст в Frame и автолейаут. Локальные стили и переменные (цвет, число, строка, логическое) с режимами, псевдонимами и областями действия, правятся в таблице переменных и привязываются к заливкам, штрихам, эффектам, модульным сеткам и свойствам экземпляров. Заливки, штрихи, эффекты и модульные сетки меняют порядок перетаскиванием строк.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Векторы без компромиссов</h3>
      Настоящие векторные сети: инструменты «Перо» и «Карандаш», режим правки вектора с собственными инструментами (перо, которое продлевает и ветвит контуры, изгиб, заливка ведром любой замкнутой области, лассо, разрез), панель точек с зеркалированием манипуляторов и радиусом скругления у каждой точки, соединение, разделение и восстановление при удалении, конструктор фигур (щелчок или протягивание по областям пересекающихся фигур, штрихов и открытых контуров, чтобы объединить их, Alt — чтобы убрать), булевы группы (объединение, вычитание, пересечение, исключение), операнды которых остаются редактируемыми на холсте, а результат следует за каждым перетаскиванием, операция на каждый операнд, сведение, контур штриха, наконечники стрелок, пунктир, штрихи по сторонам и штрихи переменной ширины (пресеты профиля ширины и инструмент «Переменная ширина», который тянет точки ширины вдоль контура, с Alt — по одной стороне). Прямоугольники с гладкими (сквиркл) углами, многоугольники, звёзды, дуги и кольца, формируемые манипуляторами размаха, начала и отношения на холсте или полями Arc панели «Дизайн».
    </td>
    <td width="50%" valign="top">
      <h3>Заливки и эффекты</h3>
      Сплошные, линейные, радиальные, угловые и ромбовидные градиенты с манипуляторами на холсте, заливки изображением (заполнить, вписать, кадрировать, тайлом) с корректировками и пресетами, несколько заливок и штрихов, каждый режим наложения, внешние и внутренние тени (spread точно смещает контур), размытие слоя и фона (равномерное или прогрессивное), шум (моно, дуо, мульти), текстура и стекло (преломление, дисперсия, иней, свет), маски. Файлы в sRGB или Display P3, выгрузки помечены цветовым профилем файла.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Текст, который набирается красиво</h3>
      Текст правится на месте на холсте (с построчным вводом IME), смешанные стили внутри абзаца, автоширина и автовысота, интерлиньяж, межбуквенные и абзацные интервалы, оформление, регистр, списки, особенности OpenType, оси вариативных шрифтов и текстовые стили, текст справа налево и смешанного направления (арабский, иврит) по алгоритму двунаправленности Юникода, формируется HarfRust и открытыми шрифтами из craft-fonts плюс системными шрифтами.
    </td>
    <td width="50%" valign="top">
      <h3>Прототип и передача в разработку</h3>
      Связи, триггеры, действия и переходы в стиле Smart Animate, переменные с условиями (if / else if / else, собранные в редакторе взаимодействий, выражения вроде <code>count + 1</code>), потоки, режим презентации с Frame устройств, подсказками активных зон и панелью Inspect, и панель живого предварительного просмотра. Alt измеряет расстояния и отступы на холсте, режим Inspect с измерениями, аннотации в цветовых категориях, список «готово для разработки» с видом фокуса и «Сравнить изменения» (до / после с различиями на уровне свойств с тех пор, как Frame отметили готовым), и код (CSS, HTML, React, Vue, Leptos, SwiftUI, Compose, ArkUI, Flutter), где компоненты принимают свои свойства как параметры, цепочки комментариев, закреплённые за Frame (ответы, @упоминания, реакции, состояние прочтения) и именованная история версий. Выгрузите любой слой в любом масштабе в PNG, JPG, WebP, SVG или PDF.
    </td>
  </tr>
</table>

<br>

<a id="built-for-agents"></a>
## Для агентов

Каждый пункт меню, инструмент и жест запускает команду из одного реестра более чем из 400 команд. Интерфейс, CLI, канал управления JSON и сервер MCP
вызывают одни и те же команды, поэтому всё, что можно нажать, может сделать и сценарий или ИИ-агент.

```sh
# Headless: render and export
figcraft-cli render landing.figcraft -o landing.png --scale 2
figcraft-cli export landing.figcraft -o out/ --format svg

# Run a script of commands without a window
figcraft-cli run build-card.json --out card.figcraft

# Every command, with its parameters
figcraft-cli commands --filter autoLayout

# Let an agent drive it over MCP (headless, or attached to the running app)
figcraft-cli mcp
figcraft-cli mcp --attach 47800
```

Настольная программа также предлагает канал управления только на loopback (`figcraft --control <port>`) для проверки состояния интерфейса, управления инструментами событиями указателя и клавиш и снимков экрана. См. [`docs/control-protocol.md`](docs/control-protocol.md), [`docs/mcp.md`](docs/mcp.md) и [`docs/cli.md`](docs/cli.md).

<a id="under-the-hood"></a>
## Под капотом

- **Сначала движок:** модель документа из чистых данных и командный движок, сверху тонкий сменный интерфейс на egui. Слоистость проверяется при сборке по крейтам workspace (`cargo xtask layers`).
- **Постоянные данные:** документ живёт в неизменяемой упорядоченной карте, поэтому снимки отмены дёшевы, а раскладка, синхронизация компонентов и измерение текста заново обходят только то, что изменилось.
- **Свой визуализатор:** tiny-skia на каждом ядре для холста и выгрузок, со смешением слоёв, эффектами и масками; булевы операции от linesweeper, геометрия от kurbo, текст от skrifa и HarfRust.
- **Работает в браузере:** весь движок и интерфейс компилируются в WebAssembly.
- **Доступность:** программы чтения с экрана получают имена, роли, значения и состояния инструментов, строк слоёв, полей, раскрывающихся списков, вкладок и меню (AccessKit на настольной системе), F6 перемещает клавиатуру между панелью инструментов, слоями, холстом и свойствами (Tab внутри них, Escape обратно на холст), учитывается системная настройка уменьшения движения, а текст панелей соответствует контрасту WCAG AA в обеих темах.
- **Языки:** английский, русский и турецкий (проверены носителями), и черновики на испанском, французском, немецком, бразильском португальском, японском, корейском, упрощённом китайском, чешском, индонезийском, грузинском, вьетнамском и боснийском, выбираются в «Настройках» или берутся из системы или браузера и переключаются сразу; добавить язык — это один файл каталога ([`docs/translating.md`](docs/translating.md)).
- **Подключаемые модули:** изолированные подключаемые модули WebAssembly (дозированный интерпретатор на чистом Rust с пределом памяти и без доступа к файлам и сети, в том числе в браузере), которые действуют через те же команды, каждый запуск — один шаг отмены, в пределах разрешений, которые запрашивает их манифест. SDK на Rust и четыре примера модулей — в [`plugins/`](plugins); см. [`docs/plugins.md`](docs/plugins.md).
- **Живые сеансы (предпросмотр):** откройте общий доступ к открытому файлу из программы (Поделиться ▸ Начать общий доступ: онлайн через сервер или в локальной сети), дайте другим короткий код присоединения, который она показывает (или ссылку-приглашение), и правьте вместе: изменения каждого синхронизируются вживую, с курсорами, выделениями, аватарами и следованием, а отмена возвращает только ваши собственные изменения. Другие присоединяются из настольной программы (ссылки-приглашения её открывают) или из веб-сборки. См. [`docs/collab-protocol.md`](docs/collab-protocol.md).
- **Свой сервер (предпросмотр):** `figcraft-server` хранит файлы команды, публикует их из программы (Файл ▸ Опубликовать на сервере… или Поделиться ▸ Онлайн со своим сервером в «Настройках») и раздаёт ссылки и коды присоединения, по которым можно править или только смотреть; файлы переживают перезапуски, и программы подключаются там, где были. Учётных записей пока нет: доступ — это ссылки. Выпуски поставляют его для Linux, а настольная программа присоединяется по `wss://`; [размещение на арендованном сервере Linux](docs/server.md#deploy-on-a-linux-server) требует единицы systemd и Caddy или nginx (или Docker). См. [`docs/server.md`](docs/server.md).
- **Никогда не падает:** в поставляемом коде нет `unwrap`, `expect` или `panic`, это обеспечивает clippy; команды выполняются за охранником, так что ошибка валит одно действие, а не сеанс.
- **Чистая комната:** реализовано только по открытой документации и наблюдаемому поведению. Нет закрытого кода, форматов файлов, значков или изображений.

<a id="get-started"></a>
## С чего начать

```sh
git clone https://github.com/storytold/figcraft
cd figcraft
cargo run --release -p figcraft            # the desktop app
cargo run --release -p figcraft-server     # the collaboration server (docs/server.md)
cargo test --workspace                     # the test suite
cargo xtask ci                             # fmt, clippy, tests, layering and asset checks
```

Шрифты для интерфейса и инструмента «Текст» берутся из [craft-fonts](https://github.com/storytold/craft-fonts), клонированного рядом с этим репозиторием (`../craft-fonts`); без него FigCraft отступает к системным шрифтам.

```sh
git clone https://github.com/storytold/craft-fonts ../craft-fonts
```

Если вы клонируете его после первой сборки, один раз выполните `cargo clean -p figcraft-text`, чтобы следующая сборка встроила шрифты.

**Начните с шаблона.** На вкладке «Шаблоны» домашнего экрана восемь стартовых файлов (мобильное приложение, посадочная страница, панель, заготовка дизайн-системы, набор вайрфреймов, размеры постов для соцсетей, слайды презентации и заготовка набора значков), также в Файл ▸ Создать из шаблона…. Они собраны в коде из оригинального синтетического содержимого, поэтому сценарии и агенты тоже могут их открыть: `file.newFromTemplate {template}` ([`docs/mcp.md`](docs/mcp.md#starter-templates)).

Для веб-сборки установите [trunk](https://trunkrs.dev/) и выполните `cargo xtask wasm`.

Новым участникам и ИИ-агентам: начните с [`AGENTS.md`](AGENTS.md), затем [`docs/`](docs/).

Установщики для macOS (универсальные, подписанные и нотариально заверенные), Windows (x64, x86 и arm64), Linux (AppImage, `.deb`, `.rpm`, Flatpak и архив), FreeBSD и веба прилагаются к каждому [выпуску GitHub](https://github.com/storytold/figcraft/releases). Сопровождающим: [`docs/releasing.md`](docs/releasing.md) объясняет, как выпуски собираются, подписываются и публикуются.

> [!IMPORTANT]
> **Состояние:** FigCraft находится в **альфе**: по нашей собственной оценке, примерно на 49 % пути к замене закрытых инструментов в настоящей работе. Почти все отслеживаемые действия дизайна интерфейса в контрольном списке меню подключены ([`docs/parity-checklist.md`](docs/parity-checklist.md)), и основной редактор работает от начала до конца, но FigCraft открывает файлы `.fig` только по возможности, имеет лишь первый предпросмотр совместной работы (живые сеансы, размещаемые из программы или на своём сервере, с отменой для каждого человека и ссылками общего доступа для правки или только просмотра; учётных записей, команд и облака пока нет), запускает собственные подключаемые модули WebAssembly и не сверялся с настоящими дизайн-документами. Честная картина по областям — в [плане](ROADMAP.md) и [`docs/target-app-parity.md`](docs/target-app-parity.md). Ожидайте шероховатости и, пожалуйста, заводите сообщения о проблемах или расскажите, что сломалось, в [Discord](https://discord.gg/artcraft).

<a id="privacy-and-online-sharing"></a>
## Конфиденциальность и общий доступ в сети

FigCraft работает без сети: у него нет учётной записи и телеметрии, и он не обращается ни к какому серверу, пока вы
не откроете общий доступ или не присоединитесь к файлу. Живые сеансы — это **предпросмотр**. Прежде чем делиться чем-то важным,
знайте, что делает общий доступ:

- **Поделиться ▸ Онлайн загружает файл на сервер.** По умолчанию это публичный сервер
  `collab.craftapps.dev`; другой, в том числе свой, можно задать в «Настройках» (а сборка может
  поставляться без него: [`docs/releasing.md`](docs/releasing.md#the-default-server)). Файл остаётся на
  сервере после того, как вы прекратите общий доступ, пока вы его не удалите (Поделиться ▸ Дополнительно ▸ Удалить с сервера…)
  или пока его никто не открывал 30 дней — тогда публичный сервер его удаляет.
- **Это не сквозное шифрование.** Соединение с сервером зашифровано (TLS), но
  сервер хранит файл незашифрованным, и тот, кто им управляет, может его прочитать. Не делитесь
  конфиденциальной работой через сервер, которому не доверяете; запустите свой
  ([`docs/server.md`](docs/server.md)) или делитесь в локальной сети.
- **Код или ссылка — это доступ.** Учётных записей нет: у кого есть код или ссылка для правки,
  тот может открыть и изменить файл, у кого код или ссылка для просмотра — может его открыть. Прекращение общего доступа отзывает
  их и отключает всех остальных.
- **Поделиться ▸ Локальная сеть сервера не использует**, но тоже не шифруется: ваша программа размещает
  сеанс, а другие подключаются к ней напрямую, поэтому используйте это в сетях, которым доверяете.
- **Без гарантий.** Публичный сервер предлагается как есть, без резервных копий и обещаний доступности, и
  файлы на нём могут быть удалены. Храните собственную сохранённую копию всего, чем делитесь.

Условия сервера по умолчанию — в [`docs/online-sharing-terms.md`](docs/online-sharing-terms.md).

<a id="the-crafting-apps"></a>
## The Crafting Apps

FigCraft — одно из приложений **Crafting Apps**: бесплатные творческие инструменты с открытым исходным кодом от команды
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

Приложения Crafting Apps разделяют одни и те же соглашения: чистая комната и чистый Rust, нативно в macOS, Windows, Linux и FreeBSD, в браузере через WebAssembly, и полностью управляемые агентами.

<br>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<h3 align="center">Приходите творить с нами</h3>

<p align="center">
  Наш Discord — место, где собираются те, кто что-то создаёт: дизайнеры, которые набрасывают своё первое приложение,
  разработчики, которым просто нужно, чтобы кнопка выглядела правильно, иллюстраторы, кинематографисты, любители шрифтов и
  немало тех, кто ещё выясняет, что им нравится создавать. Покажите, что собираете, попросите
  помощи, расскажите, что сломано или что вы хотите, чтобы FigCraft умел. Вам здесь рады.
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><b>discord.gg/artcraft</b></a> ·
  <a href="https://getartcraft.com/">getartcraft.com</a> ·
  <a href="https://getartcraft.com/apps">The Crafting Apps</a> ·
  <a href="https://getartcraft.com/apps/figcraft">FigCraft</a>
</p>

---

<a id="license-and-credits"></a>
## Лицензия и благодарности

FigCraft распространяется на условиях двойной лицензии [MIT](LICENSE-MIT) или [Apache-2.0](LICENSE-APACHE), на ваш выбор.
Copyright (c) 2026 ArtCraft Team and the FigCraft contributors. Обязательные уведомления — в [NOTICE](NOTICE).

Каждый значок в FigCraft нарисован в коде или сделан для этого проекта, а встроенные шрифты, изображения и прочие
ресурсы сохраняют свои открытые лицензии; каждый указан с автором, источником и лицензией в
[ATTRIBUTION.md](ATTRIBUTION.md).

Имя, словесный знак и логотипы ArtCraft в [`docs/brand/`](docs/brand/) являются товарными знаками
ArtCraft Team и не покрываются этой лицензией. Их можно использовать только без изменений и только как
часть этого репозитория и FigCraft, на условиях [`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt).
Форки и изменённые версии должны их удалить.

<p align="center">
  <a href="https://getartcraft.com/"><img alt="ArtCraft" src="https://raw.githubusercontent.com/storytold/vectorcraft/main/docs/brand/artcraft-mark.png" width="28"></a><br>
  <sub>Сделано командой и сообществом <a href="https://getartcraft.com/">ArtCraft</a>.</sub>
</p>

<a id="star-history"></a>
## История звёзд

[![Star History Chart](https://api.star-history.com/svg?repos=storytold/figcraft&type=Date&legend=top-left)](https://www.star-history.com/?repos=storytold%2Ffigcraft&type=date&legend=top-left)
