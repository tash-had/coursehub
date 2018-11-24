# CourseHub

> _Note:_ This document is meant to be written during (or shortly after) your initial planning meeting.     
> It does not really make sense for you to edit this document much (if at all) while working on the project - Instead, at the end of the planning phase, you can refer back to this document and decide which parts of your plan you are happy with and which parts you would like to change.


## Iteration 3

* Start date: November 15, 2018
* End date: November 29th, 2018

## Process

(Optional:) Quick introduction

#### Changes from previous iteration

List the most significant changes you made to your process (if any). 


* At most 3 items
* Start with the most significant change
* For each change, explain why you are making it and what you are hoping to achieve from it
* Ideally, for each change, you will define a clear success metric (i.e. something you can measure at the end of the iteration to determine whether the change you made was successful)

> *Note:* If you are not making any changes to your process, it means that you are happy with all of the decisions you made in the previous iterations.
> In this case, list what you consider to be the most significant process decisions your team made. For each decision, explain why you consider it successful, and what success metric you are using (or could use) to assert that the decision is successful.
> 

1. Our most important process related change is we now have a fully integrated GitHub workflow, where we do work entirely with GitHub issues. Every branch we make is required to have a corresponding issue, we must mention our issue # in our PRs, and update it as we work on it if we run into roadblocks/issues. This is useful to prioritize tasks and ensure everyone is on the same page as to who is implementing what. It also allows us to to prioritize using labels, and have a clear path of what we want to accomplish. Using this, we can have a measure of our productivity (with the issues closed) and how much of our goals we have reached (using milestones).

2. Our second most imortant process related change is we now have a build pipeline using Travis CI. This provides automated user interface tests for every pull request, and any pushes to the master branch. If the tests succeed on `master`, it will trigger a build, which will then deploy to our servers. This process is a streamlined and robust solution to the previously cumbersome and unreliable process of in-depth manual reviews (since many of us would stop paying attention during code-reviews when the changes were hundreds of lines long). This process should also help keep our master branch pristine by giving a clear indicator of whether a change will break the build **before** the the merge. We will use UI Tests so we don't have to spend so much time writing seperate front-end **and** backend tests. Our UI Tests will be E2E so they test both the front and backend simultaniously. Our deployment process will make our work a lot more exciting, since we get to see our changes live on the web almost instantly after a merge. This also means backend devs don't have to ask the front end devs to see our product live. 

3. Our third most significant change for this iteration is having daily standup meetings.  In these meetings we will discuss what we have done the previous day, what we are going to do in the coming day and any problems or difficulties we had. Our daily standup meetings are held in the evenings to work around everyone's classes during the daytime. Daily meetings ensure that everyone is up to date with the current progress of our project, while holding everyone accountable. 


#### Roles & responsibilities

Describe the different roles on the team and the responsibilities associated with each role.

Nathan, Ted: back-end; processing JSON requests from the front-end and making necessary database queries.

Cullen: database; database design and implementation.

Andrew, Labib: front-end; user experience, making requests to back-end

Tash-had: Scrum master, setting up build pipeline and deployment process w/ Travis, infrastructure/domain, integration of a third party [authentication service](https://auth0.com/), writing UI tests, helping with any front-end/back-end challenges

#### Events

Describe meetings (and other events) you are planning to have:

* When and where? In-person or online?
* What's the **purpose** of each meeting?
* Other events could be coding sessions, code reviews, quick weekly sync' meeting online, etc.

Initially we had a planning meeting in BA2179 on November 15.  In this meeting we made all major decisions and laid out the framework for what we were going to accomplish in deliverable 3.  

Our weekly update meetings will take place in BA2179. We will also have coding sessions in this room where we can work together and effectively communicate instantly with other members the issues we have and the progress we are making. In our weekly meetings we will do a stand up where everyone would share their progress. 

Every night in the last week before the deadline we will have daily standup meetings held somewhere in Bahen.  The purpose of these meetings will be for everyone to say what they accomplished in the previous day, what they are going to do in the next day and any difficulties they had.  

On Thursday, November 29 at 8pm we will hold our review meeting.  We will write up our review.md document and make sure our final product is fully functional.  The reason for this meeting is to tie everything together to make our final product. 

#### Artifacts

List/describe the artifacts you will produce in order to organize your team.       

* Artifacts can be to-do lists, task boards, schedule(s), etc.
* We want to understand:
* How do you keep track of what needs to get done?
* How do you prioritize tasks?
* How do tasks get assigned to team members?


For assigning tasks to our group members we have changed our process from verbal agreement - which can be unreliable - to taking advantage of GitHub issues which are assigned to one more members during meetings. Tasks are naturally divided based on our pre-determined roles (DB, back-end, front-end) however if one group is over/underwhelmed then tasks may be shared. During our planning meeting at the beginning of the deliverable, we went through features we planned to implement for this deliverable, chunked them down into basic instructions, and made a GitHub issue for every basic instruction, complete with an asignee, and sometimes, a milestone. We found this to be a lot better than what we did previously, which was divide parts of the project into subgroups, and have the subgroups decide how to move forward. So instead of saying "Cullen, you do database", we would discuss amongst each other what functionality the database needs to have, and make issues such as "create a 'Users' table in the database with username, user_id columns". This way, we didn't underestimate/overestimate work for subgroups. This way, we also got an idea of how our tasks collide. ie. Chunking the front-end together, we decided that one of the tasks was adding functionality for users to delete comments, but we realized that this work depends on the backend work to be done first (since there isn't much to a delete-comment aside from a button). 

