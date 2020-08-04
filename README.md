# Тестовое задание на позицию Python Programmer

[Задача](#task)
[Параметры](#param)
[Описание задачи](#desc)
[Сроки и формат сдачи тестового задания](#format)


## <a name=task>Задача</a>
Анализ репозитория GitHub.

## <a name=param>Параметры</a>
- URL публичного репозитория на github.com.  
- Дата начала анализа. Если пустая, то неограничено.  
- Дата окончания анализа. Если пустая, то неограничено.  
- Ветка репозитория. По умолчанию - master.  
- Параметры должны передаваться в скрипт через командную строку  

## <a name=desc>Описание задачи</a>
Провести анализ репозитория, используя [REST API GitHub](https://developer.github.com/v3/). Результаты анализа
выводятся в stdout. Необходимо вывести такие результаты:
- Самые активные участники. Таблица из 2 столбцов: login автора, количество его
коммитов. Таблица отсортирована по количеству коммитов по убыванию. Не
более 30 строк. Анализ производится на заданном периоде времени и заданной
ветке.
- Количество открытых и закрытых pull requests на заданном периоде времени по
дате создания PR и заданной ветке, являющейся базовой для этого PR. [Примеры](https://github.com/fastlane/fastlane/pulls)
- Количество “старых” pull requests на заданном периоде времени по дате создания
PR и заданной ветке, являющейся базовой для этого PR. Pull request считается
старым, если он не закрывается в течение 30 дней и до сих пор открыт.
- Количество открытых и закрытых issues на заданном периоде времени по дате
создания issue. [Примеры](https://github.com/fastlane/fastlane/issues)
- Количество “старых” issues на заданном периоде времени по дате создания issue.
Issue считается старым, если он не закрывается в течение 14 дней.

Нужно постараться сделать максимально надежный, отказоустойчивый скрипт, в том
числе с учетом ограничений API на кол-во запросов

Допустим, что данный скрипт необходимо выполнять регулярно. В пояснительной
записке предложите вариант реализации CI/CD для подобного сервиса.

## <a name=format>Сроки и формат сдачи тестового задания</a>
В качестве результата нужно прислать исполняемый код программы. Разрешается
использовать только стандартную библиотеку python, исключение может быть сделано
только для библиотеки requests, ее использовать можно.

Выполненное тестовое задание вы можете прислать на почту рекрутеру, выдавшему
вам тестовое задание. Название документа должно начинаться с вашего имени и
фамилии.

По срокам выполнения тестового задания мы вас не ограничиваем — вы можете
прислать его, когда будете полностью в нем уверены. Как правило, кандидаты
справляются с ним за одну рабочую неделю. После завершения работы над заданием,
пожалуйста, напишите нам, сколько времени вы потратили на него

Перед тем, как приступить к выполнению тестового задания, пожалуйста, обратите ваше
внимание на то, что оно <u>не является оплачиваемым</u>. Также, предоставляя результат
вашего тестового задания, вы принимаете тот факт, что ООО “Плейрикс” может в
настоящее время и/или в будущем разрабатывать внутри компании или получать от
третьих лиц идеи и другие материалы, похожие по содержанию на присланные вами, но
ни в коем случае не основанные на них.


Мы еще раз благодарим вас за интерес к нашей компании и желаем удачи с
выполнением тестового задания! Очень надеемся, оно покажется вам интересным :)

E-mail:
[job@playrix.com](job@playrix.com)

Сайт о работе в Playrix:
[job.playrix.com](https://job.playrix.com/)

Бонусы за рекомендации:
[job.playrix.com/open-positions/references/](https://job.playrix.com/open-positions/references/)
