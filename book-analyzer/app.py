"""Analyze new text objects uploaded to the Lab 06 book bucket."""

import logging

from chalice import Chalice

from chalicelib.analyze import analyze_book

BUCKET = "public-rau7ru"

app = Chalice(app_name="book-analyzer")
logging.getLogger().setLevel(logging.INFO)


@app.on_s3_event(bucket=BUCKET, events=["s3:ObjectCreated:*"], suffix=".txt")
def analyze_new_book(event):
    """Analyze the book identified by the incoming S3 event."""
    return analyze_book(event.bucket, event.key)

