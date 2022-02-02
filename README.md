# whpool-connect

Python 3 application used to establish a simple IMAP connection to the WHCA Pool
Reports Collection gmail service account. The purpose is to prevent
Gmail from marking the Less Secure App as disabled due to no connections
within the last month.

See `https://workspaceupdates.googleblog.com/2019/07/limit-access-LSA.html`

## Requires

* Python 3

## Running the application

```bash
# create a .env file (then manually update environment variables)
cp .env-template .env
```

### Running locally

```bash
# install requirements
pip install -r requirements.txt

# run the application
python3 whpool-connect.py
```

### Running in Docker

```bash
docker build -t whpool-connect .
docker run -it --rm --env-file=.env --read-only whpool-connect
```

## License

See the [LICENSE](LICENSE.txt) file for license rights and limitations.
