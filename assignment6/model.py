from wtforms import Form, StringField, IntegerField, validators, SubmitField,SelectField
import functools


class InputForm(Form):
	"""
		Holds values specified by the user of the web page.
		@param 	form 	the flask request.form accosiated with the post request
	"""

	start = IntegerField(label='Starting year for visualization', default=1851,
		validators=[validators.NumberRange(min=1751,max=2012)])
		
	end = IntegerField(label='ending year for visualization', default = 2012,
		validators=[validators.NumberRange(min=1751,max=2012)])
	
	month = SelectField('Which month do you want to visualize for temperature?',choices = [('January','January'),('February','February'),('March','March'),('April','April'),('May','May'),('June','June'),('July','July'),('August','August'),('September','September'),('October','October'),('November','November'),('December','December')])

	year = IntegerField(label='Year to visualize', default=2012,
		validators=[validators.NumberRange(min=1960,max=2012)])
	
	lower = IntegerField(label='Lower threshold for carbon per capita', default=0,
		validators=[validators.InputRequired()])
	
	upper = IntegerField(label='Upper threshold for carbon per capita', default=40,
		validators=[validators.InputRequired()])

	
	plot = SelectField('Choose what to vizualize',choices=[('carbon','Carbon'),('temperature','Temperature'),('co2_per_capita', 'CO2 per capita')])

        

        

	

	
