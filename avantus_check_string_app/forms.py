from django import forms
from django import forms

class StringForm(forms.Form):
    main_string = forms.CharField(max_length=100)

    string_1 = forms.CharField(max_length=100)
    string_2 = forms.CharField(max_length=100)
    string_3 = forms.CharField(max_length=100)
    string_4 = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(StringForm,self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control', 
            })

    def check(self):
        print(self.cleaned_data)
        main_string = self.cleaned_data['main_string']
        string_1 = self.cleaned_data['string_1']
        string_2 = self.cleaned_data['string_2']
        string_3 = self.cleaned_data['string_3']
        string_4 = self.cleaned_data['string_4']

        data = {"main_string":main_string}
        main_string_list = [i for i in main_string]
        s1,s2,s3,s4 = "","","",""

        for i in string_1:
            if i in main_string_list:
                    s1 += i
            if s1 == string_1:
                
                data[string_1] = f"{string_1}: yes"
                for i in string_1:
                    main_string_list.remove(i) if i in main_string_list else ""
            else:
                data[string_1] = f"{string_1}: No"
        for i in string_2:
            if i in main_string_list:
                    s1 += i
            if s2 == string_2:
                
                data[string_2] = f"{string_2}: yes"
                for i in string_2:
                    main_string_list.remove(i) if i in main_string_list else ""
            else:
                data[string_2] = f"{string_2}: No"
        for i in string_3:
            if i in main_string_list:
                    s1 += i
            if s3 == string_3:
                
                data[string_3] = f"{string_3}: yes"
                for i in string_3:
                    main_string_list.remove(i) if i in main_string_list else ""
            else:
                data[string_3] = f"{string_3}: No"
        for i in string_4:
            if i in main_string_list:
                    s4 += i
            if s4 == string_4:
                
                data[string_4] = f"{string_4}: yes"
                for i in string_4:
                    main_string_list.remove(i) if i in main_string_list else ""
            else:
                data[string_4] = f"{string_4}: No"

        return data 