# Django Layihəsi - Laboratoriya №3

Bu layihə Django framework istifadə edərək yaradılmış sadə statik veb səhifə nümunəsidir.

## Layihənin Tərkibi

### 2. Quraşdırma

Layihə aşağıdakı komponentləri əhatə edir:
- Python 3.11
- Django 5.2.8
- Virtual environment (venv)

### 4. Sadə bir statik veb səhifənin hazırlanması

Layihədə aşağıdakı fayllar yaradılıb:
- `myapp/templates/index.html` - HTML şablon faylı
- `myapp/views.py` - View funksiyası
- `myapp/urls.py` - URL konfiqurasiyası
- `myproject/urls.py` - Əsas URL konfiqurasiyası

## Quraşdırma və İstifadə

### 1. Virtual environment aktivləşdirmək

```bash
cd django_layihe
source venv/bin/activate
```

### 2. Layihəni işə salmaq

```bash
python manage.py runserver
```

### 3. Brauzerə keçid

Brauzerdə aşağıdakı ünvana daxil olun:
```
http://127.0.0.1:8000/
```

## Layihə Strukturu

```
django_layihe/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── index.html
└── venv/
```

## Əsas Konseptlər

### Model-View-Template (MVT)
- **Model**: Məlumat bazası strukturu (bu layihədə istifadə olunmayıb)
- **View**: views.py faylında index funksiyası
- **Template**: templates/index.html faylı

### URL Konfiqurasiyası
- Əsas URL konfiqurasiyası: `myproject/urls.py`
- Tətbiq URL konfiqurasiyası: `myapp/urls.py`

## Qeydlər

- Bu layihə təlim məqsədləri üçün hazırlanıb
- Production mühitində istifadə üçün əlavə təhlükəsizlik tədbirləri tələb olunur
- SECRET_KEY və DEBUG parametrləri production üçün dəyişdirilməlidir
