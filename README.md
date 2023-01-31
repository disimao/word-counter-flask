# Word Counter

## Goal

As a user when I view the application:
  * then I see a form containing a text box to enter a body of text 
  * when I submit the form with some text then I see a result containing the number of words in the text box
  * when I submit the form with an empty text then I see a form error telling me that some text input is required.

## Setup

	$ python3 -m venv .venv

	$ source .venv/bin/activate

	$ pip install -r requirements.txt

	$ flask run -p <YOUR_FAVORITE_HTTP_AVAILABLE_PORT>

## Testing

	$ python3 -m unittest discover ./

## Limitation

  * It will not count Chinese words. For that I might be useful to check out https://github.com/fxsjy/jieba usage
  * Empty text validation is not on server side
