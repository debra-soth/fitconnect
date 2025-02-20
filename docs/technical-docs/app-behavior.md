---
title: App Behavior
parent: Technical Docs
nav_order: 2
---

{: .label }
Debra Soth

{: .label }
Lenja Krah

{: .label }
Kira Beyrow

{: .no_toc }
# App Behavior

<details open markdown="block">
{: .text-delta }
<summary>Table of Contents</summary>

- [User Authentication System](#1-user-authentication-system)  
  - [Login & Sign-Up Flow](#login--sign-up-flow)  
  - [Logout Flow](#logout-flow)  
- [Profile Management](#2-profile-management)  
- [Matchmaking Logic](#3-matchmaking-logic)  
  - [Viewing Matches](#viewing-matches)  
- [Events System](#4-events-system)  
- [System Actions & Logic Handling](#5-system-actions--logic-handling)  
  - [Frontend Interaction](#frontend-interaction)  
  - [Backend Processing](#backend-processing)  

</details>

![Usage Flow](../assets/images/Usage-Flow.png)
*Figure 3: Our Usage Flow Chart*

## 1. User Authentication System

### Login & Sign-Up Flow

- User opens the website and system checks if the user is logged in (`Flask-Login` manages session state)

**If the user has an account:**

- The frontend provides a login form (`Flask-WTF` for form handling)
- User enters `username` and `password`
- The form submits a request to Flask, which validates login credentials
- Flask checks the credentials against PostgreSQL via SQLAlchemy
- If correct, the session is created, and the user is redirected to the homepage
- If incorrect, an error message is displayed, and the retry process is initiated

**If the user does not have an account:**

- They fill out the sign-up form (Username, Name, Email, Password)
- Flask validates the input (email format, password strength, uniqueness)
- If validation passes, the user is stored in PostgreSQL
- If validation fails, an error message appears

### Logout Flow

**When a user logs out:**

- `Flask-Login` clears the session
- The user is redirected to the login page

## 2. Profile Management

**Personalization Options:**

- Users can navigate to their profile
- They can update their name, email, profile picture, and preferences
- Changes are submitted via a form (`Flask-WTF`)
- Flask processes the form data, updates the PostgreSQL database using `SQLAlchemy`, and confirms the update

## 3. Matchmaking Logic

**Viewing Matches:**

- The backend fetches "people who liked you" from the `PostgreSQL` database
- Users can view profiles and either:
    - Like them back → Creates a match entry in the database
    - Remove them from likes → Deletes the entry
- `SQLAlchemy` handles these database operations
- Matched users’ contact details become visible when both parties like each other

## 4. Events System

- Users can join events
- Event details are stored in the `PostgreSQL` database
- Users click on an event → Flask updates the database with the user’s participation
- The event appears in their list of "Events" under the subpage "Your Matches"

## 5. System Actions & Logic Handling

### Frontend Interaction:

- Buttons (`Bootstrap`, `JavaScript`) trigger requests to Flask routes
- User actions (clicking, entering data) initiate form submissions

### Backend Processing:

- Flask routes process user requests
- `SQLAlchemy` queries update PostgreSQL
- `Flask-WTF` ensures form validation and CSRF protection