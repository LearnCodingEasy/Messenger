# Messenger

Messenger

## 📦 Django

- 🚀 Activate Virtual Environment 🔋

```cmd
messenger_virtual_environment\Scripts\activate
```

- Go To

```cmd
cd messenger_django
```

- Modifications To Models File

```cmd
python manage.py makemigrations
```

- Modifications To The Database

```cmd
python manage.py migrate
```

- Run Project

```cmd
python manage.py runserver
```

### 🖥️ Vue

- Go To

```cmd
cd messenger_vue
```

```cmd
npm run dev
```

```cmd
npm run build
```

### 🖥️ Vue Press

- Go To

```cmd
cd messenger_vuepress
```

```cmd
npm run docs:dev
```

# ************\_\_\_************

###### 📝 Create File Gitignore

```
.gitignore
```

###### 🖊️ Write Inside File

```
node_modules/
```

###### 📋 Review changes and formulate change action 📋 مراجعة التغييرات وصياغة إجراء التغيير

```cmd
git status
```

###### 📂 Add all new and changed files to the Staging Area. 📂 أضف كل الملفات الجديدة والمغير إلى منطقة التدريج.

```
git add *
```

###### 💾 This command sends the file from the Staging Area to the Local Repo. 💾 يرسل هذا الأمر الملف من منطقة التدريج إلى الريبو المحلي.

```cmd
git commit -m "Commit Explain Code"
```

###### 🌐 This command sends files from (Local Repo) to (Remote Repo). 🌐 يرسل هذا الأمر ملفات من (repo المحلي) إلى (ريبو عن بعد).

```cmd
git push origin main
```
