from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from MovieOn.models.comment import Comment

@login_required
def delete_comment(request, comment_id, imdb_id):
    comment = Comment.objects.get(pk=comment_id)

    if comment.user == request.user:
        if request.method == 'POST':
            comment.delete()
            return redirect('details_movie', imdb_id)
    else:
        return redirect('details_movie', imdb_id)
    context = {
        'comment': comment,
        'imdb_id': imdb_id,
    }
    return render(request, 'comment/comment_delete_form.html', context=context)