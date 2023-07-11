# course_4
<h1>Курсовая работа №4 (парсинг вакансий)</h1>
<h2>Для курса Python разработчик от SkyPro</h2>
Автор: Александра Соловьёва
<h3>Классы для работы с API:</h3>
<h4>Базовый абстрактный класс: Api</h4>
Методы класса:<br/>
<b> - get_info(self, keyword) </b><br/>
    Возвращает "сырую" информацию о вакансиях с API с поиском по keyword в виде списка словарей<br/><br/>
<b> - output_info(self, keyword) </b><br/>
    Возвращает информацию о вакансиях с API с поиском по keyword в формате:<br/>
        <i>id</i>: id вакансии. Целочисленный <br/>
        <i>name</i>: название вакансии <br/>
        <i>link</i>: ссылка на вакансию <br/>
        <i>salary</i>: зарплата. Словарь с ключами 'to' and 'from' <br/>
        <i>description</i>: Описание вакансии <br/>
        <i>date_published</i>: Дата публикации в виде строки <br/>
в виде списка словарей
<h4>Класс HeadHunter</h4>
Работает с API сайта headhunter.ru
<h4>Класс SuperJob</h4>
Работает с API сайта superjob.ru<br/>
Для работы необходима ключ в переменной окружения SJ_KEY,<br/>
либо прописать ключ в файле api_key.py
<h3>Класс для работы с вакансиями</h3>
<h4>Класс Description</h4>
Поля класса:<br/>
        <i>id</i>: id вакансии. Целочисленный <br/>
        <i>name</i>: название вакансии <br/>
        <i>link</i>: ссылка на вакансию <br/>
        <i>salary</i>: зарплата. Словарь с ключами 'to' and 'from' <br/>
        <i>description</i>: Описание вакансии <br/>
        <i>date_published</i>: Дата публикации в виде строки <br/><br/>
Класс поддерживает сравнения.
Сравнения производятся по минимальной зарплате salary['from'].<br/>
Экземпляры с отсутвующей мин зарплате считаются наименьшими.<br/>

Методы класса (статические):<br/>
 <b>- filter_with_salary(self, vacancies)</b>
    Принимает список эксземпляров собственного класса.<br/>
    Возвращает список вакансий, где присутсвует минимальная зарплата<br/><br/>
<b>- sort_by_salary(descriptions)</b>
    Принимает список эксземпляров собственного класса.<br/> 
    Возвращает список экземпляров, отсортированных по минимальной зарплате (по убыванию)<br/><br/>
<b>- sort_by_date(descriptions)</b>
    Принимает список эксземпляров собственного класса.<br/>
    Возвращает список экземпляров, отсортированных по дате публикации (по убыванию)<br/><br/>
<h3>Класс для работы с файлами</h3>
<h4>Базовый абстрактный класс: Saver</h4>
При инициализации принимает необязательный параметр <i>path</i> - путь к файлу<br/>
Методы класса:<br/>
<b>- read_datafile(self)</b><br/>
    Метод для чтения файла.<br/>
    Возвращает список словарей с данными о вакансии, 
    в формате класса Description<br/>
    Если файл пустой или отсутствует - возвращает пустой список.<br/><br/>
<b>- add_description(self, vacancies)</b><br/>
    Добавляет вакансии в файл.<br/>
    Принимает список экземпляров или экземпляр класса Description<br/><br/>
<b>- delete_description(self, vacancy)</b><br/>
    Удаляет вакансию из файла.<br/>
    Принимает на вход экземпляр класса Description<br/><br>
<b>- get_by_keywords(self, keywords)</b><br/>
    Возвращает список вакансий, содержащих ВСЕ ключевые слова<br/>
    Принимает на вход строку ключевых слов, разделённых пробелами<br/>
    Формат возврата: список словарей
<h4>Класс JsonSaver</h4>
    Класс для работы с файлами формата json

