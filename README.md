# Limbaje Formale si Automate(LFA)

## DFA

1. Labirintul este un DFA (Automat Finit Determinist) definit în fișierul `DFA.txt`:
    - **Stări (STATES):** `ENTRANCE`, `HALLWAY`, `KITCHEN`, `SECRET_ROOM`, `LIBRARY`, `EXIT`
    - **Simboluri (SIGMA):** `UP`, `DOWN`, `LEFT`, `RIGHT`, `PICK`, `DROP`
    - **Tranziții (RULES):**
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
    - **Stare Inițială (Start):** `ENTRANCE`
    - **Stări Finale (Stop):** `EXIT`

### Harta Labirintului
                      SECRET_ROOM
                          |
           KITCHEN----    HALL    ---- LIBRARY
                          |            |
                          |           EXIT
                          |
                      ENTRANCE

### Reguli de Joc
- Folosește comenzile de mișcare (`UP`, `DOWN`, `LEFT`, `RIGHT`) pentru a naviga
- Comanda `PICK` ia lingura (doar în `KITCHEN`)
- Comanda `DROP` lasă lingura
- Poți ieși doar prin `LIBRARY` -> `EXIT` dacă ai lingura

> **Note:** Ieșirea (`EXIT`) este accesibilă doar dacă ai colectat lingura din bucătărie!
## NFA
