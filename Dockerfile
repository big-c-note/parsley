FROM python:3.7
# Make directory.
RUN mkdir /parsley
# Work from the root of the repo.
WORKDIR /parsley
# Copy the requirements.
COPY requirements.txt requirements.txt 
# Install python modules.
RUN pip3 install -r requirements.txt
# Copy everything else.
COPY . /parsley
RUN pip install -e .
# Setup tests.
RUN pip install pytest-cov
ENV CC_TEST_REPORTER_ID=${{ secrets.CC_TEST_REPORTER_ID }}
RUN curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter 
RUN chmod +x ./cc-test-reporter
RUN ./cc-test-reporter before-build
CMD ["/bin/bash"]
