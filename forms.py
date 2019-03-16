from wtforms import Form, Field, TextField, TextAreaField, validators, StringField, DateField, SubmitField
from wtforms.widgets import TextInput

# Taglist field to store CSV list of items
class TagListField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []

#Field form
class MedicalForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    surname = TextField('Surname:', validators=[validators.required()])
    dob = DateField('Date of Birth:', validators=[validators.required()])
    nationality = TextField('Nationality:', validators=[validators.required()])
    blood_type = TextField('Blood type:', validators=[validators.required()])
    languages = TagListField('Languages:', validators=[validators.required()])
    medications = TagListField('Medications:')
    allergies = TagListField('Allergies:')
    diseases = TagListField('Diseases:')
    vaccines = TagListField('Vaccinations:')

