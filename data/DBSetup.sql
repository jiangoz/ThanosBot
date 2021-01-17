-- Table members
CREATE TABLE IF NOT EXISTS "members" (
	"userID"	TEXT,
	"joined_server_at"	DATETIME,
	"created_at"	DATETIME,
);

-- Table messages
CREATE TABLE IF NOT EXISTS "messages" (
	"messageID"	TEXT,
	"userID"	TEXT,
	"actualContent"	TEXT,
	"cleanContent"	TEXT,
	"channelID"	TEXT,
	"created_at"	DATETIME,
	"jumpURL"	INTEGER
);


