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

## Version 1
```mermaid
erDiagram
    Match }|--|| User: references

    User {
        string username PK
        string email 
        string password
        string name
        string gender
        int age
        int fitness_level
        string gym_membership
        string activities
        string motivation_text
        string profile_photo
    }

    Match {
        int match_id PK
        string username_1 FK
        string username_2 FK
        boolean confirmed
    }
```
FitConnect is designed to connect users based on specific criteria such as fitness level, sports, availability and other parameters. 
The data model above consists of two primary entities: **User** and **Match**. 

### User Table
The table **User** stores the profile of all users. It contains a `username` attribute which serves as the primary key of the table. And it also includes personal data such as name, gender, age and important details for matching like fitness level, preferred activites and optionally a gym membership. 
Through these attributes users can find suitable training partners with similar interests. 

### Match Table
The **Match** table manages the connections between two users who match through the app. Each relationship is uniquely identified by a `match_id`. The foreign keys `username_1` and `username_2` are used to build a direct connection between the two profiles that have matched. The `confirmed` attribute indicates whether or not both users have accepted the connection.

### Data Types
For the **User** table most attributes have the data type string except for `age` and `fitness-level`. Values for `fitness-level` will be saved as 1-10. For the attributes `gender` and `gym-membership` we might change the string to an enum in the next version of the data model to allow for a set of specific values such as "male", "female" or "non-binary" and a set of gym memberships. For `availability`, the data type is currently still a string, however, we might also change this to a structure using boolean instead, where each day of the week (Monday through Sunday) is represented as a separate column with a TRUE or FALSE value. 

In the **Match** table we chose boolean for the attribute `confirmed` to represent whether or not a match happened between two users. TRUE would mean that both users have agreed to the match whereas FALSE would mean that either a user hasn't responded to a like request or the user has rejected the request. Here, we might also explore different data types in the next data model version that might be better fitting.

