from flask import Flask, render_template, request
app = Flask(__name__)

# reverse string and captialize
def reverse(username):
	return (username[::-1]).upper()

# tell Flask what URL should trigger our function.
@app.route('/', methods=['GET', 'POST'])
def index():
	html_page = 'index.html'

	# if user clicks submit
	if request.method == 'POST':	
		extract_username = request.form.get('username')
		reverse_string = reverse(extract_username)
		return render_template(html_page, message=reverse_string)
	
	# if user access URL
	if request.method == 'GET':	
		return render_template(html_page)

# main function
if __name__ == '__main__':  #
    app.run()