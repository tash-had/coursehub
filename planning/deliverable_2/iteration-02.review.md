# CourseHub

## Iteration 02 - Review & Retrospect

 * When: November 2, 2018
 * Where: BA6180

## Process - Reflection

#### Decisions that turned out well
 
1. Splitting up into groups.  Our three groups were: frontend, backend and database.  This made it easier to organize the work that had to be done.  It is easier to organize a small amount of work between 2-3 people as opposed to having 6 people trying to tackle the entire project together. 
1. Holding weekly group meetings in addition to the weekly tutorial.  This allowed all of the subgroups to check-in and report their progress.  We also met up within our sub-groups to report on progress and decide what needed to be done.  This decision was successful because it kept everyone up to date and ensured everyone knew exactly what their task is.
1. having several group programming sessions. This allowed us to be much more efficient, because when we faced issues that involved another group members part, we were able to ask the member right away. We had organized meetings in private room at Bahen, allowing direct correspondence with one another. Since all of our code is very interconnected it was important to be able to resolve issues and questions between different group members immediately. 
1. Scraping the UofT Course Evaluation's from UofT's undergraduate course evaluation website. This was a great idea because if we hadn't done this, we would be depending on our users to write comments for courses to attract other users (there's nothing special about a course rating website with no course ratings). Now, having imported ratings from thousands of respondents through several sessions of every course at UofT, we have a sizeable dataset to provide ratings for courses, and we don't need to rely on new users volunteering their time to rate courses. 

#### Decisions that did not turn out as well as we hoped
 
1. Initially, having only Labib on front-end turned out to be totally insufficient, as we underestimated the amount of work that this would be. Ultimately, Tash-had and Andrew put in many hours assisting in this part of the project while Nathan, Ted, and Cullen worked on the backend/database.
1. Meeting once a week and this wasn't good enough as we needed to communicate more often and express our challenges to other team members. We then opted to meet multiple times per week. Near the end we met 3-4 times in a week to ensure the code was robust, all goals were met and the web-app was working correctly.

#### Planned changes
 
1. Most important process-related change that we will make: One decision that proved to be misguided was to delay coding and committing changes until the past week or so. The reason for this was because we were all busy with midterms, however in retrospect it would seem that putting in only a small amount of work on a consistent basis would have helped us have a clear focus and put us at less risk of not completing our MVP. In the future we should avoid spending more than a week without meeting and/or committing changes to the codebase.
1. Another process-related change that we will make:  Initially we didn’t not give team members specific enough tasks.  After our first meeting we split off into groups for the backend, frontend, and database.  From there we held meetings within our subgroups to decide specifically what everyone should do.  The only problem with this was we did not hold our meetings within our subgroups immediately after our initial meeting.  This left us with some time where group members did not know specifically what they should implement.  This wasted precious time until the deadline.  For future deliverables we will immediately assign very specific tasks to every team member.  
1. Another process-related change we will make is keeping our [Trello board](https://trello.com/b/QOjo3VHX/csc301) up to date with every meeting. This way, we won't waste time if someone misses a meeting, or trying to remember what we discussed in a previous meeting. 
1. Make use of GitHub issues so we have a solid issue tracking system, and not have several group members run into and report the same bug. 

## Product - Review

#### Goals and/or tasks that were met/completed:

The most important goal that we met was completing the MVP (all code in GitHub repo): 

1. **Implemented a functional database** which is the basis for our source of information. This is crucial to our website as all course information and comment information is stored in it and allows proper persistence of the data. We currently have two tables one for courses and one for comments. In our final iteration we will most likely add a user database table, so we can start the process for user accounts. 
1. **Set up of the backend** was also important so that we have all of the logic for getting courses and comments from the database. Here, the database does queries based on the information we need to acquire and give to the front-end.  We implemented the backend code based on our [UML diagram](https://drive.google.com/file/d/1m6DPvzWu5L10WlaltwL3CrcNGazQQ7-A/view?usp=sharing) 
1. **The front-end** is important to visualize all of the information in a clean manner for the users. We wanted to have to logic implemented first so that the front-end had all the information it needed to display the courses and comments.

Our other main goal of completing the video was completed:
	[This](https://www.youtube.com/watch?v=cWvscooP2Ao&feature=youtu.be) is the link to our video.
	[Here](https://docs.google.com/document/d/1ct0GLvdP1TsfQiNHcfIvCtAZUAlxfRm4cf7fKQ3mErQ/edit?usp=sharing) is the link to our script.

A secondary goal that we met was meeting weekly:

1. Our weekly meetings outside of tutorial were also completed and were needed to communicate our issues and successes. Without these meetings we would be left in the dark as to the true status of each part of the project and the more fine details of how the development process is going. 
1. Our third most important goal that we met was implementing comment and class ratings:
1. We added the ability to upvote/downvote a comment and implemented a basic rating system for the courses.  

#### Goals and/or tasks that were planned but not met/completed:
   
   We completed all our goals that we planned.

## Meeting Highlights
 
   First of all, we will implement more advanced features on top of our MVP that we have created for deliverable 2.  These include (but are not limited to)
   
1. Comment Types (Replies, Reviews, Q&As) 
1. A more aesthetic, and bug-free UI 
1. All courses available on our web-app (not just CSC courses). As such, for deliverable three any course will be able to be searched for that is offered at UofT and then users can make questions for that course, rate it and reply to others that have questions. 
1. Add functionality to allow user's to create accounts 
1. Convert all account specific endpoints (posting comments, upvoting, downvoting, rating courses, replying) to `POST` requests as opposed to insecure `GET` requests. 
1. Allow users to rate courses using the same rating categories as the UofT Undergrad Course Evaluation Page (And show total respondents), so people are more trusting of our reviews) 
1. Get users to write review courses they've already taken (by asking nicely, and periodically, possibly through email)
1. Make our product responsive accross screen sizes 
1. Integrate some sort of testing suite so we can have stop having broken code be pushed to master
1. Make every course have some sort of perma link, instead of having the data all be passed in the background to a general page called `/course-view`. This way, users can share course pages amongst eachother. 
