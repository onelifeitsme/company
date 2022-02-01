from django.urls import path
from .views import PositionCreateView, PositionChangeView, PositionDeleteView, PositionsView, SinglePositionView

urlpatterns = [
    path('create_position', PositionCreateView.as_view(), name='create_position'),
    path('change_position/<slug:slug>', PositionChangeView.as_view(), name='change_position'),
    path('delete_position/<slug:slug>', PositionDeleteView.as_view(), name='delete_position'),
    path('positions', PositionsView.as_view(), name='positions'),
    path('pos/<slug>', SinglePositionView.as_view(), name='single_position'),

]
