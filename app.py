from flask import Flask, render_template, request, redirect, url_for, abort
import os
import markdown

# Initialize Flask app
app = Flask(__name__)

# Route for homepage
@app.route('/')
def index():
    # List all markdown files in the posts directory
    posts = os.listdir('posts')

    # Render the 'index.html' template, passing in the list of posts
    return render_template('index.html', posts = posts)

# Define the route for viewing individual blog posts
@app.route('/post/<string:post_name>')
def post(post_name):
    # Construct the path to the markdown file
    post_path = f'posts/{post_name}.md'

    # Check if the file exists
    if os.path.exists(post_path):
        # Open and read the markdown file
        with open(post_path, 'r') as f:
            content = f.read()
        
        # Convert markdown content to HTML
        content = markdown.markdown(content)

        # Render the 'post.html' template
        return render_template('post.html', content = content, post_name = post_name)
    else:
        # If the file doesn't exist, return a 404 error
        abort(404)

# Run the app
if __name__ == '__main__':
    app.run(debug = True)