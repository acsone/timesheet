# -*- coding: utf-8 -*-
##############################################################################
#
#    This module copyright (C) 2015 Therp BV <http://therp.nl>.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Print employee timesheets",
    "version": "8.0.1.0.0",
    "author": "Odoo Community Association (OCA),Therp BV",
    "license": "AGPL-3",
    "category": "Human Resources",
    "summary": "Lets you print timesheets per employee and month",
    "depends": [
        'hr_timesheet',
    ],
    "data": [
        "report/hr_analytical_timesheet_employees.xml",
        "wizard/hr_analytical_timesheet_employees.xml",
    ],
    "qweb": [
    ],
    "test": [
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
    "external_dependencies": {
        'python': [],
    },
}
