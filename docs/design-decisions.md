---
title: Design Decisions
nav_order: 3
---

{: .label}
[Jane Dane]

{: .attention}

# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: functions: How to find a partner

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 11-Dec-2024

### Problem statement

The application FitConnect aims to connect people to do exercise together. The main issue is to organise this connection.
We want to make the application user-friendly, but also strctured effieciently. 
That is why we thought of two ways to organize the connection process:

### Regarded options

1) People can be matched, as it is the case with dating platforms. This would require, that all data entered can be processed and compared. For example memberships should be comparable, if this is a requirement for  someone to be matched. To realise this, a data base with all possible memberships has to be made available. But there could be a risk of not covering all possibilities.

2) Another possibility is to show all users to everyone, so that each user can decide themselves who they want to match with. This would not require the data entered to be part of a data base, nor would it require an algorithm to prevent unsuitable users from being displayed. Meanwhile the user might not have such a great sense of success, as profiles may be displayed that are only available on different days, for example. On the other hand, even if the app does not have many users in the beginning, everyone will always see several profiles to match with.

### Decision

After discussion, we all decided to go with option two. The reason for this is that it seems to be more user-friendly at the beginning of the implementation. Also, it will require less resources than option one, but will still add value to the application and will serve the purpose of connecting people.
If other topics should require less time, we want to keep the option of filtering profiles based on personal interests or strict time slots in mind.
As sort of a mix between the two alternative options, we want to add a "send like" button to every profile a user can view. After sending a like, this will pop up for the user of the liked profile. He/ she can like back or delete the like request. Only if both sides like each other, a user's contact info will be shown.

---


## 02: Database Model – Likes vs. Matches

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

Initially, the database model included a Match table to store confirmed matches. However, this approach added complexity and required extra storage and updates whenever matches changed.

### Regarded options

1) Match Table:
Each match is recorded when two users like each other

- **Pros:** Matches are stored permanently, making retrieval easy
- **Cons:** Requires updating the match table when users change likes, leading to unnecessary storage overhead

2) Query-Based Matches Using Likes Table

Instead of storing matches, the system dynamically queries mutual likes

- **Pros:** No redundant data, matches update automatically, and it scales better.
- **Cons:** Requires a query each time matches are retrieved.

---

## [Example, delete this section] 01: How to access the database - SQL or SQLAlchemy 

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-Jun-2024

### Problem statement

Should we perform database CRUD (create, read, update, delete) operations by writing plain SQL or by using SQLAlchemy as object-relational mapper?

Our web application is written in Python with Flask and connects to an SQLite database. To complete the current project, this setup is sufficient.

We intend to scale up the application later on, since we see substantial business value in it.



Therefore, we will likely:
Therefore, we will likely:
Therefore, we will likely:

+ Change the database schema multiple times along the way, and
+ Switch to a more capable database system at some point.

### Decision

We stick with plain SQL.

Our team still has to come to grips with various technologies new to us, like Python and CSS. Adding another element to our stack will slow us down at the moment.

Also, it is likely we will completely re-write the app after MVP validation. This will create the opportunity to revise tech choices in roughly 4-6 months from now.
*Decision was taken by:* github.com/joe, github.com/jane, github.com/maxi

### Regarded options

We regarded two alternative options:

+ Plain SQL
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Know-how** | ✔️ We know how to write SQL | ❌ We must learn ORM concept & SQLAlchemy |
| **Change DB schema** | ❌ SQL scattered across code | ❔ Good: classes, bad: need Alembic on top |
| **Switch DB engine** | ❌ Different SQL dialect | ✔️ Abstracts away DB engine |

---
