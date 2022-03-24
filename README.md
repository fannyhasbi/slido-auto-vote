# slido-auto-vote

This script is created to automatically vote a question that is posted on Slido. Because there is no user checking and voting limit, so we can send as many vote as we like.

## Installation
1. Clone or download this repo
  ```
  git clone https://github.com/fannyhasbi/slido-auto-vote.git
  ```

2. Go to the downloaded folder
  ```
  cd slido-auto-vote
  ```

3. Install all required libraries
  ```
  pip3 install -r requirements.txt
  ```

## Usage
1. Open the event page you want
2. Copy the event slug or id in the URL
  The event URL will look like this:
  `app.sli.do/event/qwertyuiop/live/questions `

  The event id is the word string after the `event/`, which is `qwertyuiop`

3. Open the browser's Elements in Developer Tools or right-click the page and click **Inspect**

4. Search `data-qid` and choose which question you want to vote, then copy its value
  The element you searched will look like this:
  ```html
  <div class="card question-item" role="group" aria-label="Question" data-qid="987654321">
  ```

  Copy the `987654321` because it is the question id

5. Run the script
  If you decide to vote 10 times, you should run
  ```
  EVENT=qwertyuiop QUESTION=987654321 COUNT=10 python3 main.py
  ```

