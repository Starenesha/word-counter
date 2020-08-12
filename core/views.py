import re
from collections import Counter
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import pandas as pd
from .forms import TextInputForm
from .models import Text


def result_table(request, id):
    text = Text.objects.get(id=id)
    tokens = tokenize(text.text)
    word_count = word_counter(tokens)
    df = pd.DataFrame({'Word': list(word_count.keys()), 'Count': list(word_count.values())})
    df['Freq'] = pd.cut(df['Count'], 3, labels=['low', 'medium', 'high'])
    df = df.sort_values(['Count'], ascending=False)

    data = df.to_dict(orient='records')
    return render(request, 'core/table.html', context={"table": text, 'data': data})


def all_table(request):
    texts = Text.objects.all()
    return render(request, 'core/all_table.html', context={'texts': texts})


class Index(View):
    form_model = TextInputForm
    template = 'core/index.html'

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self,request):
        bound_form = self.form_model(request.POST or None)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            text_id = new_obj.id
            return redirect(reverse('table',  args=(text_id,)))
        else:
            return render(request, self.template, context={'form': bound_form})


def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ^0-9]', '', str(text))
    return text.split()


def word_counter(tokens):
    word_counts = Counter()
    word_counts.update(tokens)
    return word_counts
