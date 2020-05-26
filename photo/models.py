from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Photo(models.Model):
    author = models.ForeignKey(
        User,  # author는 User 테이블을 향하는 외래키이다(User 테이블의 기본키가 외래키로 온다)
        on_delete=models.CASCADE,  # CASCADE: 부모가 제거될 때 자식도 제거하라
        related_name='user_photos'  # 자식들을 찾아낼 때 사용할 키워드 지정
                                    # 지정 생략할 경우 기본값으로 '모델이름_set'으로 지정됨
    )
    photo = models.ImageField(  # 이미지 필드(장고에서는 실제 이미지가 저장됨) -> Pillow 설치 필요
        upload_to='photos/%Y/%m/%d',  # 'photos/연/월/일'별 폴더에 저장되도록 함
        # default='photos/no_image.png'  # 사진이 없을 경우 기본값 지정
        default='http://placehold.it/800x600?text=blank'  # 사이트 주소 이용
    )
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # 생성될 때의 시간 자동 저장
    updated = models.DateTimeField(auto_now=True)  # 수정될 때의 시간 자동 저장

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + "님이 " \
               + self.created.strftime("%Y-%m-%d %H:%M:%S") + "에 등록한 사진"

    def get_absolute_url(self):  # 절대경로를 반환하는 함수
        return reverse('photo:photo_detail', args=[str(self.id)])
