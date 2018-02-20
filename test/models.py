# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime

class Student_data(models.Model):

	_name="student.data"

	name=fields.Char(string="Name")
	rollno=fields.Integer(string="Rollno")
	gender=fields.Selection([('male','Male'),('female','Female')],string="Gender")
	mobile=fields.Char(string="Contact_no:")
	
class Courses_data(models.Model):

	_name="courses.data"

	name=fields.Char(name="name")
	startdate=fields.Date(name="startdate")
	enddate=fields.Date(name="enddate")
	duration=fields.Integer(name="Duration",compute="compute_duration")

	@api.depends("startdate","enddate")
	def compute_duration(self):
		for line in self:
			if line.startdate and line.enddate:
				start_year=datetime.strptime(line.startdate,"%Y-%m-%d").date().year
				end_year=datetime.strptime(line.enddate,"%Y-%m-%d").date().year
				line.duration=end_year-start_year
