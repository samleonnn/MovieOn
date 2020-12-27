from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms.models import model_to_dict
from MovieOn.models.comment import Comment
from MovieOn.forms import CommentForm

@login_required
def edit_comment(request, comment_id, imdb_id):
    comment = Comment.objects.get(pk=comment_id)

    if comment.user == request.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('details_movie', imdb_id)
        else:
            fields = model_to_dict(comment)
            form = CommentForm(initial=fields, instance=comment)
    
    else:
        return redirect('details_movie', imdb_id)

    context = {
        'form': form,
        'imdb_id': imdb_id,
    }
    return render(request, 'comment/comment_edit_form.html', context=context)

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