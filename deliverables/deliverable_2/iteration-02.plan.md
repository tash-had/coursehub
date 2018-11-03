# Course Hub


## Iteration 02

* Start date: October 25, 2018
* End date: October 31, 2018

## Process


#### Roles & responsibilities



Backend - Ted, Nathan, Tash-had:  
-Implement the classes Course and Comment as specified in the UML diagram we made in Deliverable 1   
-Get data from timetable api and parse necessary information 
-Send data to backend to be able to put in database  

Frontend - Labib:  
-Implement frontend portion of web-app to display to users

Connecting frontend to backend - Andrew, Labib, Tash-had:  
-Send comments and posts to backend when user interacts with basic webpage  
-Display information received from backend i.e. ratings, textbook information

Database- Cullen:  
For the database we will have one database which holds all of the comments. In here we will keep track of the comment id, text for the comment, the course for which the comment is for (which is a foreign key for this database in relation to the course database), the timestamp and the vote count for the comment. The foreign key is important for linking the two databases. The second database will be for the courses which will contain the course code, its ratings and other auxiliary information. The database will be queried whenever a search is made by the user for a specific course and then the information will be displayed according to the information associated with that course.  

#### Events

Each Thursday we have our general weekly meeting at 4pm where we do a standup and discuss our progress and problems. We met in BA2179 typically for an hour. The purpose of these meetings is to discuss progress and decisions that require attention.
Additionally, the two multi-person teams (frontend and connecting front end to back end) will have meetings on Discord when necessary to update each other on their progress and what needs to be done.

On October 27th at 3pm, the backend team will have a meeting on Discord to decide exactly what everyone will implement.  

The frontend will meet on October 28th at 5 pm in person to discuss how we will display the information and communicate between the backend and frontend

There will be a review meeting on October 31st to determine what final touches have to be made for this iteration.

#### Artifacts



[Trello](https://trello.com/b/QOjo3VHX/csc301) is our main information centre for organizing tasks that need to be done, tasks that are in progress and ones that are finished.  

Within our own smaller teams, we have frequent meetings to discuss what needs to get done, the priority of all our tasks, and specifically what tasks should be assigned to team members.  Since we have split up our project into small teams, it is very easy to simply discuss these things during our meetings and then remember what was discussed.  

#### Git / GitHub workflow


We have different branches for the different sections of our project such as the basic ui and the database. This will allow us to keep our master branch clean and working at all times. We will have everyone review the pull requests when we are trying to merge to ensure code is acceptable for the master branch. The product manager will be responsible for merging. The reason we chose this workflow is because it allows our project to continuously have a working repository where we have no bugs, allowing us to make changes and revert changes easily.

## Product

#### Goals and tasks



Our main goal for this iteration is to fully implement our MVP.  We will create a page for every CS course at U of T and be able to add comments on each course page.  To do all this we will need to connect all components of our project.  The database will have to be fully implemented with all the functions that the backend needs to access the database.  The backend will need to have functions that can take in a request from the frontend, access the database and then return the output back to the frontend.  

Our other main goal is to complete the video showing our product.  To make this video we will need to have all our code completed so that the website is up and running.  

Our secondary goal is to meet weekly outside of tutorial.  This will ensure that we meet in person every 3-4 days to report on our progress and decide what needs to be done.  

Our less important secondary goal is to add in ratings for comments and courses.  This would include upvoting/downvoting comments and leaving a rating of a course.  If possible in this iteration, we would like to also have different types of ratings for a course such as a rating for difficulty, usefulness, etc. To achieve this goal we will need to add in a score attribute for comments and rating attribute(s) for courses.  Additionally we will need functions in our backend code to take in an upvote/downvote/rating from the user in the front end, change the rating in the database and then return the new rating to the front end.  


#### Artifacts
For this iteration we will produce a video that displays the functionality of our web-app such as the front end and using the search bar to find a course. We will also show that we have a database catalogued with all the UofT computer science courses and in addition we scraped the UofT course evals page and inserted it into our database. The search bar is used to search for courses and when clicked on it will bring you to the course page. Here you can see the information about its ratings and questions asked about the course. A rating system is implemented for the courses gathered from the UofT evaluations and a user can also add their own rating for a course. Additionally, a comment can be upvoted and downvoted. 

Another artifact that we will produce is our UML diagram.  We created it in Deliverable 1 but we will make many changes to it while writing our code for deliverable 2.  This artifact is very important to our backend team because it will be the outline for all of our backend code.  It will tell our backend team specifically what they need to implement.      


We will also have all of the code which we used to generate the web-app and its functionality. As an overview we have database files, backend logic files for courses and comments and the front end files for the display and interaction with the user.  This artifact is obviously very important to our team because it creates our whole web-app. 

Lastly we have our website that will be displayed in the video. At this time it is not publicly available but are thinking of making it public for the last deliverable. We want to create something that can actually be used and help students with course information and course selection. Our vision is to have this website as a go to place for UofT students when looking for course information, ratings and whether or not a given course is right for them. 
