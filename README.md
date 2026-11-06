# Compilation

Dépôt regroupant les TP et projets de la matière **Compilation**, réalisés en binôme
en **L3 Informatique** (Université de Limoges). Les programmes sont écrits en **Python**.

## Sommaire

| TP | Thème | Dossier | Statut |
|----|-------|---------|--------|
| TP1 | Analyse lexicale, automates finis, analyseur lexical | [`TP1_Compilation/`](TP1_Compilation/) | Terminé |
| TP2 | À venir | | À venir |

## Organisation du dépôt

Un dossier par TP, contenant le code et le rapport correspondant :

```
Compilation/
├── README.md
└── TP1_Compilation/
    ├── analyseur_lexical.py
    └── rapport_TP1_compilation.pdf
```

---

## TP1 – Analyse lexicale et automates

**Objectif :** comprendre le rôle de l'analyse lexicale, construire des automates finis
pour reconnaître les différents types de lexèmes, puis les assembler en un analyseur lexical.

### Partie 1 : Compréhension de l'analyse lexicale
Notion de lexème et de token, et identification des lexèmes d'un exemple d'instructions.

### Partie 2 : Construction des automates
Pour chaque catégorie : états, état initial et final, graphe de transition et table de transition.
Les automates sont vérifiés sur des exemples (mots acceptés et refusés).

### Partie 3 : Automates en Python
Un automate par catégorie de lexème :
- **Identificateur** : une lettre suivie de lettres ou de chiffres
- **Nombre entier** : un ou plusieurs chiffres
- **Opérateur** : `+`, `-`, `*`, `/`
- **Affectation** : `=`
- **Séparateur** : `(`, `)`, `;`

### Partie 4 : Analyseur lexical
Découpe une chaîne en lexèmes et affiche, pour chacun, son token
(`IDENTIFICATEUR`, `NOMBRE`, `OPERATEUR`, `AFFECTATION`, `SEPARATEUR`)
ou `ERREUR LEXICALE` si le lexème n'est reconnu par aucun automate.

Exemple : `x = 25 + somme2;`

### Utilisation

```bash
cd TP1_Compilation
python3 analyseur_lexical.py
```

Le programme exécute les tests des automates, puis plusieurs analyses d'exemples
(dont des cas d'erreur lexicale).

### Rapport

Le rapport complet est disponible dans
[`TP1_Compilation/rapport_TP1_compilation.pdf`](TP1_Compilation/rapport_TP1_compilation.pdf).

---

## Auteures

Dépôt réalisé en binôme par :
- DRAME Hadja Fatoumata – L3 Informatique, Université de Limoges
- KPARA Hamoudalath – L3 Informatique, Université de Limoges
