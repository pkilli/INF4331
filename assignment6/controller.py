

from flask import Flask, render_template, request
from temperature_CO2_plotter import plot_CO2, plot_temperature, plot_CO2_per_country
from model import InputForm

app = Flask(__name__)

# View
@app.route('/assignment6', methods=['GET', 'POST'])
def index():
	"""
	Function renders web page. Handles input from web page and sends values that is objects of
	class InputForm to temperature_CO2_plotter for files to load up to the wab page.
	@return A web template with plots choosen by user.
	"""
	form = InputForm(request.form)
	if request.method == 'POST':
		if form.plot.data == "carbon":
			result = plot_CO2(form.start.data,form.end.data)
		elif form.plot.data =="temperature":
			result = plot_temperature(form.start.data,form.end.data,form.month.data)
		elif form.plot.data == "co2_per_capita":
			result = plot_CO2_per_country(form.year.data,form.lower.data,form.upper.data)
	else:
		result = None	
	
	return render_template('view.html', form=form, result=result)
	
if __name__ == '__main__':
    app.run(debug=True)

