from django.dispatch import receiver, Signal


plantid_backend_response = Signal()


@receiver(plantid_backend_response)
def plantid_response_receiver(sender, **kwargs):
    print("Get API response Signal: HERE I AM")
