from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase


class AboutController(ControllerBase):
    @staticmethod
    def get():
        name = "Sagar Alande"
        school="New Jersey Institute of Technology"
        edu="Masters"
        Specs="Data Science"
        return render_template('about.html', name=name, school=school, edu=edu, Specs=Specs)
