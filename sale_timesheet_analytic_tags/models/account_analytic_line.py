# Copyright 2022 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountAnalyticLine(models.Model):

    _inherit = "account.analytic.line"

    def _update_analytic_tags_from_task(self, vals):
        task_id = vals.get("task_id")
        if task_id:
            task = self.env["project.task"].browse([task_id])
            tag_ids = []
            if task.sale_line_id.analytic_tag_ids:
                tag_ids = task.sale_line_id.analytic_tag_ids.ids
            vals["tag_ids"] = [(6, 0, tag_ids)]

    def create(self, vals):
        self._update_analytic_tags_from_task(vals)
        return super().create(vals)

    def write(self, vals):
        self._update_analytic_tags_from_task(vals)
        return super().write(vals)
