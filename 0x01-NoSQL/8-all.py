#!/usr/bin/env python3
"""interpreter used."""


def list_all(mongo_collection):
  """
  Python function that lists all documents in a collection
  Returns:
  lists all documents in mongo_collection
  """
  documents = mongo_collection.find()
  document_list = list(documents)
  return document_list
