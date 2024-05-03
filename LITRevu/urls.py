from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from authentication.views import CustomLoginView, signup_page
from posts.views import create_review_and_ticket, create_ticket, edit_review, edit_ticket, ticket_response
from blog.views import home, follow_user, unfollow_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', signup_page, name='signup'),
    path('posts/create_review_and_ticket/', create_review_and_ticket, name='create_review_and_ticket'),
    path('create_ticket/', create_ticket, name='create_ticket'),
    path('edit_ticket/<int:id>/', edit_ticket, name='edit_ticket'),
    path('edit_review/<int:id>/', edit_review, name='edit_review'),
    path('ticket_response/<int:id>/', ticket_response, name='ticket_response'),
    path('follow_user/', follow_user, name='follow_user'),
    path('unfollow_user/<str:username>/', unfollow_user, name='unfollow_user'),
    path('home/', lambda request: home(request, feed_type='home'), name='home'),
    path('my_posts/', lambda request: home(request, feed_type='my_posts'), name='my_posts'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
