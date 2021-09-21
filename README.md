# PII (Personal Identifiable Information) and secret check hooks for pre-commit

## Installation
Install pre-commit - [Install pre-commit](https://pre-commit.com/#install)

Make sure you run:

    pre-commit install
    pre-commit autoupdate

## Setting up
 * Copy `.pre-commit-config.yaml` to your repo, or if using pre-commit already, add the hooks from this project to your existing file
 * Add a `.pii-secret-exclude` file if needed (explanation below)
 * Add a `.pii-custom-regex` file if needed (explanation below)
 * Add a `.pii-ner-exclude` file if needed (explanation below)
 
## Tracking exclusions
A file is written to, which should be included in committed files, which records a hash of
files checked by the hooks.
 
## Excluding files with .pii-secret-exclude
In order to exclude files from the checks, add them to this file. HOWEVER, you should 
heavily favour excluding lines using `#PS-IGNORE`, rather than files.

## Adding your own regular expressions with .pii-custom-regex
Add our own regexes for secret or PII identification. Each one should be added one per line in the format:

    name=regex

Regexes used should be Python compatible and should not use start and end markers.

## Excluding false positives from the NER hook
Add your own list of entities that should be excluded in the .pii-custom-ner-exclude file.

## Initial run
Run the following command to identify issues in your repo.

    pre-commit run --all-files

If PII or a secret is found is a false positive, add `#PS-IGNORE` (put this in a 
comment if needed) to any affected lines or, if you are certain a file can be 
excluded and will not change in the future, add it to the `.pii-secret-exclude` file.

## When committing
This logic should be run on every commit. When you find a false positive. Add 
`#PS-IGNORE` to the affected line or exclude the file (see caveats above).

Please report issues and bugs to the Live Services Team.

## Updating the hooks
In order to run the latest version of these hooks run:

    pre-commit autoupdate

## TODO
 * Group issues at end of output rather than displaying amongst ignore messages
 * Add office (and any other relevant) extensions
 * Add help command
