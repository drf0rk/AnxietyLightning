""" WidgetFactory Module | by ANXETY """

from IPython.display import display, HTML
import ipywidgets as widgets
import time

class WidgetFactory:
    # INIT
    def __init__(self):
        self.default_style = {'description_width': 'initial'}
        self.default_layout = widgets.Layout()

    def _validate_class_names(self, class_names):
        """Validate and normalize class names."""
        if class_names is None:
            return []

        if isinstance(class_names, str):
            return [class_names.strip()]

        if isinstance(class_names, list):
            return [cls.strip() for cls in class_names if cls.strip()]

        self._log(f"Invalid class_names type: {type(class_names).__name__}", 'WARNING')
        return []

    def add_classes(self, widget, class_names):
        """Add CSS classes to a widget."""
        classes = self._validate_class_names(class_names)
        for cls in classes:
            widget.add_class(cls)

    # HTML
    def load_css(self, css_path):
        """Load CSS from a file and display it in the notebook."""
        try:
            with open(css_path, 'r') as file:
                data = file.read()
                display(HTML(f"<style>{data}</style>"))
        except Exception as e:
            print(f"Error loading CSS: {e}")

    def load_js(self, js_path):
        """Load JavaScript from a file and display it in the notebook."""
        try:
            with open(js_path, 'r') as file:
                data = file.read()
                display(HTML(f"<script>{data}</script>"))
        except Exception as e:
            print(f"Error loading JavaScript: {e}")
            
    def create_html(self, value, class_names=None):
        widget = widgets.HTML(value=value)
        self.add_classes(widget, class_names)
        return widget

    def create_header(self, value):
        return self.create_html(f'<h2>{value}</h2>', 'header')

    # Widgets
    def _create_widget(self, widget_class, description, class_names=None, style=None, layout=None, **kwargs):
        """Create a widget with default styling and layout."""
        style = self.default_style if style is None else style
        layout = self.default_layout if layout is None else layout

        widget = widget_class(description=description, style=style, layout=layout, **kwargs)
        self.add_classes(widget, class_names)
        return widget

    def create_text(self, description, placeholder, class_names=None, **kwargs):
        return self._create_widget(widgets.Text, description, class_names, placeholder=placeholder, **kwargs)

    def create_textarea(self, description, placeholder, class_names=None, **kwargs):
        return self._create_widget(widgets.Textarea, description, class_names, placeholder=placeholder, **kwargs)

    def create_dropdown(self, description, options, class_names=None, **kwargs):
        return self._create_widget(widgets.Dropdown, description, class_names, options=options, **kwargs)

    def create_select_multiple(self, description, options, class_names=None, **kwargs):
        return self._create_widget(widgets.SelectMultiple, description, class_names, options=options, **kwargs)

    def create_checkbox(self, description, value, class_names=None, **kwargs):
        return self._create_widget(widgets.Checkbox, description, class_names, value=value, indent=False, **kwargs)

    def create_button(self, description, class_names=None, **kwargs):
        return self._create_widget(widgets.Button, description, class_names, **kwargs)

    # Containers
    def _create_box(self, box_class, children, class_names=None, layout=None, **kwargs):
        """Create a box container."""
        layout = self.default_layout if layout is None else layout
        box = box_class(children=children, layout=layout, **kwargs)
        self.add_classes(box, class_names)
        return box

    def create_hbox(self, children, class_names=None, layout=None, **kwargs):
        return self._create_box(widgets.HBox, children, class_names, layout=layout, **kwargs)

    def create_vbox(self, children, class_names=None, layout=None, **kwargs):
        return self._create_box(widgets.VBox, children, class_names, layout=layout, **kwargs)

    # Other
    def display(self, widgets):
        """Display one or multiple widgets."""
        if isinstance(widgets, list):
            for widget in widgets:
                display(widget)
        else:
            display(widgets)

    def close(self, widgets, class_names=None, delay=0.2):
        """Close one or multiple widgets after a delay."""
        if not isinstance(widgets, list):
            widgets = [widgets]

        if class_names:
            for widget in widgets:
                self.add_classes(widget, class_names)

        time.sleep(delay)  # closing delay for all widgets

        # Close all widgets
        for widget in widgets:
            widget.close()

    # CallBack
    def connect_widgets(self, widget_pairs, callbacks):
        """
        Connect multiple widgets to callback functions for specified property changes.

        Parameters:
        - widget_pairs: List of tuples where each tuple contains a widget and the property name to observe.
        - callbacks: List of callback functions or a single callback function to be called on property change.
        """
        if not isinstance(callbacks, list):
            callbacks = [callbacks]

        for widget, property_name in widget_pairs:
            for callback in callbacks:
                widget.observe(lambda change, widget=widget, callback=callback: callback(change, widget), names=property_name)