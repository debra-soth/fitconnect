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

## 01: Database Choice – SQLite vs. PostgreSQL

### Meta

**Status:** ✅ Decided

**Updated:** 10-Feb-2025

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

---

## 02: How Users Join Events

### Meta

**Status:** ✅ Decided

**Updated:** 10-Feb-2025

### Problem statement

Since users should now be able to create and join events the challenge here was too design an efficient way to manage this interaction.

### Considered options

1. **One-to-Many Structure**

    Each event is owned by one user, and participants are stored as a list inside the event.

    | **Pros** | **Cons** |
    | --- | --- |
    | Simple structure|Difficult to track many-to-many relationships efficiently|
    | Easy to manage||

2. **Many-to-Many Relationship**

    A separate table (EventParticipants) stores who joins which event.

    | **Pros** |**Cons**|
    |---|---|
    |More flexible| Requires an extra table|
    |Allows multiple users to join mulitiple events||


### Decision

We implemented Option 2 (Many-to-Many Relationship) using an EventParticipants table. This approach allows multiple users to join multiple events without unnecessary data duplication, making it easier to expand the event system in the future

---

## 03: Adding "Create Event" Option

### Meta

**Status:** ✅ Decided

**Updated:** 09-Feb-2025

### Problem statement

FitConnect was originally designed as a user-matching platform that helped people find workout partners based on shared fitness interests, schedules, and locations. However, after our project presentation, we realized that just matching users was not enough to satisfy the supply and demand requirement. 
The solution was to offer an Event option where users can join fitness events and therefore meet new people (demand) and create events (supply) at the same time for other FitConnectors.

### Considered options

1. **Keeping FitConnect as a User-Matching App**

    | **Pros** | **Cons** |
    | --- | --- |
    | Simpler to develop|Users can become unsure how or when to meet|
    | More focused on individual connections|Low engagement|

2. **Allowing Users to Create and Join Events (Final Choice)**

    | **Pros** |**Cons**|
    |---|---|
    |Provides structured opportunities for engagement and ensures a steady flow of activities on the platform| Requires event moderation to prevent low-quality events|
    |Ensures a steady flow of activities on the platform| Additional UI complexity|


### Decision

We moved away from a pure user-matching approach and instead built an event-driven model that gives users more structured ways to connect. While one-on-one matching is still an option, users now have the ability to create and join events, making it much easier to find workout opportunities without relying solely on direct messaging.

This change makes the platform more engaging by ensuring that even if users don’t feel comfortable reaching out individually, they can still participate in group activities. It also helps new users immediately find something to join, rather than waiting for a match.

---

## 04: Database Model – Likes vs. Matches

### Meta

**Status:** ✅ Decided

**Updated:** 27-Jan-2025

### Problem statement

Initially, the database model included a Match table to store confirmed matches. However, this approach added complexity and required extra storage and updates whenever matches changed.

### Considered options

1) **Match Table**

   Each match is recorded when two users like each other.

   **Pros and Cons:**

   | **Pros** | **Cons** |
   | --- | --- |
   | Matches are stored permanently | Requires updating the match table when users change likes |
   | Easy retrieval | &nbsp; |

2) **Query-Based Matches Using Likes Table**

   Instead of storing matches, the system dynamically queries mutual likes.

   **Pros and Cons:**

   | **Pros** | **Cons** |
   | --- | --- |
   | No redundant data | Requires a query each time matches are retrieved |
   | Matches update automatically | &nbsp; |
   | Can scale better | &nbsp; |


### Decision

We decided to go with the second option of query-based matches to make the system more dynamic and scalable. Matches can be now detected in real-time by checking for mutual likes rather than being explicitly sstored.

---

## 05: How To Find a Partner

### Meta

**Status:** ✅ Decided

**Updated:** 11-Dec-2024

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