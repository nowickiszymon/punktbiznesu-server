from django.urls import path

from .views import Recomendations
from .views import Order
from .views import Message
from .views import Newsletter
from .views import BlogPosts

urlpatterns = [
        path('recomendations/', Recomendations.as_view(), name="recomendations"),
        path('order/', Order.as_view(), name="order"),
        path('message/', Message.as_view(), name="message"),
        path('newsletter/', Newsletter.as_view(), name="newsletter"),
        path('blog/', BlogPosts.as_view(), name="blog_posts"),
]
