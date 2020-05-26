from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):  # 5.3.5 절에서 추가
    list_display = ['id', 'author', 'created', 'updated']  # 관리자 화면 목록에 보여줄 필드 지정
    raw_id_fields = ['author']  # 외래키 필드를 선택 위젯으로 처리할 때 사용자 수가 많을 경우 직접 값을 입력하여 검색하도록 처리
    list_filter = ['created', 'updated', 'author']  # 필터 기능을 적용할 필드 지정
    search_fields = ['text', 'created']  # 검색 기능을 적용할 필드 지정
    ordering = ['-updated', '-created']  # 관리자 사이트에 적용할 정렬 방식 지정


# admin.site.register(Photo)
admin.site.register(Photo, PhotoAdmin)  # 5.3.5 절에서 수정

