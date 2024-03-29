***Design***:

I'm basing the test strategy off an architecture I've created

![alt text](https://github.com/werewolfbarmitzvah/sample_autocomplete/blob/master/misc/diagram.png)

A user of mobile or web client begins typing into a search field. The client (possibly after a small delay) takes what the user has entered
and makes a request to an API gateway to return autocompleted results to the user. The gateway forwards the request to a user service that
manages previous user search history and returns an autocompleted result from a (most likely) NoSQL database of various searches and search relations. For the sake of simplicity, this user service will also compare the text with relevant popular results.
In reality, it would probably be comprised of of a few services (user service, popular/targeted results service, some algorithmic helper service, caching service, a user vs popular/targetd ranker service, etc.).

***Test Strategy***:

I try to apply the theory of the test automation pyramid (https://martinfowler.com/articles/practical-test-pyramid.html) whenever possible. This involves building up your test automation with a larger amount of unit and integration/component/service testing and a smaller amount of end-to-end UI tests.

I would follow this approach for the autocomplete system:
- Run unit tests first
- Run automated integration/component/service tests
- UI tests would be run against a build that has shown to have the required functionality coverage and test success rate on the unit and systems test level
- Any manual testing could procede after the automated UI tests
- In my experience, most performance type tests require a little more work in setting up testing infrastructure. These could be run ad hocly as part of the development phase before release but not as part of a CI pipeline (possibly being included as part of a CI pipeline in the future)

***Tests***:

Some possible service tests could be for:

- A basic, successful request to the Gateway API
- Autocomplete results returned when authenticated vs when not authenticated
- Past user autocompletes are returned
- Popular/targeted user autocompletes are returned
- Past autocomplete expiration (i.e. if you only search once for something an autocomplete for that search will not appear after a certain time)
- New searches update the possible autocompletes
- Negative tests (invalid user, invalid auth, bad request, etc.)
- Only X number of autocompletes are returned

A few UI tests could be:

- I enter text, do I see an autocomplete?
- Can I search by an autocomplete?
- Navigation from a search page to the results page
- If I enter an invalid word, does the app alert me to a possible alternative search?

A few performance type tests could be:
- Latency of returned response from the server to the client
- How does the system handle the load of many requests in a distributed environment?
- How does the system handle the unexpected outage? If a service goes down, does the system handle that by bringing another one up?

For this project I will be writing a pseudocode example test for an end-to-end service side test that makes a request via the gateway API and verifies a result. The only component not involved is a UI. Since there is not real system (there are no unit tests or component tests), this would provide a nice "bang for you buck" in a situation where those are still in progress (i.e. mocking components are being worked on)

***Tools***:

All the service testing requests can be done through an HTTP client library. Tests would be written using a testing framework (pytest, junit, etc.). Could leverage BDD, but not required.

UI tests might also need to leverage an HTTP client library (ideally, they would mostly be run against mocks). The tests could use a testing framework such as Appium. Appium would allow (for the most part)
the ability to reuse tests across web and both mobile platforms.

***Build and run tests***:

NOTE: This is a pseudocode, sample project. It will build, but the project does not do anything.

Verify you have python 3.6 >= installed.

python -m venv env

source env/bin/activate

python setup.py install

pip install tox

tox lint

pytest autocomplete_tests.py (will not work)


***Additional Work***:

This is work (besides actual functionality) that could be added.

- BDD using cucumber
- Dockerfile
- Unit tests
