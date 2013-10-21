--
--  CREATE TABLE TO STORE ANY URLS POSTED
--
CREATE TABLE websites (
  ws_id INTEGER PRIMARY KEY AUTOINCREMENT,
  ws_date DATE,
  ws_user VARCHAR(12),
  ws_chan VARCHAR(50),
  ws_url VARCHAR(500),
  ws_localfile VARCHAR(500)
)
/
CREATE INDEX wsindex ON websites(ws_url ASC)
/
