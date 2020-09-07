from flask import Flask, request
from bible import Bible
from checkTime import checkTime
from twilio.twiml.messaging_response import MessagingResponse

b = Bible()

verse = ""
verse = b.verse_gen()
day=4
day_af = 4
app = Flask(__name__)
@app.route("/")
def Hello():
  return "hello, world"
@app.route('/incoming', methods=['POST'])
def bot():
  incoming_msg = request.values.get('Body', '').lower()
  resp = MessagingResponse()
  msg = resp.message()
  responded = False
  global verse, day
  if 'verse' in incoming_msg: 
    global day_af
    if day != day_af:
      msg.body(verse)
      responded = True
    else:  
      day = int(checkTime())
      day_af = day + 1
      verse = b.verse_gen()
      msg.body(verse)

  return str(resp)


if __name__ == "__main__":
  app.run(debug=True)