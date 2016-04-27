from flask.ext.script import Manager, Shell

from config import ConfigObject
from app import app 

if __name__ == '__main__':
	app = app 
	app.config.from_object(ConfigObject)
	manager = Manager(app)
	def make_shell_context():
		return dict(app = app)
	manager.add_command("shell", Shell(make_context=make_shell_context))
	manager.run()