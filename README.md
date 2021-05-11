# Midterm assignment to meet the following criteria:

Work with your group to create the following project. You should work together as a group on a single git project but each person should make their own submission to this assignment. Include the git project, the names of your team members and your personal responsibilities.

The project should conform to the following guidelines:

1. Create a flask API hosted on AWS that is accessible to the internet at wide. It should accept cURL calls of any type[s] you choose.

2. This API should perform NLP tasks on a string submitted by the user. The API should be able to return one or all of the available NLP services.

3. Your API should be able to return 2 services per team member minus one (so in a team of 4, include 6 services or in a team of 5 include 8 services).

4. Test your API well. Provide instructions for using your API in the Readme of your git project (and/or as documentation available through your flask app). Your API should not return a 5XX error whenever possible. Do this by catching errors in the cURL call and returning 4XX errors to the user.

# How to use this API:

*Note: To add in a "?" use "%3F" so that HTML will recognize this special character. Otherwise this API will not accecpt the "?" and the ngrams service will give a 404 error.

# Call the api via the following URL

107.20.37.178:8000

# Add the following to the base &lt;URL&gt; above to access specific services:

1. &lt;URL&gt;/

    Returns a title page and directions to help.

2. &lt;URL&gt;/help

    Displays this README file.

3. &lt;URL&gt;/test/&lt;text&gt;

    This will test that the API is running and accepting the string, &lt;text&gt;, entered by the user.

    Enter in a string of your choice for &lt;text&gt;

4. &lt;URL&gt;/sentiment/&lt;text&gt;

    This will perform sentiment analysis on &lt;text&gt;, entered by the user.

5. &lt;URL&gt;/polarity/&lt;text&gt;

    This will give a polarity for the &lt;text&gt;, entered by the user.

6. &lt;URL&gt;/subjectivity/&lt;text&gt;

    This will give a subjectivity for the &lt;text&gt;, entered by the user.

7. &lt;URL&gt;/ngrams/&lt;text&gt;/&lt;num&gt;

    This will split a given &lt;text&gt; into ngrams of a given size, &lt;num&gt;, entered by the user.

    *NOTE: num must be an integer, greater than zero and less than or equal to the number of words in the given string.

