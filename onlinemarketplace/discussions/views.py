from django.shortcuts import render, get_object_or_404, redirect
from items.models import Item
from .models import Discussion, Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_convo(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if item.created_by == request.user:
        return redirect('core:index')

    discussions = Discussion.objects.filter(item=item).filter(engaging_users__in=[request.user.id])

    if discussions:
        return redirect('discussions:inside',pk=discussions.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            discussion = Discussion.objects.create(item=item)
            discussion.engaging_users.add(request.user)
            discussion.engaging_users.add(item.created_by)
            discussion.save()
            conversation = form.save(commit=False)
            conversation.discussion = discussion
            conversation.created_by = request.user
            conversation.save()
            redirect('items:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'discussions/new.html', {
        'form' : form
    })

@login_required
def inbox(request):
    # get all the discussions that the user is in
    discussions = Discussion.objects.filter(engaging_users__in=[request.user.id])
    return render(request, 'discussions/inbox.html', {
        'discussions':discussions
    })

@login_required
def inside_convo(request,pk):
    discussion = Discussion.objects.filter(engaging_users__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = discussion
            conversation_message.created_by = request.user
            conversation_message.save()

            discussion.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request,'discussions/inside.html',{
        'discussion' : discussion,
        'form' : form
    })