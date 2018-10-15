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

Our first product insight was figuring out how to solve the problem of outdated and inaccessible course information, since this is a problem most students face when choosing their courses for upcoming semesters. We discussed how students currently find course information, and found that it was from UofT course pages, social media, and word-of-mouth. Thus, the idea of creating an up-to-date user disussion course "hub" that gathers all course information into a single page, was born. 

The next decision was choosing the form of our product presentation to consumers. Initially, some members thought we should create an Android app with a seperate website along with it. However, others argued against that idea, claiming an Android app was unecessary because a webapp suited to mobile devices can implement the same functionality as a standalone app - without having the need to download a standalone app. There was also the argument that if we did make an Android app, we would exclude iPhone users. Thus, in order to increase our user reachability and create a more intuitive experience for users, we decided our product will be a website that additionally works as a webapp for mobile devices.

After we chose the form of our product (website/webapp), the next key decision was choosing how users would view and interact with our page layout. We wanted to create a seamless user experience, so we opted to have a seperate page for each course that includes its key information, such as crowdsourced difficulty/industry applicable ratings, a crowdsourced explanation, and the top questions/answers. This page layout design keeps information for each course on a seperate page, acting as the central "hub" for that course. Previously we decided to open a new page once a user clicks on a course-related question, but due to our initial limited user-base, as well as wanting to keep users "in the hub", we have decided to float all responses to a question below it.

Another major decision was choosing roles for each of our team members. We had each of our members discuss their strengths and then we accordingly assigned people to back-end, front-end or database development. This way we use everyone's best abilities to use. After roles were assigned, we were able to discuss what frameworks and APIs we would be using for implementing our webapp, allowing us to choose the technologies based on our experience and to be able to focus more on implementation. With this decision, we are able to skip the additional hurdle of learning unfamiliar frameworks for our development process. 

Lastly, our design approach for building our webapp was a very important decision. We opted to start with a basic implementation of each section: our database, UI and backend. Another option could have been completing each one fully one at a time, but we decided that creating an operating MVP and subsequently adding new features as we go would be more efficient.

