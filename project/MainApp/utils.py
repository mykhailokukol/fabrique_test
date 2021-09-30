from django.shortcuts import render, redirect, get_object_or_404


class CreateObjectMixin:

    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, {
            'form': form,
        })

    def post(self, request):
        form = self.model_form(request.POST)
        if form.is_valid():
            new_obj = form.save()
            return redirect('/')
        return render(request, self.template, {
            'form': form,
        })
