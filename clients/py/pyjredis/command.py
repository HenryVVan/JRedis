from enum import Enum
from typing import Dict


class Command(Enum):
	SET = 0

	GET = 1

	DEL = 2

	EXISTS = 3

	INCR = 4

	DECR = 5

	INFO = 13

	SHUTDOWN = 14

	PING = 15


commands: Dict[str, Command] = {
	"SET": Command.SET,
	"GET": Command.GET,
	"DEL": Command.DEL,
	"EXISTS": Command.EXISTS,
	"INCR": Command.INCR,
	"DECR": Command.DECR,
	"INFO": Command.INFO,
	"SHUTDOWN": Command.SHUTDOWN,
	"PING": Command.PING,
}

