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
**Sample output:** Redirects to `/auth/login`  

---

## Personalize Profile Page
@app.route('/personalize')  
**Route:** `/personalize`  
**Methods:** `GET`  
**Purpose:** Renders the profile personalization page with a form  
**Sample output:** HTML page with the profile form  

---

## User Registration
@auth.route('/register')  
**Route:** `/register`  
**Methods:** `GET`, `POST`  
**Purpose:** Handles user registration with form validation and database storage  
**Sample output:** Displays registration form or redirects upon success.  

---

## User Login  
@auth.route('/login')  
**Route:** `/login`  
**Methods:** `GET`, `POST`  
**Purpose:** Authenticates users and starts a session  
**Sample output:** Redirects to dashboard upon success  

---

## User Logout  
@auth.route('/logout')  
**Route:** `/logout`  
**Methods:** `GET`  
**Purpose:** Logs out the current user and redirects to the login page  
**Sample output:** Redirect to `/login`.  

---

## Create Event  
@auth.route('/create-event')  
**Route:** `/create-event`  
**Methods:** `GET`, `POST`  
**Purpose:** Allows users to create an event  
**Sample output:** Displays event creation form or confirms event creation  

---

## Event Details  
@auth.route('/event-details/<int:event_id>')  
**Route:** `/event-details/<int:event_id>`  
**Methods:** `GET`  
**Purpose:** Displays details of a specific event  
**Sample output:** Event information with participants and options to join.  

---

## Events List 
@auth.route('/events')  
**Route:** `/events`  
**Methods:** `GET`  
**Purpose:** Shows a list of all available events  
**Sample output:** Event listing with options to join.  

---

## Join Event 
@auth.route('/join-event/<int:event_id>')  
**Route:** `/join-event/<int:event_id>`  
**Methods:** `POST`  
**Purpose:** Allows users to join a specific event  
**Sample output:** Confirmation of event participation.  

---

## Like User 
@auth.route('/like/<int:user_id>')  
**Route:** `/like/<int:user_id>`  
**Methods:** `POST`  
**Purpose:** Allows users to like another user (for connections/matching)  
**Sample output:** Confirmation of the like action.  

---

## User Profile 
@auth.route('/profile')  
**Route:** `/profile`  
**Methods:** `GET`  
**Purpose:** Displays the profile of the logged-in user  
**Sample output:** User profile information and edit options.  

---

## User Settings 
@auth.route('/settings')  
**Route:** `/settings`  
**Methods:** `GET`, `POST`  
**Purpose:** Allows users to update their account settings  
**Sample output:** Settings page with editable preferences.  

---

## User List
@auth.route('/user')  
**Route:** `/user`  
**Methods:** `GET`  
**Purpose:** Displays a list of users (for social features)  
**Sample output:** List of users with interaction options.  

---

## Specific User Profile
@auth.route('/user/<int:user_id>')  
**Route:** `/user/<int:user_id>`  
**Methods:** `GET`  
**Purpose:** Displays the profile of a specific user  
**Sample output:** Profile details of the selected user.  

---

## Your Matches 
@auth.route('/your-matches')  
**Route:** `/your-matches`  
**Methods:** `GET`  
**Purpose:** Displays potential matches based on preferences  
**Sample output:** List of matched users.