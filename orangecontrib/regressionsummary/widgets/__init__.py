import os
from Orange.widgets.widget import WidgetMetaClass

# Category info for Orange Canvas
NAME = "Regression"
DESCRIPTION = "Regression Tools"
BACKGROUND = "#D5E8D4"
ICON = os.path.join(os.path.dirname(__file__), "icons", "category.svg")
PRIORITY = 10

# Register widgets in this category
WIDGETS = ("OWRegressionSummary", "OWBackwardElimination")