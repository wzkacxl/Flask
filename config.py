import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	#app.config['SQLALCHEMY_COMMIT_ON_TREADOWN'] = True
	SQLALCHEMY_COMMIT_ON_TREADOWN = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'wangzhankangwudi@126.com'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

	@staticmethod
	def init_app(app):
		pass

	class DevelopmentConfig(Config):
		DEBUG = True
		MAIL_SERVER = 'smtp.126.com'
		MAIL_PORT = 25
		MAIL_USE_TLS = True
		MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
		MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
		SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
			'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')

	class TestingConfig(Config):
		TESTING = True
		SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
			'sqlite:///' + os.path.join(basedir,'data-test.sqlite')

	class ProductionConfig(Config):
		SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
			'sqlite:///' + os.path.join(basedir,'data.sqlite')

	Config = {
		'development': DevelopmentConfig,
		'testing': TestingConfig,
		'production': ProductionConfig,

		'default': DevelopmentConfig
	}
