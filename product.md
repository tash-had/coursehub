# YOUR PRODUCT/TEAM NAME

 > _Note:_ This document is meant to evolve throughout the planning phase of your project.    
 > That is, it makes sense for you commit regularly to this file while working on the project (especially edits/additions/deletions to the _Highlights_ section).

#### Q1: What are you planning to build?

Our project is a crowdsourced forum to help UofT Students choose courses. Currently, while navigating the ocean of UofT courses, you have to resort to sparse or biased sources like Reddit and word-of-mouth for suggestions. We want to help people have a more objective source of course information by aggregating over the opinions of many.  This website/webapp would provide an accessible resource for up to date course information which is constantly evolving. From our own experience, we know how overwhelmed students get when trying to find the right courses in an atmosphere which is both competitive and rapidly changing. We want to remedy this stressful situation with a trustworthy hub for all course-related information, wherein users can ask questions, get answers from more experienced students, and due to the ability to “vote” on all comments, actually trust the answers they get.

Currently we have one mockup for a single course, built by our front-end team. It can be seen [here](https://i.imgur.com/Q86CPfI.png)

#### Q2: Who are your target users?

Meet our friend Billy. Billy is a high school graduate who feels overwhelmed when he reads through the vast quantity of courses offered by UofT. He tries asking his friends but they are just as lost as he is. The UofT course calendar only addresses topics that will be covered, and not the level of difficulty or personality fit of the course.  While reading online forums e.g. Reddit, he finds outdated information. With no other info sources, he chooses his courses mostly at random which leads to a suboptimal educational experience.

Meet our friend Rachel. Rachel has just finished second year and has been frustrated by the bad course suggestions she has received from her friends. Given the competitive nature of course selection at UofT, she does not want to select courses she knows will be difficult to switch out of. 

#### Q3: Why would your users choose your product? What are they using today to solve their problem/need?

When picking courses, students are generally using Reddit, course evaluations, RateMyProf, and word-of-mouth to choose courses.  Our product will be superior because it will have all information about courses organized into one spot, saving hours of time that users would otherwise spend using search engines to check the reliability of their information.  Further, the ability to evaluate (“vote on”) the information provided by other users will inherently allow for greater accuracy and trustworthiness.  Information from word-of-mouth is not always reliable, as they can be based off very few sources. However with our voting system, users will be able to see a rating of any comment or review based off of multiple other users.  This will ensure that sources of information have more than one "opinion" on them.  

----

### Highlights

First we discussed what frameworks and APIs we would be using for implementing our webapp. We chose the technologies based on what we have the most experience with in order to be able to focus more on implementation. Python, SQL, and Angular 6 will be used to develop our course evaluation app. We have members who are comfortable with each of these technologies, so we can skip the additional hurdle of learning new frameworks for our development process. 

Our next major decision was deciding the main layout of our web page. We opted to have a page for each course which will have key information about the course such as its rating, a quick explanation and the questions for the course. Previously we decided to open a new page once a user clicks on a question, but due to our initial limited user-base, we have decided to float all responses to a question below it.

Another major decision was choosing roles for each of our team members. We had each of our members discuss their strengths and then we accordingly assigned people to back-end, front-end or database development. This way we use everyone's best abilities to use. 

Lastly, our design approach for building our webapp was a very important decision. We opted to start with a basic implementation of each section: our database, UI and backend. Another option could have been completing each one fully one at a time but that is less efficient as this way we can get an operating MVP and add new features as we go. 
