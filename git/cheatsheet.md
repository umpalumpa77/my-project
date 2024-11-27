# Проверка коммитов

```bash
git log
```

# Проверка статусов файлов

```bash
git status
```

# Добавить файл в отслеживание состояние для будущего коммита 
 
```bash
git add name_of_file
```

# Создание коммита 

```bash
git commit -m "Message of my commit"
```
# Отправка ветки main локального репозитория на удалённый сервер origin 

```bash
git push origin main
```

## как проверить какие ветки существуют в текущем репозитории 

```bash
git branch
```

##   Как создать новую ветку

```bash
git branch new_branch
```

## Как поменять ветку 

```bash
git checkout new_branch
```



## Установка и настройка

```bash
git --version # Проверяем сть ли git и смотрим его версию
git config --global user.name "your name" # настроить имя пользователя 
git config --global user.email "your Email" #настроить почту пользователя
git config --list # проверить ьекщие настройки git
```

## Работа с репозиториями 

```bash
git init #создать пустой репозиторий в текущей папке для дальнейшего отслеживания
git clone URL # скопировать .git репозиторий по ссылке URL
# Ссылка обычно представляет из себя
```