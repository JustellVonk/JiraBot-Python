from jira import JIRA

options = {
    'server': 'https://pmc.acronis.com/'
}
print('Login:')
login = input()
print('Password:')
password = input()
basic_auth = (login, password)

jira_instance = JIRA('https://pmc.acronis.com/', options, basic_auth)
issues = jira_instance.search_issues('reporter=alena.leonova')

print(issues)