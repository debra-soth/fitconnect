---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }
Debra Soth

{: .label }
Lenja Krah

{: .label }
Kira Beyrow

{: .no_toc }
# Reference documentation

<details open markdown="block">
{: .text-delta }
<summary>Table of Contents</summary>

- [Index Page Redirect](#index-page-redirect)  
- [Personalize Profile Page](#personalize-profile-page)  
- [User Registration](#user-registration)  
- [User Login](#user-login)  
- [User Logout](#user-logout)  
- [Create Event](#create-event)  
- [Event Details](#event-details)  
- [Event Overview](#event-overview)  
- [Join Event](#join-event)  
- [Like User](#like-user)  
- [User Profile](#user-profile)  
- [User Settings](#user-settings)  
- [User List](#user-list)  
- [Specific User Profile](#specific-user-profile)  
- [Your Matches](#your-matches)  

</details>


## Index Page Redirect
`@app.route('/')`

**Route:** `/`  
**Methods:** `GET`  
**Purpose:** Redirects users to the login page  
**Sample output:** 

![login-page](../assets/images/login-screen.png)
*Image 3: Login Page*

---

## Personalize Profile Page

`@app.route('/personalize')`  

**Route:** `/personalize`  
**Methods:** `GET`  
**Purpose:** Renders the profile personalization page with a form  
**Sample output:** 

![personalize profile page](../assets/images/personalize-profile.png) 
*Image 4: Personalize Profile Page*

---

## User Registration

`@auth.route('/register')` 

**Route:** `/register`  
**Methods:** `GET`, `POST`  
**Purpose:** Handles user registration with form validation and database storage  
**Sample output:** 

![registration](../assets/images/registration-screen.png) 
*Image 5: User Registration Page*

---

## User Login  

`@auth.route('/login')` 

**Route:** `/login`  
**Methods:** `GET`, `POST`  
**Purpose:** Authenticates users and starts a session  
**Sample output:** 

![homepage](../assets/images/user-overview.png) 
*Image 6: Homepage/User Overview Page*

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
*Image 7: Create Event Page*

---

## Event Details

`@app.route('/event-details/<int:event_id>')`

**Route:** `/event-details/<int:event_id>`  
**Methods:** `GET`  
**Purpose:** Displays details of a specific event  
**Sample output:** 

![event_details](../assets/images/event-details.png) 
*Image 8: Event Details Page*

---

## Event Overview

`@app.route('/events')`

**Route:** `/events`  
**Methods:** `GET`  
**Purpose:** Shows a list of all available events  
**Sample output:** 

![event overview](../assets/images/event-overview.png)
*Image 9: Event Overview Page*

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
*Image 10: User Profile Page*

---

## User Settings

`@auth.route('/settings')`

**Route:** `/settings`  
**Methods:** `GET`, `POST`  
**Purpose:** Allows users to update their account settings  
**Sample output:** 

![account settings](../assets/images/account-settings.png) 
*Image 11: Account Settings Page*

---

## User List

`@app.route('/user')`

**Route:** `/user`  
**Methods:** `GET`  
**Purpose:** Displays a list of users (for social features)  
**Sample output:** 

![homepage](../assets/images/user-overview.png) 
*Image 12: User Overview Page*

---

## Specific User Profile

`@app.route('/user/<int:user_id>')`

**Route:** `/user/<int:user_id>` 
**Methods:** `GET` 
**Purpose:** Displays the profile of a specific user 
**Sample output:** 

![User Details](../assets/images/user-details.png)
 *Image 13: User Details Page*

---

## Your Matches

`@app.route('/your-matches')`

**Route:** `/your-matches`  
**Methods:** `GET`  
**Purpose:** Displays potential matches based on preferences  
**Sample output:** Profile card displays: `You are already matched`

![Your Matches](../assets/images/YourMatches-Screen.png)
 *Image 14: Your Matches Page*