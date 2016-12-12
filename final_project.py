from flask import Flask, request, url_for, redirect
from random import choice
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Welcome</title>
        <link rel="stylesheet" href="project_style.css">
      </head>
      <body>
        <h1>Welcome to the SeamlessDocs Savings Calculator and Leaderboard!</h1>
        <h2>What would you like to do?</h2>
        <ul>
        	<li> <a href="{{ url_for('form') }}">Find out your savings!</a> </li>
        	<li> See the Leaderboard </li>
        </ul>
      </body>
    </html>
    """



@app.route('/form')
def savings_calc():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Savings</title>
      </head>
      <body>
        <h1>Find Out Your Savings!</h1>
        <form action="/showsavings">
          What's your city name?
          <input type="text" name="city"><br>
          What's your form name?
          <input type="text" name="form"><br>
          How many submissions have you received on your form?
          <input type="text" name="submissions"><br>
          How many pages is your form?
          <input type="text" name="pages"><br>
          What is the staff member processing the form's estimated hourly wage?
          <input type="text" name="wage"><br><br>
          <input type="submit">
        </form>
      </body>
    </html>
    """

@app.route('/showsavings')
def give_savings():
	city_name = request.args.get("city")
	form_name = request.args.get("form") 
	form_submissions = float(request.args.get("submissions"))
	form_length = float(request.args.get("pages"))
	employee_wage = float(request.args.get("wage"))

	total_pages = form_submissions * form_length
	paper_savings = total_pages * .05

	employee_time_saved = ((form_submissions * 30 )/60) #hours
	employee_wage_saved = employee_time_saved * employee_wage

	total_cost_savings = employee_wage_saved + paper_savings

	return "%s has saved %s with the online %s!" %(city_name, locale.currency(total_cost_savings, symbol=True, grouping=True), form_name)

@app.route('/leaderboard')
def show_leaderboard():
  leader_board_dict={city_name:total_cost_savings}
  return leader_board_dict


if __name__ == "__main__":
  app.run(debug=True)


