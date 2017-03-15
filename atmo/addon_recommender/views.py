from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddonRecommendationsForm


@login_required
def get_client_recommendations(request):
    form = AddonRecommendationsForm()
    recommendations = []
    if request.method == 'POST':
        form = AddonRecommendationsForm(data=request.POST)
        if form.is_valid():
            # TODO: Use addon recommender once ready
            pass
    context = {
        'form': form,
        'recommendations': recommendations
    }

    return render(request, template_name="addon_recommender/index.html", context=context)
