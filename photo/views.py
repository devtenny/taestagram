from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Photo


@login_required  # 함수형 뷰의 권한 제한(장식자 decorator)
def photo_list(request):  # 목록 뷰(함수형 뷰 -> 모든 로직 직접 구현해야 함)
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})


# 클래스형 뷰의 권한제한(믹스인 mixin)
class PhotoUploadView(LoginRequiredMixin, CreateView):  # 업로드 뷰
    # 제네릭 뷰 요소 model, fields, tmplate_name
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        # 로그인한 사용자 id를 다시 입력 요구하지 않도록
        form.instance.author_id = self.request.user.id
        if form.is_valid():  # 정당하면 저장
            form.instance.save()
            # return redirect('/')  # 루트 하드코딩
            return redirect('photo:photo_list')  # 수정
        else:  # 아니면 작성 내용 다시 출력
            return self.render_to_response({'form': form})


class PhotoDeleteView(LoginRequiredMixin, DeleteView):  # 삭제 뷰
    model = Photo
    # success_url = '/'  # 루트 하드코딩
    success_url = reverse_lazy('photo:photo_list')
    template_name = 'photo/delete.html'


class PhotoUpdateView(LoginRequiredMixin, UpdateView):  # 수정 뷰
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'
