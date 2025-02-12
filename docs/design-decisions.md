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

Status: Work in progress - **Decided** - Obsolete

Updated: 11-Dec-2024

### Problem statement

The application FitConnect aims to connect people to do exercise together. The main issue is to organise this connection.
We want to make the application user-friendly, but also strctured effieciently. 
That is why we thought of two ways to organize the connection process:

### Considered options

1) People can be matched, as it is the case with dating platforms. This would require, that all data entered can be processed and compared. For example memberships should be comparable, if this is a requirement for  someone to be matched. To realise this, a data base with all possible memberships has to be made available. But there could be a risk of not covering all possibilities.

2) Another possibility is to show all users to everyone, so that each user can decide themselves who they want to match with. This would not require the data entered to be part of a data base, nor would it require an algorithm to prevent unsuitable users from being displayed. Meanwhile the user might not have such a great sense of success, as profiles may be displayed that are only available on different days, for example. On the other hand, even if the app does not have many users in the beginning, everyone will always see several profiles to match with.

### Decision

After discussion, we all decided to go with option two. The reason for this is that it seems to be more user-friendly at the beginning of the implementation. Also, it will require less resources than option one, but will still add value to the application and will serve the purpose of connecting people.
If other topics should require less time, we want to keep the option of filtering profiles based on personal interests or strict time slots in mind.
As sort of a mix between the two alternative options, we want to add a "send like" button to every profile a user can view. After sending a like, this will pop up for the user of the liked profile. He/ she can like back or delete the like request. Only if both sides like each other, a user's contact info will be shown.



## 02: Database Model – Likes vs. Matches

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: 12-02-2025

### Problem statement

Initially, the database model included a Match table to store confirmed matches. However, this approach added complexity and required extra storage and updates whenever matches changed.

### Considered options

1) **Match Table**

    Each match is recorded when two users like each other

- **Pros:** Matches are stored permanently, making retrieval easy
- **Cons:** Requires updating the match table when users change likes, leading to unnecessary storage overhead

2) **Query-Based Matches Using Likes Table**

    Instead of storing matches, the system dynamically queries mutual likes

- **Pros:** No redundant data, matches update automatically, and it scales better.
- **Cons:** Requires a query each time matches are retrieved.

### Decision

We decided to go with the second option of query-based matches to make the system more dynamic and scalable. Matches can be now detected in real-time by checking for mutual likes rather than being explicitly sstored.


## 03: Databse Choice – SQLite vs. PostgreSQL

### Meta

Status: Work in progress - **Decided** - Obsolete

Updated:
10-02-2025

### Problem statement

We initially used SQLite due to its simplicity and easy setup. However, as we prepared for production deployment, we encountered limitations that made it unsuitable for a live, multi-user environment. The challenge was selecting a database that balances scalability, performance, and compatibility with our deployment needs.

### Considered options


| Database | Pros | Cons |
| --- | --- | --- |
| **SQLite** | No configuration needed | No built-in user management |
| | Suitable for local development | We were not able to access certain users made by other team members|
| **PostgreSQL**| Supports multiple concurrent users| Requires more setup|
| |Better performance| Requires more maintenance |

### Decision

We switched from SQLite to PostgreSQL because SQLite was only effective for local development but did not work well in a production setting. Since FitConnect is a web application that supports multiple users accessing and modifying data simultaneously, we needed a database that could handle concurrent reads and writes efficiently. PostgreSQL provides a scalable, stable, and performant solution.