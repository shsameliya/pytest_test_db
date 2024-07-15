from project import create_app
import os


# app = create_app()
# if __name__ == "__main__":
#     app = create_app(host='127.0.0.1', port=5001)
#     app.run(host=app.config.get('HOST', '127.0.0.1'), port=app.config.get('PORT', 5000))
# app.run(debug=True, port=5001)

#     app = create_app(host='127.0.0.1', port=5001)
#     app.run(host=app.config['HOST'], port=app.config['PORT'])
if __name__ == "__main__":
    app = create_app()
#     # Set environment variables
#     os.environ['FLASK_RUN_HOST'] = '127.0.0.1'
#     os.environ['FLASK_RUN_PORT'] = '5001'

