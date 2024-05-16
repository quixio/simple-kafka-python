# Python and Kakfa with QuixStreams

Supporting code for our Youtbue tutorials

# A Simple Producer

[![YouTube Playlist Thumbnail](producer_thumbnail.png?raw=true)][youtube-producer]
There's a complete [walkthrough video here][youtube-producer]. To run the code in this repo:

```sh
# Set up an environment.
cd send_to_kafka
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Run the producer.
python3 main.py
```

# A Simple Consumer

[![YouTube Playlist Thumbnail](consumer_thumbnail.png?raw=true)][youtube-consumer]
There's a complete [walkthrough video here][youtube-consumer]. To run the code in this repo:

```sh
# Set up an environment.
cd read_from_kafka
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Run the consumer.
python3 main.py
```

### TODO!

[youtube-producer]: https://youtu.be/D2NYvGlbK0M
[youtube-consumer]: https://youtu.be/eCsSAzTy5cE
