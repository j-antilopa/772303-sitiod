### Quick start

1) Установите __Docker__ и надстройку __docker-compose__:
    * [Install Docker][1]
    * [Install Docker Compose][2]
2) Запустите команду:
    ```bash
    docker-compose up
    ```
3) Перейдите по ссылке, указанной в консоли. (Похожей на эту: http://127.0.0.1:8888/?token=<some_token>)

[1]: https://docs.docker.com/install/linux/docker-ce/
[2]: https://docs.docker.com/compose/install/

### Video

[Google Drive](https://drive.google.com/open?id=1r2gnmqBSGJvwFQGI8LmUwCFF76Nyw4qX)

### Lab 5

[Отчёт](https://drive.google.com/open?id=10QIBfKIZxDNHtw19GYbmruI1KBKQR-T5)

Что такое дисперсия?
> _Дисперсия - это степень отколнения значений переменной от среднего значения. 
> В программе считалась с помощью функции `numpy.var()`_

С помощью какой функции генерировали последовательность равнораспределённых в интервале чисел?
> _С помощью функции `numpy.linspace(start=, end=, num=)`. 
> Где в параметрах `start` и `end` задаются начало и конец интервала соответсвенно, 
> а параметром `num` задаётся длина последовательности._

### Lab 6

[Отчёт](https://drive.google.com/open?id=1I3tKWcJe353XKVMLiMejY5j9CWqfIUQ2)

Зачем нужна визуализация данных?
> _Для удобного восприятия информации._

С помощью какой функции был построен график?
> _С помщью функции `matplotlib.pyplot.plot(x, y)`, где в параметры `x` и `y` передаются массивы значений 
> для каждой оси._

### Lab 7

[Отчёт](https://drive.google.com/open?id=1CKZrU1wZlDLY7v3iYt9-ZxMoHWq4Tpbf)

Что такое линейная регрессия?
> _Линейная регрессия - это модель зависимости переменной x от одной или нескольких других переменных 
> с линейной функцией зависимости._

Что такое коэффициент корреляции?
> _Коэффициент корреляции - это статистический показатель зависимости двух переменных. 
> Может принимать значения от -1 до 1._

Что показывает `intercept` ?
> _`intercept` показывает предполагаемое значение `y` при `x=0`._

Что показывает `slope` ?
> _`slope` - это величина на которую изменится предполагаемое значение `y` при изменении `x` на 1._

### Lab 8

[Отчёт](https://drive.google.com/open?id=1J5C1znZWrp6YOAx5hHntVFU5WjxPzXGF)

Что такое документно-ориентированная БД? 
> _Документно-ориентированная БД – это тип нереляционных баз данных, предназначенный для хранения и запроса данных 
> в виде документов в формате, подобном JSON. Это позволяют хранить и запрашивать данные в БД с помощью той же 
> документной модели, которая используются в коде программы. Каждая запись при этом может иметь различную структуру._

Что такое Map-Reduce в MongoDb?
> _Map-Reduce - это способ агрегации данных в ходе которого программист определяет `map` и `reduce` функции на 
> языке JavaScript, а Mongo управляет их вызовом. Сначала к каждой записи применяется функция `map`, 
> которая формирует пары ключ-значение. Далее эти пары (сгруппированные по ключу) передаётся в `reduce`, 
> где формируется одна пара ключ-значение._

В чём преимущество Map-Reduce?
> _Возможность параллельной обработке данных, а также высокая производительность._