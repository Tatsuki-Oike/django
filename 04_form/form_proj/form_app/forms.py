from django import forms

class SampleForm(forms.Form):
    text = forms.CharField(label="text")
    number = forms.IntegerField(label="number")


class DesignForm(forms.Form):
    text = forms.CharField(
        label="text", 
        widget=forms.TextInput(attrs={"class": "form-control"})
        )
    number = forms.IntegerField(
        label="number", 
        widget=forms.NumberInput(attrs={"class": "form-control"})
        )
    

class ValForm(forms.Form):
    text = forms.CharField(
        label="text", 
        widget=forms.TextInput(attrs={"class": "form-control"}),
        min_length=3,
        max_length=10,
        required=True
        )
    number = forms.IntegerField(
        label="number", 
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        min_value=50,
        max_value=100
        )
    lower_text = forms.CharField(
        label="lower_text", 
        widget=forms.TextInput(attrs={"class": "form-control"}),
        )
    
    def clean_lower_text(self):
        form_data = super().clean()
        lower_text = form_data["lower_text"]
        if (not lower_text.islower()):
            raise forms.ValidationError("すべて小文字で入力してください")


class TypeForm(forms.Form):
    # 文字
    text = forms.CharField(
        label="text", 
        widget=forms.TextInput(attrs={"class": "form-control"})
        )
    password = forms.CharField(
        label="password", 
        widget=forms.PasswordInput(attrs={"class": "form-control"})
        )
    email = forms.EmailField(
        label="email", 
        widget=forms.EmailInput(attrs={"class": "form-control"})
        )
    url = forms.URLField(
        label="url", 
        widget=forms.URLInput(attrs={"class": "form-control"})
        )
    
    # 数字
    number = forms.IntegerField(
        label="number", 
        widget=forms.NumberInput(attrs={"class": "form-control"})
        )
    float = forms.FloatField(
        label="float", 
        widget=forms.NumberInput(attrs={"class": "form-control"})
        )
    
    # 日時
    date = forms.DateField(
        label="date", 
        widget=forms.DateInput(attrs={"class": "form-control"})
        )    
    time = forms.TimeField(
        label="time", 
        widget=forms.TimeInput(attrs={"class": "form-control"})
        )    
    date_time = forms.DateTimeField(
        label="date_time", 
        widget=forms.DateTimeInput(attrs={"class": "form-control"})
        )
    
    # 簡単な選択
    check = forms.BooleanField(
        label="check", 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    select3 = forms.NullBooleanField(
        label="select3", 
        widget=forms.NullBooleanSelect(attrs={"class": 'form-select'})
    )

    # 候補複数
    data = [
        ("key1", "value1"),
        ("key2", "value2"),
        ("key3", "value3"),
        ("key4", "value4"),
    ]

    multi_item = forms.ChoiceField(
        label="multi_item", 
        choices=data,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    multi_item2 = forms.ChoiceField(
        label="multi_item2", 
        choices=data,
        widget=forms.Select(attrs={'size': 3, 'class': 'form-select'})
    )
    radio = forms.ChoiceField(
        label="radio", 
        choices=data,
        widget=forms.RadioSelect
    )

    # 複数選択
    multi_select_check = forms.MultipleChoiceField(
        label="multi_select_check", 
        choices=data,
        widget=forms.CheckboxSelectMultiple
    )