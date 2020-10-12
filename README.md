# **Приложение для изучения английских слов**

  Данное приложение служит для изучения английских слов на примерах. Слова разделены на категории, темы и уровни, присутствует транскрипция слов. Есть возможность для пользователя добавлять новые слова, администратор может добавлять и удалять пользователей.
	
  Для запуска приложения введите в командной строке python mange.py runsfcgi.  Необходимо, чтобы в системе были установлены python и nginx.
	
  Чтобы войти в программу с правами администратора, нужно перейти по адресу  и ввести логин и пароль. Логин   admin. Пароль  123.

## В программе присутствуют два класса один из них – User, описывает пользователя, второй - Word , слова.

### Класс User обладает полями: name и email.

1.name – имя пользователя.

2.email – email пользователя.

### Класс Word обладает полями: title, category, level, theme, stw, example, transcription и user.

1.title – само слово.

2.category – категория слова 

3.level – уровень слова. 

4.theme – тема слова. 

5.stw – набор слова. 

6.example – пример использования слова. 

7.transcription – транскрипция слова. 

8.user – имя пользователя добавившего слово. 

Присутствуют конфигурационные файлы для сервера nginx.