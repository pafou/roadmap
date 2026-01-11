# Guide Utilisateur pour le Générateur de Roadmap

Ce guide explique comment remplir le fichier JSON pour générer des roadmaps professionnelles au format PowerPoint.

## 📋 Table des Matières

1. [Introduction](#introduction)
2. [Structure de Base du Fichier JSON](#structure-de-base-du-fichier-json)
3. [Composants Principaux](#composants-principaux)
   - [Thèmes](#thèmes)
   - [Lignes](#lignes)
   - [Éléments](#éléments)
4. [Types d'Éléments](#types-déléments)
   - [Barres (type: bar)](#barres-type-bar)
   - [Jalons (type: milestone)](#jalons-type-milestone)
   - [Texte (type: text)](#texte-type-text)
5. [Champs Obligatoires et Optionnels](#champs-obligatoires-et-optionnels)
6. [Format des Mois](#format-des-mois)
7. [Exemple Complet](#exemple-complet)
8. [Validation du JSON](#validation-du-json)
9. [Génération de la Roadmap](#génération-de-la-roadmap)
10. [Résultat Obtenu](#résultat-obtenu)
11. [Bonnes Pratiques](#bonnes-pratiques)
12. [Dépannage](#dépannage)

## 🎯 Introduction

Le générateur de roadmap permet de créer des présentations PowerPoint professionnelles à partir de fichiers JSON. Ce guide vous explique comment structurer votre fichier JSON pour obtenir le résultat souhaité.

## 🏗️ Structure de Base du Fichier JSON

```json
{
  "$schema": "../roadmap_schema.json",
  "title": "Titre de votre Roadmap",
  "themes": [
    // Vos thèmes ici
  ]
}
```

- **`$schema`** : Référence au schéma de validation (ne pas modifier)
- **`title`** : Titre de votre roadmap (optionnel mais recommandé)
- **`themes`** : Tableau contenant les différents thèmes de votre roadmap

## 📦 Composants Principaux

### Thèmes

Un thème représente une catégorie ou un domaine de votre roadmap.

```json
{
  "name": "Nom du Thème",
  "items": [
    // Vos lignes ici
  ]
}
```

- **`name`** : Nom du thème (obligatoire)
- **`items`** : Tableau contenant les lignes du thème (obligatoire)

### Lignes

Une ligne contient une série d'éléments qui seront affichés sur la même ligne horizontale.

```json
{
  "line": {
    "items": [
      // Vos éléments ici
    ]
  }
}
```

- **`items`** : Tableau contenant les éléments de la ligne (obligatoire)

### Éléments

Les éléments sont les composants visuels individuels de votre roadmap.

## 🎯 Types d'Éléments

### Barres (type: bar)

Représentent des projets ou initiatives avec une durée.

```json
{
  "type": "bar",
  "subtype": "DDO",
  "label": "Nom du Projet",
  "start": "Jan",
  "end": "Mar",
  "year": 2026
}
```

- **`type`** : Doit être "bar" (obligatoire)
- **`label`** : Nom du projet (obligatoire)
- **`start`** : Mois de début (obligatoire)
- **`end`** : Mois de fin (obligatoire)
- **`year`** : Année (obligatoire)
- **`subtype`** : Type de barre (optionnel) - Valeurs possibles : "S", "ER", "DDO", "SL"

### Jalons (type: milestone)

Représentent des événements ponctuels.

```json
{
  "type": "milestone",
  "label": "Nom du Jalon",
  "month": "Jun",
  "year": 2026,
  "style": "ddo"
}
```

- **`type`** : Doit être "milestone" (obligatoire)
- **`label`** : Nom du jalon (obligatoire)
- **`month`** : Mois du jalon (obligatoire)
- **`year`** : Année (obligatoire)
- **`style`** : Style du jalon (optionnel) - Valeurs possibles : "default", "ddo"

### Texte (type: text)

Annotations textuelles.

```json
{
  "type": "text",
  "label": "Votre texte ici",
  "year": 2026
}
```

- **`type`** : Doit être "text" (obligatoire)
- **`label`** : Texte à afficher (obligatoire)
- **`year`** : Année (obligatoire)

## 📋 Champs Obligatoires et Optionnels

### Barres
- **Obligatoires** : type, label, start, end, year
- **Optionnels** : subtype

### Jalons
- **Obligatoires** : type, label, month, year
- **Optionnels** : style

### Texte
- **Obligatoires** : type, label, year
- **Optionnels** : aucun

## 📅 Format des Mois

Les mois doivent être spécifiés en français avec les abréviations suivantes :
- Jan, Fév, Mar, Avr, Mai, Jun, Jul, Aoû, Sep, Oct, Nov, Déc

## 📄 Exemple Complet

```json
{
  "$schema": "../roadmap_schema.json",
  "title": "Roadmap Plateform Engineering 2026",
  "themes": [
    {
      "name": "Dynamique collective",
      "items": [
        {
          "line": {
            "items": [
              {
                "type": "bar",
                "subtype": "DDO",
                "label": "Évènements",
                "start": "Jan",
                "end": "Déc",
                "year": 2026
              },
              {
                "type": "milestone",
                "label": "PI Planning 4",
                "month": "Jan",
                "year": 2026,
                "style": "ddo"
              }
            ]
          }
        }
      ]
    },
    {
      "name": "Moyens de développement",
      "items": [
        {
          "line": {
            "items": [
              {
                "type": "bar",
                "subtype": "DDO",
                "label": "IA 4 Devs",
                "start": "Jan",
                "end": "Déc",
                "year": 2026
              },
              {
                "type": "milestone",
                "label": "Mesure",
                "month": "Jan",
                "year": 2026,
                "style": "ddo"
              }
            ]
          }
        }
      ]
    }
  ]
}
```

## 🔍 Validation du JSON

Avant de générer votre roadmap, validez votre fichier JSON :

```bash
python validate_json.py
```

Ce script vérifie que :
- La structure JSON est valide
- Tous les champs obligatoires sont présents
- Les valeurs sont conformes au schéma
- Les mois sont dans le bon format

## 🚀 Génération de la Roadmap

Pour générer votre roadmap PowerPoint :

```bash
python roadmap.py
```

Le script va :
1. Lire votre fichier JSON
2. Valider la structure
3. Générer un fichier PowerPoint dans le dossier `data/`
4. Utiliser le template `Roadmap_template.pptx`

## 🎨 Résultat Obtenu

Le générateur produit un fichier PowerPoint professionnel avec :

### Structure Visuelle
- **Thèmes** : Chaque thème est affiché comme une section distincte
- **Lignes** : Chaque ligne contient une série d'éléments horizontaux
- **Barres** : Représentées comme des barres horizontales colorées
- **Jalons** : Affichés comme des points ou icônes spécifiques
- **Texte** : Annotations positionnées stratégiquement

### Caractéristiques
- **Couleurs** : Les éléments sont colorés selon leur type et sous-type
- **Positionnement** : Les éléments sont positionnés automatiquement
- **Mise en page** : Adaptée à la quantité de contenu
- **Professionnel** : Résultat prêt pour présentation

### Exemple de Résultat
- Fichier généré : `data/Roadmap_generee1.pptx`
- Format : PowerPoint standard (.pptx)
- Contenu : Tous les éléments de votre JSON organisés visuellement
- Style : Cohérent avec le template fourni

## ✅ Bonnes Pratiques

1. **Organisation** : Regroupez les éléments logiquement par thèmes
2. **Consistance** : Utilisez les mêmes styles pour des éléments similaires
3. **Validation** : Validez toujours votre JSON avant génération
4. **Noms clairs** : Utilisez des labels descriptifs
5. **Périodes réalistes** : Assurez-vous que les dates sont cohérentes
6. **Sauvegarde** : Sauvegardez vos fichiers JSON avant modification

## 🔧 Dépannage

### Problèmes Courants

**Erreur de validation JSON** :
- Vérifiez que tous les champs obligatoires sont présents
- Assurez-vous que les mois sont dans le bon format
- Vérifiez que les années sont entre 2000 et 2100

**Problème de génération** :
- Vérifiez que le fichier template existe
- Assurez-vous que python-pptx est installé
- Vérifiez les permissions d'écriture dans le dossier data/

**Résultat inattendu** :
- Vérifiez l'ordre des éléments dans votre JSON
- Assurez-vous que les années correspondent
- Vérifiez les sous-types et styles utilisés

## 📚 Ressources Complémentaires

- **Schémas** : `roadmap_schema.json` pour la validation
- **Template** : `data/Roadmap_template.pptx` pour le style
- **Exemples** : Fichiers existants dans `data/roadmap*.json`
- **Documentation** : `README.md` pour plus de détails techniques

## 🎯 Conseils Avancés

1. **Personnalisation** : Modifiez `styles_config.py` pour adapter les couleurs
2. **Multi-années** : Vous pouvez mélanger plusieurs années dans un même fichier
3. **Ordre** : L'ordre des thèmes et éléments dans le JSON détermine leur position
4. **Test** : Générez des versions tests avant la version finale

Ce guide vous permet de créer des roadmaps professionnelles en suivant une structure claire et validée.
