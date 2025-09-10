-- create_tables_sqlite.sql
CREATE TABLE device (
  device_id TEXT PRIMARY KEY,
  name TEXT,
  location TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE sensor_type (
  sensor_type_id INTEGER PRIMARY KEY,
  type_name TEXT NOT NULL,
  unit TEXT,
  description TEXT
);

CREATE TABLE sensor (
  sensor_id TEXT PRIMARY KEY,
  device_id TEXT NOT NULL,
  sensor_type_id INTEGER NOT NULL,
  pin TEXT,
  meta TEXT,
  installed_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY(device_id) REFERENCES device(device_id),
  FOREIGN KEY(sensor_type_id) REFERENCES sensor_type(sensor_type_id)
);

CREATE TABLE reading_status (
  status_id INTEGER PRIMARY KEY,
  label TEXT,
  description TEXT
);

CREATE TABLE reading (
  reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
  device_id TEXT,
  timestamp TEXT DEFAULT (datetime('now')),
  temperature REAL,
  humidity REAL,
  accel_x REAL,
  accel_y REAL,
  accel_z REAL,
  ldr_value INTEGER,
  gas_value INTEGER,
  raw_payload TEXT,
  status_id INTEGER,
  FOREIGN KEY(device_id) REFERENCES device(device_id),
  FOREIGN KEY(status_id) REFERENCES reading_status(status_id)
);

CREATE INDEX idx_reading_ts ON reading (timestamp);
CREATE INDEX idx_reading_status ON reading (status_id);
