'''
Run the app
'''

from app import *

if __name__ == "__main__":
    app.debug = True
    
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.logger.info("Starting flask app on %s:%s", host, port)
    app.logger.info("Database on: %s", app.config['DATABASE'])
    
    app.run(host=host, port=port)