# Limbaje Formale si Automate(LFA)

## DFA

1. Labirintul este un DFA (Automat Finit Determinist) definit In fiSierul `DFA.txt`:
    - **StAri (STATES):** `ENTRANCE`, `HALLWAY`, `KITCHEN`, `SECRET_ROOM`, `LIBRARY`, `EXIT`
    - **Simboluri (SIGMA):** `UP`, `DOWN`, `LEFT`, `RIGHT`, `PICK`, `DROP`
    - **TranziTii (RULES):**
        ```
        ENTRANCE    ----UP---->    HALLWAY
        HALLWAY     ---DOWN--->    ENTRANCE
        HALLWAY     ---LEFT--->    KITCHEN
        HALLWAY     ----UP---->    SECRET_ROOM
        HALLWAY     ---RIGHT--->   LIBRARY
        KITCHEN     ---RIGHT--->   HALLWAY
        SECRET_ROOM ---DOWN--->    HALLWAY
        LIBRARY     ---LEFT--->    HALLWAY
        LIBRARY     ---DOWN--->    EXIT
        ```
    - **Stare IniTialA (Start):** `ENTRANCE`
    - **Stari Finale (Stop):** `EXIT`

### Harta Labirintului
                      SECRET_ROOM
                          |
         KITCHEN  ----   HALL    ----  LIBRARY
                          |              |
                          |             EXIT
                          |
                       ENTRANCE

### Reguli de Joc
- Foloseste comenzile de miscare (`UP`, `DOWN`, `LEFT`, `RIGHT`) pentru a naviga
- Comanda `PICK` ia lingura (doar în `KITCHEN`)
- Comanda `DROP` lasa lingura
- Poti iesi doar prin `LIBRARY` -> `EXIT` daca ai lingura

> **Note:** Iesirea (`EXIT`) este accesibila doar daca ai colectat lingura din bucatarie!

## NFA

1. Automatul este un NFA (Automat Finit Nedeterminist) definit in fisierul `NFA.txt`:
    - **Stari (STATES):** `q0`, `q1`, `q2`, `q3`, `q4`, `q5`
    - **Simboluri (SIGMA):** `0`, `EPSILON`
    - **Tranzitii (RULES):**
        ```
        q0 --EPSILON--> q1
        q0 --EPSILON--> q3
        q1 --0--> q2
        q2 --0--> q1
        q3 --0--> q4
        q4 --0--> q5
        q5 --0--> q3
        ```
    - **Stare Initiala (Start):** `q0`
    - **Stari Finale (Stop):** `q1`, `q3`

### Functionalitate:
- Accepta siruri de forma `0^k` unde k este multiplu de 2 sau 3
- Calea pentru multipli de 2: `q0 -> q1 -> q2 -> q1`
- Calea pentru multipli de 3: `q0 -> q3 -> q4 -> q5 -> q3`

### Exemple:
- `0` (k=1): ❌ Respins
- `00` (k=2): ✅ Acceptat
- `000` (k=3): ✅ Acceptat
- `0000` (k=4): ✅ Acceptat
- `00000` (k=5): ❌ Respins
- `000000` (k=6): ✅ Acceptat


## PDA

1. Automatul este un PDA (Pushdown Automaton) definit in fisierul `PDA.txt`:
    - **Stari (STATES):** `q1`, `q2`, `q3`, `q4`
    - **Simboluri de intrare (SIGMA):** `0`, `1`
    - **Simboluri de stiva (GAMMA):** `0`, `$`
    - **Tranzitii (RULES):**
        ```
        q1 --EPSILON,EPSILON/$--> q2
        q2 --0,EPSILON/0--> q2
        q2 --1,0/EPSILON--> q3
        q3 --1,0/EPSILON--> q3
        q3 --EPSILON,$/EPSILON--> q4
        ```
    - **Stare Initiala (Start):** `q1`
    - **Stari Finale (Stop):** `q4`

### Functionalitate:
- Accepta siruri de forma `0^n1^n` (n ≥ 1)
- Pune pe stiva $ la inceput
- Adauga 0 pe stiva pentru fiecare 0 citit
- Scoate 0 din stiva pentru fiecare 1 citit
- Accepta cand stiva revine la $

### Exemple:
- `01`: ✅ Acceptat
- `0011`: ✅ Acceptat
- `000111`: ✅ Acceptat
- `1`: ❌ Respins
- `011`: ❌ Respins
- `001`: ❌ Respins
- `0110`: ❌ Respins
- `0101`: ❌ Respins
