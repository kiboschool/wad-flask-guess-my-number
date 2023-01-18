# Gradescope config

Docs: https://gradescope-autograders.readthedocs.io/en/latest/python/#dependencies-for-tests

## Writing tests for Gradescope

0. Write a solution
1. Write unittest-compatible tests that the solution passes
2. import the gradescope-utils and add weights to the tests
3. Double-check that the tests don't specify anything that isn't in the instructions in the student-facing README.

## Autograder config steps

1. Add project dependencies to `gradescope/requirements.txt`
2. `cd gradescope; ./make_zip.sh`
3. Upload `gradescope.zip` to the autograder
4. Zip and upload the solution as a submission for a test student, to check that everything is working as expected.

Don't commit the zip file, you can just remove it.

## What will Gradescope do?

- when you upload gradescope.zip, it will unzip and run `setup.sh`
- when a student makes an upload, it will run `run_autograder`
- That runs `run_tests.py`, which finds and runs the tests and formats the output for Gradescope
- Gradescope uses that output as the scoring for the submission
