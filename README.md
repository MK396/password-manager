# Menedżer Haseł

## Instalacja i uruchomienie

1. **Sklonuj repozytorium:**
   ```bash
   git clone <url-repozytorium>
   cd menadzer_hasel
   ```

2. **Utwórz wirtualne środowisko:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. **Zainstaluj zależności:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Utwórz plik .env i dodaj klucz django**
   ```bash
   DJANGO_SECRET_KEY='twoj-klucz'
   ```

5. **Uruchom migracje bazy danych:**
   ```bash
   python manage.py migrate
   ```

6. **Utwórz superużytkownika:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Uruchom serwer deweloperski:**
   ```bash
   python manage.py runserver
   ```

## Użycie

1. Zarejestruj nowe konto przez panel admina lub zaloguj się istniejącym
2. Dodawaj nowe hasła przez formularz (mozna wybrac tryb jawny i szyfrowany)
3. Przeglądaj swoje hasła na stronie głównej
4. Przez panel admina (/admin) można sprawdzić czy haslo uzytkownika zostało zaszyfrowane w bazie