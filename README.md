# Zendesk-Internship-Challenge

## Framework used

- Python >= 3.4.1

## Installation

### Running

Click here for more information on using pip and installing a virtual environment.

```py
$ python3 -m venv venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
```

Next, you have to set the following environment variables in your `.env` file.

```
ZENDESK_EMAIL="zendesk production account email"
ZENDESK_PASSWORD="zendesk production password"
ZENDESK_SUBDOMAIN="zendesk production subdomain"
```

After having done that, simply run the app by running the command `python zendesk.py`

## Testing

In order to run tests, the following environment variables are necessary:

```
ZENDESK_TEST_EMAIL="zendesk test account email"
ZENDESK_TEST_PASSWORD="zendesk test account password"
ZENDESK_TEST_SUBDOMAIN="zendesk test account subdomain"
```

Once finished, run the command `python -m unittest tests`
