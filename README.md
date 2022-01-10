# Vocab-improver

Vocab-Improver is a Python application which gives/sends a word of the day at a certain time to improver our vocabulary.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install -r requirements.txt .

```bash
pip install -r requirements.txt
```

## Usage

```python
from random_word import RandomWords
from discord_webhook import DiscordWebhook

# returns 'word of the day'
woday = r.word_of_the_day()

# to send webhook to the device
webhook = DiscordWebhook(url='//your webhook//', rate_limit_retry=True,
                            content=f'{worday}')
response = webhook.execute()
```
## Need to make!
To Gradually improver your vocabulary day-by-day

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Brokiemag](https://brokiemag.me)
