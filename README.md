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
           KITCHEN----    HALL    ---- LIBRARY
                          |            |
                          |           EXIT
                          |
                      ENTRANCE

### Reguli de Joc
- Foloseste comenzile de miscare (`UP`, `DOWN`, `LEFT`, `RIGHT`) pentru a naviga
- Comanda `PICK` ia lingura (doar în `KITCHEN`)
- Comanda `DROP` lasa lingura
- Poti iesi doar prin `LIBRARY` -> `EXIT` daca ai lingura

> **Note:** Iesirea (`EXIT`) este accesibila doar daca ai colectat lingura din bucatarie!
## NFA