Another benefit of using GitHub issues is that we can assign priorities to tasks, which we decide upon based on which would be most valuable to the user in a reasonable timeframe for us as developers. For example, in this iteration we chose to implement user accounts before trying to take on fancier features such as suggesting courses based on courses the user has already taken.

#### Git / GitHub workflow

Describe your Git / GitHub workflow.     
Essentially, we want to understand how your team members share a codebase and avoid conflicts.

* Be concise, yet precise.      
For example, "we use pull-requests" is not a precise statement since it leaves too many open questions - Pull-requests from where to where? Who reviews the pull-requests? Who is responsible for merging them? etc.
* If applicable, specify any naming conventions or standards you decide to adopt.
* Don't forget to **explain why** you chose this workflow.

Our Git workflow is the result of several lessons learned from mishaps over the last two deliverables.

Firstly, as discussed in our Artifacts section, we work based on GitHub issues that were assigned to us. This way, two people don't end up working on the same thing. When we are working on a new issue, we must make a branch that includes an issue number/issue description, so that we know what that branch is for.   When someone finishes the work for a particular issue in its corresponding branch, they make a PR (which must include a link to the issue number the work is for) and request reviews from other members in the group who are familiar with the work they have done. ie. Nathan (who works on backend) would not request a review from Labib (who works on front-end) but he would request a review from Ted (who also works on backend). When a PR is made, a Travis-CI build is automatically triggered, and runs all our tests. The person who a review was requested from has to quickly go over the code submitted, looking for glaring problems or syntax mistakes (ie. camelCase in python). If they find no problems with the code, and if the Travis build is successful, they approve the PR and the person who made the PR merges when ready, and deletes the branch. When the branch is merged to master, our deployment process begins. Travis-CI runs UI tests on our master branch, and if everything is successful, creates production builds of our API and front-end, deploys our API to the backend server, and deploys our front-end to our web-app host. 

We chose to use GitHub issues because in previous deliverables, we used Trello to plan out and assign tass. What we found is that no-one kept up with Trello and it wasn't updated very frequently. This was mainly due to it being a seperate service, and thus, inconvenient. GitHub Issues was convenient, had all the right things (milestones, labels, asignees) to give us a clear picture of "whos doing what" at all times. We must name our branches after a corresponding issue to avoid having several branches with unknown purposes. We made it a requirement to include issue numebrs in PRs and branches so we avoid repeating ourselves. 

This workflow gave us a much more clear picture of what's going on at any point in time. It made it much easier to stay organized since everything was on one platform, and avoid conflicts, since we we decided and assigned tasks as a group. 



## Product

#### Goals and tasks

* Describe your goals for this iteration and the tasks that you will have to complete in order to achieve these goals.
* Order the items from most to least important.
* Feel free (but not obligated) to specify some/all tasks as user stories.

Our main goal this iteration is to implement user accounts on our web application.  This will prevent a single person from rating a comment or course multiple times.  To achieve this goal we will have to add another table in the database to store user information and store which users have already rated a comment/course.  On the frontend we will have to create a registration/login screen.  The backend will have to give input from the frontend to the database and return the necessary information.

Our second most important goal this iteration is to implement replies to comments.  This will give us all comments in tree-structures.  To do this we will have to add a parent field to comments in the database.  We will also need a backend function to generate a trees of an initial comments and all replies to them.  These trees will be sent to the frontend where we will have to take them and display them on a course webpage.


#### Artifacts

List/describe the artifacts you will produce in order to present your project idea.

* Artifacts can be text, code, images, videos, interactive mock-ups and/or any other useful artifact you can think of.
* Make sure to explain the purpose of each artifact (i.e. Why is it on your to-do list? Why is it useful for your team?)
* Be concise, yet precise.         
For example: "Build the website" is not precise at all, but "Build a static home page and upload it somewhere, so that it is publicly accessible" is much clearer.

For this deliverable we will have a functional web-app with a public domain at coursehub.ca. We will present the features of our application using a short video wherein one of our group members will demonstrate our user experience. As well, our code on GitHub will of course be an essential artifact in displaying the functionality we have implemented.
