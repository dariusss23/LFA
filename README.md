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

1. Automatul este un NFA (Automat Finit Nedeterminist) definit în fișierul `NFA.txt`:
    - **Stări (STATES):** `q0`, `q1`, `q2`, `q3`, `q4`, `q5`
    - **Simboluri (SIGMA):** `0`, `EPSILON`
    - **Tranziții (RULES):**
        ```
        q0 --0--> q1
        q0 --EPSILON--> q2
        q1 --0--> q0
        q2 --0--> q3
        q3 --0--> q4
        q4 --0--> q5
        q5 --0--> q2
        ```
    - **Stare Inițială (Start):** `q0`
    - **Stări Finale (Stop):** `q0`, `q5`

### Funcționare:
- Acceptă șiruri de forma `0^k` unde k este multiplu de 2 sau 3
- Calea pentru multipli de 2: `q0 -> q1 -> q0`
- Calea pentru multipli de 3: `q0 -> q2 -> q3 -> q4 -> q5 -> q2 -> ... -> q5`

### Exemple:
- `00` (k=2): ✅ Acceptat
- `000` (k=3): ✅ Acceptat
- `0000` (k=4): ✅ Acceptat (2×2)
- `00000` (k=5): ❌ Respins
- `000000` (k=6): ✅ Acceptat (2×3)

### Diagramă:
