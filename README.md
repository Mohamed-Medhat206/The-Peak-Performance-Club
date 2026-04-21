# 🏋️ Gym Management System (Django)

A Django-based backend system designed to manage gym operations such as members, trainers, classes, equipment, and business logic like discounts and trending workouts.

---

## 🚀 Project Setup

### 1. Clone the repository

```bash
git clone <git@github.com:Mohamed-Medhat206/The-Peak-Performance-Club.git>
cd <The-Peak-Performance-Club>
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run server

```bash
python manage.py runserver
```

### 7. Open admin panel

```
http://127.0.0.1:8000/admin/
```

---

## 🧠 Django Concepts Used

### 1. Abstract Base Model

* Implemented using `baseModel`
* Contains:

  * `created_at`
  * `updated_at`
* Reused across all models to avoid duplication

---

### 2. Model Relationships

* **ForeignKey**

  * `GymClass → Trainer`
  * `Equipment → Branch`

* **ManyToManyField**

  * `GymClass ↔ Member`

---

### 3. Computed Property

* `Member.is_vip`

```python
@property
def is_vip(self):
    return self.balance > 1000
```

* Determines if a member is VIP dynamically

---

### 4. Business Logic Method

* `GymClass.calculate_discount()`

```python
def calculate_discount(self):
    if self.start_date > (timezone.now().date() + timezone.timedelta(days=30)):
        return self.base_price * 0.8
    return self.base_price
```

* Implements **Early Bird Discount**
* Applies 20% discount if class is scheduled **more than 30 days ahead**

---

### 5. Custom QuerySet & Manager (Trending Workouts)

#### QuerySet:

```python
class TrindingQuerySet(models.QuerySet):
    def trinding(self):
        return self.annotate(
            members_count=Count('members')
        ).filter(members_count__gt=15)
```

#### Manager:

```python
class TrindingManager(models.Manager):
    def get_queryset(self):
        return TrindingQuerySet(self.model, using=self._db)

    def trinding(self):
        return self.get_queryset().trinding()
```

#### Usage:

```python
GymClass.objects.trinding()
```

* Returns classes with **more than 15 members**
* Powers the **"Trending Workouts"** feature

---

### 6. Proxy Model

```python
class DamagedEquipments(Equipment):
    class Meta:
        proxy = True
```

* Used to represent **damaged equipment**
* Allows different admin behavior without creating a new table

---

## 🧪 Testing Features

### Admin Panel

* Add Members, Trainers, and Gym Classes
* Assign members to classes
* Verify:

  * Discount calculation
  * Trending classes (via member count)

---

### Django Shell

```bash
python manage.py shell
```

Example:

```python
GymClass.objects.trinding()
```

---

## 🎯 Summary

This project demonstrates:

* Clean model design using abstraction
* Advanced querying using QuerySet & Manager
* Encapsulation of business logic inside models
* Practical use of Django admin for testing and validation

---

## 👨‍💻 Author

Mohamed Medhat
