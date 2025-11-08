# Mehreen Ali Gillani, Flask Extra Credit Assignment
from flask import Flask, request

app = Flask(__name__)

main_page = '''
<html>
<body>
    <h2>Enter a number to multiply by 5:</h2>
    <form method="POST">
        <input type="number" name="number" step="any" required>
        <input type="submit" value="Calculate">
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def multiply_number():
    if request.method == 'POST':
        number = float(request.form['number'])
        result = number * 5
        return f'<h2>Result: {number} × 5 = {result}</h2><a href="/">Back</a>'
    
    return main_page

if __name__ == '__main__':
    app.run(debug=True, port = 5001) # http://127.0.0.1:5001

