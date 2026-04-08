# Menedżer Haseł

## Instalacja i uruchomienie

1. **Sklonuj repozytorium:**
   ```bash
   git clone <url-repozytorium>
   cd menadzer_hasel
   ```

2. **Utwórz wirtualne środowisko:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. **Zainstaluj zależności:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Uruchom migracje bazy danych:**
   ```bash
   python manage.py migrate
   ```

5. **Utwórz superużytkownika:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Uruchom serwer deweloperski:**
   ```bash
   python manage.py runserver
   ```

## Użycie

1. Zarejestruj nowe konto przez panel admina lub zaloguj się istniejącym
2. Dodawaj nowe hasła przez panel administratora Django (`/admin/`)
3. Przeglądaj swoje hasła na stronie głównej

## gitignore
- **baza danych i srodowisko venv** sa w gitignore