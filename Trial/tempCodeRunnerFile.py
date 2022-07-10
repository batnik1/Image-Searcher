class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1=Button(text='Button 1')
        b2=Button(text='Button 2')
        self.add_widget(b1)
        self.add_widget(b2)