# How to use instagram mass reporter
clone the repository : git clone https://github.com/Mtension420/instamassreporter.git or Download zip file.
make Two text file in same folder 1. insta accounts for reporting 2- proxies 
enter proxies like http://127.0.0.1:8080
format of insta account like username:password
# flow of script
Enter the path to the TXT file with Instagram credentials (username:password): credentials.txt
Enter the path to the TXT file with proxies (http://proxy:port): proxies.txt
Enter the username to report: example_user
# Logging In and Reporting:

The program will use the first proxy (http://proxy1:8080) to log in with user1:password1, report example_user for spam, and then log out.
At the same time (in another thread), it will use the second proxy (http://proxy2:8080) to log in with user2:password2, report example_user for spam, and log out.
# Summary:
The program logs into Instagram accounts using proxies and reports a specific user for spam.
It uses multithreading to handle multiple accounts simultaneously.
Errors are handled gracefully, with each failed attempt printing a clear error message.
