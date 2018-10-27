# Setup

# Inital 
1. Open **the api folder** with PyCharm (Open Project -> **project-team-19/coursehub-api**)
1. Ensure your PyCharm is set to Python 3.6
1. Have a look at the app.py
1. Run the project
1. When you run it, in the bottom, in the run log, it will tell you the address on which your server is running, click the address
1. Put `/api/v1.0/hello` at the end of the URL in your addressbar
1. You should see a response from the `test_endpoint` function in `app.py`
1. In the `test_endpoint` function, change something, like `"hello world" -> "hello curious george"` and save the file
1. **You do not need to re-run the project**. When you save the file, PyCharm automatically detects your change and restarts it for you (this is called hot-reloading)
1. Refresh the page you opened earlier and you should see your new message 

# Sending Parameters 
1. We'll talk about [Postman](https://www.getpostman.com/) during our next meeting.