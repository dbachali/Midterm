# Midterm
Work with your group to create the following project. You should work together as a group on a single git project but each person should make their own submission to this assignment. Include the git project, the names of your team members and your personal responsibilities.

The project should conform to the following guidelines:

1. Create a flask API hosted on AWS that is accessible to the internet at wide. It should accept cURL calls of any type[s] you choose.

2. This API should perform NLP tasks on a string submitted by the user. The API should be able to return one or all of the available NLP services.

3. Your API should be able to return 2 services per team member minus one (so in a team of 4, include 6 services or in a team of 5 include 8 services).

4. Test your API well. Provide instructions for using your API in the Readme of your git project (and/or as documentation available through your flask app). Your API should not return a 5XX error whenever possible. Do this by catching errors in the cURL call and returning 4XX errors to the user.
