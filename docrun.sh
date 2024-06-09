#!/bin/bash

export build_doc_date=$(date -u '+%d.%m.%Y')
export COMMIT_DATE=$(<server/COMMIT_DATE)
export COMMIT_HASH=$(<server/COMMIT_HASH)

mkdocs serve