# Menedżer Haseł

### Wykonane
* **Szyfrowanie przed wysłaniem na serwer:** Szyfrowanie haseł w przeglądarce przed ich wysłaniem do bazy danych. Serwer przechowuje jedynie zaszyfrowane dane (AES-256).
* **Klucz szyfrujący:** Klucz kryptograficznygenerowany jest za pomocą algorytmu **PBKDF2** (10,000 iteracji) bezpośrednio w procesie logowania.
* **Bezpieczna pamięć sesji:** Klucze są przechowywane wyłącznie w `sessionStorage`, co gwarantuje, że znikają one bezpowrotnie po zamknięciu karty przeglądarki.

* **Bezpieczny podgląd:** "Zobacz/Ukryj" z maskowaniem (`-webkit-text-security`), chroniącą przed podglądaniem haseł z ekranu.
* **Auto-Logout Guard:** Mechanizm automatycznego wylogowania sesji Django w przypadku wykrycia braku klucza kryptograficznego (np. po ponownym otwarciu karty).

* **Zabezpieczenie sesji:** Parametry `SESSION_EXPIRE_AT_BROWSER_CLOSE` oraz `SESSION_COOKIE_HTTPONLY`, aby zminimalizować ryzyko kradzieży sesji.

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

1. Załóż konto
2. Podczas logowania JS wygeneruje unikalny klucz AES i zapisze go w sessionStorage.
3. Dodaj haslo, zostanie przeslane do backendu juz zaszyfrowane
4. Przez panel admina (/admin) można sprawdzić czy haslo uzytkownika zostało zaszyfrowane w bazie
5. zamykanie karty przegladarki wymusza ponowne zalogowanie