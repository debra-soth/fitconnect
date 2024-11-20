---
title: Data Model
parent: Technical Docs
nav_order: 2
---

{: .label }
[Debra Soth]

{: .no_toc }
# Data model

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

[Visualize and describe the data model(s) of your application. This description should match the actual implementation.]

![Datenmodell version 1](/fitconnect/assets/images/Datenmodell v.1.png)

Das Datenmodell besteht zurzeit aus zwei Entitäten: Match und User.

Die User-Entität enthält alle persönlichen und fitnessbezogenen Informationen, die für ein Match erforderlich sind:

- username (string, Primary Key) ist der eindeutige Bezeichner für jeden Benutzer
- email (string) für das Einloggen als auch als Art der Kontaktaufnahme nach einem Match
- password (string)
- name ()
- gender
- age
- fitness-level (string)
- gym-membership (string)
- activities (string)
- motivation-text (string)
- profile-photo (string): Hier haben wir uns für den Datentyp string entschieden, um später den Pfad zum Profilfoto einfügen zu können

