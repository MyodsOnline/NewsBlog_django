# NewsBlog_django
Consist of two parts: one of them is FinFax_2.  
Here is some explanation: [link to google.docs](https://docs.google.com/document/d/11BdJcA0ygOtYN9qwPmDViYD8HPmAdCYOSjYUj9aHjOw/edit?usp=sharing).

Finfax_2 via NewsBlog  
Есть процесс взаимодействия с диспетчерами Fingrid, организованный в настоящее время неоптимальным образом. Взаимодействие происходит посредством емэйл сообщений со вложенными файлами. Организованная база данных отсутствует, хронология ведётся в отдельном файле.
В целях упорядочивания процесса предлагается внедрить в работу интерфейс отправки и хранения емэйл сообщений с Fingrid.
Интерфейс главного окна представляет собой блок с формой создания и отправки сообщения и блок с базой данных отправленных сообщений.
Атрибуты формы отправки сообщения:
- Номер сообщения (обязательный атрибут)
- Дата сообщения (обязательный атрибут)
- Время сообщения (обязательный атрибут)
- Текст сообщения (необязательный атрибут)
- Файл сообщения (необязательный атрибут)
- Автор сообщения (обязательный атрибут)
- Адрес получателя???
- Кнопка «Сохранить и отправить»

Блок архива сообщений — репликация базы данных по заданным полям в хронологическом порядке.
Поле «номер» является ссылкой на индивидуальную форму сообщения с выводом подробной информации о сообщении + дополнительное поле ‘is_ok’ (необязательный атрибут) — фиксируется диспетчером, если получен утвердительный ответ + рассмотреть целесообразность внесения поля «incoming» для фиксации входящих сообщений.
