---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }
[Jane Dane]

{: .no_toc }
# Reference documentation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>


## Index Page Redirect
`@app.route('/')`

**Route:** `/`  
**Methods:** `GET`  
**Purpose:** Redirects users to the login page  
**Sample output:** 

![login-page](../assets/images/login-screen.png)

---

## Personalize Profile Page

`@app.route('/personalize')`  

**Route:** `/personalize`  
**Methods:** `GET`  
**Purpose:** Renders the profile personalization page with a form  
**Sample output:** 

![personalize profile page](../assets/images/personalize-profile.png) 

---

## User Registration

`@auth.route('/register')` 

**Route:** `/register`  
**Methods:** `GET`, `POST`  
**Purpose:** Handles user registration with form validation and database storage  
**Sample output:** 

![registration](../assets/images/registration-screen.png) 

---

## User Login  

`@auth.route('/login')` 

**Route:** `/login`  
**Methods:** `GET`, `POST`  
**Purpose:** Authenticates users and starts a session  
**Sample output:** 

![homepage](../assets/images/user-overview.png) 

---

## User Logout  

`@auth.route('/logout')`

**Route:** `/logout`  
**Methods:** `GET`, `POST`  
**Purpose:** Logs out the current user and redirects to the login page  
**Sample output:** Redirect to `/login`.  

---

## Create Event

`@auth.route('/create-event')`

**Route:** `/create-event`  
**Methods:** `GET`, `POST`  
**Purpose:** Allows users to create an event  
**Sample output:** 

![create event](../assets/images/create-event.png) 

---

## Event Details

`@app.route('/event-details/<int:event_id>')`

**Route:** `/event-details/<int:event_id>`  
**Methods:** `GET`  
**Purpose:** Displays details of a specific event  
**Sample output:** 

![event_details](../assets/images/event-details.png) 

---

## Event Overview

`@app.route('/events')`

**Route:** `/events`  
**Methods:** `GET`  
**Purpose:** Shows a list of all available events  
**Sample output:** 

![event overview](../assets/images/event-overview.png)

---

## Join Event

`@auth.route('/join-event/<int:event_id>')`

**Route:** `/join-event/<int:event_id>`  
**Methods:** `POST`  
**Purpose:** Allows users to join a specific event  
**Sample output:** Browser shows: `Successfully joined the event!`

---

## Like User

`@auth.route('/like/<int:user_id>')`  
**Route:** `/like/<int:user_id>`  
**Methods:** `POST`  
**Purpose:** Allows users to like another user (for connections/matching)  
**Sample output:** Browser shows: `You liked this user! If they like you back, you'll be matched.`

---

## User Profile

`@app.route('/profile')`

**Route:** `/profile`  
**Methods:** `GET`  
**Purpose:** Displays the profile of the logged-in user  
**Sample output:** 

![own profile](../assets/images/own-profile.png) 

---

## User Settings

`@auth.route('/settings')`

**Route:** `/settings`  
**Methods:** `GET`, `POST`  
**Purpose:** Allows users to update their account settings  
**Sample output:** 

![account settings](../assets/images/account-settings.png) 

---

## User List

`@app.route('/user')`

**Route:** `/user`  
**Methods:** `GET`  
**Purpose:** Displays a list of users (for social features)  
**Sample output:** 

![homepage](../assets/images/user-overview.png) 

---

## Specific User Profile

`@app.route('/user/<int:user_id>')`

**Route:** `/user/<int:user_id>` 
**Methods:** `GET` 
**Purpose:** Displays the profile of a specific user 
**Sample output:** 

![User Details](../assets/images/user-details.png)
 
---

## Your Matches

`@app.route('/your-matches')`

**Route:** `/your-matches`  
**Methods:** `GET`  
**Purpose:** Displays potential matches based on preferences  
**Sample output:** Profile card displays: `You are already matched`