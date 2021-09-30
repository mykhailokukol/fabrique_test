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


class UpdateObjectMixin:

    model = None
    model_form = None
    template = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.model_form(instance=obj)
        return render(request, self.template, {
            'form': form,
            'obj': obj,
        })

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.model_form(request.POST, instance=obj)
        if form.is_valid():
            upd_obj = form.save()
            return redirect('/')
        return render(request, self.template, {
            'form': form,
        })


class DeleteObjectMixin:

    model = None
    template = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        return render(request, self.template, {
            'obj': obj,
        })

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        obj.delete()
        return redirect('/')
