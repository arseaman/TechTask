1. Run test with command 'pytest'
2. Added different logs to each test case to make it more informative and easier to debug
3. 'AUTHORIZATION_TOKEN' added to environment variables:
   - To run tests locally you need to create .env file in the root of project and add variable AUTHORIZATION_TOKEN={your_token_here}.
   - To run in GitHub Actions you need to add this variable in repository secrets with the same name 'AUTHORIZATION_TOKEN'.
4. Added tests.yml file to run this tests in GitHub Actions with storing artifacts with test results