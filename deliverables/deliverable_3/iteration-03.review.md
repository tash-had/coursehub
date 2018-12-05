# CourseHub


## Iteration 3 - Review & Retrospect

* When: Thursday, November 29, 2018
* Where: BA2179

## Process - Reflection


#### Decisions that turned out well



Our most important decision was implementing a [Travis](https://travis-ci.com/csc301-fall-2018/project-team-19/builds/ ) CI which automatically tests our current build by running a series of e2e UI tests. This saves us time as we do not have to write several unit tests as the e2e tests do it for us. Implementing this feature initially took a lot of time, but in the long run it saved us a lot time in writing unit tests so we could allocate this extra time to better software engineering and developing the product. 

Our second most important decision was using GitHub issues.  For every ticket, we created a GitHub issue and assigned it to the appropriate team member.  Our use of GitHub issues can be viewed on our [GitHub](https://github.com/csc301-fall-2018/project-team-19/issues). Before we were tracking issues on trello but this was not as effective. Doing the issues on github allowed us to integrate them and keep track of the issues as we correlated each branch and pull request with the associated issue(s). This process related change helped us to keep track of current issues and completed issues considerably better. Along with the Github issues, we also introduced milestones on Github which allowed us to group related issues together and organized our goals.

#### Decisions that did not turn out as well as we hoped



Our biggest process related change that was unsuccessful were UI tests. Although the Travis CI is great, for scaling purposes unit tests would be better as the UI tests were flaky and would fail and then work upon a restart. In addition, the UI tests are much slower compared to unit tests. Unit tests are more reliable and next time implementing the Travis with unit tests would be a better decision to ensure even more correct functionality of the application. 

Our second biggest process related change that was unsuccessful was having too many issues initially in one place. It was overwhelming as there was a giant list of issues with no organization to them, but then we used the github [milestones](https://github.com/csc301-fall-2018/project-team-19/milestones ) to group the issues into categories for certain features. 


#### Planned changes



As stated above, were we to take on another iteration, we would use unit tests rather than UI tests. As well, we would likely aim for a "sweet spot" for how frequently to have group meetings. Previously we had been meeting at most once a week which was inadequate, so for this iteration we decided to meet daily; we have realized this is simply too much to ask from our busy group members, and further it is difficult to write enough code in one day to justify another meeting the next day. 



## Product - Review

#### Goals and/or tasks that were met/completed:




The most important goal that was completed was implementing user accounts.  With user accounts, users are limited to voting on courses/comments once and each comment posted will show who posted it.  On [our website](coursehub.ca) you will see that all comments have an associated user who posted it and you can create and sign into an account.  

The second most important goal that we completed was allowing replies to comments.  We implemented recursive algorithms to generate comment trees.  This was an important goal that we completed because it is very important for users to give feedback and engage in debate.  On [our website](coursehub.ca) on each of the course webpages, you can view our implementation of comment trees by leaving replies to other comments.  


#### Goals and/or tasks that were planned but not met/completed:




Our most important feature that we did not implement was allowing users to record which courses they have taken. We were going to use this information to indicate whether commenters had already taken the course or were only considering enrolment. This would be useful for communicating to users whose comments could be taken as legitimate advice. We were not able to implement this feature due to the time constraint, and since we would have been unable to validate the users' selections of courses they had taken. In any case, we wanted to focus on the core features first.

Our second most important feature that we did not implement was allowing a user to delete a comment. This one is self-explanatory, and we could not accomplish it simply due to time constraints. One last feature which we had not the time to complete to our satisfaction was user profiles, as we were unhappy with the general lack of information about each user which we were able to display.

## Meeting Highlights


First, we could implement unit tests in the Travis CI instead of the flaky UI tests. As mentioned above we highlighted to cons of the UI tests but overall Travis CI is an extremely useful tool for testing our current build. 

Second, we could implement the tasks that we did not get to which would make the application even more useful. As we mentioned above, these are allowing a user to delete a comment that they made and allowing users to add courses they have taken which will show up in replies to comments for certain courses (the ones they have taken).

### Video
[Link](https://drive.google.com/uc?id=1T0_sFZ-0sWwsgNZdW8ovBNymmS7dNnDj)
