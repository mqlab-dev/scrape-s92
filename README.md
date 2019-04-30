# scrape-s92

## Description

The script automate the tasks below:

- Log in to your LinkedIn account
- Google search the targeted LinkedIn user profiles with your custom query or from connections.csv file you exported from your LinkedIn account.
- Connect to the LinkedIn members in the search result.

## Requirements

### Accounts & Browser

- [LinkedIn](https://www.linkedin.com) Account
- Download Chrome browser and driver
- Create params.py with LinkedIn credentials, Chrome driver path and search query.

### Ensure pipenv is installed

```bash
$ pipenv --version
```

### Next, activate the virtualenv and install all requisite packages:

```bash
$ pipenv shell
(scrape-s92) $ pipenv install -r dev-requirements.txt --dev
(scrape-s92) $ pipenv install -r requirements.txt
(scrape-s92) $ python app/script.py
```

### Run tests (In progress)

```bash
(scrape-s92) $ python -m unittest tests/test_script.py
```

### Tip

- The script might add more functionality later on, but be careful for now, don't get banned!
